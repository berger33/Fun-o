#!/usr/bin/env python3
"""Auditoria de qualidade e privacidade dos materiais derivados (PLANO_EXTRACAO_ARENA.md §6).

Confere, para cada vídeo extraído em `materiais/<slug>/`, os critérios que o plano exige
**antes** de marcar a gravação como `concluído`:

1. todos os arquivos obrigatórios existem (`ROTEIRO_ARENA.md` — estrutura por vídeo);
2. a linha de metadados aparece no início dos guias (`Categoria`, `Sistema`, `Assunto`,
   `Fonte`, `Confiança da extração`);
3. há timestamps `HH:MM:SS` nos documentos que precisam citar origem — ou, quando o pacote
   declarar `**Tipo de fonte:** conversa` em `metadados.md` (fonte textual, sem mídia), âncoras
   `[Mnn]` de mensagem no lugar dos timestamps (ver `materiais/CONVENCOES_FONTES_TEXTUAIS.md`);
4. `perguntas.md` tem pelo menos 10 perguntas (ou uma por conceito/etapa, se menos);
5. `capturas.md` cita arquivos existentes em `capturas/`, cada um com timestamp e nota de revisão;
6. nenhum link relativo quebrado dentro de `materiais/`;
7. varredura de privacidade: CPF/CNPJ, e-mail, telefone, segredos (tokens, chaves, JWT, chave
   privada, URL assinada) e atribuições de senha.

Privacidade do próprio relatório: o auditor **nunca imprime o valor sensível encontrado**, apenas
arquivo, linha e o tipo do achado — para não replicar segredo em log, commit ou issue.

Uso:
    python3 tools/validar_materiais.py                       # audita tudo em materiais/
    python3 tools/validar_materiais.py --video <slug>        # exige o diretório do vídeo
    python3 tools/validar_materiais.py --so-privacidade      # só a varredura sensível

Fontes textuais: se `metadados.md` declarar `**Tipo de fonte:** conversa`, o auditor troca a
exigência de timestamps por âncoras `[Mnn]` (índice da mensagem na transcrição). O material bruto
sem mascaramento, quando preservado, fica em `restrito/` — fora do Git, portanto fora desta
varredura. Convenções completas em `materiais/CONVENCOES_FONTES_TEXTUAIS.md`.

Fontes não obtidas: se `metadados.md` declarar `**Fonte obtida:** não`, o pacote é registrado como
“bloqueio declarado” e a exigência de timestamp/âncora deixa de ser falha (vira aviso). Isso evita
que um pacote honestamente vazio seja reprovado — e evita a tentação de inventar timestamp para
“passar no teste”. Os demais critérios (arquivos obrigatórios, metadados, perguntas, links e
privacidade) continuam valendo.

Saída: relatório legível; código de saída 0 = passou, 1 = falhas, 2 = achado de privacidade.
Não altera nenhum arquivo.
"""

from __future__ import annotations

import argparse
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATERIAIS = "materiais"

ARQUIVOS_OBRIGATORIOS = [
    "transcricao.md",
    "guia_de_estudo.md",
    "procedimentos.md",
    "perguntas.md",
    "glossario.md",
    "incertezas.md",
    "metadados.md",
]

CAMPOS_METADADOS = ["Categoria", "Sistema", "Assunto", "Fonte", "Confiança da extração"]

# pastas que guardam índices transversais, não vídeos
PASTAS_RESERVADAS = {"SQL", "SISTEMAS", "PROCESSOS", "capturas"}

# documento -> mínimo de timestamps HH:MM:SS esperados
TIMESTAMPS_MINIMOS = {
    "transcricao.md": 1,
    "guia_de_estudo.md": 1,
    "procedimentos.md": 1,
    "perguntas.md": 1,
    "glossario.md": 1,
}

TIMESTAMP = re.compile(r"\b\d{2}:\d{2}:\d{2}\b")
# fontes textuais (conversas/chat): a origem é ancorada pelo índice de mensagem `[Mnn]`
ANCORA_MENSAGEM = re.compile(r"\[M\d{2,}\]")
TIPO_FONTE = re.compile(r"(?im)^\s*[-*>]*\s*\**Tipo de fonte:\**\s*(?P<tipo>.+?)\s*$")
# pacote que declara, em `metadados.md`, que a fonte primária não foi obtida: por definição não pode
# haver timestamp/âncora — o plano manda registrar o bloqueio, não inventar origem.
FONTE_NAO_OBTIDA = re.compile(r"(?im)^\s*[-*>\s]*\**Fonte obtida:\**\s*(?:n[ãa]o|no|false)\b")
PERGUNTA = re.compile(r"^\s*(?:\d+[.)]|[-*])\s+.*\?", re.MULTILINE)
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
CAPTURA_LINHA = re.compile(r"(?<![\w-])(?P<arq>[A-Za-z0-9][A-Za-z0-9._/-]*\.(?:png|jpg|jpeg))\b")

# (tipo, regex) — o valor encontrado nunca é exibido no relatório
PADROES_SENSIVEIS = [
    ("CPF", re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b")),
    ("CNPJ", re.compile(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b")),
    ("e-mail", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("telefone", re.compile(r"(?:\+\s?55[\s-]?|\(\d{2}\)[\s-]?|\b\d{2}[\s.-])?(?:9?\d{4}[\s.-]\d{4})\b")),
    ("token GitHub", re.compile(r"\b(?:ghp|gho|ghs|ghu|ghr)_[A-Za-z0-9]{20,}\b|\bgithub_pat_[A-Za-z0-9_]{20,}\b")),
    ("chave AWS", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("token Slack", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("chave privada", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("URL assinada", re.compile(r"[?&](?:X-Amz-Signature|X-Amz-Credential|sig|token|access_token)=[A-Za-z0-9%._-]{16,}")),
    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{5,}\b")),
    ("atribuição de senha", re.compile(r"(?i)\b(?:senha|password|passwd|pwd|secret)\b\s*[:=]\s*\S+")),
    ("chave OpenAI", re.compile(r"\bsk-[A-Za-z0-9]{20,}\b")),
    ("Client Secret", re.compile(r"(?i)\bclient[_-]?secret\b\s*[:=]\s*\S+")),
]

IGNORAR_LINHAS = [
    re.compile(r"\[SEGREDO OMITIDO\]"),
    re.compile(r"\[DADO PESSOAL OMITIDO\]"),
    re.compile(r"@users\.noreply\.github\.com"),
    re.compile(r"^\s*(?:senha|password|senha:\s*$)\s*$", re.I),
]


class Relatorio:
    def __init__(self) -> None:
        self.erros: list[str] = []
        self.avisos: list[str] = []
        self.privacidade: list[str] = []
        self.info: list[str] = []

    def ok(self, msg: str) -> None:
        self.info.append(f"[ok]   {msg}")

    def erro(self, msg: str) -> None:
        self.erros.append(f"[falha] {msg}")

    def aviso(self, msg: str) -> None:
        self.avisos.append(f"[aviso] {msg}")

    def sensivel(self, msg: str) -> None:
        self.privacidade.append(f"[PRIVACIDADE] {msg}")

    def imprimir(self) -> None:
        for linha in dict.fromkeys(self.info + self.avisos + self.erros + self.privacidade):
            print(linha)
        print(
            f"\nresumo: {len(set(self.info))} verificações ok, {len(set(self.avisos))} avisos, "
            f"{len(set(self.erros))} falhas, {len(set(self.privacidade))} achados de privacidade"
        )

    def codigo(self) -> int:
        if self.privacidade:
            return 2
        return 1 if self.erros else 0


def ler(caminho: str) -> str:
    with open(caminho, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def auditar_privacidade(caminho: str, rel: Relatorio) -> None:
    for numero, linha in enumerate(ler(caminho).splitlines(), start=1):
        if any(padrao.search(linha) for padrao in IGNORAR_LINHAS):
            continue
        for tipo, padrao in PADROES_SENSIVEIS:
            if padrao.search(linha):
                # nunca exibe o valor; o arquivo deve ser revisado manualmente
                rel.sensivel(f"{caminho}:{numero} — possível {tipo} (valor omitido de propósito)")


def auditar_capturas(dir_video: str, rel: Relatorio) -> None:
    capturas_md = os.path.join(dir_video, "capturas.md")
    pasta = os.path.join(dir_video, "capturas")
    if not os.path.exists(capturas_md):
        rel.aviso("capturas.md ausente — o roteiro pede o arquivo mesmo quando não há imagens")
        return
    texto = ler(capturas_md)
    citadas = sorted(set(CAPTURA_LINHA.findall(texto)))
    if not citadas:
        if re.search(r"(?i)nenhuma (?:captura|imagem)", texto):
            rel.ok("capturas.md declara que não há capturas")
        else:
            rel.aviso("capturas.md não cita nenhuma imagem e não declara ausência de capturas")
        return
    for nome in citadas:
        alvo = os.path.join(dir_video, nome) if "/" in nome else os.path.join(pasta, nome)
        if not os.path.exists(alvo):
            rel.erro(f"capturas.md cita `{nome}` que não existe em capturas/")
            continue
        if not TIMESTAMP.search(texto.split(nome, 1)[0][-400:] + texto.split(nome, 1)[1][:400]):
            rel.aviso(f"captura `{nome}` sem timestamp próximo na descrição")
    if not re.search(r"(?i)privacidade|sanitiz|mascar", texto):
        rel.erro("capturas.md não registra a revisão de privacidade/sanitização")
    else:
        rel.ok("capturas.md registra revisão de privacidade")


def auditar_links(dir_video: str, rel: Relatorio) -> None:
    for raiz, _, arquivos in os.walk(dir_video):
        for nome in arquivos:
            if not nome.endswith((".md", ".csv")):
                continue
            caminho = os.path.join(raiz, nome)
            for destino in LINK.findall(ler(caminho)):
                alvo = destino.split("#", 1)[0].strip()
                if not alvo or alvo.startswith(("http://", "https://", "mailto:")):
                    continue
                resolvido = os.path.normpath(os.path.join(os.path.dirname(caminho), alvo))
                if os.path.exists(resolvido):
                    continue
                rel.erro(f"link quebrado em {caminho}: {destino}")


def tipo_de_fonte(dir_video: str) -> str:
    """Classifica o pacote como fonte de `video` (padrão) ou fonte textual (`texto`).

    O pacote se declara em `metadados.md` com uma linha `**Tipo de fonte:** conversa`. Fontes
    textuais não têm `HH:MM:SS` de mídia; a rastreabilidade é feita por âncoras `[Mnn]`.
    """
    caminho = os.path.join(dir_video, "metadados.md")
    if not os.path.exists(caminho):
        return "video"
    for encontrado in TIPO_FONTE.finditer(ler(caminho)):
        valor = encontrado.group("tipo").strip().strip("`*_ ").lower()
        if valor.startswith(("conversa", "chat", "mensagem", "texto", "e-mail", "email")):
            return "texto"
    return "video"


def fonte_nao_obtida(dir_video: str) -> bool:
    """Pacote declara `**Fonte obtida:** não` em `metadados.md` (fonte primária indisponível)."""
    caminho = os.path.join(dir_video, "metadados.md")
    return os.path.exists(caminho) and bool(FONTE_NAO_OBTIDA.search(ler(caminho)))


def auditar_video(dir_video: str) -> Relatorio:
    rel = Relatorio()
    nome = os.path.basename(dir_video.rstrip("/"))
    tipo = tipo_de_fonte(dir_video)
    sem_fonte = fonte_nao_obtida(dir_video)
    if tipo == "texto":
        rotulo = "fonte textual (âncoras `[Mnn]`)"
    elif sem_fonte:
        rotulo = "gravação sem fonte obtida (bloqueio declarado)"
    else:
        rotulo = "gravação (timestamps `HH:MM:SS`)"
    print(f"\n=== {MATERIAIS}/{nome} — {rotulo} ===")
    if sem_fonte:
        rel.aviso(
            "pacote declara `Fonte obtida: não` — exigência de timestamp/âncora não se aplica; "
            "a rastreabilidade ficará pendente enquanto a fonte não for obtida"
        )

    for arquivo in ARQUIVOS_OBRIGATORIOS:
        caminho = os.path.join(dir_video, arquivo)
        if not os.path.exists(caminho):
            rel.erro(f"arquivo obrigatório ausente: {arquivo}")
        elif os.path.getsize(caminho) < 10:
            rel.erro(f"{arquivo} está vazio")
        elif os.path.getsize(caminho) < 400:
            rel.aviso(f"{arquivo} muito curto ({os.path.getsize(caminho)} bytes)")

    conteudos = {n: ler(os.path.join(dir_video, n))
                 for n in ARQUIVOS_OBRIGATORIOS
                 if os.path.exists(os.path.join(dir_video, n))}

    if "guia_de_estudo.md" in conteudos:
        topo = conteudos["guia_de_estudo.md"][:1200]
        faltando = [campo for campo in CAMPOS_METADADOS if campo not in topo]
        if faltando:
            rel.erro(f"guia_de_estudo.md sem os metadados: {', '.join(faltando)}")
        else:
            rel.ok("guia_de_estudo.md traz Categoria/Sistema/Assunto/Fonte/Confiança")

    for arquivo, minimo in TIMESTAMPS_MINIMOS.items():
        if arquivo not in conteudos:
            continue
        if sem_fonte:
            # não há mídia analisada: cobrar timestamp/âncora seria exigir o que a fonte não tem
            continue
        if tipo == "texto":
            ancoras = len(ANCORA_MENSAGEM.findall(conteudos[arquivo]))
            if ancoras < minimo:
                rel.erro(
                    f"{arquivo}: nenhuma âncora [Mnn] de mensagem encontrada "
                    f"(fonte textual declarada em metadados.md; esperado ≥ {minimo})"
                )
            else:
                rel.ok(f"{arquivo}: {ancoras} âncoras [Mnn] de mensagem")
            continue
        achados = len(TIMESTAMP.findall(conteudos[arquivo]))
        if achados < minimo:
            rel.erro(f"{arquivo}: nenhum timestamp HH:MM:SS encontrado (esperado ≥ {minimo})")
        else:
            rel.ok(f"{arquivo}: {achados} timestamps HH:MM:SS")

    if "perguntas.md" in conteudos:
        total = len(PERGUNTA.findall(conteudos["perguntas.md"]))
        if total < 10:
            rel.erro(f"perguntas.md com {total} perguntas (o roteiro pede ≥ 10)")
        else:
            rel.ok(f"perguntas.md com {total} perguntas")

    if "incertezas.md" in conteudos and not conteudos["incertezas.md"].strip():
        rel.erro("incertezas.md vazio")

    auditar_capturas(dir_video, rel)
    auditar_links(dir_video, rel)

    for raiz, _, arquivos in os.walk(dir_video):
        for nome_arq in arquivos:
            if nome_arq.endswith((".md", ".csv", ".txt", ".py", ".json")):
                auditar_privacidade(os.path.join(raiz, nome_arq), rel)
    return rel


def varrer_privacidade_geral(raiz: str, rel: Relatorio) -> None:
    alvos: list[str] = []
    for base, _, arquivos in os.walk(os.path.join(raiz, MATERIAIS)):
        alvos += [os.path.join(base, a) for a in arquivos if a.endswith((".md", ".csv", ".txt"))]
    for doc in ("STATUS.md", "README.md", "BAIXAR_VIDEO_SOB_DEMANDA.md", "PRIVACIDADE.md"):
        caminho = os.path.join(raiz, doc)
        if os.path.exists(caminho):
            alvos.append(caminho)
    for caminho in sorted(alvos):
        auditar_privacidade(caminho, rel)
    rel.ok(f"varredura de privacidade em {len(alvos)} arquivos")


def principal() -> int:
    p = argparse.ArgumentParser(description="Auditoria de qualidade e privacidade dos materiais derivados.")
    p.add_argument("--raiz", default=RAIZ, help="raiz do repositório")
    p.add_argument("--video", default=None, help="slug do vídeo em materiais/ (ex.: meu-video)")
    p.add_argument("--so-privacidade", action="store_true", help="executa apenas a varredura sensível")
    args = p.parse_args()

    raiz = os.path.abspath(args.raiz)
    pasta_materiais = os.path.join(raiz, MATERIAIS)
    if not os.path.isdir(pasta_materiais):
        print(f"[erro] pasta `{MATERIAIS}/` não encontrada em {raiz}")
        return 1

    rel = Relatorio()
    if args.so_privacidade:
        varrer_privacidade_geral(raiz, rel)
        rel.imprimir()
        return rel.codigo()

    alvos: list[str] = []
    if args.video:
        caminho = os.path.join(pasta_materiais, args.video)
        if not os.path.isdir(caminho):
            rel.erro(f"diretório do vídeo não existe: {MATERIAIS}/{args.video}")
            rel.imprimir()
            return rel.codigo()
        alvos = [caminho]
    else:
        for nome in sorted(os.listdir(pasta_materiais)):
            caminho = os.path.join(pasta_materiais, nome)
            if not os.path.isdir(caminho) or nome in PASTAS_RESERVADAS:
                continue
            tem_materiais = any(
                os.path.exists(os.path.join(caminho, arq))
                for arq in ("transcricao.md", "metadados.md", "guia_de_estudo.md")
            )
            if tem_materiais:
                alvos.append(caminho)
            else:
                rel.aviso(f"materiais/{nome} não tem arquivos de vídeo (ignorado na auditoria por vídeo)")
        if not alvos:
            print("nenhum diretório de vídeo em materiais/ ainda — nada a auditar por vídeo.")

    for alvo in alvos:
        parcial = auditar_video(alvo)
        rel.info += parcial.info
        rel.avisos += parcial.avisos
        rel.erros += parcial.erros
        rel.privacidade += parcial.privacidade

    print("\n=== varredura de privacidade (materiais/ e documentos de controle) ===")
    varrer_privacidade_geral(raiz, rel)
    rel.imprimir()
    return rel.codigo()


if __name__ == "__main__":
    sys.exit(principal())
