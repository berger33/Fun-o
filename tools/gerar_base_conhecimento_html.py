#!/usr/bin/env python3
"""Gera o material de estudo em HTML único a partir dos derivados do acervo.

Regras do material gerado:
- inclui **apenas conhecimento** (guias, procedimentos, glossários, perguntas, pendências e
  índices temáticos). Transcrições brutas e documentos de processo do repositório ficam fora;
- **não** menciona nomes de arquivo, pastas, ligações internas nem identificadores de mídia:
  as fontes aparecem por rótulo descritivo neutro ("Conversa técnica — ...", "Treinamento — ...");
- não lê a área restrita (material pessoal, fora do Git);
- saída autocontida (CSS/JS embutidos, sem dependência de rede) em `saida/index.html` (build) e
  cópia versionada em `material-de-estudo/base-de-conhecimento-funcao-sistemas.html` (o arquivo que
  circula, para leitura e download).

Uso: python3 tools/gerar_base_conhecimento_html.py [--saida saida/index.html] [--sem-distribuivel]
"""

from __future__ import annotations

import argparse
import csv
import html
import os
import re
import datetime

import markdown

from sintese_conhecimento import SINTESES

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOME_DISTRIBUIDO = os.path.join("material-de-estudo", "base-de-conhecimento-funcao-sistemas.html")
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
ANCORA_RE = re.compile(r"\[[MP]\d+\]")
SECAO_RE = re.compile(r"§+\s*([\d\.]+)")

# tudo o que aponta "quando" algo foi dito sai do material: intervalos, carimbos e referências
INTERVALO_TEMPO = re.compile(
    r"\d{1,2}:\d{2}(?::\d{2})?(?:[.,]\d+)?\s*(?:[–—-]|a|até)\s*\d{1,2}:\d{2}(?::\d{2})?(?:[.,]\d+)?"
)
CARIMBO_TEMPO = re.compile(r"\b\d{1,2}:\d{2}(?::\d{2})?(?:[.,]\d+)?\b")
REF_ANCORA = re.compile(r"\(\s*msg\.?\s*\d+\s*\)")
DATA_ISO_PARENTESE = re.compile(r"\(\s*\d{4}-\d{2}-\d{2}\s*\)")

# trechos que falam do processo de captura (não são conhecimento sobre o trabalho)
RUIDO_DE_FONTE = re.compile(
    r"(?i)\b(?:asr|transcri\w*|transcrit\w*|inaud[íi]vel|ileg[íi]vel|"
    r"\bcues?\b|segmentos?|escuta humana|áudio|falantes?|ocr|silêncio|decib|análise quadro)\b"
)
RUIDO_DE_PROCESSO = re.compile(
    r"(?i)(?:nesta an[áa]lise|neste lote|nesta sess[ãa]o de an[áa]lise|deste lote|deste pacote|"
    r"quadro a quadro|extra[çc][ãa]o|confian[çc]a da extra|"
    r"\btriagem\b|pacotes? (?:de triagem|preliminares?|em revis[ãa]o)|"
    r"ponte tempor[áa]ria|bytes da grava[çc][ãa]o|github support)"
)

LIGACOES_TEMPO = re.compile(r"(?i)\b(?:às|as)\s+\d{1,2}:\d{2}\b")

# crases que envolvem só datas de registro da análise
CRASE_EM_DATA = re.compile(r"`{1,3}(\s*\d{4}-\d{2}-\d{2}\s*)`{1,3}")

# negrito/itálico que envolvem só tempos, âncoras de mensagem ou pontuação de separação
ESTILO_EM_TEMPO = re.compile(
    r"(\*\*|__|\*|_)((?:[^\n]*?(?:\d{1,2}:\d{2}(?::\d{2})?(?:[.,]\d+)?|\[[MP]\d+\])[^\n]*?)|"
    r"(?:[;:,·|.\-–—\s]+))\1"
)

# crases que envolvem só tempos, âncoras de mensagem ou pontuação de separação
CRASE_EM_TEMPO = re.compile(
    r"`{1,3}((?:[^`\n]*?(?:\d{1,2}:\d{2}(?::\d{2})?(?:[.,]\d+)?|\[[MP]\d+\])[^`\n]*?)|"
    r"(?:[;:,.\-–—\s]+))`{1,3}"
)


def remover_codigo(texto: str) -> str:
    """Devolve o texto sem blocos de código (para limpeza e verificação seletivas)."""
    return re.sub(r"```.*?```", "", texto, flags=re.S)


PALAVRAS_TECNICAS = re.compile(r"^[\w\.\-/\\:\[\]\(\)#%=<>+*&|,;'\"]{1,40}$")


def _e_codigo(entre_crases: str, com_crase: str) -> bool:
    """Diz se o trecho entre crases é mesmo código/campo (e não uma fala que veio marcada).

    Campo, consulta e payload continuam preservados. O que sai é fala ou trecho de documento
    citado entre aspas, que veio marcado com crase na origem.
    """
    interno = entre_crases.strip()
    if '"' in interno or "“" in interno:
        # só é considerado citação quando parece frase, não estrutura de dados
        if not re.search(r"[{}()\[\]=]|\w\s*:\s*[\"'{]", interno) and len(interno.split()) >= 5:
            return False
    return bool(PALAVRAS_TECNICAS.match(interno)) or len(interno.split()) < 12


PLACEHOLDER_CODIGO = "\x01"


def com_codigo_protegido(texto: str, tratamento) -> str:
    """Aplica o tratamento ao texto inteiro, preservando os trechos de código por marcador.

    Assim uma citação que atravessa trechos de código (ou de campo) continua sendo reconhecida
    como uma citação só, em vez de sair fragmentada.
    """
    guardados: list[str] = []

    def guarda(m: re.Match[str]) -> str:
        guardados.append(m.group(0))
        return "%s%d%s" % (PLACEHOLDER_CODIGO, len(guardados) - 1, PLACEHOLDER_CODIGO)

    protegido = re.sub(r"`[^`\n]{1,240}`", guarda, texto)
    resultado = tratamento(protegido)
    for indice, valor in enumerate(guardados):
        resultado = resultado.replace("%s%d%s" % (PLACEHOLDER_CODIGO, indice, PLACEHOLDER_CODIGO), valor)
    return resultado


def fora_de_codigo_inline(texto: str, tratamento) -> str:
    """Aplica um tratamento só ao que está fora de trechos entre crases (código, campos).

    Trecho entre crases só é preservado quando de fato parece código; falas que vieram
    marcadas entre crases entram no tratamento, para não sobrar transcrição no material.
    """
    partes = re.split(r"(`[^`\n]*`)", texto)
    for i, parte in enumerate(partes):
        if parte.startswith("`") and parte.endswith("`") and len(parte) > 2:
            if _e_codigo(parte[1:-1], parte):
                continue
            partes[i] = tratamento(parte[1:-1])
        else:
            partes[i] = tratamento(parte)
    return "".join(partes)


CITACAO_CURVA = re.compile(r"[“][^“”]{0,900}[”]", re.S)
CITACAO_ANGULAR = re.compile(r"«[^«»]{0,900}»", re.S)
CITACAO_RETA = re.compile(r'"[^"]{0,900}"', re.S)
CITACAO_SIMPLES = re.compile(r"(?<=\s)'[^']{0,200}'|'[^']{0,140}'(?=[\s.,;:])")
ANOTACAO_DE_ORIGEM = re.compile(
    r"(?i)\[\s*[^\[\]]{0,140}?\b(?:leitura|item|fala|trecho|documento|tela|planilha|anexo|"
    r"ver|conferir|captura|encerramento|in[íi]cio|retomada|continua[çc][ãa]o|momento|cena|"
    r"grava[çc][ãa]o|revis[ãa]o)\b[^\[\]]{0,140}?\]"
)


def _parece_citacao(conteudo: str) -> bool:
    """Uma sequência entre aspas só é tratada como citação quando parece fala/documento."""
    return len(conteudo.split()) >= 3 or len(conteudo) <= 60


def remover_citacoes(t: str) -> str:
    """Retira as falas e os trechos citados — a explicação fica, o literal da fonte sai.

    O material não transcreve o que foi dito: quando a origem trazia uma fala entre aspas,
    o trecho sai inteiro (não basta tirar as aspas, o conteúdo continuaria sendo transcrição).
    """
    for padrao in (CITACAO_CURVA, CITACAO_ANGULAR):
        t = padrao.sub(lambda m: " " if _parece_citacao(m.group(0)[1:-1]) else m.group(0), t)
    t = CITACAO_RETA.sub(lambda m: " " if _parece_citacao(m.group(0)[1:-1]) else m.group(0), t)
    t = CITACAO_SIMPLES.sub(" ", t)
    t = ANOTACAO_DE_ORIGEM.sub(" ", t)
    t = re.sub(r"\[\s*[;:,.·|—–\-\s]*\s*\]", " ", t)
    t = re.sub(r"[“”«»]", "", t)
    return t


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
    r"reten[çc][ãa]o|objeto|versionamento|commit|arquivo|linha do tempo|leitura de tela|"
    r"cronologia|cobertura|observa[çc][õo]es de qualidade|transcri[çc][ãa]o|"
    r"sem sql demonstrado|grava[çc][õo]es sem|o que cada grava[çc][ãa]o)[^\n]*)$"
)


def remover_subsecoes_internas(texto: str) -> str:
    """Remove subseções de controle do acervo e de narrativa de captura (não são conhecimento)."""
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
    """Remove tudo o que aponta *quando* algo foi dito e o que é narrativa de captura.

    O material explica o conhecimento; não reproduz falas nem indica em que momento da fonte
    cada informação apareceu. Blocos de código (SQL, payloads) ficam intactos — ali os valores
    são conteúdo.
    """
    partes = re.split(r"(```.*?```)", texto, flags=re.S)
    for i, parte in enumerate(partes):
        if parte.startswith("```"):
            continue
        partes[i] = _limpar_segmento(parte)
    return "\n".join(p for p in partes if p.strip())


def remover_metadados(texto: str) -> str:
    """Remove os selos de metadados e as linhas de continuação deles.

    O selo aparece como item de lista e a descrição continua nas linhas indentadas seguintes.
    Se essas linhas ficassem, sobraria texto solto de procedência no meio do conteúdo
    ("fornecido pelo responsável", "é integralmente legível)").
    """
    linhas = texto.splitlines()
    saida: list[str] = []
    cortando = False
    for linha in linhas:
        if not linha.strip():
            saida.append(linha)
            cortando = False
            continue
        m = re.match(r"^[ \t]*(?:[-*][ \t]+)?\*\*[\w/çãõáéíóúâêô ]{3,40}:\*\*", linha)
        if m or METADADOS_STRIP.match(linha):
            cortando = True
            continue
        if cortando and re.match(r"^[ \t]{2,}\S", linha):
            continue  # continuação indentada do metadado
        cortando = False
        saida.append(linha)
    return "\n".join(saida)


def _limpar_segmento(t: str) -> str:
    # subseções de controle do acervo e de narrativa de captura saem antes do filtro por linha,
    # para que o título ainda esteja presente quando a subseção for reconhecida
    t = remover_subsecoes_internas(t)

    linhas: list[str] = []
    for linha in t.splitlines():
        s = linha.strip()
        if s.startswith(">"):
            continue  # avisos de publicação / de fonte
        if re.match(r"(?i)^atualizado em\b", s):
            continue
        if RUIDO_DE_FONTE.search(linha) or RUIDO_DE_PROCESSO.search(linha):
            continue
        if RUIDO_INTERNO.search(linha) and not linha.lstrip().startswith("|") and len(linha) < 500:
            continue
        linhas.append(linha)
    t = "\n".join(linhas)

    t = remover_tabelas_indesejadas(t)
    t = poda_colunas_internas(t)
    t = desfazer_tabelas_orfas(t)

    # títulos de primeiro nível: o material monta a hierarquia
    t = re.sub(r"(?m)^#\s+.*$", "", t)
    # metadados do topo já são renderizados como selos (com as linhas de continuação)
    t = remover_metadados(t)

    # nomes de mídia explícitos do manifesto (com as crases que os envolvem)
    for nome in NOMES_DE_MIDIA:
        if nome and nome in t:
            t = re.sub(r"`?\s*" + re.escape(nome) + r"\s*`?", "", t)
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

    # ---- fora marcas de tempo e ponteiros de origem
    # crases que envolvem apenas tempos, âncoras ou pontuação não protegem conteúdo: saem antes,
    # para que as remoções alcancem os valores (ex.: `00:04:41`–`00:05:09`)
    t = CRASE_EM_TEMPO.sub(r"\1", t)
    t = CRASE_EM_DATA.sub(r"\1", t)
    t = ESTILO_EM_TEMPO.sub(r"\2", t)
    t = re.sub(r"(\*\*|__)(\s*[,;:·|—–.\-]\s*)\1", r"\2", t)
    # restos do aparato de registro: âncoras de mensagem, datas de análise e capturas
    t = re.sub(r"(?i)[;,(]?\s*(?:as\s+|com\s+)?(?:âncoras?|ancoras?)\b[^;.)\n]{0,200}[;.)]?", " ", t)
    t = re.sub(r"\[[MP]nn\]", "", t)
    t = re.sub(r"(?i)\(?\s*fontes?\s+textuais?[^)\n]{0,60}\)?", "", t)
    t = re.sub(r"(?i)\bgravando\s+\d{4}-\d{2}-\d{2}(?:\s+\d{6})?", "", t)
    t = re.sub(r"(?i)\b(grava[çc][ãa]o|sess[ãa]o|chamada|demonstra[çc][ãa]o|reuni[ãa]o|treinamento|conversa)"
               r"\s+(?:d[ea]o?\s+|em\s+)?\d{4}-\d{2}-\d{2}\b", r"\1", t)
    t = re.sub(r"(?i)\bem\s+\*{0,2}\s*\d{4}-\d{2}-\d{2}\s*\*{0,2}", "", t)
    t = re.sub(r"(?i)\bcaptura\s*\d+\b", "", t)
    t = INTERVALO_TEMPO.sub("", t)
    t = LIGACOES_TEMPO.sub("", t)
    t = CARIMBO_TEMPO.sub("", t)
    t = REF_ANCORA.sub("", t)
    t = DATA_ISO_PARENTESE.sub("", t)
    t = ANCORA_RE.sub("", t)
    t = SECAO_RE.sub("", t)

    # ---- fora citações: o material explica, não reproduz falas
    t = fora_de_codigo_inline(t, remover_citacoes)   # primeiro, falas que vieram marcadas como código
    t = com_codigo_protegido(t, remover_citacoes)    # depois, citações que atravessam campos

    # sobras de referência cruzada
    t = re.sub(r"(?i)\(\s*(?:ver|vide|conferir|cf\.)\s[^)]{0,140}\)", "", t)
    t = re.sub(r"(?i)[—–-]\s*(?:ver|vide|conferir)\s+(?:o\s+|a\s+)?se[çc][ãa]o\s+[\d\.]+[^.\n]*", "", t)
    t = re.sub(r"(?i),\s*ver\s+se[çc][ãa]o\s+[^.\n]*", "", t)
    t = re.sub(r'(?i)\bse[çc][ãa]o\s+"[^"]{0,80}"(?:\s*,?\s*item\s*\d+)?', "", t)
    t = re.sub(r"(?i)\b(ver|conferir|vide)\s*(,|;|\.|$)", r"\2", t, flags=re.M)
    t = re.sub(r"\(\s*(?:,|;|·|\||—|-|`|\*|_)*\s*\)", "", t)
    t = re.sub(r"\[\s*\]", "", t)
    t = re.sub(r"(`{1,3})\s*\1", "", t)
    t = re.sub(r"[ \t]+([,;.])", r"\1", t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = re.sub(r"(?m)^[ \t]*[-*][ \t]*$", "", t)
    # preposições e pontuação que ficaram penduradas depois das remoções
    # ("a reunião foi mascarada em;", ", a reunião detalha…")
    t = re.sub(r"(?i)\b(?:em|de|do|da|no|na|com|sobre|para|entre|as|às)\s*(?=[,;.:!?)\]]|\s*$)", "", t)
    t = re.sub(r"(?m)^(\s*[-*]?\s*)[,;:]\s*", r"\1", t)
    t = re.sub(r"(?m)^\s*[,;]\s*", "", t)
    # travessões e hífens que sobraram de remoções: "— —", "web service —."
    t = re.sub(r"(?:\s*[—–]\s*){2,}", " ", t)
    t = re.sub(r"[—–]\s*([.;,])", r"\1", t)
    t = re.sub(r"(?i)\btimestamps?\b", "", t)
    # frase que ficou sem predicado depois da remoção ("e a regra final é.")
    t = re.sub(r"(?i)(?:,\s*)?(?:e\s+)?(?:a|o|as|os)\s+[\w\sçãõáéíóúâêô]{1,40}\s+(?:é|são|era|eram|foi|foram)\s*\.", ".", t)
    # parêntese que ficou só com palavras de ligação ("(o, citado em)")
    t = re.sub(r"\([^()]{0,40}\)", lambda m: "" if re.fullmatch(
        r"(?i)[\s,;:·|—–\-]*(?:o|a|os|as|e|em|de|do|da|no|na|com|citado|citada|ver|item|fonte)?"
        r"[\s,;:·|—–\-]*", m.group(0)[1:-1]) and len(m.group(0)[1:-1].split()) <= 3 else m.group(0), t)
    # sobras de ligação interna que virou caminho solto: "(../SQL/)", "(/x/y)"
    t = re.sub(r"\(\s*(?:\.{1,2}/|/)[\w./\\-]{0,60}\)", "", t)
    # pontuação que sobra quando o valor do meio sai: "em ,", "( ,", ", ,"
    t = re.sub(r"[ \t]+(?=[,;.])", "", t)
    t = re.sub(r",\s*(?=[,;)])", "", t)
    t = re.sub(r"\(\s*(?=[,;)])", "(", t)
    t = re.sub(r"(\w)\s*,\s*(?=[.)])", r"\1", t)
    t = com_codigo_protegido(t, capitalizar_inicios)
    # respingos de remoção dentro da frase: "descrita como e outra como", "contexto ."
    t = re.sub(r"(?i)\bcomo\s+(?=(?:e|ou)\s)", "", t)
    t = re.sub(r"(?i)\b(?:de|do|da|em|com|para|e)\s+(?=[,.;:])", "", t)
    t = re.sub(r"\s+([,.;:!?])", r"\1", t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = remover_titulos_vazios(t)
    t = equilibrar_crases(t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def capitalizar_inicios(texto: str) -> str:
    """Devolve maiúscula ao início de linha e de frase depois das remoções."""
    texto = re.sub(r"(?m)^([ \t]*[-*]?[ \t]*)([a-záéíóúâêôãõç])",
                   lambda m: m.group(1) + m.group(2).upper(), texto)
    return re.sub(r"(?<=[.!?]\s)([a-záéíóúâêôãõç])", lambda m: m.group(1).upper(), texto)


def remover_titulos_vazios(texto: str) -> str:
    """Descarta títulos que ficaram sem conteúdo depois da limpeza.

    Quando o trecho de um título era só citação ou metadado, ele sai junto: um título órfão no
    material ("Fala do apresentador…") não explica nada.
    """
    linhas = texto.splitlines()
    saida: list[str] = []
    for i, linha in enumerate(linhas):
        titulo = re.match(r"^(#{2,4})\s+\S", linha)
        if titulo:
            seguinte = next((l for l in linhas[i + 1:] if l.strip()), "")
            outro = re.match(r"^(#{1,4})\s+\S", seguinte) if seguinte else None
            if not seguinte or (outro and len(outro.group(1)) <= len(titulo.group(1))):
                continue
        saida.append(linha)
    return "\n".join(saida)


COLUNA_INTERNA = re.compile(
    r"(?i)^\s*(?:grava[çc][ãa]o(?:\s*e\s*timestamps?)?|timestamps?|intervalo|carimbo|"
    r"âncora|ancora|hora|momento|an[áa]lise detalhada e captura|captura|ocorr[êe]ncias)\s*$"
)


def _celulas(linha: str) -> list[str]:
    return re.split(r"(?<!\\)\|", linha.strip().strip("|"))


def poda_colunas_internas(texto: str) -> str:
    """Descarta colunas que só indicavam *onde/em que momento* algo foi mostrado.

    O conhecimento continua: as rotinas, os resultados e as exceções permanecem; sai apenas
    a coluna que apontava para a gravação ou o carimbo de tempo. Quando a tabela inteira é um
    inventário de captura (sobra menos de duas colunas de conteúdo), ela sai por completo.
    """
    linhas = texto.splitlines()
    saida: list[str] = []
    i = 0
    while i < len(linhas):
        if not linhas[i].lstrip().startswith("|"):
            saida.append(linhas[i])
            i += 1
            continue
        bloco: list[str] = []
        j = i
        while j < len(linhas) and linhas[j].lstrip().startswith("|"):
            bloco.append(linhas[j])
            j += 1
        cabecalho = _celulas(bloco[0])
        fora = {k for k, c in enumerate(cabecalho) if COLUNA_INTERNA.match(c)}
        if not fora or len(fora) >= len(cabecalho):
            saida.extend(bloco)
            i = j
            continue
        linhas_novas: list[str] = []
        for linha in bloco:
            celulas = _celulas(linha)
            if len(celulas) <= max(fora):
                linhas_novas.append(linha)
                continue
            restantes = [c for k, c in enumerate(celulas) if k not in fora]
            if not any(re.sub(r"[\s\-–—:.]", "", c) for c in restantes):
                continue  # linha que só continha o ponteiro de origem
            linhas_novas.append("|" + "|".join(restantes) + "|")
        if linhas_novas and len(_celulas(linhas_novas[0])) >= 2:
            saida.extend(linhas_novas)
        i = j
    return "\n".join(saida)


DELIMITADOR_TABELA = re.compile(r"^\|[\s\-:|]+\|$")


def desfazer_tabelas_orfas(texto: str) -> str:
    """Converte linhas de tabela sem cabeçalho em texto corrido.

    Na origem, alguns quadros aparecem sem a linha de cabeçalho (a tabela continua depois de um
    espaço em branco). Sem isto, as barras verticais vazariam para o meio da explicação.
    """
    linhas = texto.splitlines()
    saida: list[str] = []
    i = 0
    while i < len(linhas):
        if not linhas[i].lstrip().startswith("|"):
            saida.append(linhas[i])
            i += 1
            continue
        bloco: list[str] = []
        j = i
        while j < len(linhas) and linhas[j].lstrip().startswith("|"):
            bloco.append(linhas[j])
            j += 1
        if len(bloco) >= 2 and DELIMITADOR_TABELA.match(bloco[1].strip()):
            saida.extend(bloco)  # tabela íntegra: cabeçalho, delimitador e corpo
        else:
            for linha in bloco:
                celulas = [c.strip(" *") for c in _celulas(linha)]
                celulas = [c for c in celulas if re.sub(r"[\s\-–—:.]", "", c)]
                if celulas:
                    saida.append("- " + " — ".join(celulas).rstrip(" —") + ".")
        i = j
    return "\n".join(saida)


def remover_tabelas_indesejadas(texto: str) -> str:
    """Descarta quadros de tempo e de controle interno e linhas que eram só um momento."""
    linhas = texto.splitlines()
    saida: list[str] = []
    i = 0
    while i < len(linhas):
        linha = linhas[i]
        if linha.lstrip().startswith("|"):
            bloco: list[str] = []
            j = i
            while j < len(linhas) and linhas[j].lstrip().startswith("|"):
                bloco.append(linhas[j])
                j += 1
            cabecalho = bloco[0].strip("|") if bloco else ""
            if re.search(r"(?i)\b(?:intervalo|timestamps?|carimbo|hora|âncora|ancora)\b", cabecalho) \
                    or RUIDO_INTERNO.search(cabecalho):
                i = j  # quadro de tempos ou de controle do acervo: sai inteiro
                continue
            for indice, linha_tabela in enumerate(bloco):
                if indice == 1 and re.match(r"^\|[\s\-:|]+\|$", linha_tabela.strip()):
                    saida.append(linha_tabela)
                    continue
                celulas = linha_tabela.strip().strip("|").split("|")
                if celulas:
                    primeira = CARIMBO_TEMPO.sub("", INTERVALO_TEMPO.sub("", celulas[0]))
                    if not re.sub(r"[`\s\-–—.]", "", primeira):
                        continue  # linha cuja primeira coluna era só o momento
                saida.append(linha_tabela)
            i = j
            continue
        saida.append(linha)
        i += 1
    return "\n".join(saida)

    # sobras de referência cruzada
    t = re.sub(r"(?i)\(\s*(?:ver|vide|conferir|cf\.)\s[^)]{0,140}\)", "", t)
    t = re.sub(r"(?i)[—–-]\s*(?:ver|vide|conferir)\s+(?:o\s+|a\s+)?se[çc][ãa]o\s+[\d\.]+[^.\n]*", "", t)
    t = re.sub(r"(?i),\s*ver\s+se[çc][ãa]o\s+[^.\n]*", "", t)
    t = re.sub(r'(?i)\bse[çc][ãa]o\s+"[^"]{0,80}"(?:\s*,?\s*item\s*\d+)?', "", t)
    t = t.replace("§", "seção ")
    t = re.sub(r"(?i)\b(ver|conferir|vide)\s*(,|;|\.|$)", r"\2", t, flags=re.M)
    t = re.sub(r"\(\s*(?:,|;|·|\||—|-|`|\*|_)*\s*\)", "", t)
    t = re.sub(r"\[\s*\]", "", t)
    t = re.sub(r"(`{1,3})\s*\1", "", t)
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


def _limpar_selo(valor: str, limite: int = 140) -> str:
    """Reduz a linha de metadados a um selo curto e legível."""
    texto = valor.replace("`", "").replace("*", "").strip()
    texto = re.split(r"\s+[—–]\s+|\s*;\s*|\s+\(\s*", texto)[0].strip(" .,;:")
    if len(texto) > limite:
        corte = texto[:limite].rsplit(" ", 1)[0]
        texto = corte.rstrip(" ,;.") + "…"
    return texto


def extrair_titulo_metadados(texto: str) -> tuple[str, str]:
    """Lê os selos de categoria e de confiança declarados no próprio documento."""
    categoria = confianca = ""
    mc = re.search(r"(?im)^[ \t]*(?:[-*][ \t]+)?\*\*Categoria:\*\*[ \t]*(.+?)[ \t]*$", texto)
    if mc:
        categoria = _limpar_selo(mc.group(1), 120)
    mf = re.search(r"(?im)^[ \t]*(?:[-*][ \t]+)?\*\*Confiança da extração:\*\*[ \t]*(.+?)[ \t]*$", texto)
    if mf:
        confianca = _limpar_selo(mf.group(1), 120)
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
    return ajustar_pontuacao(equilibrar_estilo(convertido))


def equilibrar_estilo(html_txt: str) -> str:
    """Remove marcas de negrito/itálico que a origem deixou desemparelhadas.

    Alguns documentos têm ênfase mal fechada (sobra de marcação na fonte). Sem isto, o trecho
    realçado vazaria até o fim do parágrafo. A marca solta sai; o texto permanece.
    """
    for tag in ("strong", "em"):
        abrir, fechar = "<%s>" % tag, "</%s>" % tag
        while html_txt.count(abrir) != html_txt.count(fechar):
            if html_txt.count(abrir) > html_txt.count(fechar):
                posicao = html_txt.rfind(abrir)
            else:
                posicao = html_txt.rfind(fechar)
            if posicao < 0:
                break
            html_txt = html_txt[:posicao] + html_txt[posicao + len(abrir):]
    return html_txt


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
        parte = re.sub(r"<(strong|em)>\s*</\1>", "", parte)
        parte = re.sub(r"<(strong|em)>\s*([,;:·|—–\-]*)\s*</\1>", r"\2", parte)
        parte = re.sub(r"\(\s*[,;·|—–-]*\s*\)", "", parte)
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
<b>Função Sistemas</b>. Ele foi escrito para ser <b>lido e entendido</b>: cada capítulo abre com a
explicação do assunto e, em seguida, traz o detalhamento do que foi aprendido. Não há transcrição de
falas nem indicação de em que momento de um vídeo algo foi dito — o que existe aqui é o
conhecimento, organizado por tema.</p>

<div class="destaque">
  <h3>Como ler</h3>
  <ul>
    <li><b>Comece pelos capítulos temáticos.</b> Cada um tem duas partes: a <i>explicação</i> inicial
    (conceitos, regras e o porquê) e o <i>detalhamento por origem</i> (o que foi aprendido em cada
    treinamento, reunião ou conversa sobre aquele tema).</li>
    <li><b>Os capítulos se cruzam.</b> Um mesmo assunto aparece sob ângulos diferentes — negócio,
    integração, teste e ambiente — e é essa combinação que forma o entendimento completo.</li>
    <li><b>Cada bloco traz selos</b> de categorias de conhecimento e de <b>confiança da extração</b>,
    para você saber o quanto aquela informação pode ser tratada como consolidada.</li>
    <li><b>Antes de executar qualquer coisa, leia o capítulo de pontos a validar.</b> Ele reúne o que
    não foi confirmado, o que pode ter mudado de versão e o que depende de decisão de alguém.</li>
    <li>Use a <b>busca</b> no topo para encontrar um termo, uma sigla, uma tela ou uma regra, e os
    botões <i>expandir</i>/<i>recolher</i> para abrir o material inteiro de uma vez.</li>
  </ul>
</div>

<div class="aviso">
  <h3>Aviso importante</h3>
  <p>Este material é <b>apoio de estudo e memória de trabalho</b>. Ele não substitui a especificação
  vigente, o runbook nem a validação com o responsável de cada frente: regras, telas e versões mudam.
  Nenhum procedimento aqui foi executado durante a produção deste material — o que existe é o que foi
  ensinado, demonstrado ou relatado, mais as ressalvas correspondentes. Onde a informação não foi
  confirmada, o material diz que não foi, em vez de completar por suposição.</p>
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

    # -- capítulos temáticos: abrem com a explicação do assunto e seguem com o detalhamento
    numero_capitulo = 0
    for chave, titulo, descricao in TEMAS:
        numero_capitulo += 1
        corpo = []
        if SINTESES.get(chave):
            corpo.append('<article class="sintese">%s</article>\n' % SINTESES[chave])
        detalhes = []
        n = 0
        for slug, (rotulo, tipo, tema) in FONTES.items():
            if tema != chave:
                continue
            n += 1
            detalhes.append(bloco_fonte(slug, rotulo, tipo, "guia_de_estudo.md", "Guia", "%d.%d" % (numero_capitulo, n)))
        if detalhes:
            corpo.append('<h3 class="subtitulo">Detalhamento por origem</h3>')
            corpo.extend(detalhes)
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

.sintese{background:linear-gradient(180deg,#f8fbff 0%,#ffffff 55%);border:1px solid #cfe0f3;
  border-left:6px solid var(--teal);border-radius:12px;padding:18px 22px;margin:0 0 20px}
.sintese h3{margin:0 0 10px;font-size:20px;color:var(--azul)}
.sintese h4{margin:18px 0 8px;font-size:16.5px;color:var(--teal)}
.sintese p{margin:0 0 10px}
.sintese ul,.sintese ol{margin:0 0 12px 22px;padding:0}
.sintese li{margin:5px 0}
.sintese b{color:#0b2b4a}
h3.subtitulo{margin:22px 0 10px;font-size:15.5px;text-transform:uppercase;letter-spacing:.05em;
  color:var(--texto-suave);border-bottom:1px solid var(--borda);padding-bottom:6px}

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
    "marca de tempo": re.compile(r"\b\d{1,2}:\d{2}(?::\d{2})?\b"),
    "aspas de citação": re.compile(r"[“”«»]"),
    "marcação de negrito solta": re.compile(r"\*\*"),
    "âncora de mensagem": re.compile(r"\[[MP]\d+\]|\[[MP]nn\]"),
    "nome de arquivo de mídia": re.compile(r"\.(?:mp4|md|json|srt|vtt|png|jpe?g|xlsx)\b"),
}


def verificar_saida(doc: str) -> list[str]:
    """Confere que o material não expõe nomes de arquivo, marcas de tempo nem refs internas."""
    conteudo = re.sub(r"<script>.*?</script>", "", doc, flags=re.S)
    conteudo = re.sub(r"<style>.*?</style>", "", conteudo, flags=re.S)
    achados = []
    for nome, padrao in VAZAMENTOS.items():
        alvo = conteudo
        if nome in ("marca de tempo", "aspas de citação", "marcação de negrito solta"):
            # conteúdo técnico (SQL, payloads, exemplos de dados) pode conter horário como dado
            alvo = re.sub(r"<pre>.*?</pre>", "", alvo, flags=re.S)
            alvo = re.sub(r"<code>.*?</code>", "", alvo, flags=re.S)
        encontrados = padrao.findall(alvo)
        if encontrados:
            exemplos = ", ".join(sorted(set(encontrados))[:3])
            achados.append("%s (%d): %s" % (nome, len(encontrados), exemplos))
    return achados


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--saida", default=os.path.join(RAIZ, "saida", "index.html"))
    p.add_argument("--sem-distribuivel", action="store_true",
                   help="não escreve a cópia publicada em material-de-estudo/")
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

    # cópia versionada: é o arquivo que circula (leitura e download). Sai do mesmo documento,
    # na mesma execução, para não divergir do que o gerador produz.
    if not args.sem_distribuivel:
        destino = os.path.abspath(os.path.join(RAIZ, NOME_DISTRIBUIDO))
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with open(destino, "w", encoding="utf-8") as fh:
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
