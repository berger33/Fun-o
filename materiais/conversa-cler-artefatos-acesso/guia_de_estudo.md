# Guia de estudo — artefatos e acessos (Cler)

- **Categoria:** `INFRA_E_ACESSO`, `PROCESSOS`, `SISTEMAS`, `DÚVIDA_OU_CONFLITO` (sem `SQL`)
- **Sistema:** Função Sistemas — módulo/ambiente **Web Empregador**; sistema **SETHI**; sistema/artefato
  **DIG** (referido como “DIG A”)
- **Assunto:** como **obter artefatos de ambientação** na prática (quem tem, quem conhece, como
  baixar) e o que se sabe, até aqui, sobre **UDL** e sobre a configuração do **SETHI** (usa `DIG A`).
- **Fonte:** recorte textual de conversa de trabalho com **Cler**, fornecido pelo responsável em
  **2026-10-15**; âncoras `[Mnn]` conforme [`../CONVENCOES_FONTES_TEXTUAIS.md`](../CONVENCOES_FONTES_TEXTUAIS.md)
- **Confiança da extração:** **alta** para o **relato** (o que cada pessoa disse); **baixa** para o
  **conteúdo técnico**: nenhuma sigla é expandida na fonte, nenhum artefato foi visto, aberto ou
  validado, e a resposta sobre o SETHI é uma **confirmação oral repassada por um colega**.

## 1. Contexto

O operador **William** está montando o ambiente de teste e precisa de dois artefatos: o pacote do
**Web Empregador** (`[M01]`) e a **UDL do SETHI** (`[M08]`). Ele pergunta a **Cler**, que responde com
honestidade em ambos os casos: “eu nao tenho” (`[M03]`, `[M09]`). A conversa termina com a informação
obtida por outra via — **`DIG A`**, confirmada com **Giraldi** (`[M14]`).

## 2. O que a conversa ensina

### 2.1 Como artefato de sistema circula na prática (`[M01]`–`[M04]`)

| Caminho observado | Âncora |
|---|---|
| Pedir diretamente a um colega (o pedido de William) | `[M01]` |
| Colega **não tem** e indica **quem tem** (“esse eu acho que só a carool”) | `[M03]` |
| Alternativa indicada: **baixar** por conta própria | `[M03]` |

**[inferência]** O “baixar” sugere que existe um **repositório/local de onde o artefato é obtido**
(além do colega), mas a fonte **não** diz onde, nem com que credencial. Não procurar nem tentar obter
por meios não autorizados: a obtenção de artefato é etapa de **ambiente**, não improviso (ver
[`incertezas.md`](incertezas.md) itens 1 e 2).

### 2.2 A dúvida conceitual sobre UDL (`[M08]`, `[M09]`)

Cler, que nunca trabalhou com o SETHI, levanta exatamente as duas hipóteses possíveis:

- o SETHI **tem UDL própria**; ou
- o SETHI **usa o DIG** (“ou vai ter que usar o dig”).

**Evidência cruzada do acervo:** a sigla **UDL** aparece também no pacote
[`../gravando-2026-07-07-155307/transcricao.md`](../gravando-2026-07-07-155307/transcricao.md), como
**nome de pasta/base compartilhada** de um cliente (`C6 UDL Base`), usada na rotina de “subir base”.
Ou seja: nas fontes, **UDL está associada a um artefato/base de ambientação**, não a um sistema.

> **O que continua desconhecido:** o significado da sigla UDL, o que exatamente o arquivo contém, quem
> o gera e qual o procedimento oficial para obtê-lo. **Nenhuma** fonte do acervo responde isso — está
> registrado como lacuna em [`incertezas.md`](incertezas.md) item 1 e no
> [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md).

### 2.3 A resposta obtida: SETHI usa `DIG A` (`[M12]`–`[M14]`)

- William não aceita a dúvida como resposta: **procura quem conhece** (“vou perguntar pro Giraldi” —
  `[M12]`) e **volta com o resultado** (“Dig A, confirmei com ele” — `[M14]`).
- **[inferência]** Portanto, para o SETHI, o caminho de ambientalização **não** é uma UDL própria, e sim
  um artefato do **DIG** — provavelmente uma variante identificada como “A”. A fonte **não** define o
  que é o DIG, o que significa “A”, nem se essa é a prática vigente.

### 2.4 O método de trabalho que a conversa exemplifica

1. **Pedir com contexto e sem pressa** (“Depois se puder… No seu tempo”, `[M01]`) e **agradecer**
   (`[M04]`, `[M13]`).
2. **Aceitar o “não tenho” como pista**, não como fim: a resposta veio com **quem tem** e com uma
   **alternativa** (`[M03]`).
3. **Escalar a pergunta a quem conhece o sistema**, em vez de assumir (`[M12]`).
4. **Fechar o ciclo**: informar a quem ajudou qual foi a resposta encontrada (`[M14]`) — é o que
   transforma uma dúvida individual em conhecimento registrável.

## 3. Riscos e cuidados

- **Não tratar “DIG A” como configuração homologada.** É confirmação oral repassada por colega
  (`[M14]`), sem tela, documento ou runbook. Antes de usar em qualquer ambiente: confirmar com o
  responsável pela ambientação.
- **Não obter artefato por caminho não oficial.** A menção a “baixar” (`[M03]`) **não** é autorização:
  a fonte não diz de onde.
- **Não registrar pessoas como “fonte de artefato”** de forma definitiva: pessoas mudam de área; o
  valor do registro é o **procedimento**, não o nome. Os nomes aqui aparecem apenas como contexto
  histórico da conversa (autorizado pela diretriz de publicação do acervo).
- **Nada foi executado**: nenhum pedido de artefato, download, acesso ou alteração de ambiente nesta
  análise.

## 4. Resumo de uma linha

Quando faltar um artefato de ambiente: **peça a quem tem, pergunte a quem conhece o sistema e registre
o procedimento** — e trate respostas orais (“usa o DIG A”) como **pista a validar**, nunca como
configuração aprovada.
