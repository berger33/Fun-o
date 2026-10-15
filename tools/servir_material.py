#!/usr/bin/env python3
"""Servidor local do material de estudo em HTML.

Serve a página gerada por `tools/gerar_base_conhecimento_html.py` e oferece o download do
arquivo. Não expõe nada além do material: a raiz do site é a pasta de saída, e a listagem de
diretório está desativada.

Rotas:
    /                  página do material (sem cache, para refletir a última geração)
    /download          baixa o arquivo HTML com nome descritivo
    /health            verificação simples de disponibilidade
    /<arquivo>         qualquer outro arquivo gerado na pasta de saída

Uso:
    python3 tools/servir_material.py [--porta 8000] [--pasta saida]
"""

from __future__ import annotations

import argparse
import http.server
import os
import socketserver
import posixpath
import urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOME_ARQUIVO = "base-de-conhecimento-funcao-sistemas.html"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, diretorio: str = RAIZ, **kwargs):
        super().__init__(*args, directory=diretorio, **kwargs)

    def do_GET(self) -> None:  # noqa: N802 (nome exigido pela biblioteca)
        caminho = urllib.parse.urlparse(self.path).path

        if caminho == "/health":
            corpo = b'{"status":"ok"}'
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(corpo)))
            self.end_headers()
            self.wfile.write(corpo)
            return

        if caminho in ("/", "/index.html", "/download"):
            arquivo = os.path.join(self.directory, "index.html")
            if not os.path.exists(arquivo):
                self.send_error(404, "material ainda nao foi gerado")
                return
            with open(arquivo, "rb") as fh:
                corpo = fh.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(corpo)))
            if caminho == "/download":
                self.send_header("Content-Disposition", 'attachment; filename="%s"' % NOME_ARQUIVO)
            else:
                self.send_header("Cache-Control", "no-store, must-revalidate")
            self.end_headers()
            self.wfile.write(corpo)
            return

        return super().do_GET()

    def log_message(self, formato: str, *args) -> None:
        print("[material] %s - %s" % (self.address_string(), formato % args), flush=True)


class Servidor(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--porta", type=int, default=8000)
    p.add_argument("--pasta", default=os.path.join(RAIZ, "saida"))
    args = p.parse_args()

    pasta = os.path.abspath(args.pasta)
    if not os.path.exists(os.path.join(pasta, "index.html")):
        print("aviso: %s ainda não contém o material gerado." % pasta)

    def fabrica(*a, **kw):
        return Handler(*a, diretorio=pasta, **kw)

    with Servidor(("0.0.0.0", args.porta), fabrica) as httpd:
        print("servindo %s em http://0.0.0.0:%d (download em /download)" % (pasta, args.porta), flush=True)
        httpd.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
