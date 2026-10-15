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

## Termos de `Gravando 2026-07-08 182343.mp4`

- **WebAutorizador / WS / API:** componentes citados numa conversa sobre versões e atualização em ambiente de teste; a relação técnica e a matriz de implantação não foram confirmadas (`00:00:23`–`00:04:27`).
- **SIC / GDOK:** identificadores citados como parte da configuração, sem expansão nem valores expostos (`00:02:58`–`00:03:04`).
- **Pasta de configuração (`config`):** área descrita verbalmente como contendo parâmetros de SIC, GDOK e API; instruções conflitantes sobre preservá-la ou apagá-la permanecem em validação (`00:00:33`, `00:02:34`–`00:03:24`).
- **Esteira:** objeto que o interlocutor tenta importar; sistema, formato e significado não identificados (`00:05:48`–`00:07:20`).
- **Teste de tolerância:** nome falado para uma tentativa de teste, sem campo, valor, critério de sucesso ou regra de negócio verificáveis (`00:05:26`, `00:07:31`–`00:08:03`).

Ver a análise completa e as ambiguidades em [`gravando-2026-07-08-182343/glossario.md`](gravando-2026-07-08-182343/glossario.md) e [`gravando-2026-07-08-182343/incertezas.md`](gravando-2026-07-08-182343/incertezas.md).

## Termos de `MICHELLE CTC PORTABILIDADE REFIN.mp4`

- **Portabilidade / refim:** propostas/fluxos tratados como distintos e relacionados; regras de associação e sincronização não foram fechadas (`00:00:24`–`00:01:22`).
- **CTC:** sigla usada para acionamento/retorno de etapa, sem expansão ou semântica técnica confirmada (`00:00:36`–`00:01:22`).
- **“CTC aciona refim”:** nome aproximado de processo falado como acionador; confirmar nome e efeito na configuração real (`00:01:07`–`00:01:22`).
- **Tela unificada / “aguarda alteração unificada”:** descrição verbal de tela e etapa de coordenação; não inspecionadas visualmente (`00:02:40`–`00:03:15`).
- **“Aguarda análise de refim de portabilidade”:** etapa alternativa citada, sem resolução quanto ao nome/uso correto (`00:07:25`–`00:07:47`).
- **CCB:** documento cuja emissão/avanço é citado como dependente da conferência dos valores do refim; campos/critério não especificados (`00:03:36`–`00:04:59`).
- **MEI:** sigla ASR sem definição na conversa (`00:15:17`–`00:15:28`).

Ver [`michelle-ctc-portabilidade-refin/glossario.md`](michelle-ctc-portabilidade-refin/glossario.md) e [`incertezas.md`](michelle-ctc-portabilidade-refin/incertezas.md); não tratar os nomes de etapa/processo como rótulos confirmados.

## Termos de `MCB - QISTA.mp4`

- **MCB:** módulo separado que, segundo a fala, armazena/consulta situação e pontuação de agentes; expansão não definida (`00:00:49`–`00:01:13`).
- **Núclea / pontuação de agente:** referência verbal à certificação e a um indicador de situação; limite `20` e suspensão não confirmados (`00:00:00`–`00:01:13`).
- **Atividade de esteira / API de consulta de pontuação:** atividade que acionaria a consulta Autorizador–MCB, com associação de esteira/atividade descrita sem configuração validada (`00:01:13`–`00:02:52`).
- **Promotora interna/externa:** classificação usada para propor cenários de validação; regra de negócio pendente (`00:07:27`–`00:09:01`).
- **WebTabelas / origem:** local e representação mencionados para consulta de promotora; nomes podem variar por ambiente e não foram vistos na tela (`00:04:22`–`00:06:46`).
- **“T-Lib”/“Telib”, QISTA, UDL:** termos reconhecidos pelo ASR sem confirmação de grafia, expansão ou função técnica (`00:03:54`–`00:04:20; 00:09:09`–`00:12:08`).
- **“Produto não encontrado”:** erro investigado sem identificação da causa ou das três tabelas correlacionadas citadas (`00:14:29`–`00:15:24`).

Ver [`mcb-qista/glossario.md`](mcb-qista/glossario.md) e [`mcb-qista/incertezas.md`](mcb-qista/incertezas.md); `190`/`061` permanecem códigos candidatos do ASR e não são valores de configuração.

## Termos de `Primeiro projeto.mp4`

- **GED / Web API de documentos anexados:** sistema e API citados para listar/baixar arquivos associados a uma proposta ou operação (`00:00:33`–`00:01:02`).
- **“Documentos anexados simplificado”:** nome verbal do novo endpoint `GET`; rota e propriedades dependem da EF aprovada (`00:01:37`–`00:02:25`).
- **Número de proposta / número de operação:** identificadores alternativos de consulta; a fala lê a regra como obrigatoriedade condicional (`00:02:25`–`00:03:42`).
- **Checklist:** informações de cadastro/análise/formalização, descritas como distintas dos arquivos GED e ausentes do retorno simplificado (`00:04:41`–`00:05:09; 00:06:56`–`00:07:37`).
- **Perfil GED / `perfil gdoc`:** configuração referenciada pelo Autorizador; grafia da chave e regra de associação precisam de confirmação (`00:07:37`–`00:08:29`).
- **Back-office:** origem da busca interna proposta para relacionar número de operação e número de proposta (`00:07:54`–`00:08:29`).
- **IDs de armazenamento / ID único / nome e extensão:** categorias de dados que a fala espera no retorno, sem confirmar os nomes de campo (`00:03:52`–`00:04:23`).
- **Opções “N”/“W” e `SELECT`:** menções sem efeito/consulta documentados; não são instrução operacional (`00:02:35`–`00:02:57; 00:13:12`–`00:16:02`).

Ver [`primeiro-projeto/glossario.md`](primeiro-projeto/glossario.md) e [`primeiro-projeto/incertezas.md`](primeiro-projeto/incertezas.md). A transcrição pública substitui identificadores e omite o trecho não técnico fora do escopo.

## Termos de `Gravando 2026-08-24 124650.mp4`

- **Autorizador / esteira:** aplicação e fluxo mencionados para criar uma proposta sintética e avançar o cenário; sequência oficial depende da EPT (`00:03:10`–`00:03:20; 00:09:55`–`00:10:10`).
- **Plugin / JSON:** componente e formato de retorno que a conversa recomenda verificar como evidência da alteração; propriedade/campo não identificado (`00:00:25`–`00:02:12; 00:12:57`–`00:13:18`). O ASR oscila nas grafias de JSON.
- **CPD / Crivo:** CPD é expandido verbalmente como consignado privado; Crivo aparece como retorno associado ao cenário, sem regra ou campo confirmado (`00:04:54`–`00:05:02`).
- **EPT / Geradoc:** artefatos/ferramenta mencionados na preparação do documento; fluxo e template não demonstrados (`00:16:01`–`00:17:25`).
- **Etapas 2/3/4:** numeração corrigida/alternada na fala; não usar como sequência oficial (`00:10:12`–`00:12:23`).

Ver [`gravando-2026-08-24-124650/glossario.md`](gravando-2026-08-24-124650/glossario.md) e [`gravando-2026-08-24-124650/incertezas.md`](gravando-2026-08-24-124650/incertezas.md). Identificadores/valores de teste estão mascarados e o trecho `00:06:01.19–00:09:31.31` foi omitido.

## Termos de `Gravando 2026-10-06 110907.mp4`

- **CDC / CQ:** siglas das áreas/sistemas citados na reunião; expansão e fronteira técnica não confirmadas (`00:00:08–00:00:11; 00:09:57–00:10:16`).
- **SIC jobs / linha de comando:** mecanismo descrito para agendar o plugin/remessa com parâmetros de data; tela e sintaxe não demonstradas (`00:02:47–00:03:23; 00:05:26–00:06:29`).
- **Itens 1.1 / 1.2 / 1.3:** numeração falada para configuração, remessa e consulta/relatório; validar na EF vigente (`00:01:34–00:03:34`).
- **Histórico financeiro / liquidação:** critérios citados para selecionar operações com seguro, sem definição completa de eventos (`00:10:47–00:12:15`).
- **Reenvio/reprocessamento:** repetir uma solicitação com erro, isolada ou em lote; controles, autorização e idempotência não descritos (`00:04:06–00:04:17; 00:16:29–00:17:25`).
- **`DTN`, “PT fim”, “Gearlog”; `CECOMP`, `TRDSP`, `PDT`, “CDCM”; `SRL`, `RPT`, `SIG`:** grafias/siglas reconhecidas pelo ASR que exigem validação; não são nomes de parâmetro, campo ou rotina confirmados (`00:01:17–00:01:22; 00:06:00–00:06:29; 00:07:32–00:07:57; 00:12:34–00:12:58; 00:14:11–00:14:42`).

Ver [`gravando-2026-10-06-110907/glossario.md`](gravando-2026-10-06-110907/glossario.md) e [`gravando-2026-10-06-110907/incertezas.md`](gravando-2026-10-06-110907/incertezas.md); sistema/projeto de referência foi mascarado e o trecho paralelo foi omitido.

## Termos de `Gravando 2026-09-23 164626.mp4`

- **GED / GEDOC / G-Doc / GDock:** grafias reconhecidas pelo ASR em contexto de consulta/anexação; relação e nomes oficiais precisam ser confirmados.
- **Autorizador:** aplicação citada como local da rotina de anexar documento à proposta; tela/caminho não verificados.
- **`document_type`, `document_name`, `user`:** três dados mencionados durante a discussão do JSON; nomes, tipos, obrigatoriedade e origem pendentes de confirmação na EF.
- **“Attach documento”:** possível nome do objeto pai no payload, ouvido pelo ASR; não padronizar frente a `attachment_document`/`attached_document` de gravações relacionadas.
- **`null`:** valor relatado para o caso sem documentos; contrato pode exigir outra representação.
- **Perfil GED / chave:** configuração de acesso mencionada em mensagens de erro; os valores ouvidos não definem permissão correta nem recomendam alteração.
- **Esteira / retorno / loop:** alternativas de fluxo ao reprocessar a proposta; regra de reentrada e idempotência pendentes.
- **CPS / CCD:** siglas reconhecidas ao falar de um tipo de documento; grafia e significado incertos.

Detalhes e timestamps em [`gravando-2026-09-23-164626/glossario.md`](gravando-2026-09-23-164626/glossario.md) e [`gravando-2026-09-23-164626/incertezas.md`](gravando-2026-09-23-164626/incertezas.md). A transcrição está integral conforme a diretriz de preservação registrada em [`PRIVACIDADE_E_RETENCAO.md`](PRIVACIDADE_E_RETENCAO.md) §13.

## Termos de `Como fazer EPT.mp4`

- **EPT / “IPT”:** plano/artefato de teste que descreve cenários, pré-condições, passos e resultados esperados; “IPT” pode ser erro ASR (`00:02:19`, `00:07:08`, `00:31:16`).
- **EF:** especificação funcional; fonte para objetivo, comportamento atual, requisitos, premissas e dependências (`00:02:19–00:02:48`, `00:27:40–00:30:21`).
- **Web API Consulta de Propostas detalhada:** endpoint verbalmente descrito com número de proposta/usuário como entradas e novos objetos na saída; rota e schema não conferidos (`00:02:48–00:06:18`).
- **Objeto `Despesa`:** objeto de retorno citado na EF/exemplo; campos não enumerados com clareza no ASR.
- **Objeto `Reaproveitamento`:** objeto relacionado ao reaproveitamento de seguro em refinanciamento; campos/regra devem vir da EF, não dos valores da aula.
- **Margem de tolerância:** exercício de recálculo com limites de valor solicitado no convênio e tolerância percentual; fórmula e limites não confirmados (`00:28:03–00:29:36`).
- **Caso / etapa:** organização da EPT em um caso com passos, com novo bloco ao iniciar caso distinto; convenção atual depende do template (`00:09:36–00:12:47`).
- **Pré-condição / premissa / resultado esperado:** itens do modelo de teste usados para descrever o estado necessário, suposições e resultado conforme a EF (`00:09:17–00:10:05`, `00:13:05–00:15:06`).
- **`Nexo`, `UTE`, `UTPT`:** grafias ASR sem definição; não as tratar como ferramentas/repositórios confirmados.

Detalhes em [`como-fazer-ept/glossario.md`](como-fazer-ept/glossario.md) e [`como-fazer-ept/incertezas.md`](como-fazer-ept/incertezas.md). Nenhum campo ou procedimento da gravação foi verificado visualmente.


## Termos de extração — `projeto EPT.mp4` (não validados)

- **ASR:** reconhecimento automático de fala; este passe `large-v3` sem VAD gerou 73 segmentos, mas a saída tem confiança insuficiente.
- **VAD:** detecção de atividade de voz; o README de origem diz que o passe com VAD reconheceu apenas um segmento.
- **“Legenda Adriana Zanotto”:** sequência repetida pelo ASR 69 vezes; não confirma nome, fala, crédito, legenda visível ou conteúdo do vídeo.
- **Cue SRT/VTT:** bloco temporizado; o cue final termina `13.28 s` depois da duração de áudio declarada.

Fonte: [`projeto-ept/glossario.md`](projeto-ept/glossario.md) e [`projeto-ept/metadados.md`](projeto-ept/metadados.md); pendente de revisão audiovisual.
