# Índice da biblioteca de materiais

Atualizado em **2026-10-14**. Conecta as gravações extraídas aos respectivos guias, procedimentos, glossários, capturas e índices temáticos.

## Situação

| Item | Estado |
|---|---|
| Vídeos no manifesto | 24 (22 conteúdos distintos) |
| Gravações concluídas e publicadas | **7** (`Apresentação projeto 19-18.mp4`, `Gravando 2026-07-07 155307.mp4`, `Gravando 2026-09-22 111258.mp4`, `Gravando 2026-10-07 152044.mp4`, `Jonas EPT explicação.mp4`, `Liberação padrão - Glauco.mp4`, `PROJETO 14-08.mp4`) |
| Duplicatas cobertas por referência | `jonas2309.mp4` = `Jonas EPT explicação.mp4` (oid `f99bd795…`) e `Gravando 2026-08-24 161729.mp4` = `Gravando 2026-08-24 124650.mp4` (oid `1b9b6afd…`; ver [`../STATUS.md`](../STATUS.md)) |
| Em análise no lote atual | **14** conteúdos distintos — transcrições automáticas preliminares de [`Gravando 2026-07-08 182343.mp4`](gravando-2026-07-08-182343/transcricao_bruta.txt), [`MICHELLE CTC PORTABILIDADE REFIN.mp4`](michelle-ctc-portabilidade-refin/transcricao_bruta.txt), [`MCB - QISTA.mp4`](mcb-qista/transcricao_bruta.txt), [`Primeiro projeto.mp4`](primeiro-projeto/transcricao_bruta.txt), [`Gravando 2026-08-24 124650.mp4`](gravando-2026-08-24-124650/transcricao_bruta.txt), [`Gravando 2026-10-06 110907.mp4`](gravando-2026-10-06-110907/transcricao_bruta.txt), [`Gravando 2026-09-23 164626.mp4`](gravando-2026-09-23-164626/transcricao_bruta.txt), [`Como fazer EPT.mp4`](como-fazer-ept/transcricao_bruta.txt), [`projeto EPT.mp4`](projeto-ept/transcricao_bruta.txt; reprocessada sem VAD após 1 segmento no primeiro passe), [`ClientSecret EWEN TREINAMENTO.mp4`](clientsecret-ewen-treinamento/transcricao_bruta.txt; sem VAD), [`explicacao mesa c6.mp4`](explicacao-mesa-c6/transcricao_bruta.txt; sem VAD), [`recalculo.mp4`](recalculo/transcricao_bruta.txt; sem VAD), [`dESAVERBAÇÃO.mp4`](desaverbacao/transcricao_bruta.txt; sem VAD) e [`Gravando 2026-10-07 132428.mp4`](gravando-2026-10-07-132428/transcricao_bruta.txt; sem VAD); a cópia idêntica `Gravando 2026-08-24 161729.mp4` está coberta por referência. Faltam revisão manual, análise visual e os demais materiais (ver os respectivos `LEIA-ME.md`) |
| Método de obtenção no Arena | Ponte seletiva por vídeo via CI (objeto LFS único ou partes selecionadas e reconstruídas) + validação de bytes/SHA-256 — ver [`BLOQUEIO_LFS_ARENA.md`](BLOQUEIO_LFS_ARENA.md) e [`PRIVACIDADE_E_RETENCAO.md`](PRIVACIDADE_E_RETENCAO.md) |

## Por categoria

- **`SISTEMAS`** — ver [`SISTEMAS/INDICE_SISTEMAS.md`](SISTEMAS/INDICE_SISTEMAS.md):
  - **SIC Minutas (do Autorizador)** / **Web Autorizador** / **API de formalização**: criação de variáveis para modelo de CCB de refinanciamento INSS (`Apresentação projeto 19-18.mp4`).
  - **Autorizador**: ambientação prática de testes a partir da EPT e coordenação com frente de API (`Gravando 2026-07-07 155307.mp4`).
  - **Autorizador Web (`WebAutorizador`)**: telas `Proposta Sintetizada` (`UI.PropostaSintetizada.aspx`), `Alteração de Convênio` (`UI.CD.ConvA.aspx` / `UI.ConfigConvenio.aspx`) e modal `Despesas` (`Gravando 2026-10-07 152044.mp4`).
  - **Planilha `Liberacao_Padrao_V30.xlsx` (`Web Site .Net`, `Plugin`, `WFIUTIL`, `FI.SQLResutil`, `WebAcesso`)**: matriz de cenários de disponibilização padrão (`Liberação padrão - Glauco.mp4`).
  - **Autorizador / Envio da Proposta ao Sistema Externo (`ServCon`, plugin, `SrvEnvioPropExt`)**: novo agrupamento `attachment_document` (campos `document_type`, `document_name`, `user`; envio como `null` sem documentos) na especificação da OS 586780 (`Gravando 2026-09-22 111258.mp4` — `00:02:30`, `00:03:05`, `00:03:50`; [`gravando-2026-09-22-111258/procedimentos.md`](gravando-2026-09-22-111258/procedimentos.md) Fluxo B).
  - **Autorizador Web / SSMS / `ServCon`-`SrvEnvioPropExt` / EPT**: demonstração do rastreio da execução do serviço em `FCSMONITOREMPR` (`ECONSULT` por nome de serviço → `ECONSULTD` por `CDIDCONS` → payload JSON no Notepad++), da leitura da EF da OS 586780 e do preenchimento da planilha `EPT_586780` com cenários do Relatório de Testes (`Jonas EPT explicação.mp4` — [`jonas-ept-explicacao/guia_de_estudo.md`](jonas-ept-explicacao/guia_de_estudo.md) §§3–6).
- **`PROCESSOS`** — ver [`PROCESSOS/INDICE_PROCESSOS.md`](PROCESSOS/INDICE_PROCESSOS.md):
  - Geração da CCB de refinanciamento com novas variáveis, atualização da API de formalização e fechamento de estimativa de horas (`Apresentação projeto 19-18.mp4`).
  - Início de execução de testes a partir da EPT (`570023`), alinhamento com operador de API (Santana) e conferência prévia antes de subir base/mudar pasta compartilhada (`Gravando 2026-07-07 155307.mp4`).
  - Identificação da despesa do tipo seguro (`Seguro A`) na proposta e rastreamento do `Cód. Política de Despesa/Tarifa` (`98`) no cadastro do convênio `989898 - CONV MS` (`Gravando 2026-10-07 152044.mp4`).
  - Execução e evidenciação de testes de disponibilização padrão na aba `Cenários` de `Liberacao_Padrao_V30.xlsx` (caso prático Portobank — `Plugin` em `Entrega inicial - Completo`) (`Liberação padrão - Glauco.mp4`).
  - Revisão de projetos na **review** ao fechar o pacote; registro de horas no Gantt/mapa e item em status IP antes do início do desenvolvimento (`Gravando 2026-09-22 111258.mp4` — `00:06:09`–`00:07:39`).
  - Demonstração de "como fazer" para o analista de CQ: investigar integração no banco, conferir proposta no Autorizador, preencher EPT (número do projeto, item da EF, etapa genérica) e acrescentar cenário de teste a partir do Relatório de Testes da pasta compartilhada (`Jonas EPT explicação.mp4` — [`jonas-ept-explicacao/procedimentos.md`](jonas-ept-explicacao/procedimentos.md) §§1–5).
- **`NEGOCIO`** — ver [`GLOSSARIO_GERAL.md`](GLOSSARIO_GERAL.md):
  - CCB (INSS), refinanciamento com múltiplos contratos, operações originais, deduplicação/concatenação de credor e somatória de saldo devedor (`Apresentação projeto 19-18.mp4`).
  - Parâmetro para margem de tolerância em operações C6 Consig (`Gravando 2026-07-07 155307.mp4`).
  - Despesa do tipo seguro (`Seguro A`) vinculada ao convênio, política de despesa/tarifa (`98`) e reaproveitamento de seguro em refinanciamento (`Gravando 2026-10-07 152044.mp4`).
  - Disponibilização/liberação padrão de módulos para clientes (ex.: Portobank) em modalidades `Entrega inicial - Completo`, `Cliente já tem o módulo`, `Fluxo Limpo Versão Padrão` e `Entrega inicial - Reduzido` (`Liberação padrão - Glauco.mp4`).
  - Nova Flag informativa de Docs anexados (OS 586780) para informar ao sistema externo os documentos anexados à proposta, a pedido da jornada de formalização do cliente C6 (`Gravando 2026-09-22 111258.mp4` — `00:02:08`–`00:02:58`).
  - Estrutura do payload do envio ao sistema externo (campos de contrato, `client`, `corban_data` da "Origem 3"), endpoints `/proposal/import` e `/proposal/update`, resposta `200 OK / success=true / type=ok / message=proposal imported` e erros `400 BadRequest`/`409 Conflict`; estruturas `corbanData`, `Credor associatedProposals`, `last_ConsultINSS`, `Insurance_reuse` a preservar sem regressão (`Jonas EPT explicação.mp4` — [`jonas-ept-explicacao/guia_de_estudo.md`](jonas-ept-explicacao/guia_de_estudo.md) §§4, 6).
- **`INFRA_E_ACESSO`**:
  - Uso de base compartilhada (`UDL Base`) e diretórios de rede (`Mesa_C6 Arquivos`), com verificação prévia para evitar sobrescrita de ambiente entre operadores (`Gravando 2026-07-07 155307.mp4` — [`guia_de_estudo.md`](gravando-2026-07-07-155307/guia_de_estudo.md) §3).
  - Integração com o SIC e execução por web service dependem da configuração do código do perfil, não demonstrada na tela (`Gravando 2026-09-22 111258.mp4` — `00:05:13`–`00:05:46`; [`incertezas.md`](gravando-2026-09-22-111258/incertezas.md) item 3).
  - Acesso SSMS aos bancos de CQ (`FCSMONITOREMPR`, `FCSPROPEMPR`) e artefatos de equipe no compartilhamento `Mesa_C6` (EF em PDF, Relatório de Testes e EPT da OS 586780 na "pasta doc"); hosts e caminhos mascarados nos derivados (`Jonas EPT explicação.mp4` — [`jonas-ept-explicacao/metadados.md`](jonas-ept-explicacao/metadados.md)).
- **`DÚVIDA_OU_CONFLITO`** — ver [`CONFLITOS_E_VALIDACAO.md`](CONFLITOS_E_VALIDACAO.md):
  - Parametrização/identificação do credor por operação e distribuição das horas "21, 3 e 16" do plano de teste (`Apresentação projeto 19-18.mp4`).
  - Grafia falada "IPT" × tag escrita `[EPT]` e etapas técnicas detalhadas de "subir na base / mudar a pastinha" (`Gravando 2026-07-07 155307.mp4`).
  - Correção de transcrição "doutor Isabel" → "Autorizador" (`00:01:31`) e continuação em `Política de Despesas e Tarifas` (`Gravando 2026-10-07 152044.mp4`).
  - Divergência entre texto da linha 86 da planilha `Liberacao_Padrao_V30.xlsx` (que cita apenas opção `C`) e instrução oral de Glauco (conferir também se a opção `W` existe) (`Liberação padrão - Glauco.mp4`).
  - Tipo do documento `document_type`: código × descrição, com conclusão falada em favor do código e ressalva não resolvida (`Gravando 2026-09-22 111258.mp4` — `00:04:02`–`00:05:08`; [`incertezas.md`](gravando-2026-09-22-111258/incertezas.md) item 1).
  - Grafia do objeto do agrupamento: `attached_document` (lido na página de layout da EF em `Jonas EPT explicação.mp4` — `00:04:20`) × `attachment_document` (registrado em `Gravando 2026-09-22 111258.mp4`); literais de número de proposta ilegíveis e finalidade de `CLOGREFIN`/`CLOGREFIND`/`EREAPSEG`/`CCOMP` não explicada (`Jonas EPT explicação.mp4` — [`jonas-ept-explicacao/incertezas.md`](jonas-ept-explicacao/incertezas.md) itens 1–2, 6).
- **`SQL`** — ver [`SQL/INDICE_SQL.md`](SQL/INDICE_SQL.md):
  - Consulta T-SQL (`SELECT TOP 1000 ... FROM FCSMONITOREMPR..ECONSULT(NOLOCK) INNER JOIN FCSMONITOREMPR..TBPERFCON`) para monitorar esteira/averbação por proposta (`CSNRPROP`) no contexto de reaproveitamento de seguro (`Gravando 2026-10-07 152044.mp4` — [`guia_de_estudo.md`](gravando-2026-10-07-152044/guia_de_estudo.md) §4).
  - Consultas T-SQL em `FCSMONITOREMPR` (`ECONSULT` × `TBPERFCON` por descrição do serviço + detalhe chave-valor em `ECONSULTD` por `CDIDCONS`) e consultas preparadas em `FCSPROPEMPR` (`CLOGREFIN`, `CLOGREFIND`, `EREAPSEG`, `CCOMP`) para obter o payload JSON do `SrvEnvioPropExt` (`Jonas EPT explicação.mp4` — [`jonas-ept-explicacao/guia_de_estudo.md`](jonas-ept-explicacao/guia_de_estudo.md) §3).
  - Instruções operacionais de banco na planilha `Liberacao_Padrao_V30.xlsx`: `TPARWFIUTIL.PWALIAS` (`WFIUTIL`), criação de procedures `.NET` (`C` e `W`) e exclusão prévia em `TRTHB` antes de `FI.SQLResutil` (`Liberação padrão - Glauco.mp4` — [`guia_de_estudo.md`](liberacao-padrao-glauco/guia_de_estudo.md) §§4–5).

- **`SQL`** — sem SQL demonstrado em `Gravando 2026-09-22 111258.mp4` (ver tabela de gravações sem SQL em [`SQL/INDICE_SQL.md`](SQL/INDICE_SQL.md)).

## Por gravação

Fila completa e estados oficiais em [`../STATUS.md`](../STATUS.md) (24 vídeos).

| Gravação | Estado | Pasta | Categorias | Resumo do conteúdo |
|---|---|---|---|---|
| `Apresentação projeto 19-18.mp4` | **concluído** | [`apresentacao-projeto-19-18/`](apresentacao-projeto-19-18/LEIA-ME.md) | `SISTEMAS`, `NEGOCIO`, `PROCESSOS`, `DÚVIDA_OU_CONFLITO` | Especificação funcional OS 552267 — atualização do modelo de CCB do INSS em refinanciamento com múltiplos contratos (3 variáveis no SIC Minutas/Web Autorizador + API de formalização + estimativa de horas). |
| `Gravando 2026-07-07 155307.mp4` | **concluído** | [`gravando-2026-07-07-155307/`](gravando-2026-07-07-155307/LEIA-ME.md) | `PROCESSOS`, `SISTEMAS`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO` | Orientação para iniciar testes no Autorizador usando a EPT (`570023` / `558139` — margem de tolerância), alinhar com Santana (API) e conferir antes de subir base/mudar pasta compartilhada. |
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
