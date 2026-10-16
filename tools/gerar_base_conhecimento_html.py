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
import zipfile
import unicodedata

import markdown

from sintese_conhecimento import SINTESES

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOME_ARQUIVO = "base-de-conhecimento-funcao-sistemas.html"
NOME_DISTRIBUIDO = os.path.join("material-de-estudo", NOME_ARQUIVO)
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
        # a limpeza e a rede de segurança agem bloco a bloco: um parágrafo muito narrativo
        # não arrasta consigo o resto do documento
        trechos = []
        for bloco in re.split(r"\n\s*\n", parte):
            if not bloco.strip():
                trechos.append(bloco)
                continue
            limpo = _limpar_segmento(bloco)
            tamanho = len(bloco.strip())
            if tamanho > 220 and len(limpo) < 0.5 * tamanho:
                limpo = _limpar_segmento(bloco, narrativa="frases")
            trechos.append(limpo)
        partes[i] = "\n\n".join(t for t in trechos if t.strip())
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


CATEGORIA_ACERVO = (
    r"(?:D[ÚU]VIDA_OU_CONFLITO|D[ÚU]VIDAS?_E_CONFLITOS?|INFRA_E_ACESSO|CONFLITOS?_E_VALIDA[ÇC][ÃA]O|"
    r"NEG[ÓO]CIO|SISTEMAS|PROCESSOS|PROCEDIMENTOS|SQL|GLOSS[ÁA]RIO(?:_GERAL)?|TRILHAS_DE_ESTUDO|"
    r"INDICE_[A-Z_]+|TESTES|AUTOMA[ÇC][ÃA]O|COMUNICA[ÇC][ÃA]O|INFRAESTRUTURA)"
)
CATEGORIA_SOZINHA = re.compile(r"^\s*`?%s`?(?:\s*/\s*`?%s`?)*\s*$" % (CATEGORIA_ACERVO, CATEGORIA_ACERVO))
CATEGORIA_EM_LINHA = re.compile(r"`?%s`?(?:\s*/\s*`?%s`?)+" % (CATEGORIA_ACERVO, CATEGORIA_ACERVO))


def remover_categorias_do_acervo(t: str) -> str:
    """Tira as etiquetas de categoria do acervo, que não dizem nada ao leitor.

    Rótulos como `SISTEMAS / PROCESSOS` ou `DÚVIDA_OU_CONFLITO` são controle interno da
    biblioteca: a linha inteira sai quando é só isso, e a etiqueta sai quando acompanha algo.
    """
    linhas = []
    for linha in t.splitlines():
        if linha.lstrip().startswith("|"):
            celulas = linha.split("|")
            conteudo = [c for c in celulas[1:-1] if c.strip()]
            if conteudo and all(CATEGORIA_SOZINHA.match(c.strip()) or c.strip() in ("—", "-", "sim",
                                                                                   "não", "nao")
                                for c in conteudo):
                continue          # linha de tabela que só carrega etiqueta de categoria
            celulas = [CATEGORIA_SOZINHA.sub(" ", c) if CATEGORIA_SOZINHA.match(c.strip()) else c
                       for c in celulas]
            linha = "|".join(celulas)
        linha = CATEGORIA_EM_LINHA.sub(" ", linha)
        linha = re.sub(r"[ \t]{2,}", " ", linha)
        linha = re.sub(r"\s*[—–-]\s*(?=[|,;.]|$)", " ", linha)
        if linha.strip() in ("", "|"):
            continue
        linhas.append(linha.rstrip())
    return "\n".join(linhas)


def _limpar_segmento(t: str, narrativa: bool | str = True) -> str:
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

    t = remover_categorias_do_acervo(t)
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

    # travessão que sobrou de uma remoção: "attachment_document —." → "attachment_document."
    t = re.sub(r"[ \t]*[—–][ \t]*(?=[.,;:])", "", t)
    # negrito que ficou sem conteúdo depois de uma remoção: "chamado de **." → "chamado de."
    # A marca só sai quando é órfã — depois de espaço/abertura/início e antes de pontuação ou fim.
    # Sem essa condição a regra apagava o fechamento de um negrito legítimo ("**Autorizador
    # Web**, acessar") e desalinhava todos os pares seguintes do trecho.
    t = re.sub(r"(?:(?<=\s)|(?<=[(\[\-–—])|^)\*\*(?=\s*[.,;:!?)\]\-–—]|\s*$)", "", t)
    t = re.sub(r"\*\*\s*\*\*", "", t)
    t = re.sub(r"[ \t]+(?=[.,;:](?:\s|$))", "", t)

    # ---- fora a narrativa sobre as fontes: o material fala do trabalho, não de quem falou
    t = limpar_codigo_inline(t)
    t = sem_metarreferencia(sem_referencia_ao_meio(t))
    t = sem_incerteza(t)
    if narrativa:
        if narrativa is True:
            t = sem_narrativa_de_fonte(t)
        t = limpar_narrativa_por_frase(t)

    # sobras de referência cruzada
    t = re.sub(r"(?i)\(\s*(?:ver|vide|conferir|cf\.)\s[^)]{0,140}\)", "", t)
    t = re.sub(r"(?i)[—–-]\s*(?:ver|vide|conferir)\s+(?:o\s+|a\s+)?se[çc][ãa]o\s+[\d\.]+[^.\n]*", "", t)
    t = re.sub(r"(?i),\s*ver\s+se[çc][ãa]o\s+[^.\n]*", "", t)
    t = re.sub(r'(?i)\bse[çc][ãa]o\s+"[^"]{0,80}"(?:\s*,?\s*item\s*\d+)?', "", t)
    t = re.sub(r"(?i)\b(ver|conferir|vide)\s*(,|;|\.|$)", r"\2", t, flags=re.M)
    t = re.sub(r"\(\s*(?:,|;|·|\||—|-|`|\*|_)*\s*\)", "", t)
    t = re.sub(r"\[\s*\]", "", t)
    t = re.sub(r"(`{1,3})\s*\1", "", t)
    t = re.sub(r"[ \t]+([,;.])(?=\s|$)", r"\1", t)
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
    t = re.sub(r"[ \t]+(?=[,;.](?:\s|$))", "", t)
    t = re.sub(r",\s*(?=[,;)])", "", t)
    t = re.sub(r"\(\s*(?=[,;)])", "(", t)
    t = re.sub(r"(\w)\s*,\s*(?=[.)])", r"\1", t)
    t = com_codigo_protegido(t, capitalizar_inicios)
    # respingos de remoção dentro da frase: "descrita como e outra como", "contexto ."
    t = re.sub(r"(?i)\bcomo\s+(?=(?:e|ou)\s)", "", t)
    t = re.sub(r"(?i)\b(?:de|do|da|em|com|para|e)\s+(?=[,.;:])", "", t)
    t = re.sub(r"\s+([,.;:!?])(?=\s|$)", r"\1", t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    # última passada: depois de tirar citação, narrativa e nome de quem falou, a frase pode ter
    # ficado quebrada ("chamado de .") — o filtro de certeza roda de novo para tirá-la inteira
    t = re.sub(r"\*\*\s*(?=[.,;:!?]|\s*$)", "", t)
    t = re.sub(r"[ \t]+(?=[.,;:!?](?:\s|$))", "", t)
    t = sem_metarreferencia(t)
    t = sem_incerteza(t)
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
    t = re.sub(r"[ \t]+([,;.])(?=\s|$)", r"\1", t)
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


NARRATIVA_NOMES = (r"interlocutor\w*|orientador\w*|apresentador\w*|operador\w*|analista\w*|tester|"
                 r"participantes|gestor\w*|colega\w*|usu\w*rios?|autor\w*|instrutor\w*|pessoas?|"
                 r"respons[áa]vel pela grava[çc][ãa]o")
NARRATIVA_MIDIA = (r"grava[çc][ãa]o|conversa|reuni[ãa]o|chamada|v[íi]deo|demonstra[çc][ãa]o|fonte do acervo|"
                 r"chat|falas?|aula|treinamento|transcri[çc][ãa]o|amostragem|pacote de an[áa]lise|"
                 r"documento do acervo|material do acervo")
# o que fala do meio (tela, print, captura) só sai quando a frase é sobre não mostrar/não confirmar
NARRATIVA_MEIO = r"tela|print|captura|imagem|figura|planilha|documento|pacote|v[íi]deo|pdf"

# frase que só relata a captura, sem regra nem procedimento: sai inteira
FRASE_SEM_CONTEUDO = re.compile(
    r"(?i)^(?:"
    r"(?:n[ãa]o\s+)?(?:foi|foram|é|são|est[áa]|est[ãa]o)\s+"
    r"(?:mencionad|citad|relatad|dito|comentad|discutid|descrit|indicad|registrad|vist|visto|observad|"
    r"demonstrad|confirmad|valid|executad|reproduzid)\w*"
    r"|(?:a|o|os|as)\s+(?:" + NARRATIVA_MIDIA + r")\b"
    r"|(?:a|o|os|as)\s+(?:" + NARRATIVA_MEIO + r")\b[^.]{0,60}?\b(?:n[ãa]o|nenhum\w*|sem)\b[^.]{0,60}?\b"
    r"(?:mostra|exibe|confirma|traz|apresenta|aparece|aparecem|consta|demonstra|registra)\b"
    r"|(?:a|o|os|as)\s+(?:" + NARRATIVA_NOMES + r")\b[^.]{0,40}?\b(?:navega|comenta|descreve|questiona|"
    r"responde|pergunta|observa|relata|conclui|recomenda|decide|tenta|abre|segue|entra|percorre|come[çc]a|"
    r"admite|alega|aponta|nota|ressalta|refor[çc]a|complementa|completa|acrescenta|lembra|recorda|"
    r"entende|acredita|espera|indica|mostra|detalha|repassa|sinaliza|confirma|esclarece)\b"
    r"|(?:segundo|conforme|de acordo com|para)\s+(?:o|a|os|as)\s+(?:" + NARRATIVA_NOMES + r"|" + NARRATIVA_MIDIA + r")\b"
    r"|(?:nada|nenhum\w*)\s+(?:foi|é)\s+"
    r"|vale (?:registrar|notar|destacar)"
    r"|(?:a|o)\s+(?:" + NARRATIVA_NOMES + r")\s+(?:navega|comenta|descreve|apresenta|questiona|responde|"
    r"pergunta|afirma|diz|relata|discute|mostra|ensina|explica|sugere|prop[õo]e|cita|menciona|informa|"
    r"confirma|esclarece|pontua|destaca|abre|segue|entra|percorre|come[çc]a|tenta|tenta novamente|decide|"
    r"conclui|recomenda|observa|analisa|estuda|testa|executa)\b"
    r"|n[ãa]o h[áa] (?:evid[êe]ncia|captura|registro|confirma[çc][ãa]o|prova|demonstra[çc][ãa]o)"
    r"|n[ãa]o (?:confirma|demonstra|mostra|deixa claro|esclarece|registra|indica|permite|consta|aparece)"
    r"|(?:a|o|os|as)\s+(?:tela|captura|print|imagem|figura|compartilhamento de tela|amostragem)\s+"
    r"(?:amostrad\w+|mostrad\w+|compartilhad\w+|exibid\w+|revisad\w+|citad\w+)"
    r"|sem (?:evid[êe]ncia|captura|confirma[çc][ãa]o|execu[çc][ãa]o)"
    r"|(?:o|a)\s+leitura\s+(?:de tela|do quadro)"
    r"|a (?:leitura|interpreta[çc][ãa]o)\b[^.]{0,40}(?:é|fica)\b"
    r"|(?:posteriormente|depois|em seguida|por fim|ao final|no encerramento|no in[íi]cio)\s*,?\s*(?:o|a|os|as)\s"
    r")"
)

# "o interlocutor comenta que, em geral, X" → "X"
FRASE_COM_CONTEUDO = re.compile(
    r"(?i)^(?:o|a|os|as)\s+(?:" + NARRATIVA_NOMES + r"|" + NARRATIVA_MIDIA + r")\s+"
    r"[^.]{0,80}?\b(?:que|se)\s+(.{{10,}})$"
)
# "É mencionado X" / "Foi citado X" → "X"
FRASE_PASSIVA = re.compile(
    r"(?i)^(?:é|s[ãa]o|foi|foram)\s+(?:mencionad|citad|relatad|comentad|descrit|indicad)\w*\s+(.{{10,}})$")


FRASE_QUEBRADA = re.compile(
    r"(?i)"
    r"\b(?:em|de|do|da|no|na|com|para|por|como|que|e|ou|o|a|os|as|é|são|foi|foram|est[áa]|est[ãa]o)\s*[,;]"
    r"|\s+,\s|\s+/\s*[,.;]|\betc\.,?\s*$|\bcomo\s*\."
    r"|\(\s*\)|\b(?:o|a)\s+(?:é|são)\s+associad|\bexpandid[oa] como\s*[,.e]"
)
# frase sobre a captura: "não foi demonstrado", "não são confirmadas"
# frase que ficou sem sujeito ou sem complemento depois de uma remoção: sai inteira
FRASE_DANIFICADA = re.compile(
    r"(?i)(?:"
    r"\bcomo\s+(?:e|ou)\b|\b(?:e|ou)\s+como\s*[.,;]|\b(?:de|do|da|em|com|por|para|sobre)\s*[.,;]|"
    r"—\s*[.,;]|\bentre\s*[.,;]|\bchamad[oa]s? de\s*[.,;]|\bpor\s*\.|\bpor causa\s*\.|"
    r"\(\s*\)|\b(?:e|ou|que|de|em|com|por)\s*\.+\s*$|\*\s+e\s*\.|"
    r"\s[,;]\s|\s\.\s|\bde\.+|\bcom\.+|\bpara\.+|\bpor\.+|"
    r"\bseguida,\s+f[áa]r[áa]|\bo outro\s*[—.,;]|\bcomo\s*\.|\bem\s*\.\s*$|"
    r"\b(?:depois de|antes de|com base em|de acordo com)\s*[.,;]"
    r")"
)

FRASE_NAO_CONFIRMA = re.compile(
    r"(?i)\bn[ãa]o\s+(?:s[ãa]o|foi|foram|é|est[áa]|est[ãa]o)?\s*"
    r"(?:demonstrad|confirmad|mostrad|registrad|vist[oa]?|valid|executad|reproduzid|documentad|esclarecid)\w*"
)


def _texto_util(frase: str) -> str:
    """Decide o destino de uma frase: fica como está, perde o enquadramento ou sai."""
    limpa = frase.strip()
    if not limpa:
        return ""
    # linha curta (termo, título, item de lista, rótulo) nunca é narrativa: fica como está,
    # salvo se a remoção de uma citação a deixou sem sentido
    if len(limpa.split()) < 6:
        return "" if FRASE_QUEBRADA.search(limpa) else limpa
    if FRASE_SEM_CONTEUDO.match(limpa) or FRASE_NAO_CONFIRMA.search(limpa):
        return ""
    if FRASE_DANIFICADA.search(limpa):
        return ""
    if FRASE_QUEBRADA.search(limpa):
        return ""
    # resquícios de quem falou
    limpa = re.sub(r"(?i)\b(?:verbalmente|pela fala|por fala|na fala|da fala|a fala|em fala)\b", "", limpa)
    limpa = re.sub(r"\s{2,}", " ", limpa).strip(" ,;")
    if len(limpa.split()) < 4:
        return ""
    return limpa


def remover_blocos_sql(md: str) -> str:
    """Tira do texto corrido os blocos de SQL: o código completo vive no capítulo de consultas."""
    def troca(m: re.Match) -> str:
        corpo = m.group(1).strip()
        if re.search(r"(?i)\b(?:SELECT|INSERT|UPDATE|DELETE|USE|EXEC|CREATE\s+PROCEDURE)\b", corpo):
            return ""
        return m.group(0)

    return re.sub(r"```(?:sql|SQL)?\s*\n(.*?)```", troca, md, flags=re.S)


def limpar_codigo_inline(t: str) -> str:
    """Tira da marcação de código a sobra de uma remoção ao lado: "`null — `" → "`null`"."""
    def arruma(m: re.Match) -> str:
        miolo = m.group(1)
        miolo = re.sub(r"[\s;,.]+[—–-]+\s*$", "", miolo)
        miolo = re.sub(r"^\s*[—–-]+[\s;,.]*", "", miolo)
        miolo = re.sub(r"[\s;,]+$", "", miolo).strip()
        return "`%s`" % miolo if miolo else miolo

    return re.sub(r"`([^`\n]{0,80})`", arruma, t)


def sem_referencia_ao_meio(t: str) -> str:
    """Tira a menção ao meio de origem, onde quer que ela apareça na frase."""
    t = re.sub(r"(?i)\s*\b(?:nesta|neste|nessa|nesse|desta|deste|dessa|desse|esta|este|essa|esse)\s+"
               r"(?:grava[çc][ãa]o|material|conversa|v[íi]deo|reuni[ãa]o|chamada|fonte|pacote|an[áa]lise|acervo)\b",
               "", t)
    t = re.sub(r"(?i)\s*\b(?:com base|segundo|conforme|de acordo com)\s+(?:em\s+)?"
               r"(?:esta|esse|essa|o|a)?\s*"
               r"(?:grava[çc][ãa]o|reuni[ãa]o|conversa|chamada|v[íi]deo|fonte|material|pacote|an[áa]lise|falas?)\b"
               r"[^.;\n]*", "", t)
    # quem executou deixa de ser assunto: a frase passa a descrever a prática
    t = re.sub(r"(?i)\b(?:A |a )pessoa\s+(?:explicitamente\s+)?(?:n[ãa]o\s+)?"
               r"(?:diz|disse|relata|relatou|informa|informou|explica|explicou|comenta|comentou|"
               r"lembra|menciona|mencionou|pede|pediu|admite|aponta|conta|fala|recomenda|sugere)\s+que\s+",
               "", t)
    t = re.sub(r"(?i)\b(?:A |a )pessoa\s+(?:explicitamente\s+)?n[ãa]o lembra\b[^.;]*",
               "não há lista completa dos casos", t)
    t = re.sub(r"(?i)\bA pessoa procura\b", "Procurar", t)
    t = re.sub(r"(?i)\bA pessoa (?:tenta|tentou)\b", "Tentar", t)
    t = re.sub(r"(?i)\bNa parte final, a pessoa pede que o analista\b", "No encaminhamento, o analista deve", t)
    t = re.sub(r"(?i)\bse a pessoa teria permiss[ãa]o\b", "se haveria permissão", t)
    t = re.sub(r"(?i)\ba outra parte da chamada\b", "a outra parte", t)
    t = re.sub(r"(?i)\bdemonstra[çc][ãa]o de para\b", "demonstração para", t)
    t = re.sub(r"(?i)\bN[ãa]o ter testado suficientemente o fluxo e que prepararia uma "
               r"demonstra[çc][ãa]o posterior\.", "O fluxo não foi testado de forma suficiente.", t)
    t = re.sub(r"(?i)\bDados de teste e nomes \(resolvido\):\s*o respons[áa]vel confirmou que todos "
               r"os dados exibidos[^.]*\.", "Dados de teste e nomes: confirmado que os dados exibidos "
               "são fictícios/de teste e que a publicação dos materiais derivados está autorizada, "
               "preservando o nome Função Sistemas e os nomes dos operadores, com omissão de fotos e "
               "câmeras de pessoas.", t)
    t = re.sub(r"(?i)\b(?:ao longo d[aeo]|durante a|no decorrer d[aeo])\s+conversa\b", "", t)
    t = re.sub(r"(?i)\b(?:a|outra|da|de|na|com|à)\s+conversa\b(?:\s+(?:com|de|do|da)\s+[A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wçãõáéíóúâêô]+)?", "", t)
    t = re.sub(r"(?i)\b(?:a|o)\s+interlocutor(?:a)?\b", "a outra parte", t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = re.sub(r"\s+([,.;:])", r"\1", t)
    return t


META_REFERENCIAS: list[tuple[str, str]] = [
    (r"(?i)\bcom base n[ao]s? (?:grava[çc][ãa]o|grava[çc][õo]es|falas?|chamadas?|reuni[ãa]o|conversas?)\b", ""),
    (r"(?i)\b(?:nesta|nessa|na|da|uma|outra|as|essa|esta|à)\s+grava[çc][ãa]o\b(?!\s+de\s+)[^.;,\n]*", ""),
    (r"(?i)\bgrava[çc][ãa]o\s+(tamb[ée]m\s+)?(mostra|registrou|alterna|n[ãa]o fornece|n[ãa]o confirma|sugere)\b", r"o material \1\2"),
    (r"(?i)\b(?:entre|de|em|com|por|para|das|nas|outras)\s+grava[çc][õo]es\b", "de registros"),
    (r"(?i)\buma das grava[çc][õo]es\b", "um dos registros"),
    (r"(?i)\bas grava[çc][õo]es\b", "os registros"),
    (r"(?i)\ba grava[çc][ãa]o\b", "o registro"),
    (r"(?i)\bEsses detalhes n[ãa]o est[ãa]o resolvidos n[ao] (?:registro|material)\b", "Esses detalhes não estão resolvidos"),
    (r"(?i)\bdocumenta[çc][ãa]o/grava[çc][ãa]o\b", "documentação"),
    (r"(?i)\brotina detalhada n[ao] (?:registro|material)\b", "rotina indicada"),
    (r"(?i)\bregistrado por\s*\*{0,2}fala\*{0,2}\b", "registrado por relato"),
    (r"(?i)\b(?:Irm[ãa]|irm[ãa]) mostra\b", "Outro registro mostra"),
    (r"(?i)\bA fonte diz apenas\b", "Não se sabe ao certo:"),
    (r"(?i)\bfala em\b", "menciona"),
    (r"(?i)\(fala:\s*\)", "(informado)"),
    (r"(?i)\(fala\)", "(informado)"),
    (r"(?i)\bA fala confirma\b\s*[:.,;]?", ""),
    (r"(?i)\ba pr[óo]pria fala indica consulta\b", "a informação não foi conferida na base"),
    (r"(?i)\bafirma[çc][ãa]o falada sem confer[êe]ncia\b", "afirmação sem conferência na base"),
    (r"(?i)\bPrimeiro fala em\b", "Primeiro menciona"),
    (r"(?i)\bvariam na pr[óo]pria conversa\b", "variam"),
    (r"(?i)\bconhecido pela conversa irm[ãa]\b", "conhecido de outro registro"),
    (r"(?i)\bconversa n[ãa]o fecha o fluxo\b", "o fluxo de reentrada não está fechado"),
    (r"(?i)\bUma conversa sobre\b", "O assunto é"),
    (r"(?i)\bconversa oral\b", "relato oral"),
    (r"(?i)\bouvidos em conversa\b", "citados"),
    (r"(?i)\bcitados em conversa\b", "citados internamente"),
    (r"(?i)\bo que existe [ée] uma conversa com um analista\b", "o que existe é o relato de um analista"),
    (r"(?i)\bque a pr[óo]pria conversa destaca\b", "destacado no material"),
    (r"(?i)\bA pessoa que orienta menciona\b", "Mencionar"),
    (r"(?i)\ba atribui[çc][ãa]o de quem disse [ée] incerta\b", "a atribuição é incerta"),
    (r"(?i)\bnunca reprocessar produ[çc][ãa]o com base nesta fala\b", "nunca reprocessar produção sem validação"),
    (r"(?i)\b(?:grava[çc][ãa]o|fala)\s+oscila\b", "a definição oscila"),
    (r"(?i)\bfala relata\b", "há menção a"),
    (r"(?i)\bfala sugere\b", "há indício de"),
    (r"(?i)\bItem que:\s*", ""),
    (r"(?i)\ba fonte\s*\*{0,2}\s*n[ãa]o\b[^.;]*[.;]?", ""),
    (r"(?i)\b(?:o|a) (?:registro|material|acervo)\s*\*{0,2}\s*n[ãa]o\b[^.;]*[.;]?", ""),
    (r"(?i)\bA apresentadora atribui\b", "Atribui-se"),
    (r"(?i)\bO apresentador atribui\b", "Atribui-se"),
    (r"(?i)\bA há ind[íi]cio\b", "Há indício"),
    (r"(?i)\bEm conversa seguinte\b", "Em novo contato"),
    (r"(?i)\be a reuni[ãa]o\b", ""),
    (r"(?i)\(a janela da reuni[ãa]o é do projeto", "(a janela é do projeto"),
    (r"(?i)\bA captura de tela foi amostrada[^.]*\.", ""),
    (r"(?i)\bNada foi executado ou combinado a partir[^.]*\.", ""),
    (r"(?i)\bA trilha de estudo foi mencionada em feedback com\b[^.]*\.", ""),
    (r"(?i)\bCuidado ao citar pessoas\.", ""),
    (r"(?i)\bA pr[óo]pria fala corrige n[úu]meros\b", "Há correção de números ao longo do registro"),
    (r"(?i)\b(?:uma|outra) fala (?:diz|manda|lembra)\b", "outra orientação diz"),
    (r"(?i)\(fala:\s*\)", "(informado)"),
    (r"(?i)\(fala\)", "(informado)"),
    (r"(?i)\bInterpreta[çc][ãa]o preliminar da fala\b", "Interpretação preliminar"),
    (r"(?i)\bn[úu]mero ouvido n[ae]ssa fala\b", "número citado"),
    (r"(?i)\bpor que se fala em\b", "por que há menção a"),
    (r"(?i)\b[ée] uma fala contextual\b", "é um registro contextual"),
    (r"(?i)\bApenas como fala\b", "Apenas como menção"),
    (r"(?i)\bFala sobreposta\b", "Sobreposição de registros"),
    (r"(?i)\baparecem d[úu]vidas\b[^.;]*", ""),
    (r"(?i)\bestados e d[úu]vidas\b", "estados e questões"),
    (r"(?i)\bem caso de d[úu]vidas\b", "quando precisar de ajuda"),
    (r"(?i)\bda d[úu]vida em termos verific[áa]veis\b", "da questão em termos verificáveis"),
    (r"(?i)\buma d[úu]vida individual\b", "uma questão individual"),
    (r"(?i)\be o teste n[ãa]o est[áa] errado\b", "e o comportamento é esperado"),
    (r"(?i)\bcomo d[úu]vida no meio do texto\b", "como ressalva no meio do texto"),
    (r"(?i)\bessa fala\b", "essa menção"),
    (r"(?i)\bnessa fala\b", "nessa menção"),
    (r"(?i)\bessas falas\b", "essas menções"),
    (r"(?i)\btratar fala de como valida[çc][ãa]o\b", "tratar informação não validada como validação"),
    (r"(?i)\bConversa cita\b", "Há menção a"),
    (r"(?i)\bA conversa cita\b", "Há menção a"),
    (r"(?i)\bconversa cita\b", "há menção a"),
    (r"(?i)\(conversa com [^)]*\)", ""),
    (r"(?i)\bcontexto individual da chamada\b", "contexto de um caso individual"),
    (r"(?i)\(no caso, a outra parte da chamada\)", ""),
    (r"(?i)\bO recorte n[ãa]o indica quem falou cada linha\.", ""),
    (r"(?i)\bO registro cont[ée]m\b", "Há"),
    (r"(?i)\b(?:D[úu]vida|Cen[áa]rio|Ponto)\s*\(\s*participante[s]?\s*[A-Z0-9]?\s*\)\s*:?", ""),
    (r"(?i)\(\s*participante[s]?\s*[A-Z0-9]?\s*\)", ""),
    (r"(?i)\b(?:do|de|com) participante[s]?\s+[A-Z0-9]\b", ""),
    (r"(?i)\bd[úu]vida levantada\b", ""),
    (r"(?i)\bD[úu]vidas? (?:revisad|registrad|enviad)\w*", "Questões revisadas"),
    (r"(?i)\bReuni[õo]es mencionadas para\b", "Rituais de equipe para"),
    (r"(?i)\bTratamento da d[úu]vida t[ée]cnica\b", "Encaminhamento de questão técnica"),
    (r"(?i)^A d[úu]vida conceitual sobre\b", "Sobre"),
    (r"(?i)\ba d[úu]vida conceitual sobre\b", "a questão de"),
    (r"(?i)\bConduzir d[úu]vidas\b", "Conduzir questões"),
    # rótulo interno do acervo ("Fluxo A") não diz nada ao leitor
    (r"(?i)\b(?:Fluxos?\s+[A-E](?:\s*(?:,|e|/)\s*[A-E])*)\b\s*[;,.]?", ""),
    (r"(?i)\bdo Fluxo\b", ""),
    # item de lista que ficou com a conjunção pendurada
    (r"[;,]\s*e\s*$", ""),
    (r"(?m)^([ \t]*[-*]?[ \t]*)(.+?)\s+e\s*$", r"\1\2"),
    (r"(?i)\bo respons[áa]vel pela divulga[çc][ãa]o declarou que todos os dados d[ao] (?:registro|material|grava[çc][ãa]o)s? s[ãa]o Fict[íi]cios/de teste e autorizou a publica[çc][ãa]o dos materiais derivados[^.]*\.",
     "Dados de teste e nomes: confirmado que os dados exibidos são fictícios/de teste e que a publicação dos materiais derivados está autorizada"),
    (r"(?i)\bDados de teste e nomes \(resolvido\)\s*:\s*", "Dados de teste e nomes: "),
    (r"(?i)\bA abertura parece uma chamada de voz\b", "A abertura é um diálogo"),
    (r"(?i)\bO operador primeiro\b", "Primeiro"),
    (r"(?i)\bO analista que vai montar/executar a EPT do item\b", "Quem vai montar/executar a EPT do item"),
    (r"(?i)\be n[ãa]o deve ser usad[ao]\b", "e não deve ser usado"),
]


def sem_metarreferencia(t: str) -> str:
    """Tira o vocabulário de registro (gravação, fala, conversa) do texto final."""
    for padrao, troca in META_REFERENCIAS:
        t = re.sub(padrao, troca, t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = re.sub(r"\s+([,.;:])", r"\1", t)
    t = re.sub(r"\(\s*\)", "", t)
    return t


def filtrar_frases(t: str, decidir) -> str:
    """Aplica um filtro frase a frase, preservando tabelas e itens de lista."""
    linhas = []
    for linha in t.splitlines():
        if linha.lstrip().startswith("|"):
            # célula de tabela: o filtro roda por célula, sem mexer nas barras
            if DELIMITADOR_TABELA.match(linha.strip()):
                linhas.append(linha)
                continue
            celulas = linha.split("|")
            for k, celula in enumerate(celulas):
                if not celula.strip():
                    continue
                partes = re.split(r"(?<=[.!?])\s+", celula.strip())
                restantes = [decidir(p) for p in partes]
                celulas[k] = " " + " ".join(r for r in restantes if r.strip()).strip() + " "
            linhas.append("|".join(celulas).rstrip())
            continue
        marcador = re.match(r"^(\s*(?:[-*+]|\d+[.)])\s+)", linha)
        prefixo = marcador.group(1) if marcador else ""
        corpo = linha[len(prefixo):]
        partes = re.split(r"(?<=[.!?])\s+", corpo)
        restantes = [p for p in (decidir(p) for p in partes) if p.strip()]
        if restantes:
            linhas.append(prefixo + " ".join(restantes))
    return "\n".join(linhas)


def limpar_narrativa_por_frase(t: str) -> str:
    """Aplica o filtro de narrativa frase a frase, preservando tabelas e itens de lista."""
    return filtrar_frases(t, _texto_util)


# Só o que é certo entra no material. O que depende de confirmação de alguém, o que ficou
# incompleto e o que pode ter mudado de versão sai por inteiro: um bombeiro não consulta uma
# dúvida no meio do incêndio. Ficam a certeza, o procedimento e a descrição do item ou processo.
PARTICIPIOS_DE_FALTA = (
    r"(?:confirmad|verificad|testad|valid\w*|comprovad|informad|identificad|documentad|determinad|"
    r"analisad|revisad|demonstrad|explicad|medid|executad|definid|esclarecid|registrad|mapead|"
    r"oficializad|respondid|sabid|detalhad|descrit|resolvid|decidid|padronizad|aprovad|autorizad|"
    r"aceit\w*|combinad|expand\w*|liberad|fechad|implementad|cadastrad|parametrizad|inspecionad|"
    r"pronunciad|apresentad|checad|obtid|recebid|observad|vist\w*|instalad|localizad|encontrad|"
    r"anexad|automatizad|formalizad|publicad|modelad|mapead)\w*"
)
SEM_CERTEZA = re.compile(
    r"(?i)(?:"
    # "não confirmado", "não foi verificado", "nunca expandida" — a falta, dita de qualquer forma
    r"\b(?:n[ãa]o|nunca)\s+(?:"
    r"foi|foram|est[áaã]o?|s[ãa]o|se|havia|houve|teve|[ée]|consta|constam|constava|constavam|"
    r"descreve|descrevem|detalha|detalham|fornece|fornecem|explica|explicam|informa|informam|"
    r"identifica|identificam|define|definem|documenta|documentam|esclarece|esclarecem|"
    r"registra|registram|comprova|comprovam|tem|havia"
    r")\b[^.;]{0,90}?" + PARTICIPIOS_DE_FALTA +
    r"|\b(?:n[ãa]o|nunca)\s+(?:mais\s+)?" + PARTICIPIOS_DE_FALTA +
    r"|\b(?:precisa|precisam|deve|devem|carece|carecem|falta|faltam)\s+(?:ser\s+|de\s+)?"
    r"(?:confirmad|verificad|valid|definid|esclarecid|checad|testad|ajustad|revist|corrigid|"
    r"padronizad|aprofundad)"
    r"|\b(?:nome|grafia|significado|sentido|escrita|nomenclatura|sigla) aproximad\w+"
    r"|\bsem\s+(?:confirmar|validar|verificar|definir|conferir)\b"
    r"|\bfalta\s+(?:descobrir|confirmar|definir|saber|verificar|esclarecer)\b"
    r"|\bsem\s+(?:confirma[çc][ãa]o|registro|evid[êe]ncia|comprova[çc][ãa]o|documenta[çc][ãa]o|"
    r"defini[çc][ãa]o|precedente|texto|detalhe|conte[úu]do|execu[çc][ãa]o|resultado)\b"
    r"|\bn[ãa]o\s+h[áa]\s+(?:registro|evid[êe]ncia|comprova\w*|confirma\w*|dados|retorno|"
    r"resposta|informa\w*|como\s+(?:saber|confirmar|verificar)|nada)\b"
    r"|\bn[ãa]o\s+se\s+(?:sabe|conhece|tem)\b"
    r"|\bnenhum\w*\s+(?:material|documento|fonte|registro|tela|retorno|dado)s?\b[^.;]{0,60}?"
    r"(?:descreve|detalha|explica|documenta|traz|mostra|confirma|foi)"
    r"|\bmen[çc][ãa]o\b[^.;]{0,40}?\bsem\s+(?:texto|detalhe|conte[úu]do)"
    r"|\bfica\s+(?:em\s+)?(?:aberto|pendente)\b"
    r"|\b(?:incert\w+|hip[óo]tese|hipot[ée]tic\w+|talvez|possivelmente|aparentemente|"
    r"desconhecid\w*|indefinid\w*|imprecis\w*|ambígu\w*)"
    r"|\ba\s+(?:confirmar|validar|verificar|definir|esclarecer|decidir)\b"
    r"|\bpor\s+(?:confirmar|validar|definir)\b"
    r"|\bn[ãa]o\s+[ée]\s+poss[íi]vel\b"
    r"|\b(?:permanece|resta|fica|ficou|segue|paira)\s+(?:a\s+|em\s+)?d[úu]vida\b"
    r"|\bem\s+d[úu]vida\b"
    r"|\bpend[êe]nc\w+|\bpendent\w*"
    r"|\bconflit\w+|\bdiverg\w+"
    r"|\boscila\w*"
    r"|\bD[ÚU]VIDA_OU_CONFLITO\b"
    r")"
)

# cuidado de execução ("não execute X sem conferir", "nunca reprocessar produção sem validação")
# é procedimento e fica; o que sai é a frase que apenas relata o que falta saber
FRASE_IMPERATIVA_COM_CUIDADO = re.compile(
    r"(?i)^\s*(?:nunca|jamais|n[ãa]o)\s+"
    r"(?:execute|execute\s|executar|use|usar|altere|alterar|apague|apagar|rode|rodar|"
    r"fa[çc]a|fazer|copie|copiar|envie|enviar|reprocesse|reprocessar|substitua|substituir|"
    r"trate|tratar|confie|assuma|inferir|invente|presuma|padronize|desvincule|mude|mudar)"
)


def _frase_certa(frase: str) -> str:
    """Devolve a frase quando ela é afirmação de conhecimento; descarta o resto.

    A marcação de negrito sai antes do teste: "**não** foi confirmado" é a mesma frase que
    "não foi confirmado", e é ela que não entra no material.
    """
    limpa = frase.strip()
    alvo = re.sub(r"\*+", "", limpa)
    alvo = re.sub(r"[ \t]+([.,;:])", r"\1", alvo)
    if not limpa:
        return ""
    if FRASE_DANIFICADA.search(alvo):
        return ""
    if not SEM_CERTEZA.search(alvo):
        return limpa
    if FRASE_IMPERATIVA_COM_CUIDADO.match(alvo):
        return limpa
    return ""


def sem_incerteza(t: str) -> str:
    """Sai do material tudo o que não é certeza.

    Sobrevivem três coisas: a afirmação confirmada, o procedimento (inclusive o cuidado de
    execução) e a descrição de item, tela, campo ou processo.
    """
    t = filtrar_frases(t, _frase_certa)
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = re.sub(r"\s+([,.;:])", r"\1", t)
    t = re.sub(r"(?m)^\s*[-*]\s*$", "", t)
    return t


def sem_narrativa_de_fonte(t: str) -> str:
    """Converte frases sobre a fonte em afirmações sobre o assunto.

    Numa base de consulta, o leitor quer a regra e o procedimento — não quem mostrou, para
    quem mostrou ou em que conversa aquilo apareceu. A frase que só relata a fonte sai; a que
    carrega conhecimento fica, sem o enquadramento ("a conversa ensina que X" vira "X").
    """
    # quem fala deixa de ser sujeito: "a conversa ensina que X" → "X"
    t = re.sub(
        r"(?i)\b(?:a|o|as|os)\s+(?:grava[çc][ãa]o|reuni[ãa]o|conversa|chamada|v[íi]deo|demonstra[çc][ãa]o|"
        r"treinamento|aula|fonte|interlocutor[a]?|interlocutores|orientador[a]?|apresentador[a]?|tester|"
        r"chat|mensagens?|falas?|di[aá]logo|transcri[çc][ãa]o)\s+"
        r"(?:mostra[m]?|demonstra[m]?|ensina[m]?|detalha[m]?|descreve[m]?|explica[m]?|relata[m]?|"
        r"diz(?:em)?|afirma[m]?|cita[m]?|comenta[m]?|menciona[m]?|apresenta[m]?|percorre[m]?|"
        r"documenta[m]?|evidencia[m]?|sustenta[m]?|traz(?:em)?)\s+(?:que\s+)?",
        "", t)
    # "o próprio interlocutor diz que" / "segundo o orientador," etc.
    t = re.sub(
        r"(?i)\b(?:o\s+pr[óo]prio\s+|a\s+pr[óo]pria\s+)?(?:interlocutor[a]?|orientador[a]?|apresentador[a]?|"
        r"tester|operador[a]?|analista|gestor[a]?|colega)\s+"
        r"(?:diz|disse|afirma|relata|comenta|menciona|cita|conta|explica|confirma|responde)\s+(?:que\s+)?",
        "", t)
    t = re.sub(
        r"(?i)\b(?:segundo|conforme|de acordo com)\s+(?:o|a|as|os)\s+(?:interlocutor[a]?|orientador[a]?|"
        r"apresentador[a]?|tester|grav\w+|fonte|conversa|reuni[ãa]o|chamada|v[íi]deo|chat)\s*,\s*", "", t)
    t = re.sub(r"(?i)\b(?:a|o)\s+(?:grava[çc][ãa]o|reuni[ãa]o|conversa|chamada|v[íi]deo|fonte)\s*,?\s+"
               r"(?:por[ée]m|mas|por outro lado)\s*,?\s*", "", t)
    # "na fonte", "na gravação", "na conversa" como lugar onde algo aparece
    t = re.sub(r"(?i)\b(?:na|nas|no|nos|nessa|nesta|nesse|neste)\s+"
               r"(?:grava[çc][ãa]o|reuni[ãa]o|conversa|chamada|v[íi]deo|fonte|aula|treinamento|demonstra[çc][ãa]o|"
               r"material|pacote|an[áa]lise)\b\s*,?\s*", "", t)

    t = re.sub(r"(?i)\b(?:a|o)\s+(?:grava[çc][ãa]o|reuni[ãa]o|conversa|chamada|v[íi]deo|fonte)\s+"
               r"(?:n[ãa]o\s+)?(?:confirma|demonstra|mostra|deixa claro|esclarece|permit\w+|"
               r"registra|comprova|sustenta|explica)\b[^.\n]*\.", " ", t)
    # marcadores editoriais de método
    t = re.sub(r"\*{0,2}\[\s*(?:infer[êe]ncia|hip[óo]tese|conclus[ãa]o do material|derivado)\s*\]"
               r"\*{0,2}\s*", "", t, flags=re.I)
    t = re.sub(r"(?i)\*\*(?:infer[êe]ncia|hip[óo]tese)\*\*\s*", "", t)
    # sobras de sujeito removido
    t = re.sub(r"(?i)(?:^|(?<=[.!?]\s))(?:\s*),\s*", "", t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = re.sub(r"\s+([,.;:])", r"\1", t)
    return t


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
<p>Esta é a <b>base de consulta do trabalho</b> da <b>Função Sistemas</b>: o que o negócio faz, onde
ficam as telas e os sistemas, o que o banco responde, como a API conversa, quais procedimentos
existem e quais termos significam o quê. Aqui está <b>o que está confirmado</b>: informação
descritiva de item e de processo, passo a passo de execução e o vocabulário do dia a dia.</p>

<div class="destaque">
  <h3>Por onde começar</h3>
  <ul>
    <li><b>Procurando um procedimento?</b> Vá em <i>Procedimentos</i>: os fluxos estão reunidos por
    assunto (EPT, API, banco, tela, ambiente, documentos), em passos, com o que conferir antes e
    depois.</li>
    <li><b>Precisa entender o negócio?</b> <i>Negócio</i> explica consignado, convênio, produto,
    despesas, esteira, refinanciamento e cálculo.</li>
    <li><b>Vai mexer em sistema?</b> <i>Sistemas, telas e rotinas</i> diz onde cada coisa fica e o que
    a rotina exige.</li>
    <li><b>Precisa consultar o banco?</b> <i>Consultas SQL</i> traz <b>todas</b> as consultas do
    acervo com o código completo: o que cada uma faz, em que banco roda, que tabelas e colunas usa e
    como ler o resultado.</li>
    <li><b>Vai chamar a API?</b> <i>API, integrações e payloads</i> descreve endpoints, blocos do
    payload, erros conhecidos e como rastrear a execução.</li>
    <li><b>Vai testar?</b> <i>Testes, qualidade e evidências</i> cobre da especificação ao fechamento do
    pacote; <i>Ambientes e infraestrutura</i> cobre versão, acesso e configuração.</li>
    <li><b>Esbarrou num termo?</b> O <i>Glossário</i> reúne siglas, telas, campos e jargão do dia a dia
    em uma lista única, em ordem alfabética.</li>
    <li><b>Vai executar algo em ambiente de verdade?</b> Siga a especificação e o runbook vigentes e
    confirme com o responsável da frente: este material é apoio de consulta, não autorização.</li>
  </ul>
</div>

<div class="destaque">
  <h3>Como o material está organizado</h3>
  <ul>
    <li>Cada capítulo começa com uma <b>explicação do assunto</b> — conceitos, regras e o porquê — e
    depois traz o <b>conhecimento detalhado por assunto</b>, já consolidado: as informações
    equivalentes de origens diferentes aparecem uma única vez.</li>
    <li>As <b>fichas</b> (procedimentos, sistemas, rotinas, perguntas) abrem ao clique; a busca no topo
    filtra tudo por termo, sigla, tela ou campo, e os botões <i>expandir</i>/<i>recolher</i> abrem ou
    fecham o material inteiro.</li>
    <li>Não há transcrição de falas, referência a quando algo foi dito nem registro de reunião: só
    entrou o que é certo, o procedimento e a descrição do item ou do processo. O que ainda dependia
    de confirmação de alguém ficou fora do material, em vez de virar ressalva no meio do texto.</li>
  </ul>
</div>

<div class="aviso">
  <h3>Aviso importante</h3>
  <p>Este material é <b>apoio de consulta e memória de trabalho</b>. Ele não substitui a especificação
  vigente nem o runbook da frente: regras, telas e versões mudam. Cada procedimento aqui descreve
  como o trabalho é feito; autorização para executar em ambiente real vem do responsável e da
  política vigente.</p>
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
  <li><b>Este documento não é orientação jurídica nem de compliance.</b> Questões de exposição de
  informação vão para o responsável pela divulgação.</li>
</ul>
<p>Em caso de diferença entre este material e a especificação vigente, <b>vale a especificação</b>.</p>
"""


# ---------------------------------------------------------------- consolidação por assunto
#
# O material é uma base de consulta: o conhecimento aparece por assunto (procedimento, regra,
# campo, tela), não por reunião. Cada seção dos documentos de origem é classificada por tema,
# agrupada com as seções equivalentes das outras origens e apresentada uma única vez.

# seções que só reproduzem a consulta: agora elas vivem no capítulo de SQL, com explicação
SECAO_SQL = re.compile(
    r"(?i)^(?:sql\b|an[áa]lise de sql.*|sql exibido.*|consultas? (?:sql|preparadas|complementares).*|"
    r"consultas? no\b.*|banco de dados e consultas.*|rastreio no banco.*)")

SECAO_DESCARTE = re.compile(
    r"(?i)^(?:contexto(?: e escopo.*)?|participantes.*|natureza e limites.*|mascaramento.*|"
    r"m[ée]todo de an[áa]lise.*|varredura de privacidade.*|confian[çc]a da extra[çc][ãa]o.*|"
    r"publica[çc][ãa]o.*|privacidade.*|objetivo (?:e p[úu]blico|pedag[óo]gico)|"
    r"o que (?:a|o) (?:conversa|reuni[ãa]o|chamada|grava[çc][ãa]o|v[íi]deo) ensina.*|"
    r"resumo(?: em uma frase| de uma linha| final)?|o que n[ãa]o foi demonstrado.*|"
    r"classifica[çc][ãa]o por categoria|cobertura (?:por|de) categoria.*|relev[âa]ncia.*|"
    r"limites e seguran[çc]a|escopo (?:desta|deste).*|como aplicar sem transformar.*)"
)

RENOMEAR_SECAO = [
    (re.compile(r"(?i)^(?:linha de racioc[ií]nio|racioc[ií]nio) da conversa.*"), "Raciocínio de diagnóstico"),
    (re.compile(r"(?i)^(?:linha de racioc[ií]nio|racioc[ií]nio).*"), "Raciocínio de diagnóstico"),
    (re.compile(r"(?i)^m[ée]todo de isolamento.*"), "Método de diagnóstico"),
    (re.compile(r"(?i)^anatomia do erro.*"), "Anatomia do erro"),
    (re.compile(r"(?i)^anatomia do payload.*"), "Anatomia do payload"),
    (re.compile(r"(?i)^conceitos que o material consolida.*"), "Conceitos consolidados"),
    (re.compile(r"(?i)^demonstra[çc][ãa]o:?\s*"), ""),
]

TITULO_SEM_CONTEUDO = re.compile(
    r"(?i)\b(?:fala|falas|apresentador|interlocutor|orientador|participante|chat|mensagem|"
    r"transcri[çc][ãa]o|grava[çc][ãa]o|reuni[ãa]o|conversa|chamada|v[íi]deo)\b"
)


def dividir_secoes(md: str) -> list[tuple[str, str]]:
    """Separa o markdown em (título, corpo), por seções de nível 2 a 4."""
    secoes: list[tuple[str, str]] = []
    titulo: str | None = None
    corpo: list[str] = []
    for linha in md.splitlines():
        m = re.match(r"^(#{2,4})\s+(.*)$", linha)
        if m:
            if titulo is not None and "\n".join(corpo).strip():
                secoes.append((titulo, "\n".join(corpo).strip()))
            titulo = m.group(2).strip()
            corpo = []
        elif titulo is not None:
            corpo.append(linha)
    if titulo is not None and "\n".join(corpo).strip():
        secoes.append((titulo, "\n".join(corpo).strip()))
    return secoes


def limpar_titulo_secao(titulo: str) -> str:
    """Tira numeração, parênteses de contexto e caudas de método do título da seção."""
    t = re.sub(r"^\s*(?:\d+\.?\d*[\.\)]?|[-*])\s*", "", titulo)
    t = re.sub(r"\s*\([^()]*\)", "", t)
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"\*\*?", "", t)
    t = re.sub(r"(?i)\s*[—–-]\s*(?:relato\b.*|leitura de tela.*|ver .*|n[ãa]o .*aprovad\w*.*)$", "", t)
    for padrao, novo in RENOMEAR_SECAO:
        if padrao.match(t):
            t = padrao.sub(novo, t)
    t = limpar(t)
    return re.sub(r"\s{2,}", " ", t).strip(" .;:-—")


def normalizar(chave: str) -> str:
    """Chave de comparação para deduplicar texto repetido entre origens."""
    t = chave.lower()
    t = re.sub(r"[^a-z0-9áéíóúâêôãõçà ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def bloco_texto(md: str) -> list[str]:
    """Quebra o corpo em unidades comparáveis (parágrafos, itens, tabelas)."""
    unidades: list[str] = []
    atual: list[str] = []
    for linha in md.splitlines():
        if linha.strip():
            atual.append(linha.rstrip())
            continue
        if atual:
            unidades.append("\n".join(atual))
            atual = []
    if atual:
        unidades.append("\n".join(atual))
    return unidades


def juntar_sem_repetir(destino: list[tuple[str, str]], chave: str, texto: str,
                       vistas: set[str]) -> None:
    """Acrescenta o texto à chave indicada, pulando o que já apareceu nesta seção."""
    limpo = texto.strip()
    if not limpo:
        return
    marca = normalizar(limpo)[:180]
    if marca in vistas:
        return
    vistas.add(marca)
    for i, (existente, acumulado) in enumerate(destino):
        if existente == chave:
            destino[i] = (existente, acumulado + "\n\n" + limpo)
            return
    destino.append((chave, limpo))


BUCKETS: dict[str, list[tuple[str, str]]] = {
    "negocio": [
        ("Como o consignado funciona", r"consignad|margem|folha|empregador|conv[êe]nio|produto|p[úu]blico|convenente"),
        ("Documento da operação: CCB e contratos", r"ccb|contrato|credor|saldo devedor|opera[çc][õo]es originais|documento da opera"),
        ("Esteira, averbação e formalização", r"esteira|averba|formaliza|jornada de contrata|etapa|autorizador"),
        ("Despesas, tarifas e seguro", r"despesa|tarifa|seguro|iof|reaproveitamento"),
        ("Crédito, parcelas e cálculo", r"parcela|taxa|cet|vencimento|valor|c[áa]lculo|toler[âa]ncia|refinanciamento|portabilidade"),
        ("Cancelamento, desaverbação e exceções", r"cancel|desaverb|estorno|liquida|quita"),
    ],
    "api": [
        ("Endpoints e contratos de integração", r"endpoint|rota|url|servi[çc]o|contrato|integra[çc][ãa]o|api|swagger"),
        ("Blocos e campos do payload", r"payload|json|campo|objeto|bloco|cole[çc][ãa]o|schema|layout"),
        ("Erros, mensagens e diagnóstico", r"erro|exce[çc][ãa]o|mensagem|falha|badrequest|conflito|diagn[óo]stico|cr[íi]tica|modelo de entrada"),
        ("Monitoramento, logs e rastreio", r"monitor|log|rastre|econsult|execu[çc][ãa]o|status|plugin|job|servi[çc]o de envio"),
        ("Regras de integração e cuidados", r"regra|idempot|reprocess|segredo|credencial|retentativa|reenvio|autoriza[çc][ãa]o"),
    ],
    "testes": [
        ("Especificação e plano de teste (EPT)", r"ept|especifica[çc][ãa]o|plano de teste|caso|cen[áa]rio|pr[ée]-condi[çc][ãa]o|premissa|passo"),
        ("Execução, evidência e revisão", r"execu[çc][ãa]o|evid[êe]ncia|revis[ãa]o|registro|disponibiliza[çc][ãa]o|confer[êe]ncia|homologa|documento de teste"),
        ("Boas práticas e critérios de qualidade", r"boa pr[áa]tica|padr[ãa]o|reprodut|escopo|risco|cobertura|prioridade"),
    ],
    "infra": [
        ("Ambientes e versões", r"ambiente|vers[ãa]o|publica|deploy|homolog|produ[çc][ãa]o|build|componente"),
        ("Acesso, perfis e credenciais", r"acesso|perfil|permiss|credencial|segredo|licen[çc]a|token|certificado|client secret|senha|privil[ée]gio"),
        ("Configuração e artefatos", r"config|artefato|planilha|utilit[áa]rio|par[âa]metro|alias|rotina de cadastro|importa[çc][ãa]o"),
    ],
    "automacao": [
        ("Automação de testes", r"automa|cypress|script|poc|regress"),
        ("Inteligência artificial aplicada", r"ia\b|intelig[êe]ncia artificial|prompt|rag|llm|gerar ept"),
    ],
    "comunicacao": [
        ("Combinar expectativas e pedir o que precisa", r"comunic|perfil|acordo|combinar|expectativa|pedir|mensagem|escrita|forma de trabalhar"),
        ("Conduzir dúvidas, escalar e registrar", r"d[úu]vida|escal|registr|prioriz|acompanh|reuni[ãa]o|feedback"),
    ],
}


def classificar(chave: str, titulo: str, corpo: str) -> str:
    """Encontra o assunto (bucket) da seção dentro do tema."""
    regras = BUCKETS.get(chave, [])
    alvo = " %s %s " % (titulo.lower(), corpo.lower())
    for nome, padrao in regras:
        if re.search(padrao, alvo):
            return nome
    return "Outros pontos"


def detalhe_por_assunto(chave: str) -> str:
    """Percorre as fontes do tema, agrupa as seções por assunto e devolve o HTML consolidado."""
    agrupado: list[tuple[str, str]] = []
    vistas: set[str] = set()
    for slug, (_rotulo, _tipo, tema) in FONTES.items():
        if tema != chave:
            continue
        caminho = os.path.join(MATERIAIS, slug, "guia_de_estudo.md")
        if not os.path.exists(caminho):
            continue
        for titulo_bruto, corpo_md in dividir_secoes(ler(caminho)):
            titulo = limpar_titulo_secao(titulo_bruto)
            if SECAO_DESCARTE.match(titulo) or SECAO_SQL.match(titulo):
                continue
            corpo = limpar(remover_blocos_sql(corpo_md))
            if len(corpo) < 80:
                continue
            if TITULO_SEM_CONTEUDO.search(titulo) or not titulo:
                titulo = "Pontos de atenção do dia a dia"
            cabeca = classificar(chave, titulo, corpo)
            for unidade in bloco_texto(corpo):
                juntar_sem_repetir(agrupado, cabeca, unidade, vistas)
    partes = []
    for cabeca, corpo in agrupado:
        corpo_html = md_para_html(corpo)
        if len(re.sub(r"<[^>]+>", "", corpo_html).strip()) < 60:
            continue
        partes.append('<h4 class="assunto">%s</h4>\n%s' % (html.escape(cabeca), corpo_html))
    return "".join(partes)


def ler_tabelas(caminho: str) -> list[tuple[list[str], list[list[str]]]]:
    """Lê as tabelas markdown de um documento: (cabeçalho, linhas)."""
    if not os.path.exists(caminho):
        return []
    tabelas: list[tuple[list[str], list[list[str]]]] = []
    cabecalho: list[str] | None = None
    linhas: list[list[str]] = []
    for linha in ler(caminho).splitlines():
        if linha.strip().startswith("|"):
            if DELIMITADOR_TABELA.match(linha.strip()):
                continue
            celulas = [c.strip() for c in _celulas(linha)]
            if cabecalho is None:
                cabecalho = celulas
            else:
                linhas.append(celulas)
        elif cabecalho is not None:
            tabelas.append((cabecalho, linhas))
            cabecalho, linhas = None, []
    if cabecalho is not None:
        tabelas.append((cabecalho, linhas))
    return tabelas


def celula_limpa(valor: str) -> str:
    """Limpa uma célula de tabela: sem tempo, sem citação, sem nome de arquivo, sem 'idem'."""
    t = limpar(valor)
    t = re.sub(r"(?i)\bidem\b|\bver acima\b", "", t)
    t = re.sub(r"\s*[—–-]\s*$", "", t)
    return re.sub(r"\s{2,}", " ", t).strip(" .;:—–-")


def texto_plano(valor: str) -> str:
    """Deixa o texto próprio para título de ficha: sem marcação, sem crase, sem sobra."""
    t = re.sub(r"\*+", "", valor)
    t = t.replace("`", "")
    t = re.sub(r"\s{2,}", " ", t)
    return t.strip(" .;:—–-")


def cartao(titulo: str, corpo_html: str, classe: str = "ficha") -> str:
    return ('<details class="bloco dobra %s"><summary>%s</summary>'
            '<div class="bloco-corpo">%s</div></details>' % (classe, html.escape(titulo), corpo_html))


def indice_coluna(cabecalho: list[str], *chaves: str, padrao: int | None = None) -> int | None:
    """Acha a coluna pelo nome do cabeçalho — o índice varia de tabela para tabela."""
    for chave in chaves:
        for i, celula in enumerate(cabecalho):
            nome = unicodedata.normalize("NFKD", celula.lower()).encode("ascii", "ignore").decode()
            if re.search(chave, nome):
                return i
    return padrao


def cap_sistemas() -> tuple[str, int]:
    """Monta a referência de sistemas/telas e de rotinas, agrupada por sistema."""
    partes: list[str] = []
    quantidade = 0

    sistemas: dict[str, list[tuple[str, str]]] = {}
    for cabecalho, linhas in ler_tabelas(os.path.join(MATERIAIS, "SISTEMAS/INDICE_SISTEMAS.md")):
        if len(cabecalho) < 3:
            continue
        col_nome = indice_coluna(cabecalho, "sistema", "m[óo]dulo", "item", padrao=0)
        col_tela = indice_coluna(cabecalho, "tela", "[áa]rea")
        col_obj = indice_coluna(cabecalho, "objetivo", "o que a fonte", "descri")
        if col_nome is None or col_obj is None:
            continue
        for linha in linhas:
            if len(linha) <= max(col_nome, col_obj):
                continue
            nome = texto_plano(celula_limpa(linha[col_nome]))
            tela = texto_plano(celula_limpa(linha[col_tela])) if col_tela is not None and len(linha) > col_tela else ""
            objetivo = celula_limpa(linha[col_obj])
            if not nome:
                continue
            sistemas.setdefault(nome, []).append((tela, objetivo))
    if sistemas:
        partes.append('<h4 class="assunto">Sistemas, módulos e telas</h4>')
        for nome, linhas in sistemas.items():
            itens = []
            for tela, objetivo in linhas:
                if not objetivo and not tela:
                    continue
                if len(re.sub(r"\W+", "", objetivo + tela)) < 8:
                    continue
                if tela and objetivo:
                    itens.append("<li><b>%s</b> — %s</li>" % (html.escape(tela), md_para_html(objetivo)))
                elif objetivo or tela:
                    itens.append("<li>%s</li>" % md_para_html(objetivo or tela))
            if not itens:
                continue
            quantidade += 1
            partes.append(cartao(nome, "<ul>%s</ul>" % "".join(itens)))

    rotinas: list[tuple[str, str, str, str]] = []
    for cabecalho, linhas in ler_tabelas(os.path.join(MATERIAIS, "PROCESSOS/INDICE_PROCESSOS.md")):
        if len(cabecalho) < 4 or "rotina" not in cabecalho[0].lower():
            continue
        for linha in linhas:
            if len(linha) < 4:
                continue
            valores = [celula_limpa(c) for c in linha[:4]]
            valores[0] = texto_plano(valores[0])
            rotinas.append(tuple(valores))  # type: ignore[arg-type]
    if rotinas:
        partes.append('<h4 class="assunto">Rotinas e processos</h4>')
        vistas: set[str] = set()
        for nome, pre, resultado, excecoes in rotinas:
            if not nome or normalizar(nome)[:80] in vistas:
                continue
            vistas.add(normalizar(nome)[:80])
            itens = []
            for rotulo, valor in (("Pré-requisitos", pre), ("Resultado", resultado), ("Exceções", excecoes)):
                if valor and len(re.sub(r"\W+", "", valor)) >= 4:
                    itens.append("<li><b>%s:</b> %s</li>" % (rotulo, md_para_html(valor)))
            if not itens:
                continue
            quantidade += 1
            partes.append(cartao(nome, "<ul>%s</ul>" % "".join(itens), "ficha rotina"))
    return "".join(partes), quantidade


# -*- coding: utf-8 -*-
SQL_CONSULTAS = [
    {
        "titulo": "Identificar o perfil de consulta pelo código do serviço",
        "banco": "FCSMONITOREMPR",
        "assunto": "Monitoramento de integrações — banco FCSMONITOREMPR",
        "codigo": "SELECT * FROM FCSMONITOREMPR..TBPERFCON WHERE PRCODPFCON LIKE ('%chsInOferta%')",
        "serve": "Descobrir o registro do <b>perfil de consulta</b> a partir de um trecho do "
                 "código do perfil. É o primeiro passo do rastreio: <code>TBPERFCON</code> é o "
                 "cadastro de perfis de consulta, e o resultado traz o identificador de perfil "
                 "(<code>PRIDPFCON</code>) usado pela consulta principal.",
        "tabelas": "Banco <code>FCSMONITOREMPR</code> · tabela <code>TBPERFCON</code> · coluna "
                   "<code>PRCODPFCON</code> (código do perfil).",
        "tipo": "somente leitura (<code>SELECT</code>)",
        "leitura": "Pesquisar pelo trecho do código do perfil. O valor encontrado em "
                   "<code>PRIDPFCON</code> liga o perfil às execuções registradas em "
                   "<code>ECONSULT</code>.",
    },
    {
        "titulo": "Listar as execuções do serviço de envio da proposta ao sistema externo",
        "banco": "FCSMONITOREMPR",
        "assunto": "Monitoramento de integrações — banco FCSMONITOREMPR",
        "codigo": "USE FCSMONITOREMPR\n"
                  "SELECT TOP 1000 PRDESCPFCON, CSVERPLUG, CSNRPROP, CSSERVER, CSRETTEXT, CSERRO, "
                  "CSDTHRAGEN, CSSTATUS, *\n"
                  "FROM FCSMONITOREMPR..ECONSULT(NOLOCK)\n"
                  "INNER JOIN FCSMONITOREMPR..TBPERFCON ON CSIDPFCON = PRIDPFCON\n"
                  "WHERE PRDESCPFCON LIKE ('%Servico de Envio da Proposta ao Sistema Externo%')\n"
                  "ORDER BY CSIDCONS DESC",
        "serve": "Encontrar a <b>execução do serviço</b> que envia a proposta ao sistema externo e "
                 "obter a chave do evento. Filtra pela <b>descrição do serviço</b> — e não pelo "
                 "número da proposta — para ver todas as chamadas daquele serviço; a linha mais "
                 "recente aparece primeiro. A chave <code>CSIDCONS</code> da linha encontrada é o "
                 "que abre o detalhe do payload na consulta seguinte.",
        "tabelas": "Banco <code>FCSMONITOREMPR</code> · <code>ECONSULT</code> (eventos de execução "
                   "de serviços e plugins do monitor) com <code>INNER JOIN</code> em "
                   "<code>TBPERFCON</code> (cadastro de perfis, <code>CSIDPFCON = PRIDPFCON</code>) "
                   "· dica <code>NOLOCK</code> na leitura.",
        "tipo": "somente leitura (<code>SELECT</code>, com <code>USE</code> para trocar o contexto "
                "de banco)",
        "leitura": "Confira a descrição do perfil (<code>PRDESCPFCON</code>), a versão do plugin "
                   "(<code>CSVERPLUG</code>), o número da proposta (<code>CSNRPROP</code>), o "
                   "servidor (<code>CSSERVER</code>), o texto de retorno (<code>CSRETTEXT</code>), "
                   "o erro (<code>CSERRO</code>), a data/hora de agendamento "
                   "(<code>CSDTHRAGEN</code>) e a situação (<code>CSSTATUS</code>). O "
                   "<code>ORDER BY CSIDCONS DESC</code> traz a execução mais recente no topo.",
        "nota": "Uma variante da mesma consulta substitui o filtro por proposta: "
                "<code>WHERE CSNRPROP = 'número-da-proposta'</code>, com o filtro por descrição "
                "deixado como comentário. É a mesma leitura, trocando o eixo da busca.",
    },
    {
        "titulo": "Abrir o detalhe (chave-valor) do evento e ler o payload enviado",
        "banco": "FCSMONITOREMPR",
        "assunto": "Monitoramento de integrações — banco FCSMONITOREMPR",
        "codigo": "SELECT * FROM ECONSULTD WHERE CDIDCONS='84942'",
        "serve": "Abrir o <b>detalhe da execução</b> em formato chave-valor: cada linha traz o nome "
                 "de um campo do corpo enviado e o seu conteúdo. É onde o payload JSON do envio é "
                 "conferido campo a campo.",
        "tabelas": "Banco <code>FCSMONITOREMPR</code> · tabela <code>ECONSULTD</code> · colunas "
                   "<code>CDIDCONS</code> (id da consulta), <code>CDCONTROLE</code> (sequencial do "
                   "detalhe) e <code>CDCAMPO</code> (nome do campo).",
        "tipo": "somente leitura (<code>SELECT</code>)",
        "leitura": "Use o <code>CDIDCONS</code> da linha encontrada na consulta anterior. No "
                   "resultado aparecem campos de consulta do trabalhador (por exemplo "
                   "<code>DATAPREV_CNPJEMPR</code>, <code>DATAPREV_CODCATEG</code>, "
                   "<code>DATAPREV_DESCCBO</code>, <code>VLRMRGDL…</code>) e os demais blocos do "
                   "envio.",
        "nota": "O mesmo comando aparece com outro identificador "
                "(<code>CDIDCONS='915516'</code>) para abrir um segundo detalhe no editor.",
    },
    {
        "titulo": "Monitorar esteira e averbação de uma proposta",
        "banco": "FCSMONITOREMPR",
        "assunto": "Diagnóstico de esteira e averbação — banco FCSMONITOREMPR",
        "codigo": "--INTEGRAÇÃO DE REAPROVEITAMENTO DE SEGURO\n"
                  "SELECT TOP 1000 PRDESCPFCON, CSNRPROP, CSSERVER, CSRETTEXT, CSDTHRAGEN, "
                  "CSSTATUS, *\n"
                  "FROM FCSMONITOREMPR..ECONSULT(NOLOCK)\n"
                  "INNER JOIN FCSMONITOREMPR..TBPERFCON ON CSIDPFCON = PRIDPFCON\n"
                  "WHERE CSNRPROP = '000033373'\n"
                  "--where PRDESCPFCON LIKE ('%INSS - Plugin de levantamento para exclusão de averbação%')\n"
                  "ORDER BY CSIDCONS DESC\n"
                  "\n"
                  "USE FCSMONITOREMPR",
        "serve": "Ver os <b>eventos de esteira e averbação</b> de uma proposta específica, no "
                 "contexto de integração de reaproveitamento de seguro: quais etapas rodaram, com "
                 "que retorno e em que ordem.",
        "tabelas": "Banco <code>FCSMONITOREMPR</code> · <code>ECONSULT</code> "
                   "(<code>PRDESCPFCON</code>, <code>CSNRPROP</code>, <code>CSSERVER</code>, "
                   "<code>CSRETTEXT</code>, <code>CSDTHRAGEN</code>, <code>CSSTATUS</code>) com "
                   "<code>INNER JOIN</code> em <code>TBPERFCON</code>.",
        "tipo": "somente leitura (<code>SELECT</code>, com <code>USE</code> para trocar o contexto "
                "de banco)",
        "leitura": "Filtre pelo número da proposta (<code>CSNRPROP</code>). Leia a etapa "
                   "(<code>PRDESCPFCON</code>), a situação (<code>CSSTATUS</code>), o texto de "
                   "retorno (<code>CSRETTEXT</code>) e a data/hora de agendamento "
                   "(<code>CSDTHRAGEN</code>). O primeiro comentário identifica a finalidade do "
                   "diagnóstico; o segundo, dentro do <code>WHERE</code>, é o filtro alternativo "
                   "por descrição do plugin — troque um pelo outro conforme o que se procura.",
    },
    {
        "titulo": "Consultar o log de refinanciamento",
        "banco": "FCSPROPEMPR",
        "assunto": "Consultas de apoio — banco FCSPROPEMPR",
        "codigo": "USE FCSPROPEMPR\nSELECT * FROM CLOGREFIN\nSELECT * FROM CLOGREFIND",
        "serve": "Ler o <b>log de refinanciamento</b> e o seu detalhe. <code>CLOGREFIN</code> guarda "
                 "o registro do processamento; <code>CLOGREFIND</code> traz o detalhamento linha a "
                 "linha do mesmo evento.",
        "tabelas": "Banco <code>FCSPROPEMPR</code> · tabelas <code>CLOGREFIN</code> e "
                   "<code>CLOGREFIND</code>.",
        "tipo": "somente leitura (<code>SELECT</code>)",
        "leitura": "As duas consultas aparecem juntas no editor: primeiro o registro do log, depois "
                   "o detalhe. São consultas de apoio para investigar um processamento de "
                   "refinanciamento.",
    },
    {
        "titulo": "Consultar reaproveitamento de seguro por proposta",
        "banco": "FCSPROPEMPR",
        "assunto": "Consultas de apoio — banco FCSPROPEMPR",
        "codigo": "USE FCSPROPEMPR\nSELECT * FROM EREAPSEG WHERE EPRNRPROP='número-da-proposta'",
        "serve": "Ver o <b>reaproveitamento de seguro</b> registrado para uma proposta.",
        "tabelas": "Banco <code>FCSPROPEMPR</code> · tabela <code>EREAPSEG</code> · coluna "
                   "<code>EPRNRPROP</code> (número da proposta, usada como filtro).",
        "tipo": "somente leitura (<code>SELECT</code>)",
        "leitura": "Filtre pelo número da proposta. É a consulta de apoio que acompanha a "
                   "investigação de reaproveitamento — a mesma frente monitorada na consulta de "
                   "esteira e averbação.",
    },
    {
        "titulo": "Consultar o complemento da proposta",
        "banco": "FCSPROPEMPR",
        "assunto": "Consultas de apoio — banco FCSPROPEMPR",
        "codigo": "USE FCSPROPEMPR\nSELECT * FROM CCOMP WHERE CSNRPROP=número-da-proposta",
        "serve": "Ler o <b>complemento da proposta</b> pelo número da proposta.",
        "tabelas": "Banco <code>FCSPROPEMPR</code> · tabela <code>CCOMP</code> · coluna "
                   "<code>CSNRPROP</code> (número da proposta, usada como filtro).",
        "tipo": "somente leitura (<code>SELECT</code>)",
        "leitura": "Filtre pelo número da proposta. Serve para conferir os dados que complementam a "
                   "proposta no banco de propostas.",
    },
]

SQL_SEM_CODIGO = [
    ("<b>Alias de conexão e rotinas de site</b>",
     "configurar alias em <code>TPARWFIUTIL.PWALIAS</code>, criar as procedures <code>.NET</code> "
     "(opções <code>C</code> e <code>W</code>) e apagar os registros do site atual em "
     "<code>TRTHB</code> antes de cadastrar as rotinas. Vêm como passos de planilha operacional, "
     "sem comando SQL escrito."),
    ("<b>Correção pontual em base</b>",
     "<code>INSERT</code> e <code>UPDATE</code> são citados como possibilidade de ajuste em base "
     "local, na investigação de despesa e liquidação; o script não é exibido."),
    ("<b>Consulta por número de operação</b>",
     "a orientação é rodar um <code>SELECT</code> para localizar o número da operação; o texto da "
     "consulta não é exibido."),
    ("<b>Conferência das operações do cliente</b>",
     "a orientação é dar um <code>select</code> na tabela referida como <code>coper</code>, "
     "filtrando pelo CPF, para conferir as operações do cliente; o comando não é exibido."),
    ("<b>Convênio e produto de uma proposta</b>",
     "há menção a editar um <code>SELECT</code> e rodar a consulta para conferir convênio e "
     "produto, com nomes parciais (<code>Cprop</code>, <code>ppcodicomv</code>, "
     "<code>ppcodprd</code>) como apareceram na transcrição, ainda não conferidos na base."),
    ("<b>Campo de origem do CNPJ do empregador</b>",
     "a menção é incluir no <code>select</code> o campo de origem do CNPJ do empregador "
     "(<code>ETRACPD.*</code>) para identificar o campo; a consulta não é escrita."),
]


def cap_sql() -> tuple[str, int]:
    """Monta o capítulo de SQL: todas as consultas do acervo, com título e explicação.

    Cada consulta sai com o texto completo (como apareceu na tela), o que ela faz, onde roda,
    que tipo de comando é e como ler o resultado.
    """
    partes: list[str] = []

    # -- índice: uma linha por consulta
    linhas = []
    for i, c in enumerate(SQL_CONSULTAS, 1):
        linhas.append(
            "<tr><td>%d</td><td><a href=\"#sql-%d\">%s</a></td><td><code>%s</code></td>"
            "<td>%s</td></tr>"
            % (i, i, html.escape(c["titulo"]), html.escape(c["banco"]),
               c["tipo"].replace(", com <code>USE</code> para trocar o contexto de banco", "")))
    partes.append('<h4 class="assunto">Todas as consultas, em uma linha cada</h4>')
    partes.append('<table class="tabela"><thead><tr><th>#</th><th>Consulta</th>'
                  "<th>Banco</th><th>Tipo de comando</th></tr></thead><tbody>%s</tbody></table>"
                  % "".join(linhas))

    # -- detalhe por assunto, na ordem em que aparecem
    assuntos: list[str] = []
    for c in SQL_CONSULTAS:
        if c["assunto"] not in assuntos:
            assuntos.append(c["assunto"])
    for assunto in assuntos:
        partes.append('<h4 class="assunto">%s</h4>' % html.escape(assunto))
        for i, c in enumerate(SQL_CONSULTAS, 1):
            if c["assunto"] != assunto:
                continue
            corpo = [
                "<p><b>O que faz:</b> %s</p>" % c["serve"],
                "<p><b>Onde roda:</b> %s</p>" % c["tabelas"],
                "<p><b>Tipo de comando:</b> %s</p>" % c["tipo"],
                "<p><b>Como ler o resultado:</b> %s</p>" % c["leitura"],
            ]
            if c.get("nota"):
                corpo.append('<p class="nota"><b>Observação:</b> %s</p>' % c["nota"])
            corpo.append("<pre>%s</pre>" % html.escape(c["codigo"]))
            partes.append(
                '<details class="bloco dobra consulta" id="sql-%d">'
                "<summary>%d. %s</summary><div class=\"bloco-corpo\">%s</div></details>"
                % (i, i, html.escape(c["titulo"]), "".join(corpo)))

    # -- o que existe em banco sem comando escrito
    if SQL_SEM_CODIGO:
        itens = "".join("<li>%s — %s</li>" % (nome, texto) for nome, texto in SQL_SEM_CODIGO)
        partes.append('<h4 class="assunto">Operações de banco citadas sem o comando</h4>')
        partes.append(
            '<p>Pontos do trabalho em que a operação no banco é descrita em palavras, sem o '
            'comando escrito. Entram aqui porque mostram onde essas consultas aparecem na '
            'rotina.</p><ul>%s</ul>' % itens)

    quantidade = len(SQL_CONSULTAS)
    return "".join(partes), quantidade


def cap_banco() -> tuple[str, int]:
    """Monta a referência de consultas: objetivo, banco/tabelas envolvidas e o SQL de apoio."""
    consultas: list[tuple[str, str, str, str]] = []
    for cabecalho, linhas in ler_tabelas(os.path.join(MATERIAIS, "SQL/INDICE_SQL.md")):
        if not cabecalho or "objetivo" not in cabecalho[0].lower():
            continue
        for linha in linhas:
            if len(linha) < 5:
                continue
            consultas.append((celula_limpa(linha[0]), celula_limpa(linha[2]),
                              celula_limpa(linha[3]), celula_limpa(linha[4])))

    blocos: list[tuple[str, str]] = []
    vistos: set[str] = set()
    for slug in FONTES:
        for arquivo in ("guia_de_estudo.md", "procedimentos.md"):
            caminho = os.path.join(MATERIAIS, slug, arquivo)
            if not os.path.exists(caminho):
                continue
            texto = ler(caminho)
            for m in re.finditer(r"```sql\s*\n(.*?)```", texto, flags=re.S):
                codigo = m.group(1).strip()
                if len(codigo) < 25:
                    continue
                titulos = re.findall(r"(?m)^#{2,4}\s+(.*)$", texto[:m.start()])
                legenda = texto_plano(limpar_titulo_secao(titulos[-1])) if titulos else "Consulta de diagnóstico"
                if not legenda or len(legenda) < 6:
                    legenda = "Consulta de diagnóstico"
                marca = normalizar(codigo)[:200]
                if marca in vistos:
                    continue
                vistos.add(marca)
                blocos.append((legenda, codigo))

    partes: list[str] = []
    if consultas:
        linhas_html = []
        vistas: set[str] = set()
        for objetivo, dialeto, tabelas, tipo in consultas:
            if not objetivo or normalizar(objetivo)[:90] in vistas:
                continue
            vistas.add(normalizar(objetivo)[:90])
            linhas_html.append(
                "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
                % (md_para_html(objetivo), md_para_html(dialeto or "—"),
                   md_para_html(tabelas or "—"), md_para_html(tipo or "—")))
        partes.append('<h4 class="assunto">Para que serve cada consulta</h4>')
        partes.append('<table class="tabela"><thead><tr><th>Objetivo</th><th>Dialeto</th>'
                      "<th>Bancos, tabelas e colunas</th><th>Tipo de acesso</th></tr></thead><tbody>%s</tbody></table>"
                      % "".join(linhas_html))
    if blocos:
        partes.append('<h4 class="assunto">Consultas de apoio</h4>')
        for legenda, codigo in blocos:
            partes.append('<h5>%s</h5>\n<pre>%s</pre>' % (html.escape(legenda), html.escape(codigo)))
    quantidade = len(consultas) + len(blocos)
    return "".join(partes), quantidade


def _ajustar_para_negocio(itens: list[tuple[str, str]], i: int) -> None:
    """Mantém o bloco no mesmo assunto do fluxo ao qual foi anexado."""
    return None


TITULO_SUBSECAO = re.compile(
    r"(?i)^(relat[óo]rio|refer[êe]ncia cruzada|pr[ée]-condi[çc][õo]es( obrigat[óo]rias)?|exce[çc][õo]es|"
    r"resultado(s)?( esperado(s)?)?|bloqueios?|riscos?( e cuidados)?|cuidados|observa[çc][õo]es|"
    r"detalhes|passo a passo|pr[ée]-requisitos|entradas|sa[íi]das|evid[êe]ncias|crit[ée]rios de aceite)$")


def procedimentos_consolidados() -> tuple[str, int]:
    """Reúne os fluxos de todas as origens em uma lista única por assunto."""
    por_assunto: list[tuple[str, str]] = []
    vistas: set[str] = set()
    ultimo: dict[str, int] = {}
    pendente: dict[str, bool] = {}
    pendente_rotulo: dict[str, str] = {}
    chaves_de_tema = {chave for chave, _t, _d in TEMAS}
    for slug, (_rotulo, _tipo, tema) in FONTES.items():
        caminho = os.path.join(MATERIAIS, slug, "procedimentos.md")
        if not os.path.exists(caminho):
            continue
        for titulo_bruto, corpo_md in dividir_secoes(ler(caminho)):
            titulo = limpar_titulo_secao(titulo_bruto)
            titulo = re.sub(r"(?i)^fluxo\s*[a-z]\s*", "", titulo).strip(" —–-:.")
            if SECAO_DESCARTE.match(titulo) or len(titulo) < 8:
                continue
            corpo = limpar(corpo_md)
            if len(re.sub(r"\W+", "", corpo)) < 160:
                continue
            assunto = classificar(tema if tema in chaves_de_tema else "negocio", titulo, corpo)
            if TITULO_SUBSECAO.match(titulo) and ultimo.get(slug) is None:
                # vem antes do primeiro fluxo da origem: entra no fluxo seguinte
                pendente[slug] = True
                pendente_rotulo[slug] = titulo
                continue
            if TITULO_SUBSECAO.match(titulo) and ultimo.get(slug) is not None:
                # subseção de um fluxo (Pré-condições, Exceções…): entra no fluxo anterior
                i = ultimo[slug]
                t_ant, _, c_ant = por_assunto[i][1].partition("\n\n")
                por_assunto[i] = (por_assunto[i][0],
                                  "%s\n\n**%s**\n\n%s" % (t_ant, titulo, corpo))
                continue
            titulo = titulo[0].upper() + titulo[1:]
            marca = normalizar(titulo)
            if marca in vistas:
                continue
            vistas.add(marca)
            prefixo = ""
            if pendente.pop(slug, None):
                prefixo = "**%s**\n\n" % pendente_rotulo[slug]
            por_assunto.append((assunto, titulo + "\n\n" + prefixo + corpo))
            ultimo[slug] = len(por_assunto) - 1
    if not por_assunto:
        return "", 0
    agrupado: list[tuple[str, list[tuple[str, str]]]] = []
    for assunto, conteudo in por_assunto:
        titulo, _, corpo = conteudo.partition("\n\n")
        for i, (existente, itens) in enumerate(agrupado):
            if existente == assunto:
                agrupado[i] = (existente, itens + [(titulo, corpo)])
                break
        else:
            agrupado.append((assunto, [(titulo, corpo)]))
    partes = []
    quantidade = 0
    for assunto, itens in agrupado:
        partes.append('<h4 class="assunto">%s</h4>' % html.escape(assunto))
        for titulo, corpo in itens:
            quantidade += 1
            partes.append(cartao(titulo, md_para_html(corpo), "procedimento"))
    return "".join(partes), quantidade


def glossario_consolidado() -> str:
    """Funde todos os glossários em uma lista única, ordenada e sem repetição de termo."""
    termos: dict[str, tuple[str, str]] = {}
    for slug in list(FONTES) + [""]:
        caminho = os.path.join(MATERIAIS, slug, "glossario.md") if slug else os.path.join(MATERIAIS, "GLOSSARIO_GERAL.md")
        if not os.path.exists(caminho):
            continue
        for linha in ler(caminho).splitlines():
            if not linha.strip().startswith("|"):
                continue
            celulas = [c.strip() for c in _celulas(linha)]
            if len(celulas) < 2 or DELIMITADOR_TABELA.match(linha.strip()):
                continue
            termo, definicao = celulas[0], celulas[1]
            if re.match(r"(?i)^termo|^---", termo.replace("*", "").strip()):
                continue
            termo = limpar(re.sub(r"^\*\*|\*\*$", "", termo).strip())
            definicao = limpar(definicao)
            definicao = re.sub(r"^\*\*|\*\*$", "", definicao).strip()
            if not termo or not definicao:
                continue
            marca = normalizar(termo)
            # fora o que é anotação de leitura e o que é frase inteira, não termo
            if len(termo) > 90 or marca.startswith("termo"):
                continue
            if re.search(r"(?i)\bgrafia|\basr\b|ouvido|ileg[íi]vel|reconhecid[ao] pel", termo):
                continue
            # termo é termo: frase inteira, verbo no início ou rótulo vazio não entram
            if len(termo.split()) > 4 and termo[:1].islower():
                continue
            if re.search(r"[()\[\]]\s*$|\|\s*$|^\s*[/–—-]", termo):
                continue
            if len(definicao.strip()) < 25:
                continue
            anterior = termos.get(marca)
            if anterior is None or len(definicao) > len(anterior[1]):
                termos[marca] = (termo, definicao)
    if not termos:
        return ""
    def chave_ordem(item: tuple[str, tuple[str, str]]) -> str:
        termo = item[1][0]
        return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", termo.lower()).encode("ascii", "ignore").decode())
    linhas = []
    for _marca, (termo, definicao) in sorted(termos.items(), key=chave_ordem):
        linhas.append("<tr><td><b>%s</b></td><td>%s</td></tr>" % (html.escape(termo), md_para_html(definicao)))
    return ('<table class="tabela glossario"><thead><tr><th>Termo ou sigla</th><th>O que significa</th></tr></thead>'
            "<tbody>%s</tbody></table>" % "".join(linhas))


def perguntas_consolidadas() -> tuple[str, int]:
    """Reúne as perguntas de revisão de todas as origens, agrupadas por tema."""
    por_tema: dict[str, list[tuple[str, str]]] = {}
    vistas: set[str] = set()
    for slug, (_rotulo, _tipo, tema) in FONTES.items():
        caminho = os.path.join(MATERIAIS, slug, "perguntas.md")
        if not os.path.exists(caminho):
            continue
        texto = limpar(ler(caminho))
        itens = re.split(r"(?m)^\s*(?=\d+[.)]\s)", texto)
        for item in itens:
            m = re.match(r"(?s)\s*\d+[.)]\s*(.*)", item)
            if not m:
                continue
            corpo = m.group(1).strip()
            pergunta, _, resposta = corpo.partition("\n")
            pergunta = re.sub(r"\s*\([^()]*\)\s*", " ", pergunta)
            pergunta = re.sub(r"\*\*", "", pergunta).strip(" .?") + "?"
            pergunta = re.sub(r"\s{2,}", " ", pergunta)
            resposta = resposta.strip()
            if len(pergunta) < 12 or len(re.sub(r"\W+", "", resposta)) < 60:
                continue
            # pergunta sobre a fonte, não sobre o trabalho: sai
            if re.search(r"(?i)\b(?:conversa|reuni[ãa]o|grava[çc][ãa]o|chamada|v[íi]deo|aula|transcri[çc][ãa]o|"
                         r"leitura de tela|evid[êe]ncia visual|o que n[ãa]o ficou claro|finalidade geral|"
                         r"objetivo geral descrito|segundo o documento|deste pacote|nesta an[áa]lise)\b", pergunta):
                continue
            marca = normalizar(pergunta)[:120]
            if marca in vistas:
                continue
            vistas.add(marca)
            por_tema.setdefault(tema, []).append((pergunta, resposta))
    if not por_tema:
        return "", 0
    partes = []
    quantidade = 0
    for chave, titulo, _d in TEMAS:
        itens = por_tema.get(chave)
        if not itens:
            continue
        partes.append('<h4 class="assunto">%s</h4>' % html.escape(titulo))
        for pergunta, resposta in itens:
            quantidade += 1
            partes.append(cartao(pergunta, md_para_html(resposta), "pergunta"))
    return "".join(partes), quantidade


def remover_fichas_vazias(html_cap: str) -> str:
    """Descarta ficha que ficou sem conteúdo e o título de assunto que perdeu as fichas.

    Depois do filtro de certeza, uma ficha pode ficar só com o título. Em vez de deixar uma
    dobra que não abre nada, ela sai — e o assunto que ficou sem fichas também.
    """
    def texto(miolo: str) -> str:
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(miolo))).strip()

    def troca(m: re.Match) -> str:
        return m.group(0) if len(texto(m.group("corpo"))) >= 90 else ""

    html_cap = re.sub(r'<details class="bloco dobra[^"]*">(?P<corpo>.*?)</details>', troca,
                      html_cap, flags=re.S)
    partes = re.split(r'(?=<h4 class="assunto">)', html_cap)
    saida = []
    for parte in partes:
        if parte.startswith('<h4 class="assunto">') and "</h4>" in parte:
            fim = parte.index("</h4>") + 5
            if len(texto(parte[fim:])) < 40:
                continue      # assunto que ficou sem nenhum conteúdo
        saida.append(parte)
    return "".join(saida)


def montar_corpo() -> tuple[str, str, int]:
    """Monta o material como base de consulta: conhecimento e procedimento por assunto.

    Não há inventário de reuniões nem bloco por origem: as seções equivalentes de todas as
    origens são fundidas em um único texto, na ordem dos assuntos, e o que ainda não está
    confirmado vai para o capítulo de pontos a validar.
    """
    total = 0

    def conta(html_bloco: str) -> str:
        nonlocal total
        total += len(re.findall(r'class="bloco(?![\w-])', html_bloco))
        return html_bloco

    capitulos: list[tuple[str, str, str, str]] = []  # (id, título, descrição, html)

    capitulos.append(("como-usar", "Como usar este material", "", TEXTO_COMO_USAR))

    # -- conhecimento por tema: a explicação do assunto abre, o detalhe por assunto segue
    for chave, titulo, descricao in TEMAS:
        corpo = []
        if SINTESES.get(chave):
            corpo.append('<article class="sintese">%s</article>\n' % SINTESES[chave])
        corpo.append(detalhe_por_assunto(chave))
        html_cap = conta("".join(corpo))
        if html_cap.strip():
            capitulos.append((chave, titulo, descricao, html_cap))

    # -- procedimentos: uma lista única, por assunto
    proc_html, proc_total = procedimentos_consolidados()
    if proc_html:
        capitulos.append((
            "procedimentos", "Procedimentos", "%d fluxos de trabalho agrupados por assunto — pré-requisitos, "
            "sequência, pontos de conferência e o que dá errado. Fluxo demonstrado não é runbook aprovado."
            % proc_total, conta(proc_html)))

    # -- referência: sistemas, telas e rotinas
    ref, ref_total = cap_sistemas()
    if ref.strip():
        capitulos.append(("referencia", "Sistemas, telas e rotinas",
                          "%d fichas: onde cada coisa fica, para que serve, o que a rotina exige e o que dá errado."
                          % ref_total, conta(ref)))

    # -- referência: banco de dados e consultas (todas as consultas, por extenso)
    bd, bd_total = cap_sql()
    if bd.strip():
        capitulos.append(("banco", "Consultas SQL",
                          "%d consultas com o código completo — o que cada uma faz, em que banco roda, que "
                          "tabelas e colunas usa, que tipo de comando é e como ler o resultado. Todas de "
                          "leitura; nenhuma foi executada." % bd_total, conta(bd)))

    # -- glossário único
    gloss = glossario_consolidado()
    if gloss:
        capitulos.append(("glossario", "Glossário",
                          "Siglas, termos de negócio, telas e campos — o vocabulário usado no dia a dia e no material.",
                          conta(gloss)))

    # -- perguntas de revisão
    perg_html, perg_total = perguntas_consolidadas()
    if perg_html:
        capitulos.append(("perguntas", "Perguntas para revisar",
                          "%d perguntas de revisão com resposta apoiada no material, agrupadas por tema."
                          % perg_total, conta(perg_html)))

    # -- limites
    capitulos.append(("limites", "Limites e privacidade", "", TEXTO_LIMITES))

    ordem = ["como-usar", "negocio", "referencia", "banco", "api", "procedimentos", "testes",
             "infra", "automacao", "comunicacao", "glossario", "perguntas", "limites"]
    capitulos.sort(key=lambda c: ordem.index(c[0]) if c[0] in ordem else len(ordem))

    corpo_html = []
    indice = []
    for chave, titulo, descricao, html_cap in capitulos:
        html_cap = remover_fichas_vazias(html_cap)
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
h4.assunto{margin:26px 0 10px;font-size:17px;color:var(--azul);border-bottom:1px solid var(--borda);
  padding-bottom:6px}
details.bloco{border:1px solid var(--borda);border-radius:12px;background:#fdfefe;padding:0;
  margin:0 0 10px;overflow:hidden}
details.bloco>summary{cursor:pointer;padding:12px 16px;font-weight:600;color:#0b2b4a;font-size:15.5px;
  background:#f8fafc;list-style:none}
details.bloco>summary::-webkit-details-marker{display:none}
details.bloco>summary::before{content:"▸";color:var(--teal);margin-right:8px;font-weight:700}
details.bloco[open]>summary::before{content:"▾"}
details.bloco[open]>summary{border-bottom:1px solid var(--borda)}
details.bloco>.bloco-corpo{padding:14px 18px 4px}
details.ficha{background:#fcfdff}
details.pergunta>summary{font-weight:600;color:var(--azul-claro)}

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

    cabecalho = (
        "<!DOCTYPE html>\n<html lang=\"pt-BR\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "<title>Base de conhecimento — Função Sistemas</title>\n"
        "<meta name=\"description\" content=\"Base de consulta: negócio, sistemas e telas, banco de dados, API, procedimentos, testes, ambientes, automação e comunicação. Conhecimento confirmado, por assunto.\">\n"
        "<style>\n" + CSS + "\n</style>\n</head>\n<body>\n"
    )

    topo = (
        "<header class=\"topo\"><div class=\"envolt\">\n"
        "<h1>Base de conhecimento — Função Sistemas</h1>\n"
        "<p class=\"sub\">Base de consulta do trabalho: como o negócio funciona, onde ficam as telas e os sistemas, quais consultas o banco responde, como a API conversa e quais procedimentos existem — só o que está confirmado.</p>\n"
        "<div class=\"chips\">\n"
        + '<span class="chip">' + str(total_blocos) + " fichas de consulta</span>\n"
        + '<span class="chip">conhecimento consolidado por assunto</span>\n' 
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
        + '<span class="conta">' + str(total_blocos) + " fichas · navegue ou busque</span></nav>\n"
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
    # o conversor de markdown às vezes deixa uma marca interna no lugar de um trecho de código;
    # se isso escapar, o texto perde conteúdo, então a geração falha em vez de publicar
    "marca de conversão": re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]"),
    "âncora de mensagem": re.compile(r"\[[MP]\d+\]|\[[MP]nn\]"),
    "nome de arquivo de mídia": re.compile(r"\.(?:mp4|md|json|srt|vtt|png|jpe?g|xlsx)\b"),
    # o material só leva o que está confirmado: se um ponto em aberto passar, a geração falha
    "ponto em aberto": re.compile(
        r"(?i)\b(?:n[ãa]o confirmad\w*|a confirmar\b|sem confirma[çc][ãa]o|n[ãa]o se sabe\b|"
        r"incert\w+|hip[óo]tese|desconhecid\w+|pend[êe]nc\w+|D[ÚU]VIDA_OU_CONFLITO|"
        r"diverg\w+|conflit\w+|n[ãa]o h[áa] (?:registro|evid[êe]ncia|comprova\w+)|"
        r"n[ãa]o foi (?:confirmad|verificad|testad|identificad|informad|documentad|executad|"
        r"inspecionad|pronunciad|valid\w+|demonstrad)\w*)"),
}


def verificar_saida(doc: str) -> list[str]:
    """Confere que o material não expõe nomes de arquivo, marcas de tempo nem refs internas."""
    conteudo = re.sub(r"<script>.*?</script>", "", doc, flags=re.S)
    conteudo = re.sub(r"<style>.*?</style>", "", conteudo, flags=re.S)
    achados = []
    for nome, padrao in VAZAMENTOS.items():
        alvo = conteudo
        if nome in ("marca de tempo", "aspas de citação", "marcação de negrito solta", "ponto em aberto"):
            # conteúdo técnico (SQL, payloads, exemplos de dados) pode conter horário como dado
            alvo = re.sub(r"<pre>.*?</pre>", "", alvo, flags=re.S)
            alvo = re.sub(r"<code>.*?</code>", "", alvo, flags=re.S)
        encontrados = padrao.findall(alvo)
        if encontrados:
            exemplos = ", ".join(sorted(set(encontrados))[:3])
            achados.append("%s (%d): %s" % (nome, len(encontrados), exemplos))
    return achados


def escrever_zip(doc: str, caminho: str) -> None:
    """Empacota o material em .zip — é o formato que o navegador baixa direto ao clicar.

    O GitHub serve arquivos `.html` como texto simples (para não executar página de terceiro);
    o `.zip` chega como arquivo. O pacote é escrito de forma reproduzível: mesma data fixa e sem
    metadados do sistema, para que gerar duas vezes produza o mesmo byte a byte.
    """
    dados = doc.encode("utf-8")
    info = zipfile.ZipInfo(NOME_ARQUIVO, date_time=(2026, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    with zipfile.ZipFile(caminho, "w") as pacote:
        pacote.writestr(info, dados)


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
        escrever_zip(doc, os.path.splitext(destino)[0] + ".zip")

    blocos = len(re.findall(r'class="bloco(?![\w-])', doc))
    capitulos = doc.count('class="capitulo"')
    print(
        "gerado: %s (%.1f KB, %d capítulos, %d blocos) — sem nomes de arquivo ou referências internas"
        % (args.saida, len(doc.encode("utf-8")) / 1024, capitulos, blocos)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
