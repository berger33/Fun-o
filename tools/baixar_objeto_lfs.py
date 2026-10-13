#!/usr/bin/env python3
"""Baixa UM único objeto Git LFS deste repositório, sem `git lfs pull` geral.

Motivo: o repositório guarda os vídeos em Git LFS. Em ambientes sem o cliente
`git-lfs` (ou com o host de conteúdo bloqueado para o cliente), é possível baixar
somente o arquivo pedido usando a API LFS do próprio repositório.

Uso:
    python3 tools/baixar_objeto_lfs.py "Apresentação projeto 19-18.mp4"
    python3 tools/baixar_objeto_lfs.py --verificar "Apresentação projeto 19-18.mp4"
    python3 tools/baixar_objeto_lfs.py --remoto https://github.com/ORG/REPO.git ARQUIVO

Comportamento:
    - confere o nome no `manifesto.csv` (tamanho esperado);
    - lê o ponteiro LFS do arquivo no clone para obter o `oid` (SHA-256) e o tamanho;
    - consulta a API LFS do remoto (sem autenticação; usa token só se o servidor exigir);
    - baixa para `<arquivo>.parcial` com retomada (HTTP Range) e grava no nome final
      apenas depois de conferir tamanho e SHA-256.

Segurança: nunca executa nada do vídeo e nunca imprime token. Nenhum arquivo é
commitado; `*.mp4` continua rastreado por LFS (não use `git add` no vídeo baixado).

Limitação conhecida: se o host de conteúdo do LFS (`objects.githubusercontent.com` / `github-cloud.githubusercontent.com`) estiver bloqueado na rede, o download falha
com erro TLS; o script reporta o host e o erro exato. Ver
`materiais/BLOQUEIO_LFS_ARENA.md`.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import ssl
import subprocess
import sys
import urllib.error
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LFS_JSON = "application/vnd.git-lfs+json"


def sha256_de(caminho: str, bloco: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with open(caminho, "rb") as fh:
        for parte in iter(lambda: fh.read(bloco), b""):
            h.update(parte)
    return h.hexdigest()


def ler_manifesto(raiz: str = RAIZ) -> dict[str, int]:
    caminho = os.path.join(raiz, "manifesto.csv")
    with open(caminho, newline="", encoding="utf-8-sig") as fh:
        return {l["arquivo"]: int(l["bytes"]) for l in csv.DictReader(fh)}


def ler_ponteiro(caminho: str) -> tuple[str, int] | None:
    """Devolve (oid, tamanho) se o arquivo for um ponteiro LFS válido."""
    try:
        with open(caminho, "r", encoding="utf-8", errors="strict") as fh:
            linhas = [l.strip() for l in fh.read().splitlines() if l.strip()]
    except (OSError, UnicodeDecodeError):
        return None
    dados: dict[str, str] = {}
    for linha in linhas[1:]:
        if " " in linha:
            chave, valor = linha.split(" ", 1)
            dados[chave] = valor
    oid = dados.get("oid", "")
    if not oid.startswith("sha256:") or not dados.get("size", "").isdigit():
        return None
    return oid.split(":", 1)[1], int(dados["size"])


def remoto_do_git(raiz: str = RAIZ) -> str:
    saida = subprocess.run(
        ["git", "-C", raiz, "remote", "get-url", "origin"],
        capture_output=True, text=True, check=True,
    )
    return saida.stdout.strip()


def token_disponivel() -> str | None:
    for var in ("GH_TOKEN", "GITHUB_TOKEN"):
        if os.environ.get(var):
            return os.environ[var]
    try:
        saida = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
        if saida.returncode == 0 and saida.stdout.strip():
            return saida.stdout.strip()
    except FileNotFoundError:
        pass
    return None


def post_json(url: str, corpo: dict, token: str | None) -> dict:
    dados = json.dumps(corpo).encode()
    cabecalhos = {"Accept": LFS_JSON, "Content-Type": LFS_JSON}
    if token:
        cabecalhos["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=dados, headers=cabecalhos, method="POST")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def pedir_objeto(remoto: str, oid: str, tamanho: int) -> dict:
    url = remoto.rstrip("/") + "/info/lfs/objects/batch"
    corpo = {"operation": "download", "transfers": ["basic"],
             "objects": [{"oid": oid, "size": tamanho}]}
    try:
        resposta = post_json(url, corpo, None)
    except urllib.error.HTTPError as erro:
        if erro.code not in (401, 403, 404):
            raise
        token = token_disponivel()
        if not token:
            raise SystemExit(
                f"[erro] API LFS respondeu HTTP {erro.code} e não há token em "
                "GH_TOKEN/GITHUB_TOKEN nem em `gh auth token`."
            )
        resposta = post_json(url, corpo, token)
    objeto = (resposta.get("objects") or [{}])[0]
    if "actions" not in objeto or "download" not in objeto["actions"]:
        raise SystemExit(f"[erro] API LFS não devolveu ação de download: {objeto.get('error', objeto)}")
    return objeto


def erro_rede(host: str, exc: Exception) -> None:
    sys.stderr.write(
        f"\n[erro] falha de rede ao acessar `{host}`: {exc}\n"
        "       Se a mensagem for `SSL_ERROR_SYSCALL`/`SSL_connect`, o host de conteúdo do\n"
        "       LFS está bloqueado no egress deste ambiente (não é ausência do objeto).\n"
        "       Libere `objects.githubusercontent.com` e `github-cloud.githubusercontent.com`\n"
        "       ou use uma máquina com Git LFS funcional. Diagnóstico em\n"
        "       `materiais/BLOQUEIO_LFS_ARENA.md`.\n"
    )
    raise SystemExit(2)


def baixar(href: str, destino: str, tamanho: int) -> None:
    parcial = destino + ".parcial"
    host = href.split("/")[2]
    ja_tem = os.path.getsize(parcial) if os.path.exists(parcial) else 0
    cabecalhos = {"Range": f"bytes={ja_tem}-"} if ja_tem else {}
    req = urllib.request.Request(href, headers=cabecalhos)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            if ja_tem and resp.status != 206:  # servidor ignorou o Range: recomeça
                ja_tem = 0
            modo = "ab" if ja_tem else "wb"
            restante = tamanho - ja_tem
            with open(parcial, modo) as saida:
                while True:
                    bloco = resp.read(8 * 1024 * 1024)
                    if not bloco:
                        break
                    saida.write(bloco)
                    restante -= len(bloco)
                    if restante <= 0:
                        break
    except (urllib.error.URLError, ssl.SSLError, OSError, TimeoutError) as exc:
        erro_rede(host, exc)
    if os.path.getsize(parcial) != tamanho:
        raise SystemExit(
            f"[erro] download incompleto: {os.path.getsize(parcial)} de {tamanho} bytes "
            f"em `{parcial}`. Rode de novo para retomar."
        )
    os.replace(parcial, destino)


def verificar(caminho: str, oid: str, tamanho: int) -> bool:
    if not os.path.exists(caminho):
        print(f"[falta] {caminho} não existe")
        return False
    if ler_ponteiro(caminho) is not None:
        print(f"[erro] `{os.path.basename(caminho)}` ainda é o ponteiro LFS "
              f"({os.path.getsize(caminho)} bytes), não o vídeo. Baixe os bytes primeiro.")
        return False
    obtido = os.path.getsize(caminho)
    if obtido != tamanho:
        print(f"[erro] tamanho {obtido} != {tamanho} esperado")
        return False
    resumo = sha256_de(caminho)
    if resumo != oid:
        print(f"[erro] sha256 {resumo} != {oid} esperado")
        return False
    print(f"[ok] {os.path.basename(caminho)}: {obtido} bytes, sha256 {resumo}")
    return True


def principal() -> int:
    p = argparse.ArgumentParser(description="Baixa um único objeto Git LFS deste repositório.")
    p.add_argument("arquivo", help="nome idêntico ao do manifesto.csv")
    p.add_argument("--raiz", default=RAIZ, help="raiz do repositório (padrão: diretório do script/..)")
    p.add_argument("--remoto", default=None, help="URL do remoto git (padrão: origin)")
    p.add_argument("--verificar", action="store_true", help="apenas confere o arquivo local")
    args = p.parse_args()

    manifesto = ler_manifesto(args.raiz)
    if args.arquivo not in manifesto:
        raise SystemExit(f"[erro] `{args.arquivo}` não está no manifesto.csv deste repositório.")
    esperado_manifesto = manifesto[args.arquivo]

    caminho = os.path.join(args.raiz, args.arquivo)
    ponteiro = ler_ponteiro(caminho)
    if ponteiro is None:
        print(f"[info] `{args.arquivo}` não é um ponteiro LFS (talvez já seja o vídeo); vou conferir.")
        if args.verificar:
            resumo = sha256_de(caminho)
            print(f"[ok] tamanho {os.path.getsize(caminho)} bytes, sha256 {resumo}")
            return 0
        raise SystemExit("[erro] nada a baixar por este script (não há ponteiro).")
    oid, tamanho = ponteiro
    if tamanho != esperado_manifesto:
        raise SystemExit(
            f"[erro] ponteiro diz {tamanho} bytes, manifesto.csv diz {esperado_manifesto}. "
            "Não baixe até conciliar as fontes."
        )

    if args.verificar:
        return 0 if verificar(caminho, oid, tamanho) else 1

    remoto = args.remoto or remoto_do_git(args.raiz)
    print(f"[1/3] objeto: {args.arquivo} — {tamanho} bytes — sha256 {oid}")
    objeto = pedir_objeto(remoto, oid, tamanho)
    href = objeto["actions"]["download"]["href"]
    host = href.split("/")[2]
    print(f"[2/3] API LFS OK; baixando de {host} (retomável)")
    baixar(href, caminho, tamanho)
    print("[3/3] conferindo integridade")
    return 0 if verificar(caminho, oid, tamanho) else 1


if __name__ == "__main__":
    sys.exit(principal())
