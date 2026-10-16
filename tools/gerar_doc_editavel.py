#!/usr/bin/env python3
"""Converte o material de consulta (HTML) em uma versão .docx editável.

O .docx é a mesma matéria do HTML, reorganizada para edição no Word:

- capítulos em Título 1, assuntos em Título 2 e cada ficha em Título 3 — dá para navegar pelo
  Painel de Navegação (Exibir › Painel de Navegação) e recolher/expandir seções pelo triângulo
  ao lado do título;
- tabelas nativas (com cabeçalho repetido em cada página), listas com marcadores e numeração,
  blocos de código em fonte monoespaçada sobre fundo cinza, notas e avisos em caixas coloridas;
- rodapé com número de página e um Sumário no começo com os capítulos do material.

O material continua autocontido e sem referências internas de arquivo. A conversão lê o mesmo
HTML publicado (`material-de-estudo/base-de-conhecimento-funcao-sistemas.html`), então o conteúdo
do .docx acompanha o do HTML.

Requisito: `pip install python-docx`
Uso: python3 tools/gerar_doc_editavel.py [--html ARQUIVO] [--saida ARQUIVO] [--sem-distribuivel]
"""

from __future__ import annotations

import argparse
import datetime
import html as _html
import hashlib
import os
import re
import zipfile
from html.parser import HTMLParser

try:  # dependência opcional: só este gerador precisa dela
    from docx import Document
    from docx.enum.style import WD_STYLE_TYPE
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
    from docx.oxml import OxmlElement, parse_xml
    from docx.oxml.ns import nsdecls, qn
    from docx.shared import Cm, Pt, RGBColor
except ImportError as erro:  # pragma: no cover - mensagem para quem roda o gerador
    raise SystemExit(
        "python-docx não está instalado (%s).\nInstale com: pip install python-docx" % erro
    )

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOME_HTML = "base-de-conhecimento-funcao-sistemas.html"
NOME_DOCX = "base-de-conhecimento-funcao-sistemas.docx"
CAMINHO_HTML = os.path.join(RAIZ, "material-de-estudo", NOME_HTML)
CAMINHO_DOCX = os.path.join(RAIZ, "material-de-estudo", NOME_DOCX)

COR = {
    "azul": "123A63",
    "azul-claro": "1E5A92",
    "teal": "0F766E",
    "texto": "1F2937",
    "suave": "4B5563",
    "cinza": "EEF2F6",
    "aviso": "FDF3E3",
    "destaque": "EAF1F9",
    "borda": "D7DEE8",
    "branco": "FFFFFF",
}

MESMA_DATA = (2026, 10, 15, 12, 0, 0)

# O Word recusa caracteres de controle; marcas internas de conversão de markdown também não são
# conteúdo e saem do texto (o gerador do HTML já falha se alguma escapar).
CONTROLE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")  # data fixa do material: mantém o .docx reproduzível

VAZIOS = {"br", "hr", "img", "input", "meta", "link", "col", "source", "wbr", "area", "base",
          "embed", "track", "param"}
# nada disso entra no documento: é interface do HTML (busca, botões, menu lateral, roteiro)
DESCARTAR = {("script", None), ("style", None), ("input", None), ("nav", "lateral"),
             ("div", "barra"), ("div", "vazio"), ("button", None)}
# blocos "de caixa" (fundo colorido): dentro deles um título vira linha em negrito, não Título
CAIXAS = {"aviso", "destaque"}


class Elemento:
    """Nó simples da árvore montada a partir do HTML."""

    __slots__ = ("tag", "attrs", "filhos")

    def __init__(self, tag: str, attrs: dict[str, str] | None = None) -> None:
        self.tag = tag
        self.attrs = attrs or {}
        self.filhos: list[Elemento] = []

    @property
    def classes(self) -> set[str]:
        return set((self.attrs.get("class") or "").split())

    def __repr__(self) -> str:  # pragma: no cover - depuração
        return "<%s %s>" % (self.tag, " ".join(sorted(self.classes)))


class ConstrutorHTML(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.raiz = Elemento("#raiz")
        self.pilha = [self.raiz]

    def handle_starttag(self, tag, attrs):  # noqa: D102
        no = Elemento(tag, {k: (v or "") for k, v in attrs})
        self.pilha[-1].filhos.append(no)
        if tag not in VAZIOS:
            self.pilha.append(no)

    def handle_startendtag(self, tag, attrs):  # noqa: D102
        self.pilha[-1].filhos.append(Elemento(tag, {k: (v or "") for k, v in attrs}))

    def handle_endtag(self, tag):  # noqa: D102
        for i in range(len(self.pilha) - 1, 0, -1):
            if self.pilha[i].tag == tag:
                del self.pilha[i:]
                return

    def handle_data(self, data):  # noqa: D102
        no = Elemento("#texto")
        no.attrs["dados"] = data
        self.pilha[-1].filhos.append(no)


# ------------------------------------------------------------------ utilidades de árvore


IDS_DE_INTERFACE = {"vazio", "busca", "topo", "expandir", "recolher", "baixar"}


def descartavel(no: Elemento) -> bool:
    if no.attrs.get("id") in IDS_DE_INTERFACE:
        return True
    for tag, classe in DESCARTAR:
        if no.tag == tag and (classe is None or classe in no.classes):
            return True
    return False


def limpar_arvore(no: Elemento) -> None:
    no.filhos = [f for f in no.filhos if not descartavel(f)]
    for filho in no.filhos:
        limpar_arvore(filho)


def achar(no: Elemento, tag: str, classe: str | None = None) -> Elemento | None:
    for filho in no.filhos:
        if filho.tag == tag and (classe is None or classe in filho.classes):
            return filho
    return None


def achar_todos(no: Elemento, tag: str, classe: str | None = None) -> list[Elemento]:
    achados = []
    if no.tag == tag and (classe is None or classe in no.classes):
        achados.append(no)
    for filho in no.filhos:
        achados.extend(achar_todos(filho, tag, classe))
    return achados


def buscar(no: Elemento, tag: str, classe: str | None = None) -> Elemento | None:
    """Primeiro elemento com essa tag/classe em toda a árvore (busca em profundidade)."""
    achados = achar_todos(no, tag, classe)
    return achados[0] if achados else None


def texto_visivel(no: Elemento, espaco: str = " ") -> str:
    """Todo o texto da árvore (usado para conferir que nada ficou fora do .docx)."""
    if no.tag == "#texto":
        return re.sub(r"\s+", " ", no.attrs["dados"])
    pedacos = [texto_visivel(f) for f in no.filhos]
    return espaco.join(p for p in pedacos if p.strip())


def enxugar(linhas: list[str]) -> str:
    texto = " ".join(linhas)
    return re.sub(r"\s+", " ", texto).strip()


# ------------------------------------------------------------------ estilos do documento


def _sucessores(tipo: str, a_partir: str | None = None) -> tuple[str, ...]:
    """Ordem dos elementos filhos exigida pelo Word; `a_partir` corta a lista na posição certa.

    A ordem importa: `pBdr` vem antes de `shd`, e os dois antes de `spacing`/`ind`. Inserir fora de
    ordem faz o Word reclamar do arquivo.
    """
    lista = (
        ("w:pBdr", "w:shd", "w:tabs", "w:suppressAutoHyphens", "w:kinsoku", "w:wordWrap",
                "w:overflowPunct", "w:topLinePunct", "w:autoSpaceDE", "w:autoSpaceDN", "w:bidi",
                "w:adjustRightInd", "w:snapToGrid", "w:spacing", "w:ind", "w:contextualSpacing",
            "w:mirrorIndents", "w:suppressOverlap", "w:jc", "w:textDirection",
            "w:textAlignment", "w:textboxTightWrap", "w:outlineLvl", "w:divId", "w:cnfStyle",
            "w:rPr", "w:sectPr", "w:pPrChange")
        if tipo == "pPr" else
        ("w:tcBorders", "w:shd", "w:noWrap", "w:tcMar", "w:textDirection", "w:tcFitText",
         "w:vAlign", "w:hideMark", "w:headers", "w:cellIns", "w:cellDel", "w:cellMerge",
         "w:tcPrChange")
    )
    if a_partir and a_partir in lista:
        lista = lista[lista.index(a_partir):]
    return lista


def fundo(pPr, cor: str) -> None:
    shd = parse_xml('<w:shd %s w:val="clear" w:color="auto" w:fill="%s"/>' % (nsdecls("w"), cor))
    pPr.insert_element_before(shd, *_sucessores("pPr", a_partir="w:tabs"))


def borda_esquerda(pPr, cor: str, tamanho: int = 18) -> None:
    pBdr = parse_xml(
        '<w:pBdr %s><w:left w:val="single" w:sz="%d" w:space="6" w:color="%s"/></w:pBdr>'
        % (nsdecls("w"), tamanho, cor)
    )
    pPr.insert_element_before(pBdr, *_sucessores("pPr", a_partir="w:pBdr"))


def estilo_novo(doc, nome: str):
    return doc.styles.add_style(nome, WD_STYLE_TYPE.PARAGRAPH)


def configurar_estilos(doc) -> None:
    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = RGBColor.from_string(COR["texto"])
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.12

    titulos = {
        "Title": (26, True, COR["azul"], 0, 4),
        "Subtitle": (12, False, COR["suave"], 0, 14),
        "Heading 1": (19, True, COR["azul"], 0, 8),
        "Heading 2": (14, True, COR["azul-claro"], 16, 6),
        "Heading 3": (11.5, True, COR["teal"], 11, 3),
    }
    for nome, (tam, negrito, cor, antes, depois) in titulos.items():
        st = doc.styles[nome]
        st.font.name = "Calibri"
        st.font.size = Pt(tam)
        st.font.bold = negrito
        st.font.italic = False
        st.font.color.rgb = RGBColor.from_string(cor)
        st.paragraph_format.space_before = Pt(antes)
        st.paragraph_format.space_after = Pt(depois)
        st.paragraph_format.keep_with_next = nome in ("Heading 1", "Heading 2", "Heading 3")

    doc.styles["Title"].paragraph_format.keep_with_next = True
    doc.styles["Heading 1"].paragraph_format.page_break_before = True

    legenda = estilo_novo(doc, "Legenda")
    legenda.base_style = doc.styles["Normal"]
    legenda.font.size = Pt(10)
    legenda.font.italic = True
    legenda.font.color.rgb = RGBColor.from_string(COR["suave"])
    legenda.paragraph_format.space_after = Pt(10)

    codigo = estilo_novo(doc, "Codigo")
    codigo.base_style = doc.styles["Normal"]
    codigo.font.name = "Consolas"
    codigo.font.size = Pt(8.5)
    codigo.font.color.rgb = RGBColor.from_string("0F172A")
    codigo.paragraph_format.space_before = Pt(0)
    codigo.paragraph_format.space_after = Pt(0)
    codigo.paragraph_format.line_spacing = 1.0
    codigo.paragraph_format.left_indent = Cm(0.5)
    codigo.paragraph_format.keep_together = True
    _fundo_estilo(codigo, COR["cinza"])

    nota = estilo_novo(doc, "Nota")
    nota.base_style = doc.styles["Normal"]
    nota.font.size = Pt(9.5)
    nota.font.italic = True
    nota.font.color.rgb = RGBColor.from_string(COR["suave"])
    nota.paragraph_format.left_indent = Cm(0.5)
    nota.paragraph_format.space_before = Pt(4)

    for nome, cor_fundo, cor_borda in (("Aviso", COR["aviso"], "B45309"),
                                       ("Destaque", COR["destaque"], COR["azul-claro"])):
        st = estilo_novo(doc, nome)
        st.base_style = doc.styles["Normal"]
        st.font.size = Pt(10.5)
        st.paragraph_format.left_indent = Cm(0.35)
        st.paragraph_format.right_indent = Cm(0.15)
        st.paragraph_format.space_before = Pt(4)
        st.paragraph_format.space_after = Pt(4)
        pPr = st.element.get_or_add_pPr()
        borda_esquerda(pPr, cor_borda)
        fundo(pPr, cor_fundo)

    rodape = estilo_novo(doc, "Rodape")
    rodape.base_style = doc.styles["Normal"]
    rodape.font.size = Pt(9)
    rodape.font.italic = True
    rodape.font.color.rgb = RGBColor.from_string(COR["suave"])
    rodape.paragraph_format.space_before = Pt(14)


def _fundo_estilo(st, cor: str) -> None:
    fundo(st.element.get_or_add_pPr(), cor)


# ------------------------------------------------------------------ conversão


class Conversor:
    def __init__(self, raiz: Elemento, capitulos: list[str] | None = None) -> None:
        self.raiz = raiz
        self.capitulos = capitulos or []
        self.doc = Document()
        self.marcadores: set[str] = set()
        self.usados: list[str] = []
        self.proximo_id = 0
        self.quebrados: list[str] = []
        self.codigos = 0
        self.tabelas = 0
        self.fichas = 0
        self.texto: list[str] = []
        for no in self._todos(raiz):
            ident = no.attrs.get("id")
            if ident:
                self.marcadores.add(self._nome_marcador(ident))

    # -- utilidades ---------------------------------------------------------------
    @staticmethod
    def _todos(no: Elemento):
        yield no
        for filho in no.filhos:
            yield from Conversor._todos(filho)

    @staticmethod
    def _nome_marcador(ident: str) -> str:
        return re.sub(r"[^A-Za-z0-9_]", "_", ident)[:40]

    def _guardar(self, texto: str) -> None:
        if texto:
            self.texto.append(texto)

    def _hyperlink(self, p, texto: str, ancora: str) -> None:
        nome = self._nome_marcador(ancora)
        if nome not in self.marcadores:
            self.quebrados.append(ancora)
            self._run(p, texto)
            return
        self.usados.append(ancora)
        h = OxmlElement("w:hyperlink")
        h.set(qn("w:anchor"), nome)
        h.set(qn("w:history"), "1")
        r = OxmlElement("w:r")
        rPr = OxmlElement("w:rPr")
        cor = OxmlElement("w:color")
        cor.set(qn("w:val"), COR["azul-claro"])
        sub = OxmlElement("w:u")
        sub.set(qn("w:val"), "single")
        rPr.append(cor)
        rPr.append(sub)
        r.append(rPr)
        t = OxmlElement("w:t")
        t.set(qn("xml:space"), "preserve")
        t.text = texto
        r.append(t)
        h.append(r)
        p._p.append(h)
        self._guardar(texto)

    def _run(self, p, texto: str, negrito=False, italico=False, codigo=False, cor=None):
        texto = CONTROLE.sub("", texto)
        if not texto:
            return None
        r = p.add_run(texto)
        r.bold = negrito or None
        r.italic = italico or None
        if codigo:
            r.font.name = "Consolas"
            r.font.size = Pt(9)
            r.font.color.rgb = RGBColor.from_string("0F172A")
        if cor:
            r.font.color.rgb = RGBColor.from_string(cor)
        return r

    def _marcador(self, p, ident: str) -> None:
        nome = self._nome_marcador(ident)
        self.proximo_id += 1  # id sequencial: `hash()` varia entre execuções
        inicio = OxmlElement("w:bookmarkStart")
        inicio.set(qn("w:id"), str(self.proximo_id))
        inicio.set(qn("w:name"), nome)
        fim = OxmlElement("w:bookmarkEnd")
        fim.set(qn("w:id"), inicio.get(qn("w:id")))
        p._p.insert(0, inicio)
        p._p.append(fim)

    # -- conteúdo inline ----------------------------------------------------------
    def inline(self, nos: list[Elemento], p, negrito=False, italico=False, caixa=False) -> None:
        for no in nos:
            if no.tag == "#texto":
                texto = re.sub(r"\s+", " ", no.attrs["dados"])
                if texto.strip() == "" and not texto:
                    continue
                self._run(p, texto, negrito, italico)
                self._guardar(texto)
            elif no.tag in ("b", "strong"):
                self.inline(no.filhos, p, True, italico, caixa)
            elif no.tag in ("i", "em"):
                self.inline(no.filhos, p, negrito, True, caixa)
            elif no.tag == "code":
                texto = enxugar([texto_visivel(no)])
                self._run(p, texto, negrito, italico, codigo=True)
                self._guardar(texto)
            elif no.tag == "a":
                href = no.attrs.get("href", "")
                texto = enxugar([texto_visivel(no)])
                if href.startswith("#"):
                    self._hyperlink(p, texto, href[1:])
                else:
                    self._run(p, texto, negrito, italico, cor=COR["azul-claro"])
                    self._guardar(texto)
            elif no.tag == "br":
                p.add_run().add_break()
            elif no.tag == "p":
                if p.runs:
                    p.add_run().add_break()
                self.inline(no.filhos, p, negrito, italico, caixa)
            elif no.tag in ("ul", "ol"):
                self.listas(no, 0)
            elif no.tag in ("table", "pre", "details"):
                self.bloco(no, caixa)
            else:
                self.inline(no.filhos, p, negrito, italico, caixa)

    # -- blocos -------------------------------------------------------------------
    def paragrafo(self, estilo: str | None = None):
        p = self.doc.add_paragraph(style=estilo)
        return p

    def titulo(self, nivel: int, texto: str, ident: str | None = None):
        p = self.doc.add_paragraph(texto, style="Heading %d" % nivel)
        if ident:
            self._marcador(p, ident)
        self._guardar(texto)
        return p

    def caixa_paragrafo(self, estilo: str, conteudo: list[Elemento]) -> None:
        primeiro = conteudo[0] if conteudo else None
        if primeiro is not None and primeiro.tag in ("h3", "h4"):
            p = self.doc.add_paragraph(style=estilo)
            self._run(p, enxugar([texto_visivel(primeiro)]), negrito=True)
            self._guardar(enxugar([texto_visivel(primeiro)]))
            conteudo = conteudo[1:]
        atual = None
        for no in conteudo:
            if no.tag in ("p", "ul", "ol", "table", "div"):
                if no.tag == "div":
                    atual = self.caixa_paragrafo(estilo, no.filhos)
                    continue
                atual = None
                self.bloco(no, caixa=estilo)
            elif no.tag in ("h3", "h4"):
                p = self.doc.add_paragraph(style=estilo)
                self._run(p, enxugar([texto_visivel(no)]), negrito=True)
                self._guardar(enxugar([texto_visivel(no)]))
            elif no.tag == "#texto" and not no.attrs["dados"].strip():
                continue
            else:
                if atual is None:
                    atual = self.doc.add_paragraph(style=estilo)
                self.inline([no], atual, caixa=True)

    def listas(self, no: Elemento, nivel: int) -> None:
        ordenada = no.tag == "ol"
        base = "List Number" if ordenada else "List Bullet"
        nome = base if nivel == 0 else "%s %d" % (base, min(nivel + 1, 3))
        if nome not in [s.name for s in self.doc.styles]:
            nome = base
        for item in no.filhos:
            if item.tag != "li":
                continue
            p = self.doc.add_paragraph(style=nome)
            self.inline(item.filhos, p)
            self._guardar(enxugar([texto_visivel(item)]))

    def tabela(self, no: Elemento) -> None:
        linhas: list[tuple[bool, Elemento]] = []
        for parte in no.filhos:
            if parte.tag in ("thead", "tbody", "tfoot"):
                linhas.extend((parte.tag == "thead", tr) for tr in parte.filhos if tr.tag == "tr")
            elif parte.tag == "tr":
                linhas.append((False, parte))
        if not linhas:
            return
        colunas = max(len([c for c in tr.filhos if c.tag in ("td", "th")]) for _, tr in linhas)
        tabela = self.doc.add_table(rows=0, cols=colunas)
        tabela.style = "Table Grid"
        for indice, (cabecalho, tr) in enumerate(linhas):
            linha = tabela.add_row()
            celulas = [c for c in tr.filhos if c.tag in ("td", "th")]
            for i, celula in enumerate(celulas):
                if i >= colunas:
                    break
                destino = linha.cells[i]
                destino.text = ""
                p = destino.paragraphs[0]
                p.paragraph_format.space_after = Pt(2)
                if cabecalho or celula.tag == "th":
                    self.inline(celula.filhos, p, negrito=True)
                    for r in p.runs:
                        r.font.color.rgb = RGBColor.from_string(COR["branco"])
                else:
                    self.inline(celula.filhos, p)
                if cabecalho or celula.tag == "th":
                    tcPr = destino._tc.get_or_add_tcPr()
                    shd = parse_xml('<w:shd %s w:val="clear" w:color="auto" w:fill="%s"/>'
                                    % (nsdecls("w"), COR["azul"]))
                    tcPr.insert_element_before(shd, *_sucessores("tcPr"))
            if indice == 0 and (cabecalho or linhas[0][0]):
                trPr = linha._tr.get_or_add_trPr()
                trPr.append(OxmlElement("w:tblHeader"))
        self.tabelas += 1
        self.doc.add_paragraph()

    def codigo(self, no: Elemento) -> None:
        texto = "".join(f.attrs["dados"] if f.tag == "#texto" else texto_visivel(f)
                        for f in no.filhos)
        linhas = texto.strip("\n").split("\n")
        paragrafos = []
        for linha in linhas:
            p = self.doc.add_paragraph(style="Codigo")
            self._run(p, CONTROLE.sub("", linha).replace("\t", "    ") or " ", codigo=True)
            paragrafos.append(p)
        if paragrafos:
            paragrafos[0].paragraph_format.space_before = Pt(6)
            paragrafos[-1].paragraph_format.space_after = Pt(8)
            for a, b in zip(paragrafos, paragrafos[1:]):
                a.paragraph_format.keep_with_next = True
        self.codigos += 1
        self._guardar(texto)

    def bloco(self, no: Elemento, caixa: str | None = None) -> None:
        tag = no.tag
        if tag == "#texto":
            texto = re.sub(r"\s+", " ", no.attrs["dados"])
            if texto.strip():
                p = self.doc.add_paragraph(style=caixa) if caixa else self.doc.add_paragraph()
                self._run(p, texto)
                self._guardar(texto)
            return
        if descartavel(no):
            return
        if "aviso" in no.classes:
            return self.caixa_paragrafo("Aviso", no.filhos)
        if "destaque" in no.classes:
            return self.caixa_paragrafo("Destaque", no.filhos)
        if tag in ("script", "style", "nav", "button", "input"):
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            texto = enxugar([texto_visivel(no)])
            if not texto:
                return
            if "cap-titulo" in no.classes:
                return self.titulo(1, texto, no.attrs.get("id"))
            if caixa:
                p = self.doc.add_paragraph(style=caixa)
                self._run(p, texto, negrito=True)
                self._guardar(texto)
                return
            # título de subseção (assunto do capítulo) fica no nível 2; o que aparece dentro de
            # uma síntese desce para o nível 4, deixando o nível 3 só para as fichas
            if tag == "h3" or "assunto" in no.classes:
                return self.titulo(2, texto, no.attrs.get("id"))
            return self.titulo(4, texto, no.attrs.get("id"))
        if tag == "p":
            if "cap-desc" in no.classes:
                p = self.doc.add_paragraph(style="Legenda")
                self.inline(no.filhos, p)
                return
            estilo = "Nota" if "nota" in no.classes else caixa
            p = self.doc.add_paragraph(style=estilo)
            self.inline(no.filhos, p, caixa=bool(caixa))
            return
        if tag in ("ul", "ol"):
            if caixa:
                for item in no.filhos:
                    if item.tag != "li":
                        continue
                    p = self.doc.add_paragraph(style=caixa)
                    self._run(p, "•  ", negrito=False)
                    self.inline(item.filhos, p, caixa=True)
            else:
                self.listas(no, 0)
            return
        if tag == "table":
            self.tabela(no)
            return
        if tag == "pre":
            self.codigo(no)
            return
        if tag == "details":
            resumo = achar(no, "summary")
            ident = no.attrs.get("id")
            if resumo is not None:
                texto = enxugar([texto_visivel(resumo)])
                p = self.titulo(3, texto, ident)
                self.fichas += 1
            else:
                p = None
            antes = len(self.doc.paragraphs)
            corpo = achar(no, "div", "bloco-corpo")
            for filho in (corpo.filhos if corpo is not None else no.filhos):
                if filho is resumo:
                    continue
                self.bloco(filho, caixa)
            for parag in self.doc.paragraphs[antes:]:
                atual = parag.paragraph_format.left_indent
                if atual is None or atual < Cm(0.45):
                    parag.paragraph_format.left_indent = Cm(0.45)
            return
        if tag == "footer" and "rodape" in no.classes:
            texto = enxugar([texto_visivel(no)])
            p = self.doc.add_paragraph(style="Rodape")
            self._run(p, texto)
            self._guardar(texto)
            return
        if tag in ("hr", "br", "img", "span", "summary", "div", "section", "article", "main",
                   "header", "footer", "li", "thead", "tbody", "tr", "td", "th", "a", "b",
                   "strong", "i", "em", "code"):
            if tag == "span" and not no.filhos:
                return
            if tag in ("li", "td", "th", "tr", "thead", "tbody", "summary"):
                self.inline(no.filhos, self.doc.add_paragraph())
                return
            for filho in no.filhos:
                self.bloco(filho, caixa)
            return
        for filho in no.filhos:
            self.bloco(filho, caixa)

    # -- montagem -----------------------------------------------------------------
    def capa(self, topo: Elemento) -> None:
        h1 = buscar(topo, "h1")
        sub = buscar(topo, "p", "sub")
        chips = buscar(topo, "div", "chips")
        if h1 is not None:
            p = self.doc.add_paragraph(enxugar([texto_visivel(h1)]), style="Title")
            self._guardar(enxugar([texto_visivel(h1)]))
        if sub is not None:
            p = self.doc.add_paragraph(style="Subtitle")
            self.inline(sub.filhos, p)
        if chips is not None:
            itens = [enxugar([texto_visivel(c)]) for c in achar_todos(chips, "span")]
            p = self.doc.add_paragraph()
            self._run(p, "  ·  ".join(i for i in itens if i), cor=COR["suave"])
            self._guardar(" ".join(itens))
        p = self.doc.add_paragraph(style="Legenda")
        self._run(
            p,
            "Versão editável do material de consulta, gerada a partir da versão publicada em HTML. "
            "Mesmo conteúdo, organizado em títulos, tabelas e listas para edição no Word.",
        )

    def sumario(self) -> None:
        capitulos = self.capitulos
        self.titulo(1, "Sumário")
        p = self.doc.add_paragraph()
        self._run(
            p,
            "No Word, use Exibir › Painel de Navegação para ir direto a qualquer capítulo ou ficha, "
            "ou clique no triângulo ao lado de um título para recolher e expandir a seção. "
            "As fichas ficam no terceiro nível de título.",
        )
        for i, titulo in enumerate(capitulos, 1):
            p = self.doc.add_paragraph()
            p.paragraph_format.space_after = Pt(2)
            self._run(p, "%d. %s" % (i, titulo), negrito=True)
            self._guardar(titulo)

    def rodape_paginas(self) -> None:
        secao = self.doc.sections[0]
        p = secao.footer.paragraphs[0]
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        self._run(p, "Base de conhecimento — Função Sistemas  ·  página ", cor=COR["suave"])
        self._campo(p, "PAGE")
        self._run(p, " de ", cor=COR["suave"])
        self._campo(p, "NUMPAGES")
        for r in p.runs:
            r.font.size = Pt(8.5)

    def _campo(self, p, instrucao: str, valor: str = "1") -> None:
        """Campo do Word (página, total de páginas) com um resultado já preenchido."""
        for tipo, conteudo in (("begin", None), ("separate", None), (None, instrucao)):
            r = p.add_run()
            if tipo is None:
                texto = OxmlElement("w:instrText")
                texto.set(qn("xml:space"), "preserve")
                texto.text = " %s " % conteudo
                r._r.append(texto)
            else:
                marca = OxmlElement("w:fldChar")
                marca.set(qn("w:fldCharType"), tipo)
                r._r.append(marca)
            r.font.size = Pt(8.5)
        r = p.add_run(valor)
        r.font.size = Pt(8.5)
        r = p.add_run()
        fim = OxmlElement("w:fldChar")
        fim.set(qn("w:fldCharType"), "end")
        r._r.append(fim)
        r.font.size = Pt(8.5)

    def converter(self) -> None:
        configurar_estilos(self.doc)
        topo = buscar(self.raiz, "header", "topo")
        main = buscar(self.raiz, "main")
        if topo is not None:
            self.capa(topo)
        self.sumario()
        if main is not None:
            for filho in main.filhos:
                self.bloco(filho)
        self.rodape_paginas()

        props = self.doc.core_properties
        props.title = "Base de conhecimento — Função Sistemas"
        props.subject = "Material de consulta interno (versão editável)"
        props.author = "Função Sistemas"
        props.comments = ("Mesmo conteúdo do material publicado em HTML. Uso interno; não substitui "
                          "especificação, runbook ou validação do responsável de cada frente.")
        # data fixa: duas execuções geram o mesmo arquivo
        props.created = datetime.datetime(*MESMA_DATA[:3], 9, 0, 0)
        props.modified = datetime.datetime(*MESMA_DATA[:3], 9, 0, 0)
        props.revision = 1


# ------------------------------------------------------------------ empacotamento


def escrever_docx(doc, caminho: str) -> bytes:
    """Salva o .docx de forma reproduzível: data fixa em todas as partes do pacote."""
    os.makedirs(os.path.dirname(os.path.abspath(caminho)), exist_ok=True)
    doc.save(caminho)
    with zipfile.ZipFile(caminho) as origem:
        partes = [(n, origem.read(n)) for n in origem.namelist()]
    with zipfile.ZipFile(caminho, "w", zipfile.ZIP_DEFLATED) as destino:
        for nome, dados in partes:
            info = zipfile.ZipInfo(nome, date_time=MESMA_DATA)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            destino.writestr(info, dados)
    with open(caminho, "rb") as fh:
        return fh.read()


def conferir(caminho: str, esperado: str) -> list[str]:
    """Confere o pacote gerado: XML bem formado, texto presente, nada de HTML cru."""
    from xml.dom import minidom

    problemas = []
    with zipfile.ZipFile(caminho) as pacote:
        ruins = pacote.testzip()
        if ruins:
            problemas.append("pacote corrompido em %s" % ruins)
        for nome in pacote.namelist():
            if nome.endswith(".xml") or nome.endswith(".rels"):
                try:
                    minidom.parseString(pacote.read(nome))
                except Exception as erro:  # pragma: no cover - só aparece se o XML quebrar
                    problemas.append("XML inválido em %s: %s" % (nome, erro))
        texto = pacote.read("word/document.xml").decode("utf-8")

    visivel = re.sub(r"<[^>]+>", "", texto)
    visivel = re.sub(r"\s+", " ", _html.unescape(visivel))
    if len(visivel) < len(esperado) * 0.9:
        problemas.append("texto do .docx (%d) bem menor que o do HTML (%d)"
                         % (len(visivel), len(esperado)))
    for marca in ("<p>", "</p>", "class=\"", "<code>", "&amp;lt;"):
        if marca in visivel:
            problemas.append("sobrou HTML cru no documento: %s" % marca)
    return problemas


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--html", default=CAMINHO_HTML)
    p.add_argument("--saida", default=os.path.join(RAIZ, "saida", NOME_DOCX))
    p.add_argument("--sem-distribuivel", action="store_true",
                   help="não escreve a cópia publicada em material-de-estudo/")
    args = p.parse_args()

    if not os.path.exists(args.html):
        print("[falha] não encontrei o material em HTML: %s" % args.html)
        return 1

    with open(args.html, encoding="utf-8") as fh:
        marcação = fh.read()

    construtor = ConstrutorHTML()
    construtor.feed(marcação)

    # o índice do material está no menu lateral do HTML — que é interface e sai do documento;
    # os títulos são lidos antes, para montar o Sumário
    nav = buscar(construtor.raiz, "nav", "lateral")
    capitulos = []
    for link in (achar_todos(nav, "a") if nav is not None else []):
        texto = enxugar([texto_visivel(link)])
        if texto:
            capitulos.append(texto)

    limpar_arvore(construtor.raiz)

    esperado = texto_visivel(construtor.raiz)
    conversor = Conversor(construtor.raiz, capitulos)
    conversor.converter()

    problemas = conferir_documento(conversor, esperado)
    if problemas:
        for problema in problemas:
            print("[falha] %s" % problema)
        return 1

    dados = escrever_docx(conversor.doc, args.saida)
    if not args.sem_distribuivel:
        escrever_docx(conversor.doc, CAMINHO_DOCX)

    print(
        "gerado: %s (%.1f KB) — %d capítulos, %d fichas, %d tabelas, %d blocos de código"
        % (args.saida, len(dados) / 1024, len(achar_todos(construtor.raiz, "h2", "cap-titulo")),
           conversor.fichas, conversor.tabelas, conversor.codigos)
    )
    print("sha256: %s" % hashlib.sha256(dados).hexdigest()[:16])
    return 0


def conferir_documento(conversor: "Conversor", esperado: str) -> list[str]:
    problemas = []
    if conversor.quebrados:
        problemas.append("ligações para âncoras inexistentes: %s" % sorted(set(conversor.quebrados)))
    produzido = " ".join(conversor.texto)
    produzido = re.sub(r"\s+", " ", produzido)
    if len(produzido) < len(esperado) * 0.9:
        problemas.append("texto convertido (%d) bem menor que o do HTML (%d)"
                         % (len(produzido), len(esperado)))
    return problemas


if __name__ == "__main__":
    raise SystemExit(main())
