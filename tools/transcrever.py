#!/usr/bin/env python3
"""Transcrição automática de uma gravação, com timestamps (uso típico: no runner do CI).

Este script NÃO executa nem altera nada do vídeo: apenas lê os bytes, extrai o áudio para um
WAV temporário e transcreve com `faster-whisper`. Ele existe porque a transcrição automática
precisa dos pesos do modelo, hospedados fora dos hosts permitidos no sandbox do Arena — o
runner do GitHub Actions tem acesso a eles (ver `.github/workflows/transcrever-gravacao.yml`).

Saídas em `--saida`:
    transcricao_bruta.txt  — fala com carimbo `[HH:MM:SS]` por segmento
    transcricao.srt        — legendas com timestamps
    transcricao.vtt        — idem em WebVTT
    transcricao_meta.json  — modelo, idioma, duração, segmentos, sha256 do vídeo, tempos

A transcrição automática é insumo, não verdade: revise termos técnicos, nomes e números antes
de publicar qualquer derivado, e registre a confiança em `metadados.md`.

Uso:
    python3 tools/transcrever.py --video "ARQUIVO.mp4" [--modelo large-v3] [--idioma pt]
    Acrescente `--sem-vad` para enviar o áudio inteiro ao reconhecedor sem detecção prévia de fala.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def sha256_de(caminho: str, bloco: int = 8 * 1024 * 1024) -> str:
    h = hashlib.sha256()
    with open(caminho, "rb") as fh:
        for parte in iter(lambda: fh.read(bloco), b""):
            h.update(parte)
    return h.hexdigest()


def bytes_do_manifesto(arquivo: str, raiz: str) -> int | None:
    import csv

    caminho = os.path.join(raiz, "manifesto.csv")
    if not os.path.exists(caminho):
        return None
    with open(caminho, newline="", encoding="utf-8-sig") as fh:
        for linha in csv.DictReader(fh):
            if linha["arquivo"] == arquivo:
                return int(linha["bytes"])
    return None


def achar_ffmpeg() -> str:
    """Prefere o ffmpeg do sistema; cai para o binário do wheel imageio-ffmpeg."""
    sistema = shutil.which("ffmpeg")
    if sistema:
        return sistema
    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception as erro:  # pragma: no cover - depende do ambiente
        raise SystemExit(
            "[erro] ffmpeg não encontrado. Instale o ffmpeg do sistema ou `pip install imageio-ffmpeg`."
        ) from erro


def extrair_audio(video: str, destino_wav: str) -> None:
    comando = [
        achar_ffmpeg(), "-hide_banner", "-loglevel", "error", "-y",
        "-i", video, "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", destino_wav,
    ]
    subprocess.run(comando, check=True)


def ler_wav_16k(caminho: str) -> "object":
    """Lê o WAV mono 16 kHz como array float32 (evita o decodificador PyAV do faster-whisper)."""
    import wave

    import numpy as np

    with wave.open(caminho, "rb") as fh:
        if fh.getframerate() != 16000:
            raise SystemExit("[erro] WAV extraído não está em 16 kHz")
        quadros = fh.readframes(fh.getnframes())
    return np.frombuffer(quadros, dtype=np.int16).astype(np.float32) / 32768.0


def hhmmss(segundos: float) -> str:
    return time.strftime("%H:%M:%S", time.gmtime(int(segundos)))


def srt_tempo(segundos: float) -> str:
    ms = int(round(segundos * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def vtt_tempo(segundos: float) -> str:
    return srt_tempo(segundos).replace(",", ".")


def principal() -> int:
    p = argparse.ArgumentParser(description="Transcreve uma gravação com timestamps (faster-whisper).")
    p.add_argument("--video", required=True, help="caminho do arquivo original")
    p.add_argument("--raiz", default=RAIZ, help="raiz do repositório (para conferir o manifesto)")
    p.add_argument("--saida", default=None, help="diretório de saída (padrão: pasta do vídeo)")
    p.add_argument("--modelo", default="large-v3", help="modelo faster-whisper (ex.: tiny, small, medium, large-v3)")
    p.add_argument("--idioma", default="pt", help="idioma falado (ex.: pt)")
    p.add_argument("--sem-vad", action="store_true", help="transcreve sem filtro de detecção de fala (VAD)")
    p.add_argument("--sem-conferir-manifesto", action="store_true")
    args = p.parse_args()

    if not os.path.exists(args.video):
        raise SystemExit(f"[erro] vídeo não encontrado: {args.video}")
    nome = os.path.basename(args.video)
    tam = os.path.getsize(args.video)
    if not args.sem_conferir_manifesto:
        esperado = bytes_do_manifesto(nome, args.raiz)
        if esperado is not None and esperado != tam:
            raise SystemExit(f"[erro] {nome}: {tam} bytes, manifesto diz {esperado}. Não transcreva sem conciliar.")

    saida = args.saida or os.path.dirname(os.path.abspath(args.video))
    os.makedirs(saida, exist_ok=True)

    print(f"[1/3] extraindo áudio de {nome} ({tam} bytes)")
    inicio = time.time()
    with tempfile.TemporaryDirectory() as tmp:
        wav = os.path.join(tmp, "audio.wav")
        extrair_audio(args.video, wav)
        estado_vad = "sem filtro VAD" if args.sem_vad else "com filtro VAD"
        print(f"[2/3] transcrevendo com {args.modelo} (idioma {args.idioma}, {estado_vad})")
        try:
            from faster_whisper import WhisperModel
        except ImportError:
            raise SystemExit("[erro] instale `faster-whisper` (pip install faster-whisper).")

        modelo = WhisperModel(args.modelo, device="cpu", compute_type="int8")
        try:
            import av

            print(f"      (PyAV {getattr(av, '__version__', 'desconhecida')} — decodificação feita pelo próprio script)")
        except Exception:
            pass
        audio = ler_wav_16k(wav)
        segmentos, info = modelo.transcribe(
            audio, language=args.idioma, beam_size=5, vad_filter=not args.sem_vad,
            condition_on_previous_text=False,
        )
        segmentos = list(segmentos)

    linhas_txt: list[str] = []
    linhas_srt: list[str] = []
    linhas_vtt: list[str] = ["WEBVTT", ""]
    for i, seg in enumerate(segmentos, start=1):
        texto = seg.text.strip()
        if not texto:
            continue
        linhas_txt.append(f"[{hhmmss(seg.start)}] {texto}")
        linhas_srt += [str(i), f"{srt_tempo(seg.start)} --> {srt_tempo(seg.end)}", texto, ""]
        linhas_vtt += [f"{vtt_tempo(seg.start)} --> {vtt_tempo(seg.end)}", texto, ""]

    bruto = os.path.join(saida, "transcricao_bruta.txt")
    with open(bruto, "w", encoding="utf-8") as fh:
        fh.write(f"# Transcrição automática — {nome}\n")
        fh.write(f"# modelo: {args.modelo} | idioma: {args.idioma} | segmentos: {len(segmentos)}\n")
        fh.write("# ATENÇÃO: transcrição automática é insumo, não verdade. Revise termos técnicos,\n")
        fh.write("# nomes, números e jargões antes de publicar qualquer derivado.\n\n")
        fh.write("\n".join(linhas_txt) + "\n")
    with open(os.path.join(saida, "transcricao.srt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(linhas_srt))
    with open(os.path.join(saida, "transcricao.vtt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(linhas_vtt))

    meta = {
        "arquivo": nome,
        "bytes": tam,
        "sha256": sha256_de(args.video),
        "modelo": args.modelo,
        "idioma_declarado": args.idioma,
        "idioma_detectado": getattr(info, "language", None),
        "probabilidade_idioma": round(getattr(info, "language_probability", 0.0), 4),
        "duracao_audio_s": round(getattr(info, "duration", 0.0), 2),
        "segmentos": len(segmentos),
        "filtro_vad": not args.sem_vad,
        "duracao_transcricao_s": round(time.time() - inicio, 1),
        "ferramenta": "faster-whisper (CTranslate2)",
    }
    with open(os.path.join(saida, "transcricao_meta.json"), "w", encoding="utf-8") as fh:
        json.dump(meta, fh, ensure_ascii=False, indent=2)

    print(f"[3/3] pronto: {len(segmentos)} segmentos, {meta['duracao_transcricao_s']}s de processamento")
    print(f"      arquivos em {saida}")
    return 0


if __name__ == "__main__":
    sys.exit(principal())
