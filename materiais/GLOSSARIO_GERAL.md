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
