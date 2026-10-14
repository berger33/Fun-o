#!/usr/bin/env python3
"""Reconstrói vídeos divididos em partes LFS e valida cada bloco por bytes/SHA-256.

Sem argumentos, mantém o comportamento de reconstruir todos os vídeos listados em
partes-videos.json. Use --video para reconstruir somente um original, como faz a
ponte de transcrição quando o arquivo fonte foi dividido.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def reconstruir(registro: dict) -> None:
    target = ROOT / registro["original"]
    tmp = target.with_suffix(target.suffix + ".reconstruindo")
    total = 0
    with tmp.open("wb") as out:
        for parte in registro["parts"]:
            path = ROOT / parte["name"]
            digest = hashlib.sha256()
            tamanho = 0
            with path.open("rb") as fh:
                while True:
                    bloco = fh.read(8 * 1024 * 1024)
                    if not bloco:
                        break
                    out.write(bloco)
                    digest.update(bloco)
                    tamanho += len(bloco)
            if tamanho != parte["bytes"] or digest.hexdigest() != parte["sha256"]:
                tmp.unlink(missing_ok=True)
                raise SystemExit(f"Parte inválida: {parte['name']}")
            total += tamanho
    if total != registro["bytes"]:
        tmp.unlink(missing_ok=True)
        raise SystemExit(f"Tamanho final inválido: {registro['original']}")
    tmp.replace(target)
    print(f"Reconstruído e validado: {registro['original']} ({total} bytes)")


def main() -> int:
    parser = argparse.ArgumentParser(description="Reconstrói vídeos divididos em partes LFS.")
    parser.add_argument("--video", help="reconstrói somente este original listado em partes-videos.json")
    args = parser.parse_args()

    registros = json.loads((ROOT / "partes-videos.json").read_text(encoding="utf-8"))
    if args.video:
        selecionados = [r for r in registros if r["original"] == args.video]
        if not selecionados:
            raise SystemExit(f"Vídeo não dividido ou ausente no índice de partes: {args.video}")
    else:
        selecionados = registros
    for registro in selecionados:
        reconstruir(registro)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
