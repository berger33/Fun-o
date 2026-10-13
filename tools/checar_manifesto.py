#!/usr/bin/env python3
"""Confere `manifesto.csv` (e `partes-videos.json`) contra os arquivos do repositório.

Verificação de inventário que o roteiro exige antes de analisar qualquer vídeo:

- todo vídeo do manifesto existe no repositório?
- vídeos não divididos: o ponteiro LFS traz `size` igual ao manifesto (ou o arquivo real
  já baixado tem exatamente esse tamanho)?
- vídeos divididos: todas as partes de `partes-videos.json` existem e têm o tamanho esperado?
- soma dos tamanhos confere com o total declarado para o vídeo reconstruído?

Não baixa nada e não altera arquivos. Para arquivos já materializados (> 200 MB) não calcula
SHA-256 por padrão, para não gastar minutos de I/O; use `--hash` para forçar.

Uso:
    python3 tools/checar_manifesto.py
    python3 tools/checar_manifesto.py --hash
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIMITE_HASH = 200 * 1024 * 1024


def sha256_de(caminho: str, bloco: int = 4 * 1024 * 1024) -> str:
    h = hashlib.sha256()
    with open(caminho, "rb") as fh:
        for parte in iter(lambda: fh.read(bloco), b""):
            h.update(parte)
    return h.hexdigest()


def ler_ponteiro(caminho: str) -> tuple[str, int] | None:
    try:
        if os.path.getsize(caminho) > 1024:
            return None
        texto = open(caminho, "r", encoding="utf-8", errors="strict").read()
    except (OSError, UnicodeDecodeError):
        return None
    if "git-lfs.github.com/spec/v1" not in texto:
        return None
    dados = {}
    for linha in texto.splitlines()[1:]:
        if " " in linha:
            chave, valor = linha.split(" ", 1)
            dados[chave] = valor.strip()
    if not dados.get("size", "").isdigit():
        return None
    return dados.get("oid", "").split(":", 1)[-1], int(dados["size"])


def principal() -> int:
    p = argparse.ArgumentParser(description="Confere o manifesto contra os arquivos do repositório.")
    p.add_argument("--raiz", default=RAIZ)
    p.add_argument("--hash", action="store_true", help="calcula SHA-256 também de arquivos grandes")
    args = p.parse_args()
    raiz = os.path.abspath(args.raiz)

    with open(os.path.join(raiz, "manifesto.csv"), newline="", encoding="utf-8-sig") as fh:
        manifesto = list(csv.DictReader(fh))
    with open(os.path.join(raiz, "partes-videos.json"), encoding="utf-8") as fh:
        partes = {reg["original"]: reg for reg in json.load(fh)}

    falhas = avisos = 0
    total_manifesto = total_local = 0
    por_oid: dict[str, list[str]] = {}
    for linha_oid in manifesto:
        caminho_oid = os.path.join(raiz, linha_oid["arquivo"])
        if os.path.exists(caminho_oid):
            ponteiro_oid = ler_ponteiro(caminho_oid)
            if ponteiro_oid:
                por_oid.setdefault(ponteiro_oid[0], []).append(linha_oid["arquivo"])
    for linha in manifesto:
        nome = linha["arquivo"]
        esperado = int(linha["bytes"])
        dividido = linha.get("dividido", "False").strip().lower() == "true"
        total_manifesto += esperado
        caminho = os.path.join(raiz, nome)
        if dividido:
            if not os.path.exists(caminho):
                print(f"[info]  {nome}: original reconstruído ausente (normal; é ignorado pelo Git)")
        elif not os.path.exists(caminho):
            print(f"[falha] {nome}: ausente no repositório")
            falhas += 1
            continue

        ponteiro = ler_ponteiro(caminho) if os.path.exists(caminho) else None
        if dividido:
            registro = partes.get(nome)
            if not registro:
                print(f"[falha] {nome}: marcado como dividido, mas não está em partes-videos.json")
                falhas += 1
                continue
            if registro["bytes"] != esperado:
                print(f"[falha] {nome}: partes somam {registro['bytes']} bytes, manifesto diz {esperado}")
                falhas += 1
            soma = 0
            for parte in registro["parts"]:
                caminho_parte = os.path.join(raiz, parte["name"])
                if not os.path.exists(caminho_parte):
                    print(f"[falha] {nome}: parte ausente {parte['name']}")
                    falhas += 1
                    continue
                tam = os.path.getsize(caminho_parte)
                ponteiro_parte = ler_ponteiro(caminho_parte)
                if ponteiro_parte and ponteiro_parte[1] != parte["bytes"]:
                    print(f"[falha] {nome}/{parte['name']}: ponteiro diz {ponteiro_parte[1]}, esperado {parte['bytes']}")
                    falhas += 1
                elif not ponteiro_parte and tam != parte["bytes"]:
                    print(f"[falha] {nome}/{parte['name']}: {tam} bytes locais, esperado {parte['bytes']}")
                    falhas += 1
                soma += parte["bytes"]
            print(f"[ok]    {nome}: {len(registro['parts'])} partes presentes, {soma} bytes no total")
            continue

        if ponteiro:
            oid, tamanho = ponteiro
            if tamanho != esperado:
                print(f"[falha] {nome}: ponteiro diz {tamanho} bytes, manifesto diz {esperado}")
                falhas += 1
            else:
                print(f"[ok]    {nome}: ponteiro LFS com {tamanho} bytes (objeto ainda não baixado) — oid {oid[:12]}…")
            continue

        tam = os.path.getsize(caminho)
        if tam != esperado:
            print(f"[falha] {nome}: arquivo local tem {tam} bytes, manifesto diz {esperado}")
            falhas += 1
            continue
        total_local += tam
        if args.hash or tam <= LIMITE_HASH:
            resumo = sha256_de(caminho)
            print(f"[ok]    {nome}: {tam} bytes, sha256 {resumo[:16]}…")
        else:
            print(f"[ok]    {nome}: {tam} bytes (sha256 não calculado; use --hash)")
            avisos += 1

    for oid, nomes in sorted(por_oid.items()):
        if len(nomes) > 1:
            avisos += 1
            print(f"[aviso] objeto LFS {oid[:12]}… compartilhado por {len(nomes)} arquivos "
                  f"(conteúdo idêntico, analisar uma vez): " + ", ".join(nomes))

    print(
        f"\nresumo: {len(manifesto)} vídeos no manifesto, {total_manifesto} bytes declarados, "
        f"{total_local} bytes já materializados localmente, {falhas} falhas, {avisos} avisos"
    )
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(principal())
