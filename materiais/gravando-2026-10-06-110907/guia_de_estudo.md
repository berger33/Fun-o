> **Fonte do guia:** transcrição automática `faster-whisper large-v3`; o MP4 e as telas não foram revisados neste lote. Trate os pontos como leitura preliminar da conversa, não como regra vigente.

# Guia de estudo — Gravando 2026-10-06 110907.mp4

- **Categoria:** `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `INFRA_E_ACESSO`, `SQL` (menção sem consulta), `DÚVIDA_OU_CONFLITO`
- **Sistema:** CDC (sigla conforme a fala; expansão/arquitetura não confirmadas), SIC/jobs, plugin de remessa e serviço externo
- **Assunto:** visão de uma proposta de integração para cancelamento de seguro, incluindo cadastro de regras, envio, agendamento por linha de comando, consulta de status/reenvio e relatório
- **Confiança da extração:** **baixa a média** — ASR com 683 segmentos, sem revisão de áudio/telas ou consulta à EF; nomes de siglas, campos e parâmetros são incertos e parte do final foi omitida por ser conversa paralela.
- **Público sugerido:** analistas de qualidade e equipes que revisam especificação/fluxos de integração; validar com a equipe responsável.
- **Pré-requisitos:** EF aprovada, regras de negócio e esquema autorizados, responsável funcional do CDC, sandbox e serviço externo simulado; não usar dados/endpoint de produção com base nesta gravação.
- **Fonte:** `Gravando 2026-10-06 110907.mp4` (770228772 bytes; SHA-256 `66e36717…`), áudio declarado `00:23:52.43`.

## 1. Contexto e escopo aparente

A reunião parece percorrer uma especificação em discussão, não mostrar uma funcionalidade implantada (**00:00:00–00:00:45; 00:19:42–00:20:09**). O objetivo descrito é identificar operações com seguro que atendam a regras de negócio e enviar uma solicitação de cancelamento a um sistema externo, armazenando o resultado para acompanhamento (**00:02:29–00:02:46; 00:19:17–00:19:37**).

A fala atribui o trabalho ao CDC e diferencia esse fluxo de uma entrega do Autorizador (**00:09:57–00:10:16; 00:22:27–00:22:44**). A sigla, a arquitetura e a propriedade do fluxo não foram verificadas. A própria conversa diz que o trabalho ainda dependia de decisões/comitê e alinhamento com os analistas do CDC (**00:09:15–00:09:47; 00:19:51–00:20:09**); prazos, prioridade e destino de release são relatos daquele momento, não estado atual.

## 2. Componentes descritos na conversa

### Item 1.1 — configuração de regras

A pessoa descreve uma tela para definir parâmetros e regras por grupo/produto/tipo de operação, histórico financeiro e motivo de cancelamento (**00:00:48–00:01:31; 00:10:47–00:11:24**). Também menciona URL do serviço, referência a segredo e proxy (**00:00:51–00:00:59; 00:01:26–00:01:33**). Não há valores de configuração nem URL/segredo nos materiais; consultar somente a EF aprovada e um cofre autorizado.

### Item 1.2 — remessa e execução

A remessa seria iniciada por uma tela com período de datas, acionaria um plugin e mostraria/exportaria logs (**00:01:34–00:02:25**). A fala também propõe uma linha de comando com comportamento equivalente, potencialmente agendada como job no SIC (**00:02:47–00:03:23; 00:05:26–00:06:29**). São citadas variáveis de data e exemplos relativos à data do sistema/dia útil (**00:06:35–00:07:18**), mas os nomes/formatos do ASR não são confiáveis o bastante para copiar como sintaxe.

### Item 1.3 — acompanhamento, reenvio e relatório

A tela de consulta mostraria operações, situação/observação e erros; a fala considera selecionar uma ou várias solicitações com erro e pedir novo envio (**00:03:23–00:04:17; 00:16:29–00:17:13**). O relatório teria filtros semelhantes à tela e mostraria lote, operação, tipo, valor do seguro e estado do envio (**00:04:19–00:04:53; 00:17:27–00:17:53**). A conversa oscila sobre o formato do relatório (`RPT`/`SIG`) e não estabelece um desenho final (**00:07:32–00:07:57; 00:18:57–00:19:11**).

## 3. Regra de negócio — somente hipótese a validar

A explicação associa o envio a operações liquidadas com seguro e a um histórico financeiro selecionado na configuração (**00:10:22–00:11:24**). Liquidação, estorno e cancelamento são citados, mas a pessoa explicitamente não lembra todos os casos e ainda não tinha lido o projeto (**00:11:38–00:12:15; 00:15:37–00:15:55**). Não está determinado se refinanciamento qualifica, que eventos exatos disparam cancelamento, nem como o serviço externo interpreta o motivo.

A gravação diz que a seleção depende de identificar corretamente a despesa do seguro na **operação** e reconhece que a equipe não sabe qual tabela/campo usar (**00:14:02–00:15:21**). Não usar nomes de tabela reconhecidos pelo ASR para consulta ou implementação.

## 4. Plano de testes conceitual (não executado)

Somente após EF e regras aprovadas, em sandbox com dados sintéticos e serviço externo stub/mock:

- validar a configuração permitida e as combinações de grupo/produto/tipo de operação/histórico;
- testar intervalos de data e cada variável documentada na EF, incluindo limites e cálculo por calendário; não inferir nomes ou formatos pelo ASR;
- testar execução manual e agendada, logs, resultado aceito/rejeitado e persistência do estado;
- cobrir resposta de sucesso/erro, timeout, repetição e proteção contra cancelamento duplicado/idempotência;
- testar reenvio individual e em lote de solicitações com falha, verificando autorização, contagem, auditoria e não duplicação;
- comparar filtros/resultados da tela com o relatório e validar formato final;
- interromper se o cenário exigir URL real, segredo, dados de cliente, consulta/alteração de base ou envio real.

O roteiro seguro e suas pré-condições estão em [`procedimentos.md`](procedimentos.md). Nenhuma chamada, consulta, configuração ou reenvio foi realizado neste lote.

## 5. Limites desta análise

- O MP4 e as telas não foram acessados; os nomes das rotinas, menus, campos e parâmetros não foram confirmados.
- Há somente uma menção a `SELECT`; não foi transcrita consulta SQL. A tabela/campo da despesa da operação ficou em aberto (**00:12:34–00:12:58; 00:14:11–00:15:21**).
- Termos como `CDC`, `CQ`, `SIC`, `SRL`, `CECOMP`, `TRDSP`, `PDT`, `RPT` e `SIG` podem ser siglas ou erros do ASR; veja [`glossario.md`](glossario.md) e [`incertezas.md`](incertezas.md).
- Referência nominal a outro sistema/projeto foi mascarada em `00:18:23–00:18:27`; o trecho não técnico sobre incidente foi omitido em `00:23:04.06–00:23:47.48`.
