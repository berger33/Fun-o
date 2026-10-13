# Glossário geral

| Termo / sigla | Definição sustentada | Categoria | Fonte e timestamp |
|---|---|---|---|
| **CCB (INSS)** | Cédula de Crédito Bancário do INSS; documento cujo modelo está sendo alterado | NEGOCIO | [`apresentacao-projeto-19-18`](apresentacao-projeto-19-18/glossario.md) — 00:00:25, 00:01:41 |
| **Refinanciamento (refim)** | Operação que agrupa múltiplos contratos (operações originais) com informações no documento | NEGOCIO | idem — 00:00:25 |
| **Operações originais / contratos de origem** | Contratos anteriores que compõem o refinanciamento | NEGOCIO | idem — 00:00:49 |
| **Credor** | Titular das operações de origem; exibido uma única vez quando o mesmo, concatenado quando distinto | NEGOCIO | idem — 00:01:00 – 00:01:37 |
| **Saldo devedor** | Valor devido por contrato; passa a ser exibido como **somatória** no refinanciamento | NEGOCIO | idem — 00:01:37 – 00:01:55 |
| **SIC Minutas** | Módulo onde as novas variáveis serão criadas | SISTEMAS | idem — item I (00:05:03) |
| **Web Autorizador** | Módulo indicado no limite de escopo da entrega | SISTEMAS | idem — item 1.3 (00:00:00) |
| **API de formalização** | Interface a atualizar com as novas variáveis | SISTEMAS | idem — 00:02:09 |
| **Jornada de contratação** | Fluxo em que o usuário emite a CCB | PROCESSOS | idem — 00:02:13 |
| **CQ** | Controle de qualidade | PROCESSOS | idem — 00:07:04 |
| **Plano de teste** | Artefato de teste com esforço citado ("21, 3 e 16") | PROCESSOS | idem — 00:07:32 |
| **Reprot** | Referência de página do documento de teste ("Página 3 REPROT - CÉDULA") | SISTEMAS | idem — 00:06:18 |
| **EPT** | Artefato de especificação/plano de teste vinculado a um item ágil (ex.: `570023 - [EPT]` vinculado a `558139 - [ÁGIL]`), utilizado para guiar a execução dos testes | PROCESSOS | [`gravando-2026-07-07-155307`](gravando-2026-07-07-155307/glossario.md) — 00:00:01, 00:00:07, 00:00:51 |
| **Margem de tolerância (parâmetro)** | Parâmetro funcional alvo dos itens `558139` e `570023` no contexto C6 Consig | NEGOCIO | idem — 00:00:00, 00:00:07 |
| **Base / UDL Base ("subir na base, mudar a pastinha")** | Ambiente compartilhado de banco/arquivos usado nos testes de CQ, cuja alteração requer verificar antes se outro operador já modificou | INFRA_E_ACESSO | idem — 00:00:00, 00:01:18 – 00:01:24 |
| **Despesas / Tarifas (Seguro A)** | Quadro da tela `Proposta Sintetizada` onde aparecem `Vlr. IOF` e as despesas do convênio, incluindo despesas do tipo seguro (`Seguro A`) | NEGOCIO / SISTEMAS | [`gravando-2026-10-07-152044`](gravando-2026-10-07-152044/glossario.md) — 00:00:11 – 00:01:26 |
| **Cód. Política de Despesa/Tarifa (`98`)** | Código que vincula um convênio (`989898 - CONV MS`) à sua política de despesas e tarifas, consultado no botão `Despesas` da tela de convênio | SISTEMAS / NEGOCIO | idem — 00:03:07 – 00:03:21 |
| **Reaproveitamento de seguro** | Funcionalidade de refinanciamento em que o seguro da operação anterior é reaproveitado, monitorada em testes de integração | NEGOCIO | idem — 00:00:00 |
| **`FCSMONITOREMPR` (`ECONSULT` / `TBPERFCON`)** | Banco e tabelas de monitoramento de consultas/eventos de esteira e averbação por proposta (`CSNRPROP`) | SQL / SISTEMAS | idem — 00:00:00 |
| **Disponibilização padrão (`Liberacao_Padrao_V30.xlsx`)** | Processo de validação e evidenciação de pacotes de liberação padrão guiado pela aba `Cenários` da planilha `Liberacao_Padrao_V30.xlsx` | PROCESSOS | [`liberacao-padrao-glauco`](liberacao-padrao-glauco/glossario.md) — 00:00:29 – 00:02:47 |
| **Entrega inicial - Completo (coluna `G`)** | Modalidade de disponibilização padrão aplicada quando o cliente ainda não possui o módulo (ex.: Portobank) | PROCESSOS / NEGOCIO | idem — 00:02:00 – 00:02:28 |
| **Opções `C` e `W` (procedures `.NET`)** | Opções de criação/conferência de procedures `.NET` na liberação padrão (planilha cita `C`, mas deve-se conferir também `W`) | SISTEMAS / SQL | idem — 00:02:33 – 00:02:43 |
| **`TPARWFIUTIL` (`PWALIAS`) / `WFIUTIL` / `TRTHB` / `FI.SQLResutil` / `WebAcesso`** | Tabelas, campos e utilitários descritos nos cenários de `Web Site .Net` e `Plugin` da planilha de liberação padrão | SISTEMAS / SQL | idem — 00:00:50, 00:01:40 |

> Definições completas, com todas as fontes e timestamps, em
> [`apresentacao-projeto-19-18/glossario.md`](apresentacao-projeto-19-18/glossario.md).

Quando houver entradas, cada termo/sigla deve trazer definição sustentada pelo vídeo, categoria e todas as fontes com timestamps. Divergências de definição entre gravações ficam registradas em [`CONFLITOS_E_VALIDACAO.md`](CONFLITOS_E_VALIDACAO.md), sem escolher uma versão.

## Termos de `PROJETO 14-08.mp4`

- **ServCom / Envio da Proposta ao Sistema Externo:** módulo e plugin que enviam a proposta à instituição para formalização digital (00:00:03).
- **CRN:** *Company Registration Number* — campo de layout com o CNPJ do empregador (tela em 00:02:00).
- **ETRACPD / ETRAINSS:** prefixos de campos de origem usados nas tabelas de layout das EFs (00:02:00; 00:07:00).
- **simulation_id:** ID da simulação de reaproveitamento (pro rata) retornado pelo plugin de consulta de reaproveitamento de seguro; vazio fora de reaproveitamento (00:06:00).
- **OS 556576:** "Gravação do ID da simulação na consulta do pro rata" (00:05:36).

## Termos de `Gravando 2026-09-22 111258.mp4`

- **attachment_document:** nome do agrupamento que informa documentos anexados no envio ao sistema externo (RFP001 `001.1`, `00:02:30`; especificação `00:03:05`). Ver [`glossário do lote`](gravando-2026-09-22-111258/glossario.md).
- **document_type / document_name / user:** campos do agrupamento — tipo do documento, nome do documento anexado e usuário que anexou (`00:03:05`). `document_type` como **código** ou **descrição**: em aberto (`00:04:02`–`00:05:08`).
- **null:** valor enviado quando não há documento anexado ou quando a informação não existe na base (`00:03:43`–`00:03:50`).
- **SIC:** sistema de onde, segundo a fala, as informações devem ser obtidas; exige código do perfil (`00:05:13`–`00:05:20`).
- **Código do perfil:** configuração necessária no SIC e no web service; valor não registrado (`00:05:22`–`00:05:34`).
- **Review:** revisão feita ao fechar o pacote de versão; local de apresentação de projetos (`00:06:09`–`00:06:35`).
- **IP:** situação do item de desenvolvimento; sigla não definida na gravação (`00:07:30`).

## Termos de `Jonas EPT explicação.mp4`

- **ECONSULTD:** tabela de **detalhe** da consulta (`FCSMONITOREMPR`), em chave-valor (`CDIDCONS`, `CDCONTROLE`, `CDCAMPO` + conteúdo), onde fica o JSON do payload do envio ao sistema externo (`00:03:11`–`00:03:42`).
- **Rastreio por nome do serviço:** variação do diagnóstico em `ECONSULT` filtrando por `PRDESCPFCON LIKE ('%Servico de Envio da Proposta ao Sistema Externo%')` em vez de por `CSNRPROP` (`00:02:50`).
- **Payload do envio ao sistema externo:** JSON com campos de contrato (`contract_amount`, `contract_net_amount`, `bank_code`, `formalization_type "D"`, …), objeto `client` e objeto `corban_data` (`00:04:30`–`00:05:20`).
- **`client` (objeto do payload):** bloco de dados do cliente; o novo agrupamento de documentos anexados entra dentro dele ("ele vai estar em client", `00:05:04`).
- **`corban_data` / Origem 3:** dados da promotora/correspondente no payload (`id "001010"` = "Origem 3" da proposta); a EF define `phone` (Telefone Corban ≤9) e `phone_area_code` (DDD Corban ≤3) "de acordo com o cadastro da Origem 3" (`00:05:00`).
- **`/proposal/import` e `/proposal/update`:** fluxos de integração citados nos cenários de teste (importação de proposta nova e atualização de proposta existente com documento anexado no checklist) (`00:09:00`–`00:09:30`).
- **Resposta de sucesso da integração:** `200 OK` com `success=true`, `type=ok`, `message=proposal imported` e `details` conforme o padrão do serviço; falha de validação → `400 BadRequest`/`409 Conflict` (`00:09:20`).
- **Estruturas a preservar sem regressão:** `corbanData`, `Credor associatedProposals`, `last_ConsultINSS`, `Insurance_reuse` (`00:09:20`).
- **Planilha EPT (`EPT_586780`):** documento de casos de teste do CQ (colunas `CT`, `Ref.`, `Etapa`, `Resultado esperado`, `Status`, `Observações`; seções de prê-missas e validações básicas) — aqui vista **preenchida**, complementando a visão de `Gravando 2026-07-07 155307.mp4` (`00:05:50`–`00:08:10`).
- **Relatório de Testes (`Relatorio_de_Testes_586780`):** documento Word padrão "CQ - Controle de Qualidade / Evidências de Testes" com cenários prontos a reaproveitar na EPT (`00:08:27`–`00:09:30`).
