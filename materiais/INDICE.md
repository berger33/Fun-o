# Índice da biblioteca de materiais

Atualizado em **2026-10-13**. Conecta as gravações extraídas aos respectivos guias, procedimentos, glossários, capturas e índices temáticos.

## Situação

| Item | Estado |
|---|---|
| Vídeos no manifesto | 24 (22 conteúdos distintos) |
| Gravações concluídas e publicadas | **6** (`Apresentação projeto 19-18.mp4`, `Gravando 2026-07-07 155307.mp4`, `Gravando 2026-09-22 111258.mp4`, `Gravando 2026-10-07 152044.mp4`, `Liberação padrão - Glauco.mp4`, `PROJETO 14-08.mp4`) |
| Em análise no lote atual | **0** — próximo da fila (`Jonas EPT explicação.mp4`) disparado pela ponte no commit de encerramento deste lote |
| Método de obtenção no Arena | Ponte seletiva por vídeo via CI (`git lfs pull --include`) + validação de bytes e SHA-256 — ver [`BLOQUEIO_LFS_ARENA.md`](BLOQUEIO_LFS_ARENA.md) e [`PRIVACIDADE_E_RETENCAO.md`](PRIVACIDADE_E_RETENCAO.md) |

## Por categoria

- **`SISTEMAS`** — ver [`SISTEMAS/INDICE_SISTEMAS.md`](SISTEMAS/INDICE_SISTEMAS.md):
  - **SIC Minutas (do Autorizador)** / **Web Autorizador** / **API de formalização**: criação de variáveis para modelo de CCB de refinanciamento INSS (`Apresentação projeto 19-18.mp4`).
  - **Autorizador**: ambientação prática de testes a partir da EPT e coordenação com frente de API (`Gravando 2026-07-07 155307.mp4`).
  - **Autorizador Web (`WebAutorizador`)**: telas `Proposta Sintetizada` (`UI.PropostaSintetizada.aspx`), `Alteração de Convênio` (`UI.CD.ConvA.aspx` / `UI.ConfigConvenio.aspx`) e modal `Despesas` (`Gravando 2026-10-07 152044.mp4`).
  - **Planilha `Liberacao_Padrao_V30.xlsx` (`Web Site .Net`, `Plugin`, `WFIUTIL`, `FI.SQLResutil`, `WebAcesso`)**: matriz de cenários de disponibilização padrão (`Liberação padrão - Glauco.mp4`).
  - **Autorizador / Envio da Proposta ao Sistema Externo (`ServCon`, plugin, `SrvEnvioPropExt`)**: novo agrupamento `attachment_document` (campos `document_type`, `document_name`, `user`; envio como `null` sem documentos) na especificação da OS 586780 (`Gravando 2026-09-22 111258.mp4` — `00:02:30`, `00:03:05`, `00:03:50`; [`gravando-2026-09-22-111258/procedimentos.md`](gravando-2026-09-22-111258/procedimentos.md) Fluxo B).
- **`PROCESSOS`** — ver [`PROCESSOS/INDICE_PROCESSOS.md`](PROCESSOS/INDICE_PROCESSOS.md):
  - Geração da CCB de refinanciamento com novas variáveis, atualização da API de formalização e fechamento de estimativa de horas (`Apresentação projeto 19-18.mp4`).
  - Início de execução de testes a partir da EPT (`570023`), alinhamento com operador de API (Santana) e conferência prévia antes de subir base/mudar pasta compartilhada (`Gravando 2026-07-07 155307.mp4`).
  - Identificação da despesa do tipo seguro (`Seguro A`) na proposta e rastreamento do `Cód. Política de Despesa/Tarifa` (`98`) no cadastro do convênio `989898 - CONV MS` (`Gravando 2026-10-07 152044.mp4`).
  - Execução e evidenciação de testes de disponibilização padrão na aba `Cenários` de `Liberacao_Padrao_V30.xlsx` (caso prático Portobank — `Plugin` em `Entrega inicial - Completo`) (`Liberação padrão - Glauco.mp4`).
  - Revisão de projetos na **review** ao fechar o pacote; registro de horas no Gantt/mapa e item em status IP antes do início do desenvolvimento (`Gravando 2026-09-22 111258.mp4` — `00:06:09`–`00:07:39`).
- **`NEGOCIO`** — ver [`GLOSSARIO_GERAL.md`](GLOSSARIO_GERAL.md):
  - CCB (INSS), refinanciamento com múltiplos contratos, operações originais, deduplicação/concatenação de credor e somatória de saldo devedor (`Apresentação projeto 19-18.mp4`).
  - Parâmetro para margem de tolerância em operações C6 Consig (`Gravando 2026-07-07 155307.mp4`).
  - Despesa do tipo seguro (`Seguro A`) vinculada ao convênio, política de despesa/tarifa (`98`) e reaproveitamento de seguro em refinanciamento (`Gravando 2026-10-07 152044.mp4`).
  - Disponibilização/liberação padrão de módulos para clientes (ex.: Portobank) em modalidades `Entrega inicial - Completo`, `Cliente já tem o módulo`, `Fluxo Limpo Versão Padrão` e `Entrega inicial - Reduzido` (`Liberação padrão - Glauco.mp4`).
  - Nova Flag informativa de Docs anexados (OS 586780) para informar ao sistema externo os documentos anexados à proposta, a pedido da jornada de formalização do cliente C6 (`Gravando 2026-09-22 111258.mp4` — `00:02:08`–`00:02:58`).
- **`INFRA_E_ACESSO`**:
  - Uso de base compartilhada (`UDL Base`) e diretórios de rede (`Mesa_C6 Arquivos`), com verificação prévia para evitar sobrescrita de ambiente entre operadores (`Gravando 2026-07-07 155307.mp4` — [`guia_de_estudo.md`](gravando-2026-07-07-155307/guia_de_estudo.md) §3).
  - Integração com o SIC e execução por web service dependem da configuração do código do perfil, não demonstrada na tela (`Gravando 2026-09-22 111258.mp4` — `00:05:13`–`00:05:46`; [`incertezas.md`](gravando-2026-09-22-111258/incertezas.md) item 3).
- **`DÚVIDA_OU_CONFLITO`** — ver [`CONFLITOS_E_VALIDACAO.md`](CONFLITOS_E_VALIDACAO.md):
  - Parametrização/identificação do credor por operação e distribuição das horas "21, 3 e 16" do plano de teste (`Apresentação projeto 19-18.mp4`).
  - Grafia falada "IPT" × tag escrita `[EPT]` e etapas técnicas detalhadas de "subir na base / mudar a pastinha" (`Gravando 2026-07-07 155307.mp4`).
  - Correção de transcrição "doutor Isabel" → "Autorizador" (`00:01:31`) e continuação em `Política de Despesas e Tarifas` (`Gravando 2026-10-07 152044.mp4`).
  - Divergência entre texto da linha 86 da planilha `Liberacao_Padrao_V30.xlsx` (que cita apenas opção `C`) e instrução oral de Glauco (conferir também se a opção `W` existe) (`Liberação padrão - Glauco.mp4`).
  - Tipo do documento `document_type`: código × descrição, com conclusão falada em favor do código e ressalva não resolvida (`Gravando 2026-09-22 111258.mp4` — `00:04:02`–`00:05:08`; [`incertezas.md`](gravando-2026-09-22-111258/incertezas.md) item 1).
- **`SQL`** — ver [`SQL/INDICE_SQL.md`](SQL/INDICE_SQL.md):
  - Consulta T-SQL (`SELECT TOP 1000 ... FROM FCSMONITOREMPR..ECONSULT(NOLOCK) INNER JOIN FCSMONITOREMPR..TBPERFCON`) para monitorar esteira/averbação por proposta (`CSNRPROP`) no contexto de reaproveitamento de seguro (`Gravando 2026-10-07 152044.mp4` — [`guia_de_estudo.md`](gravando-2026-10-07-152044/guia_de_estudo.md) §4).
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

## Índices temáticos

- [`SQL/INDICE_SQL.md`](SQL/INDICE_SQL.md)
- [`SISTEMAS/INDICE_SISTEMAS.md`](SISTEMAS/INDICE_SISTEMAS.md)
- [`PROCESSOS/INDICE_PROCESSOS.md`](PROCESSOS/INDICE_PROCESSOS.md)
- [`GLOSSARIO_GERAL.md`](GLOSSARIO_GERAL.md)
- [`CONFLITOS_E_VALIDACAO.md`](CONFLITOS_E_VALIDACAO.md)
- [`PRIVACIDADE_E_RETENCAO.md`](PRIVACIDADE_E_RETENCAO.md)

## Gravações publicadas (detalhe)

- [`PROJETO 14-08.mp4`](projeto-14-08/LEIA-ME.md) — ServCom: campo CNPJ do empregador (`CRN`) e campo `simulation_id` (OS 556576) no plugin de envio ao sistema externo.
