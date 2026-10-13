# Guia de estudo — Jonas EPT explicação.mp4

- **Categoria:** `SQL`, `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO`
- **Sistema:** Função Sistemas — Autorizador Web / módulo `ServCon` (plugin `SrvEnvioPropExt` — "Serviço de Envio da Proposta ao Sistema Externo"), bancos SQL Server `FCSMONITOREMPR` e `FCSPROPEMPR` (ambiente de CQ)
- **Assunto:** demonstração de tela em chamada do Teams: como investigar a integração "envio de proposta ao sistema externo" (OS 586780 — "[ÁGIL] (I) Nova Flag informativa de Docs anexados no SrvEnvioPropExt") via consultas SQL em `ECONSULT`/`ECONSULTD`, ler o payload JSON enviado, e como preencher a EPT (planilha de casos de teste) e aproveitar cenários do Relatório de Testes da pasta compartilhada.
- **Fonte:** gravação de tela `Jonas EPT explicação.mp4` (`00:10:25`, Teams, 2026-09-23), transcrição automática revisada contra a tela (OCR). Duplicata `jonas2309.mp4` (mesmo oid).
- **Confiança da extração:** média — fala esparsa e áudio de chamada; conteúdo de tela rico e bem legível por OCR nas áreas principais; literais numéricos (números de proposta) e alguns nomes de coluna ficaram parcialmente ilegíveis (ver [`incertezas.md`](incertezas.md)).

## 1. Contexto e objetivo da gravação

A gravação é uma chamada do Teams em que **Jonas** compartilha a tela para um colega (o chat visível indica **William**) que ficará responsável por montar/executar a EPT do item **OS 586780 "[ÁGIL] (I) Nova Flag informativa de Docs anexados no SrvEnvioPropExt"** — o mesmo item da especificação `DS586780` da gravação `Gravando 2026-09-22 111258` (ver [`../gravando-2026-09-22-111258/guia_de_estudo.md`](../gravando-2026-09-22-111258/guia_de_estudo.md)). O próprio chat resume o motivo: "consegue falar?" / "eu te mostro aqui melhor do que ficar mandando msg" (`00:09:00`–`00:09:20`).

Três entregas didáticas:

1. **Rastrear a execução do plugin no banco** (`00:02:50`–`00:04:00`): achar em `FCSMONITOREMPR..ECONSULT` o registro do "Serviço de Envio da Proposta ao Sistema Externo" e pegar o `CSIDCONS`; consultar `ECONSULTD` com esse id para ver o **JSON do payload** enviado ao sistema externo.
2. **Entender o payload** (`00:04:10`–`00:05:20`): onde o novo agrupamento de documentos anexados entra — **dentro do objeto `client`** do JSON ("ele vai estar em client", `00:05:04`–`00:05:06`) — usando a Especificação Funcional (PDF) e o payload real (Notepad++).
3. **Preencher a EPT** (`00:05:35`–`00:09:42`): estrutura da planilha `EPT_586780`, colunas de referência (número do projeto, item da EF, etapa — "pode ser bem genérica"), e **acrescentar cenário de teste** lendo o `Relatorio_de_Testes_586780` da pasta compartilhada ("pasta doc").

## 2. Layout da gravação (linha do tempo)

| Intervalo | Tela | Conteúdo |
|---|---|---|
| `00:00:00` | SSMS | Consultas SQL já preparadas + grade `ECONSULT` (plugins: `Plugin CPO - Token`, `CFD - Plugin de Levantamento para Exclusão de Av…`) |
| `00:00:10`–`00:02:30` | Autorizador Web | `Cadastro de Decisão`, `Proposta Sintetizada` (cliente de teste, matriz `0001 - BANCO FUNÇÃO S/A`, "Enviar Token"), `ESCOLHAPCS`, `Aprovação/Consulta` |
| `00:01:20`–`00:01:40` | Teams | Canais C6; mensagens sobre filtro CPF/CNPJ e "Eu vou fazer a EPT dele" |
| `00:02:50`–`00:05:45` | SSMS | Consulta `ECONSULT`×`TBPERFCON` por nome do serviço; `ECONSULTD` por `CDIDCONS=84942`; tabelas `FCSPROPEMPR` no editor (`CLOGREFIN`, `CLOGREFIND`, `EREAPSEG`, `CCOMP`) |
| `00:04:10`–`00:05:30` | Edge (PDF) | Especificação Funcional da OS 586780 (41 páginas): tabelas de layout com endereço do cliente, bloco `attached_document`, campos corban |
| `00:04:30`–`00:05:20` | Notepad++ | Payload JSON completo do envio (campos de contrato, `client{…}`, `corban_data{…}`) |
| `00:05:50`–`00:08:10` | Excel | Planilha `EPT_586780`: premissas, validações básicas e tabela de casos de teste |
| `00:07:00`–`00:07:20` | Teams | Chat com William (motivo da chamada) |
| `00:08:30` | Explorador | Pasta compartilhada `Mesa_C6` ("pasta doc"): `D586780` (PDF) e `Relatorio_de_Testes_586780` (Word) |
| `00:09:00`–`00:09:30` | Word | `Relatório de Testes` (CQ): cenários 001.1 de importação e atualização com passos e resultado esperado |
| `00:09:40`–`00:10:25` | Excel/Teams | Encerramento ("Obrigado Jonas", `00:10:18`) |

## 3. SQL exibido na tela (00:00:00 e 00:02:50–00:05:45)

Todas as consultas do editor são **T-SQL de leitura (`SELECT`)**, executadas no SSMS conectado ao banco `FCSMONITOREMPR` do ambiente de CQ (usuário `sa`); literais numéricos ilegíveis estão marcados e detalhados em [`incertezas.md`](incertezas.md).

```sql
SELECT * FROM FCSMONITOREMPR..TBPERFCON WHERE PRCODPFCON LIKE ('%chsInOferta%')

USE FCSMONITOREMPR
SELECT TOP 100? PRDESCPFCON, CSVERPLUG, CSNRPROP, CSSERVER, CSRETTEXT, CSERRO, CSDTHRAGEN, CSSTATUS, *
FROM FCSMONITOREMPR..ECONSULT(NOLOCK)
INNER JOIN FCSMONITOREMPR..TBPERFCON ON CSIDPFCON = PRIDPFCON --where CSNRPROP='8??83216?'
WHERE PRDESCPFCON LIKE ('%Servico de Envio da Proposta ao Sistema Externo%')
ORDER BY CSIDCONS DESC

SELECT * FROM ECONSULTD WHERE CDIDCONS='84942'

use FCSPROPEMPR
SELECT * FROM CLOGREFIN
SELECT * FROM CLOGREFIND
SELECT * FROM ECONSULTD WHERE CDIDCONS='915516'   -- linha repetida no editor
USE FCSPROPEMPR
SELECT * FROM EREAPSEG WHERE EPRNRPROP='8??8321??'
Use FCSPROPEMPR
SELECT * FROM CCOMP WHERE CSNRPROP=8??83288?
```

- **Dialeto:** T-SQL (Microsoft SQL Server) — `SELECT TOP`, banco qualificado `FCSMONITOREMPR..ECONSULT`, hint `(NOLOCK)`, `USE` para troca de contexto, interface SSMS.
- **Tipo de comando:** somente leitura; nenhuma escrita é executada na gravação.
- **Consulta principal (rastreio do serviço):** projeta `ECONSULT` (tabela de consultas/eventos de execução de serviços/plugins do monitor — mesmo modelo usado em [`../gravando-2026-10-07-152044/guia_de_estudo.md`](../gravando-2026-10-07-152044/guia_de_estudo.md) §4) com junção a `TBPERFCON` (cadastro de perfis de consulta, `CSIDPFCON = PRIDPFCON`), filtrando **pela descrição do serviço** (`PRDESCPFCON LIKE '%Servico de Envio da Proposta ao Sistema Externo%'`) em vez de filtrar por número de proposta (o filtro antigo por `CSNRPROP` está comentado). `ORDER BY CSIDCONS DESC` traz a execução mais recente primeiro.
- **Detalhe do evento (payload):** `SELECT * FROM ECONSULTD WHERE CDIDCONS='84942'` — `ECONSULTD` guarda o detalhe da consulta em formato **chave-valor** (colunas `CDIDCONS` = id da consulta, `CDCONTROLE` = sequencial do detalhe, `CDCAMPO` = nome do campo, mais coluna de conteúdo e coluna de id de linha — leituras parciais). Na grade exibida (`00:05:40`), os campos trazem dados de consulta de trabalhador (ex.: `DATAPREV_CNPJEMPR`, `DATAPREV_CODCATEG`, `DATAPREV_CODCBO`, `DATAPREV_CODCNAE`, `DATAPREV_DESCCBO`, `DATAPREV_DESCCNAE`, `VLRMRGDL…`) para `CDIDCONS 84942`. É essa tabela que o Jonas aponta como o lugar onde "o JSON" do envio pode ser consultado (`00:03:32`–`00:03:37`).
- **Consultas no `FCSPROPEMPR`:** `CLOGREFIN`, `CLOGREFIND`, `EREAPSEG` (por `EPRNRPROP` = número da proposta) e `CCOMP` (por `CSNRPROP`) — presentes no editor mas **sem execução/explicação na gravação**; a finalidade delas não é dita (ver [`incertezas.md`](incertezas.md) item 6).
- **Resultado da consulta principal (`00:02:50`–`00:03:40`, captura `02`):** primeira linha `PRDESCPFCON = "Serviço de Envio de Proposta ao Sistema Externo"`, `CSNRPROP ≈ 000033264` (proposta de teste; leitura incerta), `CSIDCONS = 84942`, `CSIDPFCON = 533`, `CSUSUARIO = JAFONSO`, `CSDTHRAGEN = 2026-09-23 09:30:26.000`, `CSDTHRSOL = 2026-09-23 09:30:12.100`; as demais linhas visíveis são de outros serviços (`CFD - Plugin de Levantamento para Exclusão de Av…`, `Plugin CPO - Token`) com `CSSTATUS` `P`/`C`, textos de retorno "FINALIZADO OK" / "Plugin CPD - Token finalizado com sucesso" e tokens `SrvTok…` em `CSNREXTERNO`.

## 4. O payload JSON do envio ao sistema externo (00:04:30–00:05:20)

O Notepad++ (aba não salva "*new 8*", 191 linhas, CRLF/UTF-8) mostra o payload enviado pelo plugin para uma proposta de teste. **Estrutura de campos** (valores de clientes de teste e dados pessoais omitidos aqui de propósito):

- **Campos de contrato/financeiros:** `certified_agent_cnpj_cpf`, `formalization_type` (com valor `"D"`), `formalization_subtype`, `refinancing_amount`, `max_financed_iof_tax`, `expenses_value`, `insurance_expenses_value`, `first_parcel_date`, `annual/month_interest_cl_rate(_max)`, `effective_annual/month_rate(_max)`, `month/annual_interest_ap_rate`, `annual_late_charges`, `account_type`, `bank_code` (`"001"`), `agency_number` (`"0001"`), `account_number`, `contract_amount` (2078.59), `contract_parcel_amount` (89.47), `contract_net_amount` (2000.0), `contract_parcel_quantity` (30), `last_parcel_date`, `interest_remuneration_default`, `fine_default`, `proposal_hash_id`, `loan_track_status_code` (80), `contract_parcels`/`contract_guarantee`/`insurance` (null), `drift_fraud`.
- **Objeto `client { … }`:** `id`, `tax_identifier`, `name`, `verification_code`, `pensioner_enrollment`, `enrollment`, `mother_name`, `phone_area_code`, `phone`, `birthday`, `marital_status`, `nationality`, `national_document`, `address_street`, `address_number`, `zip_code`, `neighborhood`, `city`, `state`, `address_complement`, `country`, `email`.
- **Objeto `corban_data { … }`** (promotora/correspondente): `id` (`"001010"` — mesma "Origem 3" que aparece na URL da Proposta Sintetizada `Origem3=001010`), `company_name`, `fancy_name`, `document`, `address_street`, `address_number`, `zip_code`, `neighborhood`, `city`, `state`.
- Os valores de contrato conferem com a tela `Dados da Operação` da Proposta Sintetizada (`00:02:00`): Valor Cliente 2.000,00, Valor Parcela 89,47, Valor Financiado 2.078,59.

**Ponto-chave da fala:** o novo agrupamento de documentos anexados (item da OS 586780) entra **dentro do objeto `client`** ("acima de client / ele vai estar / em client", `00:05:01`–`00:05:06`; "então ele entraria aqui / nessas novas informações", `00:05:20`–`00:05:23`). A Especificação Funcional (`00:04:20`) mostra o bloco como **"Início do objeto `attached_document`"** com campos `document_type` (Tipo do documento) e `document_name` (Nome do documento) — em **conflito de leitura** com a gravação anterior, que registrou `attachment_document` (ver [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md) e [`incertezas.md`](incertezas.md) item 1).

## 5. A EPT — planilha de casos de teste (00:05:50–00:08:10, captura 06)

A planilha `EPT_586780.xls` (Excel em "Modo de Compatibilidade") documenta os casos de teste do item:

- **Título do item:** "C6 Consig - 586780 - [ÁGIL] (I) Nova Flag informativa de Docs anexados no SrvEnvioPropExt".
- **Seções auxiliares:** "Premissas Gerais", "Validações Básicas", "Premissas Específicas" (conteúdo parcialmente legível; também aparece outro item "C6 Consig - 59??8? - [ÁGIL] (I) …abilidade de Consulta de Saldo…", leitura incerta).
- **Tabela de casos:** colunas `CT | Ref. | Descrição | Etapa | Pré-Condições/Condições | Cenário de Testes | Resultado esperado | Status | Observações` (rótulos lidos por OCR, podendo haver variação).
- **Caso 001.1:** "Implementar no módulo 'ServCon', no serviço (plugin) 'Envio da Proposta ao Sistema Externo', novo agrupamento responsável por identificar documentação anexa para compor as informações do cliente" — a mesma redação da solução proposta na EF (RFP001).
- **Pré-condição:** "Usuário deve possuir direitos de acesso… no módulo Web Autorizador… configurado"; em `Versões`, "Comparar versão entregue na ficha de…".
- **Orientações da fala para o preenchimento:** na primeira linha, indicar o **número do projeto** e o **item da EF**; a coluna **Etapa** "pode ser bem genérica" (`00:05:56`–`00:06:11`, `00:07:38`–`00:07:44`).

## 6. O Relatório de Testes e os cenários a acrescentar (00:08:27–00:09:42, captura 07)

Jonas manda o colega abrir o documento da "pasta doc" (compartilhamento `Mesa_C6`): `Relatorio_de_Testes_586780` (Word, 99 KB) e `D586780` (PDF da EF, 365 KB), "dá uma lida, e acrescenta esse cenário" (`00:08:32`–`00:08:36`). O documento (padrão "CQ - CONTROLE DE QUALIDADE / EVIDÊNCIAS DE TESTES / FUNÇÃO SISTEMAS", com "Data Entrega", seções `Versões` e `<Prints>`) traz os cenários já escritos:

- **Cenário 1 (importação):** "001.1 - Cenário 1 - Importação de proposta com documentos anexados deve preencher o [novo agrupamento]" — "Uma proposta do módulo ServCon será enviada pelo fluxo `/proposal/import` e possui ao menos um documento anexado no checklist."
- **Cenário de atualização:** "Uma proposta já existente será atualizada pelo fluxo `/proposal/update` e possui ao menos um documento anexado no checklist." — `Prioridade: Alta`; `Parâmetros`: Endpoint `/proposal/update`; proposta existente com exatamente um documento anexado no checklist; usuário autenticado com privilégios compatíveis com os direitos de origem; proposta preparada sem anexos no checklist; proposta preparada com um documento anexado pelo mesmo fluxo funcional da rotina de anexação do módulo Autorizador.
- **Objetivo:** validar que o novo agrupamento de documentos anexados é incluído dentro de `Client` sem alterar indevidamente os demais blocos do payload.
- **Passos (8):** (1) garantir que a proposta exista no sistema; (2) garantir que a proposta possua documento anexado no checklist; (3) acionar o envio da proposta pelo endpoint (`/proposal/import` ou `/proposal/update`, conforme o cenário); (4) capturar a requisição gerada pelo plugin antes do envio ao sistema externo; (5) validar no objeto `Client` a presença do agrupamento de documentos anexados conforme a nomenclatura homologada; (6) conferir se os campos de tipo do documento, nome do documento e usuário responsável pela anexação estão preenchidos com os dados corretos do anexo; (7) verificar se os demais objetos do payload permanecem sem regressão, especialmente as estruturas `corbanData`, `Credor associatedProposals`, `last_ConsultINSS` e `Insurance_reuse`; (8) validar a resposta HTTP e o corpo de retorno da integração.
- **Resultado esperado (sucesso):** status `200 OK` com `success=true`, `type=ok`, `message=proposal imported` e `details` conforme o padrão do serviço; o objeto `Client` deve conter o agrupamento de documentos anexados com os campos do documento e do usuário corretos.
- **Falha/erro:** agrupamento não enviado no update, com nome incorreto, campos incompletos ou causando regressão nos demais blocos do payload = comportamento incorreto; erro de validação da request deve seguir o tratamento padrão do serviço com `400 BadRequest` ou `409 Conflict`, conforme a regra aplicável.
- O documento tem anotação de tarefa: "ler doc gerado pela [colega] e verificar se tem algum cenário válido para o nosso teste" (`00:09:10`).

## 7. O que esta gravação adiciona ao acervo

- **Fluxo completo de investigação** da integração SrvEnvioPropExt: tela do Autorizador → registro em `ECONSULT` (por nome do serviço) → detalhe/payload em `ECONSULTD` (por `CDIDCONS`) → JSON no Notepad++ → posição do novo agrupamento em `client`.
- **Tabelas novas no acervo:** `ECONSULTD` (detalhe chave-valor de consultas), `CLOGREFIN`, `CLOGREFIND`, `EREAPSEG`, `CCOMP` (`FCSPROPEMPR`; sem explicação de conteúdo na gravação).
- **Endpoints de integração:** `/proposal/import` e `/proposal/update`; resposta de sucesso `200 OK / success=true / type=ok / message=proposal imported`; erros `400 BadRequest` / `409 Conflict`.
- **Estruturas de payload citadas:** `corbanData`, `Credor associatedProposals`, `last_ConsultINSS`, `Insurance_reuse`.
- **Artefatos de processo CQ:** a planilha EPT e o Relatório de Testes com cenários prontos — material de referência para montar EPT de itens semelhantes.
- **Conflito registrado:** `attached_document` (neste vídeo) × `attachment_document` (gravação anterior) — a decidir com validação nas telas (ver [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md)).

## 8. Riscos e cuidados

- Consultas são de leitura, mas apontam o caminho de rastreio no banco de **CQ**; os valores exibidos são dados fictícios de teste (clientes "de teste" com CPF/CNPJ de teste).
- O número da proposta exibido na grade e nos filtros tem leitura incerta — **não usar como referência numérica** sem validar (ver [`incertezas.md`](incertezas.md) item 2).
- A grafia do agrupamento (`attached_document` × `attachment_document`) está em conflito entre gravações — não padronizar sem validação.
- Os caminhos de rede exibidos (compartilhamento `Mesa_C6`, pasta de usuário) foram mascarados nos derivados por higiene.
