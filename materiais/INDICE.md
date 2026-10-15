# Índice da biblioteca de materiais

Atualizado em **2026-10-14**. Conecta as gravações extraídas aos respectivos guias, procedimentos, glossários, capturas e índices temáticos.

## Situação

| Item | Estado |
|---|---|
| Vídeos no manifesto | 24 (22 conteúdos distintos) |
| Gravações concluídas e publicadas | **7** (`Apresentação projeto 19-18.mp4`, `Gravando 2026-07-07 155307.mp4`, `Gravando 2026-09-22 111258.mp4`, `Gravando 2026-10-07 152044.mp4`, `Jonas EPT explicação.mp4`, `Liberação padrão - Glauco.mp4`, `PROJETO 14-08.mp4`) |
| Duplicatas cobertas por referência | `jonas2309.mp4` = `Jonas EPT explicação.mp4` (mesmo oid `f99bd795…` — ver [`../STATUS.md`](../STATUS.md)) |
| Em análise no lote atual | **0** |
| Em revisão | **4** — `Gravando 2026-07-08 182343.mp4`, `MICHELLE CTC PORTABILIDADE REFIN.mp4`, `MCB - QISTA.mp4` e `Primeiro projeto.mp4`; próxima pendência da fila: `Gravando 2026-08-24 124650.mp4` (= `Gravando 2026-08-24 161729.mp4`) |
| Método de obtenção no Arena | Ponte seletiva por vídeo via CI (`git lfs pull --include`) + validação de bytes e SHA-256 — ver [`BLOQUEIO_LFS_ARENA.md`](BLOQUEIO_LFS_ARENA.md) e [`PRIVACIDADE_E_RETENCAO.md`](PRIVACIDADE_E_RETENCAO.md) |

## Por categoria

- **`SISTEMAS`** — ver [`SISTEMAS/INDICE_SISTEMAS.md`](SISTEMAS/INDICE_SISTEMAS.md):
  - **SIC Minutas (do Autorizador)** / **Web Autorizador** / **API de formalização**: criação de variáveis para modelo de CCB de refinanciamento INSS (`Apresentação projeto 19-18.mp4`).
  - **Autorizador**: ambientação prática de testes a partir da EPT e coordenação com frente de API (`Gravando 2026-07-07 155307.mp4`).
  - **Autorizador Web (`WebAutorizador`)**: telas `Proposta Sintetizada` (`UI.PropostaSintetizada.aspx`), `Alteração de Convênio` (`UI.CD.ConvA.aspx` / `UI.ConfigConvenio.aspx`) e modal `Despesas` (`Gravando 2026-10-07 152044.mp4`).
  - **WebAutorizador / WS / API**: conversa sobre versões e atualização em ambiente de teste; a relação entre componentes e a matriz de implantação não foi confirmada. A configuração (SIC/GDOK/API) deve ser preservada, mas há instruções de exclusão conflitantes (`Gravando 2026-07-08 182343.mp4` — [`guia_de_estudo.md`](gravando-2026-07-08-182343/guia_de_estudo.md) §§2–4).
  - **Planilha `Liberacao_Padrao_V30.xlsx` (`Web Site .Net`, `Plugin`, `WFIUTIL`, `FI.SQLResutil`, `WebAcesso`)**: matriz de cenários de disponibilização padrão (`Liberação padrão - Glauco.mp4`).
  - **Autorizador / Envio da Proposta ao Sistema Externo (`ServCon`, plugin, `SrvEnvioPropExt`)**: novo agrupamento `attachment_document` (campos `document_type`, `document_name`, `user`; envio como `null` sem documentos) na especificação da OS 586780 (`Gravando 2026-09-22 111258.mp4` — `00:02:30`, `00:03:05`, `00:03:50`; [`gravando-2026-09-22-111258/procedimentos.md`](gravando-2026-09-22-111258/procedimentos.md) Fluxo B).
  - **Autorizador Web / SSMS / `ServCon`-`SrvEnvioPropExt` / EPT**: demonstração do rastreio da execução do serviço em `FCSMONITOREMPR` (`ECONSULT` por nome de serviço → `ECONSULTD` por `CDIDCONS` → payload JSON no Notepad++), da leitura da EF da OS 586780 e do preenchimento da planilha `EPT_586780` com cenários do Relatório de Testes (`Jonas EPT explicação.mp4` — [`jonas-ept-explicacao/guia_de_estudo.md`](jonas-ept-explicacao/guia_de_estudo.md) §§3–6).
  - **Portabilidade/refim e CTC**: discussão verbal de tela unificada, acionamento e etapas de espera; o desenho citado é de outro cliente e a configuração do alvo não foi verificada (`MICHELLE CTC PORTABILIDADE REFIN.mp4` — [`michelle-ctc-portabilidade-refin/guia_de_estudo.md`](michelle-ctc-portabilidade-refin/guia_de_estudo.md) §§2–3).
  - **Autorizador / MCB / API de consulta de pontuação / WebTabelas**: conversa sobre configuração de atividade/esteira, consulta da certificação de agente e classificação da promotora; versões, tela e contrato de API não foram verificados (`MCB - QISTA.mp4` — [`mcb-qista/guia_de_estudo.md`](mcb-qista/guia_de_estudo.md) §§2–4).
  - **Autorizador / Web API de documentos anexados / GED-Gdoc**: novo endpoint simplificado para consultar arquivos por proposta ou operação, sem dados de checklist; parâmetros, perfil e resposta ainda dependem da EF aprovada (`Primeiro projeto.mp4` — [`primeiro-projeto/guia_de_estudo.md`](primeiro-projeto/guia_de_estudo.md) §§1–4).
- **`PROCESSOS`** — ver [`PROCESSOS/INDICE_PROCESSOS.md`](PROCESSOS/INDICE_PROCESSOS.md):
  - Geração da CCB de refinanciamento com novas variáveis, atualização da API de formalização e fechamento de estimativa de horas (`Apresentação projeto 19-18.mp4`).
  - Início de execução de testes a partir da EPT (`570023`), alinhamento com operador de API (Santana) e conferência prévia antes de subir base/mudar pasta compartilhada (`Gravando 2026-07-07 155307.mp4`).
  - Identificação da despesa do tipo seguro (`Seguro A`) na proposta e rastreamento do `Cód. Política de Despesa/Tarifa` (`98`) no cadastro do convênio `989898 - CONV MS` (`Gravando 2026-10-07 152044.mp4`).
  - Execução e evidenciação de testes de disponibilização padrão na aba `Cenários` de `Liberacao_Padrao_V30.xlsx` (caso prático Portobank — `Plugin` em `Entrega inicial - Completo`) (`Liberação padrão - Glauco.mp4`).
  - Revisão de projetos na **review** ao fechar o pacote; registro de horas no Gantt/mapa e item em status IP antes do início do desenvolvimento (`Gravando 2026-09-22 111258.mp4` — `00:06:09`–`00:07:39`).
  - Demonstração de "como fazer" para o analista de CQ: investigar integração no banco, conferir proposta no Autorizador, preencher EPT (número do projeto, item da EF, etapa genérica) e acrescentar cenário de teste a partir do Relatório de Testes da pasta compartilhada (`Jonas EPT explicação.mp4` — [`jonas-ept-explicacao/procedimentos.md`](jonas-ept-explicacao/procedimentos.md) §§1–5).
  - **Preparação de ambiente e importação de teste de tolerância**: a gravação menciona WebAutorizador/WS/API, configuração e importação de uma “esteira”, mas não estabelece uma sequência aprovada; ver [`gravando-2026-07-08-182343/procedimentos.md`](gravando-2026-07-08-182343/procedimentos.md).
  - **Hipótese de coordenação portabilidade/refim:** a fala menciona acionamento por CTC e etapa de espera para conferir valores da CCB, mas há conflito sobre dependência e nomes de processo; teste apenas proposto, não validado (`MICHELLE CTC PORTABILIDADE REFIN.mp4` — [`michelle-ctc-portabilidade-refin/procedimentos.md`](michelle-ctc-portabilidade-refin/procedimentos.md)).
  - **Teste hipotético da consulta MCB do agente:** planejar cenários para promotora interna/externa e observar consulta/resultado na esteira, somente em sandbox aprovado; nomes, estados e critérios ainda não confirmados (`MCB - QISTA.mp4` — [`mcb-qista/procedimentos.md`](mcb-qista/procedimentos.md) Fluxo A).
  - **Teste hipotético do endpoint GED simplificado:** cobrir entrada por proposta, por operação, ambas/nenhuma, conteúdo sem checklist e download; contrato e critérios formais pendentes (`Primeiro projeto.mp4` — [`primeiro-projeto/procedimentos.md`](primeiro-projeto/procedimentos.md) Fluxo A).
- **`NEGOCIO`** — ver [`GLOSSARIO_GERAL.md`](GLOSSARIO_GERAL.md):
  - CCB (INSS), refinanciamento com múltiplos contratos, operações originais, deduplicação/concatenação de credor e somatória de saldo devedor (`Apresentação projeto 19-18.mp4`).
  - Parâmetro para margem de tolerância em operações C6 Consig (`Gravando 2026-07-07 155307.mp4`).
  - Menção a um teste de tolerância/importação de esteira; valores falados não têm campos ou regra confirmados e não devem ser reutilizados (`Gravando 2026-07-08 182343.mp4` — `00:05:26`–`00:08:03`).
  - Portabilidade associada a refim: conferir valores do refim antes de avançar/gerar CCB é a justificativa verbal; dependência entre propostas e critério de validação continuam sem decisão (`MICHELLE CTC PORTABILIDADE REFIN.mp4` — [`michelle-ctc-portabilidade-refin/guia_de_estudo.md`](michelle-ctc-portabilidade-refin/guia_de_estudo.md) §2).
  - Certificação/pontuação de agentes e validação da proposta por classificação interna/externa da promotora aparecem como regras do negócio a confirmar; escala, estados e comportamento não foram validados (`MCB - QISTA.mp4` — [`mcb-qista/guia_de_estudo.md`](mcb-qista/guia_de_estudo.md) §§2–3).
  - Consulta de documentos GED por proposta ou operação, inclusive em operação sem proposta enviada na requisição; associação no back-office e regra de retorno precisam de validação formal (`Primeiro projeto.mp4` — [`primeiro-projeto/guia_de_estudo.md`](primeiro-projeto/guia_de_estudo.md) §§1–4).
  - Despesa do tipo seguro (`Seguro A`) vinculada ao convênio, política de despesa/tarifa (`98`) e reaproveitamento de seguro em refinanciamento (`Gravando 2026-10-07 152044.mp4`).
  - Disponibilização/liberação padrão de módulos para clientes (ex.: Portobank) em modalidades `Entrega inicial - Completo`, `Cliente já tem o módulo`, `Fluxo Limpo Versão Padrão` e `Entrega inicial - Reduzido` (`Liberação padrão - Glauco.mp4`).
  - Nova Flag informativa de Docs anexados (OS 586780) para informar ao sistema externo os documentos anexados à proposta, a pedido da jornada de formalização do cliente C6 (`Gravando 2026-09-22 111258.mp4` — `00:02:08`–`00:02:58`).
  - Estrutura do payload do envio ao sistema externo (campos de contrato, `client`, `corban_data` da "Origem 3"), endpoints `/proposal/import` e `/proposal/update`, resposta `200 OK / success=true / type=ok / message=proposal imported` e erros `400 BadRequest`/`409 Conflict`; estruturas `corbanData`, `Credor associatedProposals`, `last_ConsultINSS`, `Insurance_reuse` a preservar sem regressão (`Jonas EPT explicação.mp4` — [`jonas-ept-explicacao/guia_de_estudo.md`](jonas-ept-explicacao/guia_de_estudo.md) §§4, 6).
- **`INFRA_E_ACESSO`**:
  - Uso de base compartilhada (`UDL Base`) e diretórios de rede (`Mesa_C6 Arquivos`), com verificação prévia para evitar sobrescrita de ambiente entre operadores (`Gravando 2026-07-07 155307.mp4` — [`guia_de_estudo.md`](gravando-2026-07-07-155307/guia_de_estudo.md) §3).
  - Integração com o SIC e execução por web service dependem da configuração do código do perfil, não demonstrada na tela (`Gravando 2026-09-22 111258.mp4` — `00:05:13`–`00:05:46`; [`incertezas.md`](gravando-2026-09-22-111258/incertezas.md) item 3).
  - Acesso SSMS aos bancos de CQ (`FCSMONITOREMPR`, `FCSPROPEMPR`) e artefatos de equipe no compartilhamento `Mesa_C6` (EF em PDF, Relatório de Testes e EPT da OS 586780 na "pasta doc"); hosts e caminhos mascarados nos derivados (`Jonas EPT explicação.mp4` — [`jonas-ept-explicacao/metadados.md`](jonas-ept-explicacao/metadados.md)).
  - Configuração associada a SIC/GDOK/API e recomendação falada de backup antes de alterações; não há caminho nem valores publicados e a rotina de atualização permanece sem validação (`Gravando 2026-07-08 182343.mp4` — `00:02:58`–`00:03:24`).
  - MCB/API, app settings e UDL aparecem em relato de ambiente local e versões divergentes; sem URL/segredo publicado e sem sequência de implantação aprovada (`MCB - QISTA.mp4` — [`mcb-qista/incertezas.md`](mcb-qista/incertezas.md) §2).
  - O teste da API GED é descrito como dependente de Autorizador, subsite, Gdoc e versão da Web API; nenhuma combinação/versão de implantação foi validada (`Primeiro projeto.mp4` — [`primeiro-projeto/procedimentos.md`](primeiro-projeto/procedimentos.md) Fluxo B).
- **`DÚVIDA_OU_CONFLITO`** — ver [`CONFLITOS_E_VALIDACAO.md`](CONFLITOS_E_VALIDACAO.md):
  - Parametrização/identificação do credor por operação e distribuição das horas "21, 3 e 16" do plano de teste (`Apresentação projeto 19-18.mp4`).
  - Grafia falada "IPT" × tag escrita `[EPT]` e etapas técnicas detalhadas de "subir na base / mudar a pastinha" (`Gravando 2026-07-07 155307.mp4`).
  - Correção de transcrição "doutor Isabel" → "Autorizador" (`00:01:31`) e continuação em `Política de Despesas e Tarifas` (`Gravando 2026-10-07 152044.mp4`).
  - Divergência entre texto da linha 86 da planilha `Liberacao_Padrao_V30.xlsx` (que cita apenas opção `C`) e instrução oral de Glauco (conferir também se a opção `W` existe) (`Liberação padrão - Glauco.mp4`).
  - Tipo do documento `document_type`: código × descrição, com conclusão falada em favor do código e ressalva não resolvida (`Gravando 2026-09-22 111258.mp4` — `00:04:02`–`00:05:08`; [`incertezas.md`](gravando-2026-09-22-111258/incertezas.md) item 1).
  - Grafia do objeto do agrupamento: `attached_document` (lido na página de layout da EF em `Jonas EPT explicação.mp4` — `00:04:20`) × `attachment_document` (registrado em `Gravando 2026-09-22 111258.mp4`); literais de número de proposta ilegíveis e finalidade de `CLOGREFIN`/`CLOGREFIND`/`EREAPSEG`/`CCOMP` não explicada (`Jonas EPT explicação.mp4` — [`jonas-ept-explicacao/incertezas.md`](jonas-ept-explicacao/incertezas.md) itens 1–2, 6).
  - Instruções incompatíveis sobre excluir/preservar a pasta de configuração, além de dúvidas sobre “AWS”, a opção “N” e a importação de esteira; nenhum desses pontos deve ser usado como regra operacional sem confirmação (`Gravando 2026-07-08 182343.mp4` — [`incertezas.md`](gravando-2026-07-08-182343/incertezas.md)).
  - **MICHELLE CTC PORTABILIDADE REFIN:** fluxo ilustrado é de outro cliente; divergência entre dependência e avanço independente das propostas; nomes de processos/etapas, criação das propostas, CTC e cenário de teste não confirmados (`michelle-ctc-portabilidade-refin/incertezas.md`).
  - **MCB - QISTA:** validar pontuação/certificação e regra interna/externa; nomes de API/telas/tabelas, atividade de esteira e códigos reconhecidos pelo ASR são incertos; diagnóstico de “produto não encontrado” não identifica as tabelas e não autoriza alteração de base (`mcb-qista/incertezas.md`).
  - **Primeiro projeto:** confirmar regra dos parâmetros proposta/operação, precedência quando ambos são informados, resolução GED/back-office, campos do retorno, separação do checklist, endpoint de download e efeito de “N/W”; ASR incompleto para validar telas e identificadores sanitizados (`primeiro-projeto/incertezas.md`).
- **`SQL`** — ver [`SQL/INDICE_SQL.md`](SQL/INDICE_SQL.md):
  - Consulta T-SQL (`SELECT TOP 1000 ... FROM FCSMONITOREMPR..ECONSULT(NOLOCK) INNER JOIN FCSMONITOREMPR..TBPERFCON`) para monitorar esteira/averbação por proposta (`CSNRPROP`) no contexto de reaproveitamento de seguro (`Gravando 2026-10-07 152044.mp4` — [`guia_de_estudo.md`](gravando-2026-10-07-152044/guia_de_estudo.md) §4).
  - Consultas T-SQL em `FCSMONITOREMPR` (`ECONSULT` × `TBPERFCON` por descrição do serviço + detalhe chave-valor em `ECONSULTD` por `CDIDCONS`) e consultas preparadas em `FCSPROPEMPR` (`CLOGREFIN`, `CLOGREFIND`, `EREAPSEG`, `CCOMP`) para obter o payload JSON do `SrvEnvioPropExt` (`Jonas EPT explicação.mp4` — [`jonas-ept-explicacao/guia_de_estudo.md`](jonas-ept-explicacao/guia_de_estudo.md) §3).
  - Instruções operacionais de banco na planilha `Liberacao_Padrao_V30.xlsx`: `TPARWFIUTIL.PWALIAS` (`WFIUTIL`), criação de procedures `.NET` (`C` e `W`) e exclusão prévia em `TRTHB` antes de `FI.SQLResutil` (`Liberação padrão - Glauco.mp4` — [`guia_de_estudo.md`](liberacao-padrao-glauco/guia_de_estudo.md) §§4–5).

- **`SQL`** — sem SQL demonstrado em `Gravando 2026-09-22 111258.mp4`, `MICHELLE CTC PORTABILIDADE REFIN.mp4`, `MCB - QISTA.mp4` e `Primeiro projeto.mp4`; nesta última há somente menção a um `SELECT` não reproduzido (ver [`SQL/INDICE_SQL.md`](SQL/INDICE_SQL.md)).

## Por gravação

Fila completa e estados oficiais em [`../STATUS.md`](../STATUS.md) (24 vídeos).

| Gravação | Estado | Pasta | Categorias | Resumo do conteúdo |
|---|---|---|---|---|
| `Apresentação projeto 19-18.mp4` | **concluído** | [`apresentacao-projeto-19-18/`](apresentacao-projeto-19-18/LEIA-ME.md) | `SISTEMAS`, `NEGOCIO`, `PROCESSOS`, `DÚVIDA_OU_CONFLITO` | Especificação funcional OS 552267 — atualização do modelo de CCB do INSS em refinanciamento com múltiplos contratos (3 variáveis no SIC Minutas/Web Autorizador + API de formalização + estimativa de horas). |
| `Gravando 2026-07-07 155307.mp4` | **concluído** | [`gravando-2026-07-07-155307/`](gravando-2026-07-07-155307/LEIA-ME.md) | `PROCESSOS`, `SISTEMAS`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO` | Orientação para iniciar testes no Autorizador usando a EPT (`570023` / `558139` — margem de tolerância), alinhar com Santana (API) e conferir antes de subir base/mudar pasta compartilhada. |
| `Gravando 2026-07-08 182343.mp4` | **em revisão** | [`gravando-2026-07-08-182343/`](gravando-2026-07-08-182343/LEIA-ME.md) | `SISTEMAS`, `PROCESSOS`, `INFRA_E_ACESSO`, `NEGOCIO`, `DÚVIDA_OU_CONFLITO` | Transcrição preliminar e análise de atualização/configuração de WebAutorizador/WS/API e tentativa de importar esteira de teste de tolerância; instruções de exclusão conflitam, sem runbook validado. Sem capturas por privacidade. |
| `MICHELLE CTC PORTABILIDADE REFIN.mp4` | **em revisão** | [`michelle-ctc-portabilidade-refin/`](michelle-ctc-portabilidade-refin/LEIA-ME.md) | `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `DÚVIDA_OU_CONFLITO` | Transcrição automática organizada; discussão conceitual de portabilidade/refim, acionamento CTC, tela/etapa unificada e consistência da CCB. Desenho de outro cliente; dependências e teste sem validação. Sem capturas; fonte não revista visualmente. |
| `MCB - QISTA.mp4` | **em revisão** | [`mcb-qista/`](mcb-qista/LEIA-ME.md) | `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO` | Transcrição automática e análise preliminar sobre consulta MCB de certificação/pontuação de agente, promotora interna/externa e erro de cadastro. Códigos, regras e componentes não confirmados; sem SQL/teste/capturas, fonte não revista neste lote. |
| `Primeiro projeto.mp4` | **em revisão** | [`primeiro-projeto/`](primeiro-projeto/LEIA-ME.md) | `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `INFRA_E_ACESSO`, `SQL` (menção sem consulta), `DÚVIDA_OU_CONFLITO` | Transcrição automática sanitizada e análise preliminar sobre novo endpoint GED simplificado por proposta/operação, retorno sem checklist e perfil GED. Contrato, operação→proposta, download e opções N/W pendentes; sem capturas/teste, fonte não revista neste lote. |
| `Gravando 2026-10-07 152044.mp4` | **concluído** | [`gravando-2026-10-07-152044/`](gravando-2026-10-07-152044/LEIA-ME.md) | `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `SQL`, `DÚVIDA_OU_CONFLITO` | Identificação da despesa do tipo seguro (`Seguro A`) na Proposta Sintetizada do Autorizador Web, descoberta do `Cód. Política de Despesa/Tarifa: 98` no convênio `989898 - CONV MS` e consulta T-SQL em `FCSMONITOREMPR..ECONSULT`. |
| `Liberação padrão - Glauco.mp4` | **concluído** | [`liberacao-padrao-glauco/`](liberacao-padrao-glauco/LEIA-ME.md) | `PROCESSOS`, `SISTEMAS`, `NEGOCIO`, `SQL`, `DÚVIDA_OU_CONFLITO` | Treinamento conduzido por Glauco sobre o uso da planilha `Liberacao_Padrao_V30.xlsx` (aba `Cenários`) para testes de disponibilização padrão, com exemplo prático Portobank (`Plugin` em `Entrega inicial - Completo`) e alerta sobre procedures `.NET` (`C` e `W`). |
| `Gravando 2026-09-22 111258.mp4` | **concluído** | [`gravando-2026-09-22-111258/`](gravando-2026-09-22-111258/LEIA-ME.md) | `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO` | Reunião (C6 Consig, OS 586780) sobre a *Nova Flag informativa de Docs anexados*: novo agrupamento `attachment_document` (`document_type`, `document_name`, `user`; `null` sem documentos) no plugin de envio ao sistema externo, com dúvida código × descrição, integração SIC/web service e fluxo de teste e review. Sem SQL demonstrado. |
| `Jonas EPT explicação.mp4` (duplicata `jonas2309.mp4`) | **concluído** | [`jonas-ept-explicacao/`](jonas-ept-explicacao/LEIA-ME.md) | `SQL`, `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO` | Demonstração para o analista de CQ: rastrear o `SrvEnvioPropExt` (OS 586780) em `FCSMONITOREMPR..ECONSULT`/`ECONSULTD`, ler o payload JSON (agrupamento dentro de `client`), preencher a EPT e acrescentar cenários (`/proposal/import`, `/proposal/update`) do Relatório de Testes. |

## Índices temáticos

- [`SQL/INDICE_SQL.md`](SQL/INDICE_SQL.md)
- [`SISTEMAS/INDICE_SISTEMAS.md`](SISTEMAS/INDICE_SISTEMAS.md)
- [`PROCESSOS/INDICE_PROCESSOS.md`](PROCESSOS/INDICE_PROCESSOS.md)
- [`GLOSSARIO_GERAL.md`](GLOSSARIO_GERAL.md)
- [`CONFLITOS_E_VALIDACAO.md`](CONFLITOS_E_VALIDACAO.md)
- [`PRIVACIDADE_E_RETENCAO.md`](PRIVACIDADE_E_RETENCAO.md)

## Gravações publicadas (detalhe)

- [`PROJETO 14-08.mp4`](projeto-14-08/LEIA-ME.md) — ServCom: campo CNPJ do empregador (`CRN`) e campo `simulation_id` (OS 556576) no plugin de envio ao sistema externo.
