# Conflitos e validações pendentes

Atualizado em **2026-10-14**.

## Conflitos entre gravações

Nenhum conflito **de regras de negócio** entre gravações distintas foi identificado nos 7 vídeos concluídos até o momento. Foi registrado o primeiro conflito **de leitura de tela** entre gravações (ver §"Pendências de `Jonas EPT explicação.mp4`", item 1). Há duplicidade de **arquivo** confirmada no manifesto:

### Duplicidades confirmadas por objeto LFS (2026-10-13)

| Arquivos | Objeto LFS (oid, prefixo) | Evidência | Ação adotada |
|---|---|---|---|
| `Gravando 2026-08-24 124650.mp4` = `Gravando 2026-08-24 161729.mp4` | `1b9b6afd8564…` | Mesmo `oid` nos dois ponteiros versionados (`tools/checar_manifesto.py`) | Analisar uma única vez e apontar a segunda entrada para o mesmo material; o plano proíbe fundir gravações **diferentes**, não cópias byte-idênticas. |
| `Jonas EPT explicação.mp4` = `jonas2309.mp4` | `f99bd7955fbc…` | Mesmo `oid` nos dois ponteiros versionados | **Concluído (2026-10-13):** analisada como `Jonas EPT explicação.mp4` (`materiais/jonas-ept-explicacao/`); `jonas2309.mp4` marcada como concluída por referência no `STATUS.md` — bytes idênticos (SHA-256 `f99bd795…` conferido na coleta). |

Consequência para a contagem: 24 arquivos no manifesto correspondem a **22 conteúdos distintos**.

## Pendências técnicas e operacionais registradas por vídeo

1. **`Apresentação projeto 19-18.mp4`** (ver [`apresentacao-projeto-19-18/incertezas.md`](apresentacao-projeto-19-18/incertezas.md)):
   - **Parametrização/identificação do credor por operação (00:03:34 – 00:06:45):** ficou em aberto na reunião verificar no fonte/query (suspeita de convênio × informação da proposta).
   - **Conciliação de escopo de módulos (00:00:00 × 00:05:03):** item 1.3 cita **Web Autorizador**, item I cita **SIC Minutas do Autorizador** e a fala cita **API de formalização / jornada de contratação**.
   - **Distribuição de horas do plano de teste (00:07:32):** valores falados `"21, 3 e 16"` sem explicação da quebra.
2. **`Gravando 2026-07-07 155307.mp4`** (ver [`gravando-2026-07-07-155307/incertezas.md`](gravando-2026-07-07-155307/incertezas.md)):
   - **Procedimento técnico de "subir na base" e "mudar a pastinha" (00:01:18 – 00:01:24):** apenas mencionado verbalmente na ligação; deverá ser complementado quando demonstrado nos vídeos mais longos da fila.
   - **Sigla falada "IPT" × tag escrita `[EPT]` (00:00:01 – 00:00:51):** o ASR transcreveu "IPT", enquanto a tela mostra `[EPT]` no item `570023`.
3. **`Gravando 2026-10-07 152044.mp4`** (ver [`gravando-2026-10-07-152044/incertezas.md`](gravando-2026-10-07-152044/incertezas.md)):
   - **Erro de reconhecimento automático ("doutor Isabel" × "Autorizador", 00:01:31):** corrigido na transcrição limpa com base nas abas abertas do **Autorizador Web**.
   - **Continuação da consulta em `Política de Despesas e Tarifas` (00:03:41 – 00:04:10):** o vídeo encerra logo após o orientador indicar a consulta da política `98` em si.
4. **`Liberação padrão - Glauco.mp4`** (ver [`liberacao-padrao-glauco/incertezas.md`](liberacao-padrao-glauco/incertezas.md)):
   - **Divergência entre texto da planilha `Liberacao_Padrao_V30.xlsx` e instrução oral de Glauco (linha 86, 00:02:35 – 00:02:43):** a linha 86 da planilha diz apenas `"Criação de procedures: .NET - com a opção C, sem erros."`, mas Glauco alerta expressamente que esse texto está desatualizado e que é necessário também fazer/conferir se a opção **`W`** existe lá.

## Pendências de `Gravando 2026-09-22 111258.mp4` (2026-10-13)

Detalhes e evidências em [`gravando-2026-09-22-111258/incertezas.md`](gravando-2026-09-22-111258/incertezas.md).

1. **`document_type`: código × descrição (`00:04:02`–`00:05:08`):** a fala conclui "código", mas um participante lembra que a descrição foi pedida ao cliente. **Validar com o responsável pela RFP001 antes de implementar.**
2. **Campos já existentes na base (`00:03:10`–`00:03:29`):** afirmação falada sem conferência; a própria fala indica consulta ("vale consultar").
3. **Código do perfil no web service e no SIC (`00:05:13`–`00:05:46`):** risco de falha por configuração ausente; não há valor nem tela. **Não registrar valores.**
4. **Considerações e Anexo I da especificação:** lidos só em miniatura; **validar a página 3 completa e o anexo** no PDF `DS586780 (3)`.
5. **Demais páginas do PDF (41):** não analisadas nesta gravação (só páginas 2–3).

## Diretrizes já validadas pelo responsável

- **Dados de teste e nomes (resolvido em 2026-10-13):** o responsável confirmou que todos os dados exibidos nas gravações são fictícios/de teste e autorizou a publicação dos materiais derivados preservando o nome **Função Sistemas** e os **nomes dos operadores** (Jonas, William, Gabriel, Michelle, Felipe, Zé, Santana, etc.), mantendo a omissão de fotos/câmeras de pessoas.
- **Retenção de objetos no GitHub:** os ramos temporários de ponte são removidos imediatamente após a coleta; detalhes em [`PRIVACIDADE_E_RETENCAO.md`](PRIVACIDADE_E_RETENCAO.md).

## Pendências de `PROJETO 14-08.mp4` (2026-10-13)

- **Campo de origem do CNPJ (`ETRACPD.*`) desconhecido:** aguardar retorno do Zé e o complemento da EF (`00:01:27–00:03:00`).
- **Número do item 2:** fala oscila entre 556776/556576/55676; a tela confirma **OS 556576** — validar se existe OS 556776 distinta.
- **Gantt do pacote 4:** envio prometido para segunda-feira, com as horas do Gabriel (`00:08:47–00:09:21`) — conferir recebimento fora desta biblioteca.

## Pendências de `Jonas EPT explicação.mp4` (2026-10-13)

Detalhes e evidências em [`jonas-ept-explicacao/incertezas.md`](jonas-ept-explicacao/incertezas.md).

1. **Grafia do objeto do agrupamento: `attached_document` × `attachment_document` (conflito entre gravações).** A página de tabelas de layout da EF exibida nesta gravação (`00:04:20`) lê-se como **`attached_document`** ("Início do objeto attached_document"), enquanto a gravação `Gravando 2026-09-22 111258.mp4` registrou **`attachment_document`** (página 3 do mesmo PDF `DS586780`). Pode ser divergência real dentro da própria especificação ou erro de leitura em uma das gravações. **As duas formas permanecem registradas; não padronizar sem conferir o PDF.**
2. **Literais de número de proposta ilegíveis:** `CSNRPROP` na grade (`000033264` aproximado; leituras alternativas `000003264`/`800033264`) e filtros `8??83216?`/`8??8321??`/`8??83288?` no editor — não confirmados quadro a quadro; **não usar como referência numérica**.
3. **Finalidade das tabelas `CLOGREFIN`, `CLOGREFIND`, `EREAPSEG`, `CCOMP` (`FCSPROPEMPR`):** consultas preparadas no editor, sem execução ou explicação na gravação.
4. **Ajuste do número da proposta no envio ao sistema externo (`00:09:31`–`00:09:39`):** citado como "a única coisa que a gente tem que ajustar", sem detalhamento (EPT, relatório ou payload).

## Pendências de `Gravando 2026-07-08 182343.mp4` (2026-10-14)

Detalhes em [`gravando-2026-07-08-182343/incertezas.md`](gravando-2026-07-08-182343/incertezas.md).

1. **Exclusão de arquivos/configuração (`00:00:33` × `00:02:34`):** falas incompatíveis sobre preservar ou apagar `config`; mais adiante, o interlocutor recomenda backup (`00:03:09`–`00:03:24`). **Não executar exclusão** até confirmação por responsável técnico e runbook vigente.
2. **Matriz WebAutorizador/WS/API/SIC (`00:02:04`–`00:04:27`):** relação entre componentes e exceção de atualização não foram demonstradas; “AWS” pode ser reconhecimento incorreto. Confirmar nomes, dependências e versões.
3. **Opção “N” e erro genérico (`00:03:41`, `00:04:29`–`00:04:39`):** contexto e efeito não comprovados; não tratar como padrão seguro.
4. **Importação da esteira/teste de tolerância (`00:05:48`–`00:08:03`):** sistema, arquivo, destino, campos e critério de sucesso ausentes; números falados não devem ser reutilizados como regras.
5. **Cobertura:** o ASR termina em `00:08:20.29`; detector de silêncio a `-42 dB` aponta silêncio a partir de aproximadamente `00:08:28`, mas não houve escuta humana integral nem inspeção visual quadro a quadro. Manter estado `em revisão`.

## Pendências de `MICHELLE CTC PORTABILIDADE REFIN.mp4` (2026-10-14)

Detalhes e timestamps em [`michelle-ctc-portabilidade-refin/incertezas.md`](michelle-ctc-portabilidade-refin/incertezas.md).

1. **Diagrama de outro cliente:** não é especificação do alvo C6; obter e validar a configuração vigente antes de reutilizar qualquer etapa.
2. **Esteiras dependentes ou independentes:** a conversa oscila entre avanço coordenado/aguarda validação do refim e avanço independente; definir com negócio os status e condições de bloqueio/liberação.
3. **Nomes e sequência das etapas:** “CTC aciona refim”, “aguarda alteração unificada” e “aguarda análise de refim de portabilidade” são rótulos aproximados/alternativos, sem confirmação em tela.
4. **Criação e vínculo de propostas:** esclarecer se o cenário gera automaticamente duas propostas, como tratar múltiplas portabilidades e quais produtos/convênios/esteiras são aplicáveis.
5. **Limite do teste CTC:** sugestão de pular CTC decorre de indisponibilidade durante aquela discussão; não é autorização para contornar integração/controles em produção.
6. **Cobertura da fonte:** 388 segmentos ASR; mídia, tela e desenho não foram revisados visualmente nesta etapa. Manter estado **em revisão** até conferência humana e validação técnica.

## Pendências de `MCB - QISTA.mp4` (2026-10-14)

Detalhes e timestamps em [`mcb-qista/incertezas.md`](mcb-qista/incertezas.md).

1. **Pontuação/certificação:** escala, limite, estados e suspensão são falas ASR, não regra técnica ou de negócio verificada.
2. **Consulta MCB:** confirmar atividade de esteira, vínculo de configuração, versão/contrato da API, resposta e efeito na proposta. URL/segredos ausentes e não devem ser inferidos.
3. **Promotora interna/externa:** comportamento de validação apenas sugerido; obter critério oficial e resultados esperados.
4. **Nomes e códigos:** “T-Lib”/“Telib”, “TEORGS”, “Origem 3”, QISTA e códigos `190`/`061` precisam de conferência; não usar como parâmetro.
5. **Erro “produto não encontrado”:** menção a três tabelas correlacionadas sem identificação, causa ou consulta. Não realizar alteração de base.
6. **Cobertura:** transcrição `large-v3` com 199 segmentos; vídeo/telas não foram revisados visualmente nem escutados nesta etapa. Manter estado **em revisão**.

## Pendências de `Primeiro projeto.mp4` (2026-10-14)

Detalhes e timestamps em [`primeiro-projeto/incertezas.md`](primeiro-projeto/incertezas.md).

1. **Parâmetros proposta/operação:** confirmar se basta um, se ambos são aceitos, precedência para vínculos divergentes e erro quando nenhum é informado.
2. **GED/back-office:** validar a resolução interna operação→proposta e comportamento quando o vínculo não existir; confirmar perfil/chave GED.
3. **Retorno/checklist/download:** confirmar nomes dos campos e se o endpoint simplificado exclui todo o checklist; identificar se o download usa outro endpoint ou parâmetro.
4. **Ambiente/evidência:** versões aprovadas e opções “N/W” não foram definidas; não transformar recomendação oral em procedimento de implantação.
5. **SQL:** somente um `SELECT` é mencionado, sem texto/tabelas; nenhuma consulta é reproduzida ou autorizada por esta gravação.
6. **Sanitização/cobertura:** identificador de cliente e nome de base foram substituídos por marcadores; segmento não técnico entre `00:16:15.94–00:17:48.66` foi omitido. Fonte, EF e telas não foram revisadas neste lote; manter **em revisão**.

## Pendências de `Gravando 2026-08-24 124650.mp4` (2026-10-14)

Detalhes e timestamps em [`gravando-2026-08-24-124650/incertezas.md`](gravando-2026-08-24-124650/incertezas.md).

1. **Contrato do plugin/JSON:** a alteração e a propriedade esperada do retorno não são nomeadas; confirmar na EF/EPT aprovada.
2. **Etapas da esteira:** o ASR oscila entre etapa 2, 3 e 4 (`00:10:12–00:12:23`); usar sequência autorizada, não inferência oral.
3. **CPD/Crivo e ferramenta:** grafias/funções de CPD, Crivo, Geradoc e limite de envio precisam de confirmação; o limite citado não é política.
4. **Dados de teste:** identificadores e valor exemplificativo foram substituídos por marcadores; não os reutilizar como valores nem requisitos.
5. **Sanitização:** o intervalo `00:06:01.19–00:09:31.31` foi omitido por privacidade/segurança; nenhuma consulta SQL ou dado de identificador foi transferido para o derivado público.
6. **Cobertura:** ASR `large-v3` com 352 segmentos, áudio declarado `00:18:45.82`; vídeo/telas não foram revisados neste lote. Não houve teste, execução SQL ou captura. Manter estado **em revisão**.
7. **Duplicidade:** `Gravando 2026-08-24 161729.mp4` tem o mesmo OID LFS e fica coberto por referência; não criar uma segunda análise.
