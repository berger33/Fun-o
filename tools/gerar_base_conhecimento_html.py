#!/usr/bin/env python3
"""Gera o material de estudo em HTML único a partir dos derivados do acervo.

Regras do material gerado:
- inclui **apenas conhecimento** (guias, procedimentos, glossários, perguntas, pendências e
  índices temáticos). Transcrições brutas e documentos de processo do repositório ficam fora;
- **não** menciona nomes de arquivo, pastas, ligações internas nem identificadores de mídia:
  as fontes aparecem por rótulo descritivo neutro ("Conversa técnica — ...", "Treinamento — ...");
- não lê a área restrita (material pessoal, fora do Git);
- saída autocontida (CSS/JS embutidos, sem dependência de rede) em `saida/index.html`.

Uso: python3 tools/gerar_base_conhecimento_html.py [--saida saida/index.html]
"""

from __future__ import annotations

import argparse
import csv
import html
import os
import re
import datetime

import markdown

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATERIAIS = os.path.join(RAIZ, "materiais")

# ---------------------------------------------------------------- catálogo de fontes

# slug -> (rótulo neutro, tipo, tema do guia)
FONTES = {
    "apresentacao-projeto-19-18": ("Reunião de projeto — CCB de refinanciamento, SIC Minutas e API de formalização", "Reunião", "negocio"),
    "gravando-2026-07-07-155307": ("Chamada de trabalho — início dos testes a partir da EPT e ambientação no Autorizador", "Chamada", "testes"),
    "gravando-2026-07-08-182343": ("Sessão de ambiente — componentes, versões e importação de teste de tolerância", "Sessão", "infra"),
    "gravando-2026-08-24-124650": ("Sessão técnica — execução de cenário, plugin e retorno em JSON", "Sessão", "api"),
    "gravando-2026-09-22-111258": ("Revisão de pacote (OS 586780) — documentos anexados no envio ao sistema externo", "Revisão", "api"),
    "gravando-2026-09-23-164626": ("Sessão técnica — anexação de documentos no GED e JSON do plugin", "Sessão", "api"),
    "gravando-2026-10-06-110907": ("Sessão de projeto — cancelamento de seguro por serviço externo", "Sessão", "negocio"),
    "gravando-2026-10-07-152044": ("Demonstração — despesas e tarifas do convênio; rastreio no monitor de serviços", "Demonstração", "negocio"),
    "jonas-ept-explicacao": ("Demonstração — investigação de integração no banco e preenchimento de EPT", "Demonstração", "testes"),
    "liberacao-padrao-glauco": ("Orientação — disponibilização padrão de pacote", "Orientação", "testes"),
    "michelle-ctc-portabilidade-refin": ("Discussão — portabilidade e refinanciamento (CTC)", "Discussão", "negocio"),
    "mcb-qista": ("Discussão — pontuação e certificação de promotora; esteira", "Discussão", "negocio"),
    "primeiro-projeto": ("Sessão de projeto — consulta de documentos anexados por API", "Sessão", "api"),
    "projeto-14-08": ("Reunião — CNPJ do empregador e identificador de simulação", "Reunião", "negocio"),
    "clientsecret-ewen-treinamento": ("Treinamento — credencial de integração, Test API e licenças", "Treinamento", "infra"),
    "como-fazer-ept": ("Aula — como montar a EPT e o recálculo com tolerância", "Aula", "testes"),
    "desaverbacao": ("Investigação — cancelamento e exclusão de averbação", "Investigação", "negocio"),
    "explicacao-mesa-c6": ("Treinamento — CQ, ambientes, planejamento e EF/EPT", "Treinamento", "testes"),
    "recalculo": ("Treinamento — limites, tolerância e recálculo do convênio", "Treinamento", "negocio"),
    "conversa-matheus-refin-api": ("Conversa técnica — inclusão de proposta de refinanciamento pela API", "Conversa", "api"),
    "conversa-jonas-testa-api": ("Conversa técnica — depuração de erro de modelo na API de inclusão", "Conversa", "api"),
    "conversa-cler-artefatos-acesso": ("Conversa de equipe — obtenção de artefatos de ambientação", "Conversa", "infra"),
    "conversa-oscar-automacao-testes": ("Conversa de equipe — automação de testes e trilha de estudo", "Conversa", "automacao"),
    "conversa-gabriel-comunicacao-estudos": ("Conversa com analista — comunicação de perfil e trilha de estudo", "Conversa", "comunicacao"),
}

# fontes cuja extração não rendeu conteúdo instrutivo (registradas como lacuna, sem corpo)
SEM_CONTEUDO = {
    "averbacao": "Investigação sobre averbação — fonte não obtida no período de análise",
    "projeto-ept": "Sessão sobre EPT — áudio sem reconhecimento utilizável",
    "gravando-2026-10-07-132428": "Sessão de tela — fonte não obtida no período de análise",
}

TEMAS = [
    ("negocio", "Negócio", "Produtos, convênios, despesas, portabilidade, refinanciamento, averbação e cálculos."),
    ("api", "API, integrações e payloads", "Serviços, endpoints, estruturas de envio, respostas e tratamento de erro."),
    ("testes", "Testes, qualidade e evidências", "EPT, cenários, execução de teste, disponibilização padrão e conferência."),
    ("infra", "Ambientes, infraestrutura e acesso", "Componentes, versões, credenciais de integração, licenças e artefatos de ambientação."),
    ("automacao", "Automação e IA aplicada", "Automação de testes, trilha de inteligência artificial e critérios de escolha do que automatizar."),
    ("comunicacao", "Comunicação e trabalho em equipe", "Como combinar expectativas, pedir ajuda e explicar o próprio jeito de trabalhar."),
]

# ---------------------------------------------------------------- limpeza de texto

NOMES_DE_MIDIA: list[str] = []


def carregar_nomes_de_midia() -> None:
    """Nomes de arquivos de mídia do manifesto — usados apenas para removê-los do material."""
    caminho = os.path.join(RAIZ, "manifesto.csv")
    if not os.path.exists(caminho):
        return
    with open(caminho, encoding="utf-8", errors="replace") as fh:
        for linha in csv.DictReader(fh):
            for chave, valor in linha.items():
                if valor and ("arquivo" in chave.lower() or "nome" in chave.lower()):
                    NOMES_DE_MIDIA.append(valor.strip())
                    NOMES_DE_MIDIA.append(valor.strip() + ".part001")


ARQUIVO_RE = re.compile(r"[A-Za-zÀ-ÿ0-9_\-\.]*(?:\.(?:md|mp4|png|jpe?g|json|txt|srt|vtt|csv|ya?ml|xlsx|docx|pdf))\b", re.I)
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]*)\)")
ANCORA_RE = re.compile(r"\[M(\d{2,})\]")
SECAO_RE = re.compile(r"§+\s*([\d\.]+)")


def equilibrar_crases(texto: str) -> str:
    """Conserta linhas com número ímpar de crases (quebram o negrito na conversão).

    Alguns documentos trazem trechos com crase desbalanceada (artefato de leitura de tela).
    Nesses casos, trechos de um único caractere entre crases são unidos e, se a contagem
    continuar ímpar, as crases restantes daquela linha são removidas.
    """
    saida: list[str] = []
    for linha in texto.splitlines():
        if linha.count("`") % 2 == 0:
            saida.append(linha)
            continue
        novo = re.sub(r"`([^`\n])`", r"\1", linha)
        if novo.count("`") % 2 == 1:
            novo = novo.replace("`", "")
        saida.append(novo)
    return "\n".join(saida)


# vocabulário de controle interno do acervo (não é conhecimento sobre o trabalho):
# linhas e subseções que falam de arquivo, ponteiro, integridade e versionamento saem do material
RUIDO_INTERNO = re.compile(
    r"(?i)\b(?:manifesto|oid|\blfs\b|ponteiro|checksum|sha-?256|branch|commit|git\b|"
    r"duplicata|duplicidade|byte a byte|bytes conferidos)\b"
)

SUBSECAO_INTERNA = re.compile(
    r"(?im)^(#{2,4})\s+([^\n]*(?:manifesto|oid|lfs|ponteiro|integridade|duplicidade|"
    r"reten[çc][ãa]o|objeto|versionamento|commit|arquivo)[^\n]*)$"
)


def remover_subsecoes_internas(texto: str) -> str:
    """Remove subseções cujo título trate de controle interno do acervo, não do trabalho."""
    linhas = texto.splitlines()
    saida: list[str] = []
    cortando_em = None
    for linha in linhas:
        m_titulo = re.match(r"^(#{2,4})\s+(.*)$", linha)
        if m_titulo:
            nivel = len(m_titulo.group(1))
            if SUBSECAO_INTERNA.match(linha):
                cortando_em = nivel
                continue
            if cortando_em is not None and nivel <= cortando_em:
                cortando_em = None
            if cortando_em is not None:
                continue
        elif cortando_em is not None:
            continue
        saida.append(linha)
    return "\n".join(saida)


METADADOS_STRIP = re.compile(
    r"(?m)^[ \t]*(?:[-*][ \t]+)?\*\*(?:Categoria|Sistema|Assunto|Fonte|Tipo de fonte|"
    r"Arquivo/registro de origem|Slug em|Participantes|Extensão do recorte|Data/hora|"
    r"Natureza da fonte|Natureza da evidência|Categorias aplicáveis|Sistemas/artefatos citados|"
    r"Sistemas\/ferramentas identificados|Método de análise|Varredura de privacidade|Capturas|"
    r"Estado|Limitações|Publicação reduzida)[^\n]*$"
)


def limpar(texto: str) -> str:
    """Remove avisos de publicação, ligações, nomes de arquivo e referências internas."""
    linhas: list[str] = []
    for linha in texto.splitlines():
        if linha.lstrip().startswith(">"):
            continue  # avisos de publicação / fonte no topo dos documentos
        linhas.append(linha)
    t = "\n".join(linhas)

    t = remover_subsecoes_internas(t)

    # linhas de controle do acervo (e as tabelas inteiras que elas encabeçam) saem do material
    resultado: list[str] = []
    pulando_tabela = False
    for linha in t.splitlines():
        em_tabela = linha.lstrip().startswith("|")
        if em_tabela and pulando_tabela:
            continue
        if RUIDO_INTERNO.search(linha):
            if em_tabela:
                pulando_tabela = True
                continue
            if len(linha) < 500:
                continue
        pulando_tabela = False
        resultado.append(linha)
    t = "\n".join(resultado)

    t = equilibrar_crases(t)

    # títulos de primeiro nível: o material monta a hierarquia
    t = re.sub(r"(?m)^#\s+.*$", "", t)
    # metadados do topo já são renderizados como selos
    t = re.sub(r"(?m)^[ \t]*(?:[-*][ \t]+)?\*\*Confiança da extração:\*\*[^\n]*$", "", t)
    t = METADADOS_STRIP.sub("", t)

    # nomes de mídia explícitos do manifesto
    for nome in NOMES_DE_MIDIA:
        if nome and nome in t:
            t = t.replace(nome, "a fonte")
    t = re.sub(r"(?i)grava[çc][ãa]o de tela", "a fonte", t)

    # ligações: mantém o texto quando ele é descritivo; descarta quando é caminho/arquivo
    def troca_link(m: re.Match[str]) -> str:
        rotulo, destino = m.group(1), m.group(2)
        alvo = rotulo or destino
        if "/" in destino or ARQUIVO_RE.search(alvo) or not alvo.strip():
            return ""
        return alvo.strip()

    t = LINK_RE.sub(troca_link, t)
    t = ARQUIVO_RE.sub("", t)
    t = re.sub(r"\b(?:materiais|restrito|tools|saida)/", "", t)
    # marcadores de anonimização digitados entre sinais de menor/maior viram texto literal
    t = re.sub(r"<([a-zà-ÿ][a-zà-ÿ0-9_\- ]{1,30})>", r"`\1`", t, flags=re.I)
    t = ANCORA_RE.sub(lambda m: "(msg. %s)" % m.group(1), t)
    t = SECAO_RE.sub(lambda m: "seção " + m.group(1), t)

    # sobras de referência cruzada
    t = re.sub(r"(?i)\(\s*(?:ver|vide|conferir|cf\.)\s[^)]{0,140}\)", "", t)
    t = re.sub(r"(?i)[—–-]\s*(?:ver|vide|conferir)\s+(?:o\s+|a\s+)?se[çc][ãa]o\s+[\d\.]+[^.\n]*", "", t)
    t = re.sub(r"(?i),\s*ver\s+se[çc][ãa]o\s+[^.\n]*", "", t)
    t = re.sub(r'(?i)\bse[çc][ãa]o\s+"[^"]{0,80}"(?:\s*,?\s*item\s*\d+)?', "", t)
    t = t.replace("§", "seção ")
    t = re.sub(r"(?i)\b(ver|conferir|vide)\s*(,|;|\.|$)", r"\2", t, flags=re.M)
    t = re.sub(r"\(\s*(?:,|;|·|\||—|-)*\s*\)", "", t)
    t = re.sub(r"\[\s*\]", "", t)
    t = re.sub(r"[ \t]+([,;.])", r"\1", t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = re.sub(r"(?m)^[-*]\s+(?=(?:[-*]|\s*$))", "", t)
    t = re.sub(r"(?m)^\s*[-*]\s*$", "", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def selo_categoria(valor: str) -> str:
    """Reduz a linha de categoria a uma lista limpa de marcadores."""
    v = valor.replace("`", "").replace("*", "")
    for separador in ["(", " — ", " – ", " - ", ". "]:
        if separador in v:
            v = v.split(separador)[0]
    return re.sub(r"\s+", " ", v).strip(" .,;:")


def selo_confianca(valor: str) -> str:
    """Reduz a linha de confiança a um rótulo curto (alta, média, baixa…)."""
    v = valor.replace("`", "").replace("*", "").split("—")[0]
    v = re.split(r"[.;,]", v)[0]
    v = re.sub(r"\s+", " ", v).strip(" .,;:")
    if len(v) > 30:
        v = v[:27].rstrip(" ,;") + "…"
    return v


def extrair_titulo_metadados(texto: str) -> tuple[str, str]:
    """Lê os selos de categoria e de confiança declarados no próprio documento."""
    categoria = confianca = ""
    mc = re.search(r"(?im)^[ \t]*(?:[-*][ \t]+)?\*\*Categoria:\*\*[ \t]*(.+?)[ \t]*$", texto)
    if mc:
        categoria = mc.group(1)
    mf = re.search(r"(?im)^[ \t]*(?:[-*][ \t]+)?\*\*Confiança da extração:\*\*[ \t]*(.+?)[ \t]*$", texto)
    if mf:
        confianca = mf.group(1)
    return categoria, confianca


def md_para_html(texto: str, nivel: int = 3) -> str:
    """Converte markdown em HTML, rebaixando os títulos para caber na hierarquia da página."""
    linhas = []
    for linha in texto.splitlines():
        m = re.match(r"^(#{2,6})\s+(.*)$", linha)
        if m:
            novo = min(len(m.group(1)) + nivel, 6)
            linhas.append("#" * novo + " " + m.group(2))
        else:
            linhas.append(linha)
    corpo = "\n".join(linhas)
    convertido = markdown.markdown(corpo, extensions=["tables", "fenced_code", "sane_lists", "attr_list"])
    convertido = convertido.replace("<table>", '<table class="tabela">')
    # resíduos de negrito que a conversão não fechou (crases fragmentadas na origem)
    convertido = re.sub(r"\*\*([^*<>]{1,200}?)\*\*", r"<strong>\1</strong>", convertido)
    convertido = convertido.replace("**", "")
    return ajustar_pontuacao(convertido)


def ajustar_pontuacao(html_txt: str) -> str:
    """Corrige sobras de pontuação no texto corrido — sem tocar em código.

    Trechos de código (SQL, payloads, expressões) ficam intactos: ali `..` pode ser
    separador de esquema e a pontuação faz parte do conteúdo.
    """
    partes = re.split(r"(<pre>.*?</pre>|<code>.*?</code>)", html_txt, flags=re.S)
    for i, parte in enumerate(partes):
        if parte.startswith("<pre>") or parte.startswith("<code>"):
            continue
        parte = re.sub(r"`{2,}", "", parte)
        parte = re.sub(r"\.{2,}(?=\s|<|$)", ".", parte)
        parte = re.sub(r",{2,}", ",", parte)
        parte = re.sub(r";{2,}", ";", parte)
        parte = re.sub(r"\s+([,.;:!?])", r"\1", parte)
        parte = re.sub(r"([,;:])\s*\.", r".", parte)
        parte = re.sub(r"\s{2,}(?=[^\s<])", " ", parte)
        partes[i] = parte
    return "".join(partes)


# ---------------------------------------------------------------- leitura do acervo

def ler(caminho: str) -> str:
    if not os.path.exists(caminho):
        return ""
    with open(caminho, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def bloco_fonte(slug: str, rotulo: str, tipo: str, arquivo: str, titulo_secao: str,
                numero_selo: str, aberto: bool = False) -> str:
    bruto = ler(os.path.join(MATERIAIS, slug, arquivo))
    if len(bruto) < 400:
        return ""
    categoria, confianca = extrair_titulo_metadados(bruto)
    if not categoria or not confianca:
        # documentos complementares herdam os selos do guia da mesma fonte
        cat_guia, conf_guia = extrair_titulo_metadados(ler(os.path.join(MATERIAIS, slug, "guia_de_estudo.md")))
        categoria = categoria or cat_guia
        confianca = confianca or conf_guia
    corpo = md_para_html(limpar(bruto))
    if len(corpo) < 200:
        return ""
    selos = ['<span class="selo selo-tipo">%s</span>' % html.escape(tipo)]
    categoria = selo_categoria(categoria)
    confianca = selo_confianca(confianca)
    if categoria:
        selos.append('<span class="selo selo-cat">%s</span>' % html.escape(categoria))
    if confianca:
        selos.append('<span class="selo selo-conf">confiança: %s</span>' % html.escape(confianca))
    return (
        '<article class="bloco" id="%s">\n'
        '<h4 class="bloco-titulo"><span class="bloco-num">%s</span> %s</h4>\n'
        '<p class="bloco-selos">%s</p>\n'
        '<div class="bloco-corpo">%s</div>\n'
        "</article>\n"
    ) % (slug, numero_selo, html.escape(rotulo), " ".join(selos), corpo)


def capitulo(chave: str, titulo: str, descricao: str, conteudo: str) -> str:
    desc = '<p class="cap-desc">%s</p>\n' % html.escape(descricao) if descricao else ""
    return (
        '<section class="capitulo" id="cap-%s">\n'
        '<h2 class="cap-titulo">%s</h2>\n'
        "%s%s\n</section>\n"
    ) % (chave, html.escape(titulo), desc, conteudo)


def detalhes(titulo: str, conteudo: str, aberto: bool = False) -> str:
    return (
        '<details class="dobra"%s><summary>%s</summary><div class="dobra-corpo">%s</div></details>\n'
    ) % (" open" if aberto else "", html.escape(titulo), conteudo)


# ---------------------------------------------------------------- montagem

TEXTO_COMO_USAR = """
<p>Este é o material de estudo consolidado do acervo de treinamentos e conversas de trabalho da
<b>Função Sistemas</b>. Ele reúne, em um único documento navegável, o conhecimento extraído de
todas as fontes analisadas — e nada além disso: as transcrições integrais (fala bruta) e os
documentos de processo ficaram de fora, porque o que interessa aqui é o conteúdo, não o registro.</p>

<div class="destaque">
  <h3>Como ler</h3>
  <ul>
    <li><b>Os capítulos são temáticos.</b> Um mesmo assunto pode aparecer em mais de um capítulo, sob
    ângulos diferentes (negócio, API, teste, ambiente).</li>
    <li><b>Cada bloco traz a origem como selo</b> — tipo de fonte (treinamento, reunião, conversa…),
    categorias de conhecimento e <b>confiança da extração</b>.</li>
    <li><b>Referências de tempo</b> (por exemplo <code>00:04:20</code>) apontam para o trecho da fonte
    que sustenta a informação, quando a fonte é uma gravação.</li>
    <li><b>O que não está confirmado está marcado como tal.</b> O capítulo
    <a href="#cap-pendencias">Pontos a validar</a> reúne tudo que depende de confirmação humana.</li>
    <li>Use a <b>busca</b> no topo para filtrar por termo, sigla, tela ou regra, e os botões
    <i>expandir</i>/<i>recolher</i> para abrir tudo de uma vez.</li>
  </ul>
</div>

<div class="aviso">
  <h3>Aviso importante</h3>
  <p>Este material é <b>apoio de estudo e memória de trabalho</b>. Ele não substitui a especificação
  vigente, o runbook nem a validação com o responsável de cada frente: regras, telas e versões
  mudam. Nenhum procedimento aqui foi executado durante a extração — o que existe é o que foi
  demonstrado, ensinado ou relatado, mais as ressalvas correspondentes. Onde a fonte não confirmou,
  o material diz que não confirmou, em vez de completar por suposição.</p>
</div>
"""

TEXTO_LIMITES = """
<p>Este material foi montado a partir de conteúdo já publicado no acervo de estudo, que passou por
revisão de privacidade antes de virar documentação.</p>
<ul>
  <li><b>Dados de identificação direta</b> (documentos, contatos, endereços, matrícula, dados de
  familiares) foram omitidos ou substituídos por marcadores. A estrutura das mensagens e dos
  documentos técnicos foi preservada, porque é ela que ensina.</li>
  <li><b>Nomes de pessoas</b> aparecem apenas quando a política de publicação do acervo autorizou,
  e somente como contexto; nenhuma informação pessoal de quem aparece nas fontes é reproduzida
  aqui.</li>
  <li><b>Servidores, pastas de rede e caminhos internos</b> aparecem de forma genérica: a estrutura
  do caminho é mantida (é o que ensina), o hospedeiro não.</li>
  <li><b>Nada deste material foi obtido executando testes, consultas a banco ou chamadas a sistemas
  de produção</b>: é documentação do que foi ensinado e demonstrado.</li>
  <li><b>Este documento não é orientação jurídica nem de compliance.</b> Dúvidas de exposição de
  informação devem ir para o responsável pela divulgação.</li>
</ul>
<p>Se um trecho deste material conflitar com a especificação vigente, <b>vale a especificação</b> —
e o conflito deve ser registrado para correção do próprio acervo.</p>
"""


def montar_corpo() -> tuple[str, str, int]:
    """Retorna (html dos capítulos, html do índice lateral, número de blocos)."""
    total = 0

    def conta(html_bloco: str) -> str:
        nonlocal total
        total += html_bloco.count('class="bloco"')
        return html_bloco

    # -- mapa das fontes
    linhas = []
    for slug, (rotulo, tipo, _tema) in FONTES.items():
        bruto = ler(os.path.join(MATERIAIS, slug, "guia_de_estudo.md"))
        _cat, conf = extrair_titulo_metadados(bruto)
        resumo = selo_confianca(conf) or "—"
        linhas.append(
            '<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>'
            % (html.escape(rotulo), html.escape(tipo), html.escape(resumo))
        )
    for slug, descricao in SEM_CONTEUDO.items():
        linhas.append(
            '<tr class="linha-vazia"><td><b>%s</b></td><td>—</td><td>sem conteúdo instrutivo extraível</td></tr>'
            % html.escape(descricao)
        )
    mapa = (
        '<table class="tabela"><thead><tr><th>Fonte</th><th>Tipo</th><th>Confiança da extração</th></tr></thead>'
        "<tbody>%s</tbody></table>" % "".join(linhas)
    )

    capitulos: list[tuple[str, str, str]] = []  # (id, título, html)

    capitulos.append(("como-usar", "Como usar este material", "", TEXTO_COMO_USAR))
    capitulos.append(("mapa", "Mapa das fontes", "O que compõe este material, por tipo de fonte e confiabilidade da extração.", mapa))

    # -- visão geral do negócio e do sistema (índices temáticos)
    conteudo = ""
    conteudo += cap_bloco_indice("Sistemas, módulos e telas", "sistemas/INDICE_SISTEMAS.md", "sistemas")
    conteudo += cap_bloco_indice("Consultas e bancos de dados", "SQL/INDICE_SQL.md", "sqldb")
    conteudo += cap_bloco_indice("Rotinas e processos", "PROCESSOS/INDICE_PROCESSOS.md", "processos")
    conteudo += md_para_html(limpar(ler(os.path.join(MATERIAIS, "GLOSSARIO_GERAL.md"))))
    capitulos.append(("panorama", "Panorama: sistemas, consultas, rotinas e vocabulário", "Catálogo consolidado de sistemas, de consultas a banco, de rotinas operacionais e do vocabulário do domínio.", conteudo))

    # -- guias por tema
    numero_capitulo = 0
    for chave, titulo, descricao in TEMAS:
        numero_capitulo += 1
        corpo = []
        n = 0
        for slug, (rotulo, tipo, tema) in FONTES.items():
            if tema != chave:
                continue
            n += 1
            corpo.append(bloco_fonte(slug, rotulo, tipo, "guia_de_estudo.md", "Guia", "%d.%d" % (numero_capitulo, n)))
        if corpo:
            capitulos.append((chave, titulo, descricao, conta("".join(corpo))))

    # -- glossário por fonte
    corpo = []
    for i, (slug, (rotulo, tipo, _t)) in enumerate(FONTES.items(), start=1):
        b = bloco_fonte(slug, rotulo, tipo, "glossario.md", "Glossário", "G.%02d" % i)
        if b:
            corpo.append(b)
    if corpo:
        capitulos.append(("glossario", "Glossário por fonte", "Termos, siglas e campos com o significado sustentado por cada fonte.", conta("".join(corpo))))

    # -- procedimentos passo a passo
    corpo = []
    for i, (slug, (rotulo, tipo, _t)) in enumerate(FONTES.items(), start=1):
        b = bloco_fonte(slug, rotulo, tipo, "procedimentos.md", "Procedimentos", "P.%02d" % i)
        if b:
            corpo.append(b)
    if corpo:
        capitulos.append(("passos", "Procedimentos passo a passo", "Fluxos completos — pré-condições, sequência, validações, resultado e exceções — como foram ensinados, sem substituir o runbook oficial.", conta("".join(corpo))))

    # -- perguntas e respostas
    corpo = []
    for i, (slug, (rotulo, tipo, _t)) in enumerate(FONTES.items(), start=1):
        b = bloco_fonte(slug, rotulo, tipo, "perguntas.md", "Perguntas", "Q.%02d" % i, aberto=False)
        if b:
            corpo.append(b)
    if corpo:
        perguntas_total = 0
        for slug in FONTES:
            txt = ler(os.path.join(MATERIAIS, slug, "perguntas.md"))
            perguntas_total += len(re.findall(r"(?m)^\s*(?:\d+[.)]|[-*])\s+.*\?", txt))
        capitulos.append(("faq", "Perguntas e respostas", "%d perguntas de revisão, com resposta e justificativa apoiadas na fonte, agrupadas por origem." % perguntas_total, conta("".join(corpo))))

    # -- pendências
    conteudo = md_para_html(limpar(ler(os.path.join(MATERIAIS, "CONFLITOS_E_VALIDACAO.md"))))
    corpo = []
    for i, (slug, (rotulo, tipo, _t)) in enumerate(FONTES.items(), start=1):
        b = bloco_fonte(slug, rotulo, tipo, "incertezas.md", "Lacunas e validações", "V.%02d" % i)
        if b:
            corpo.append(b)
    capitulos.append(("pendencias", "Pontos a validar", "Tudo que a fonte não confirmou, que depende de decisão humana ou que pode ter mudado de versão. É o capítulo mais importante antes de agir: leia-o junto do procedimento que pretende executar.", conta(conteudo + "".join(corpo))))

    # -- trilhas de estudo
    conteudo = md_para_html(limpar(ler(os.path.join(MATERIAIS, "TRILHAS_DE_ESTUDO.md"))))
    capitulos.append(("trilhas", "Trilhas de estudo", "O que estudar, em que ordem e com qual caso prático, a partir do que o próprio time apontou como necessário.", conteudo))

    # -- limites
    capitulos.append(("limites", "Limites, privacidade e uso responsável", "", TEXTO_LIMITES))

    # montagem final
    corpo_html = []
    indice = []
    for chave, titulo, descricao, html_cap in capitulos:
        corpo_html.append(capitulo(chave, titulo, descricao, html_cap))
        indice.append('<li><a href="#cap-%s">%s</a></li>' % (chave, html.escape(titulo)))
    return "".join(corpo_html), "<ul>%s</ul>" % "".join(indice), total


def cap_bloco_indice(titulo: str, caminho: str, ancora: str) -> str:
    bruto = ler(os.path.join(MATERIAIS, caminho))
    if not bruto:
        return ""
    return detalhes(titulo, md_para_html(limpar(bruto), nivel=4), aberto=False)


CSS = """
:root{
  --azul:#123a63; --azul-claro:#1e5a92; --teal:#0f766e; --ambar:#b45309; --vermelho:#b91c1c;
  --texto:#1f2937; --texto-suave:#4b5563; --borda:#e2e8f0; --fundo:#f5f7fa; --card:#ffffff;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--fundo);color:var(--texto);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  font-size:16px;line-height:1.62}
a{color:var(--azul-claro);text-decoration:none}
a:hover{text-decoration:underline}

header.topo{background:linear-gradient(135deg,#0b2b4a 0%,#123a63 45%,#0f766e 100%);color:#fff;
  padding:34px 28px 26px}
header.topo .envolt{max-width:1180px;margin:0 auto}
header.topo h1{margin:0 0 6px;font-size:30px;letter-spacing:-.3px}
header.topo p.sub{margin:0 0 16px;font-size:16px;opacity:.92;max-width:900px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px}
.chip{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.28);border-radius:999px;
  padding:5px 12px;font-size:13px}
.barra{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
#busca{flex:1 1 320px;min-width:240px;padding:11px 14px;border-radius:10px;border:1px solid rgba(255,255,255,.35);
  background:rgba(255,255,255,.95);color:#111827;font-size:15px}
.botao{cursor:pointer;border:1px solid rgba(255,255,255,.45);background:rgba(255,255,255,.12);color:#fff;
  padding:10px 14px;border-radius:10px;font-size:14px;white-space:nowrap}
.botao:hover{background:rgba(255,255,255,.22)}
.botao.baixar{background:#fff;color:#0b2b4a;border-color:#fff;font-weight:600}

.envolt{max-width:1180px;margin:0 auto;padding:0 28px}
.layout{display:grid;grid-template-columns:290px minmax(0,1fr);gap:28px;align-items:start;padding:26px 0 60px}
nav.lateral{position:sticky;top:16px;max-height:calc(100vh - 32px);overflow:auto;background:var(--card);
  border:1px solid var(--borda);border-radius:14px;padding:16px 14px}
nav.lateral h2{font-size:13px;text-transform:uppercase;letter-spacing:.08em;color:var(--texto-suave);margin:0 0 10px}
nav.lateral ul{list-style:none;margin:0;padding:0}
nav.lateral li{margin:2px 0}
nav.lateral a{display:block;padding:7px 9px;border-radius:8px;color:var(--texto);font-size:14.5px}
nav.lateral a:hover{background:#eef2f7;text-decoration:none}
nav.lateral .conta{color:var(--texto-suave);font-size:12.5px;margin-top:10px;display:block}

main{min-width:0}
.capitulo{background:var(--card);border:1px solid var(--borda);border-radius:14px;padding:24px;
  margin-bottom:22px;box-shadow:0 1px 2px rgba(15,23,42,.04)}
.cap-titulo{margin:0 0 4px;font-size:23px;color:var(--azul);border-bottom:3px solid var(--teal);
  display:inline-block;padding-bottom:6px}
.cap-desc{color:var(--texto-suave);margin:10px 0 18px}

.bloco{border:1px solid var(--borda);border-radius:12px;padding:16px 18px;margin:0 0 16px;background:#fdfefe}
.bloco-titulo{margin:0 0 6px;font-size:17px;color:#0b2b4a}
.bloco-num{display:inline-block;min-width:44px;color:var(--teal);font-variant-numeric:tabular-nums;font-weight:700}
.bloco-selos{margin:0 0 12px}
.selo{display:inline-block;font-size:12px;border-radius:999px;padding:3px 10px;margin:0 6px 6px 0;
  border:1px solid var(--borda);background:#f1f5f9;color:var(--texto-suave)}
.selo-tipo{background:#e0f2fe;border-color:#bae6fd;color:#075985}
.selo-cat{background:#ecfdf5;border-color:#bbf7d0;color:#065f46}
.selo-conf{background:#fff7ed;border-color:#fed7aa;color:#9a3412}

.bloco-corpo h4,.bloco-corpo h5,.bloco-corpo h6{margin:18px 0 8px;color:var(--azul-claro)}
.bloco-corpo h4{font-size:16.5px}
.bloco-corpo h5{font-size:15px;text-transform:none}
.bloco-corpo p{margin:0 0 10px}
.bloco-corpo ul,.bloco-corpo ol{margin:0 0 12px 22px;padding:0}
.bloco-corpo li{margin:4px 0}
.bloco-corpo code{background:#f1f5f9;border:1px solid var(--borda);border-radius:5px;padding:1px 5px;
  font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:13.5px}
.bloco-corpo pre{background:#0f172a;color:#e2e8f0;border-radius:10px;padding:14px 16px;overflow-x:auto;
  font-size:13px;line-height:1.5}
.bloco-corpo pre code{background:none;border:0;color:inherit;padding:0}
.bloco-corpo blockquote{margin:10px 0;padding:10px 14px;border-left:4px solid var(--ambar);
  background:#fffbeb;border-radius:0 8px 8px 0;color:#78350f}

table.tabela{width:100%;border-collapse:collapse;margin:12px 0 18px;display:block;overflow-x:auto;font-size:14.5px}
table.tabela th,table.tabela td{border:1px solid var(--borda);padding:8px 10px;text-align:left;vertical-align:top}
table.tabela thead th{background:#eef2f7;color:var(--azul);font-size:13.5px;text-transform:none}
table.tabela tbody tr:nth-child(even){background:#fafcfe}
table.tabela .linha-vazia,table.tabela .linha-vazia td{color:var(--texto-suave);background:#f8fafc}

details.dobra{border:1px solid var(--borda);border-radius:10px;padding:10px 14px;margin:10px 0;background:#fbfdff}
details.dobra>summary{cursor:pointer;font-weight:600;color:var(--azul)}
details.dobra[open]>summary{margin-bottom:10px}
.dobra-corpo{margin-top:6px}

.destaque{background:#f0fdfa;border:1px solid #99f6e4;border-radius:12px;padding:16px 18px;margin:16px 0}
.destaque h3{margin:0 0 8px;color:#0f766e;font-size:17px}
.aviso{background:#fffbeb;border:1px solid #fcd34d;border-radius:12px;padding:16px 18px;margin:16px 0}
.aviso h3{margin:0 0 8px;color:var(--ambar);font-size:17px}

footer.rodape{background:#0b2b4a;color:#cbd5e1;padding:22px 28px;font-size:14px}
footer.rodape .envolt{max-width:1180px}
#vazio{display:none;background:#fff;border:1px dashed var(--borda);border-radius:12px;padding:18px;
  color:var(--texto-suave);margin-bottom:22px}
#topo{position:fixed;right:18px;bottom:18px;background:var(--azul);color:#fff;border:0;border-radius:50%;
  width:46px;height:46px;font-size:18px;cursor:pointer;box-shadow:0 6px 16px rgba(15,23,42,.25);display:none}

@media (max-width:900px){
  .layout{grid-template-columns:1fr}
  nav.lateral{position:static;max-height:none}
  header.topo h1{font-size:24px}
}
@media print{
  header.topo{background:#0b2b4a !important;-webkit-print-color-adjust:exact}
  nav.lateral,#busca,.botao,#topo{display:none !important}
  .layout{display:block}
  details.dobra{page-break-inside:avoid}
  details.dobra>summary{list-style:none}
  .capitulo{box-shadow:none;page-break-inside:auto}
  body{background:#fff}
}
"""

JS = """
(function(){
  var busca=document.getElementById('busca');
  var blocos=Array.prototype.slice.call(document.querySelectorAll('.bloco'));
  var capitulos=Array.prototype.slice.call(document.querySelectorAll('.capitulo'));
  var vazio=document.getElementById('vazio');
  var dobras=Array.prototype.slice.call(document.querySelectorAll('details.dobra'));

  function normaliza(s){return (s||'').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');}

  function aplicar(){
    var termo=normaliza(busca.value.trim());
    if(!termo){
      blocos.forEach(function(b){b.style.display='';});
      capitulos.forEach(function(c){c.style.display='';});
      dobras.forEach(function(d){d.open=false;});
      vazio.style.display='none';
      return;
    }
    var achou=0;
    blocos.forEach(function(b){
      var ok=normaliza(b.textContent).indexOf(termo)>=0;
      b.style.display=ok?'':'none';
      if(ok)achou++;
    });
    capitulos.forEach(function(c){
      var visiveis=c.querySelectorAll('.bloco:not([style*="display: none"])').length;
      var temBloco=c.querySelector('.bloco')!==null;
      c.style.display=(!temBloco||visiveis>0)?'':'none';
    });
    dobras.forEach(function(d){
      if(normaliza(d.textContent).indexOf(termo)>=0){d.open=true;}
    });
    vazio.style.display=achou?'none':'block';
  }

  busca.addEventListener('input',aplicar);

  document.getElementById('expandir').addEventListener('click',function(){
    dobras.forEach(function(d){d.open=true;});
  });
  document.getElementById('recolher').addEventListener('click',function(){
    dobras.forEach(function(d){d.open=false;});
  });

  var topo=document.getElementById('topo');
  window.addEventListener('scroll',function(){
    topo.style.display=window.scrollY>500?'block':'none';
  });
  topo.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});

  // quando a página é aberta fora do servidor (arquivo local), o link de download
  // gera o próprio documento em vez de apontar para o endereço de download
  var dl=document.getElementById('baixar');
  dl.addEventListener('click',function(e){
    if(location.protocol!=='file:'&&location.protocol!=='blob:'){return;}
    e.preventDefault();
    var conteudo='<!DOCTYPE html>\n'+document.documentElement.outerHTML;
    var blob=new Blob([conteudo],{type:'text/html;charset=utf-8'});
    var a=document.createElement('a');
    a.href=URL.createObjectURL(blob);
    a.download='base-de-conhecimento-funcao-sistemas.html';
    document.body.appendChild(a);a.click();
    setTimeout(function(){URL.revokeObjectURL(a.href);a.remove();},1500);
  });
})();
"""


def montar_documento() -> str:
    carregar_nomes_de_midia()
    corpo, indice, total_blocos = montar_corpo()
    hoje = datetime.date.today().strftime("%d/%m/%Y")
    fontes_total = len(FONTES) + len(SEM_CONTEUDO)

    cabecalho = (
        "<!DOCTYPE html>\n<html lang=\"pt-BR\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "<title>Base de conhecimento — Função Sistemas</title>\n"
        "<meta name=\"description\" content=\"Material de estudo consolidado: sistemas, negócio, API, testes, ambientes, automação e comunicação.\">\n"
        "<style>\n" + CSS + "\n</style>\n</head>\n<body>\n"
    )

    topo = (
        "<header class=\"topo\"><div class=\"envolt\">\n"
        "<h1>Base de conhecimento — Função Sistemas</h1>\n"
        "<p class=\"sub\">Material de estudo consolidado a partir dos treinamentos, demonstrações, reuniões e conversas de trabalho analisados. Organizado por tema, com as ressalvas e os pontos que ainda dependem de validação.</p>\n"
        "<div class=\"chips\">\n"
        + '<span class="chip">' + str(fontes_total) + " fontes analisadas</span>\n"
        + '<span class="chip">' + str(total_blocos) + " blocos de conhecimento</span>\n"
        + "<span class=\"chip\">uso interno</span>\n"
        + '<span class="chip">atualizado em ' + hoje + "</span>\n"
        "</div>\n"
        "<div class=\"barra\">\n"
        "<input id=\"busca\" type=\"search\" placeholder=\"Buscar por termo, sigla, tela, regra ou campo...\">\n"
        "<button class=\"botao\" id=\"expandir\">Expandir tudo</button>\n"
        "<button class=\"botao\" id=\"recolher\">Recolher tudo</button>\n"
        "<a class=\"botao baixar\" id=\"baixar\" href=\"download\" download>Baixar este material</a>\n"
        "</div>\n</div></header>\n"
    )

    miolo = (
        "<div class=\"envolt\"><div class=\"layout\">\n"
        "<nav class=\"lateral\"><h2>Índice</h2>" + indice
        + '<span class="conta">' + str(total_blocos) + " blocos · navegue ou busque</span></nav>\n"
        "<main><div id=\"vazio\">Nenhum bloco corresponde à busca. Tente outro termo.</div>" + corpo + "</main>\n"
        "</div></div>\n"
        "<button id=\"topo\" title=\"Voltar ao topo\">&#8593;</button>\n"
    )

    rodape = (
        "<footer class=\"rodape\"><div class=\"envolt\">Material de estudo interno — não substitui especificação, runbook ou validação do responsável de cada frente. "
        "Dados de identificação direta foram omitidos; nenhum sistema foi consultado ou alterado durante a produção deste conteúdo.</div></footer>\n"
        "<script>\n" + JS + "\n</script>\n</body>\n</html>\n"
    )

    return cabecalho + topo + miolo + rodape


VAZAMENTOS = {
    "extensão de arquivo": re.compile(r"\.(?:md|mp4|png|jpe?g|json|srt|vtt|csv|xlsx|docx|pdf)\b", re.I),
    "caminho de pasta interna": re.compile(r"\b(?:materiais|restrito|tools|saida)/", re.I),
    "ligação entre documentos": re.compile(r"\]\("),
    "referência a documento interno": re.compile(
        r"\b(?:PLANO_EXTRACAO|LEIA-ME|CONFLITOS_E_VALIDACAO|PRIVACIDADE_E_RETENCAO|INDICE_SQL|"
        r"GLOSSARIO_GERAL|INDICE_SISTEMAS|INDICE_PROCESSOS)\b", re.I),
    "jargão de controle interno do acervo": re.compile(
        r"(?i)\b(?:manifesto|oid|\blfs\b|ponteiro|checksum|sha-?256|branch|commit)\b"),
    "âncora de mensagem não convertida": re.compile(r"\[M\d+\]"),
}


def verificar_saida(doc: str) -> list[str]:
    """Confere que o material não expõe nomes de arquivo nem referências internas."""
    conteudo = re.sub(r"<script>.*?</script>", "", doc, flags=re.S)
    conteudo = re.sub(r"<style>.*?</style>", "", conteudo, flags=re.S)
    achados = []
    for nome, padrao in VAZAMENTOS.items():
        encontrados = padrao.findall(conteudo)
        if encontrados:
            exemplos = ", ".join(sorted(set(encontrados))[:3])
            achados.append("%s (%d): %s" % (nome, len(encontrados), exemplos))
    return achados


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--saida", default=os.path.join(RAIZ, "saida", "index.html"))
    args = p.parse_args()
    doc = montar_documento()

    achados = verificar_saida(doc)
    if achados:
        for a in achados:
            print("[falha] vazamento de referência interna — %s" % a)
        return 1

    os.makedirs(os.path.dirname(os.path.abspath(args.saida)), exist_ok=True)
    with open(args.saida, "w", encoding="utf-8") as fh:
        fh.write(doc)
    blocos = doc.count('class="bloco"')
    capitulos = doc.count('class="capitulo"')
    print(
        "gerado: %s (%.1f KB, %d capítulos, %d blocos) — sem nomes de arquivo ou referências internas"
        % (args.saida, len(doc.encode("utf-8")) / 1024, capitulos, blocos)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
