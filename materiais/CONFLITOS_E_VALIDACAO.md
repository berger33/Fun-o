# Conflitos e validações pendentes

Atualizado em **2026-10-16**.

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

## Pendências de `Gravando 2026-07-08 182343.mp4` — atualizadas em 2026-10-16 (fonte primária verificada)

Detalhes e evidências em [`gravando-2026-07-08-182343/incertezas.md`](gravando-2026-07-08-182343/incertezas.md) e [`gravando-2026-07-08-182343/capturas.md`](gravando-2026-07-08-182343/capturas.md).

1. **Exclusão × preservação da configuração (RESOLVIDO no material / PENDENTE de validação técnica):** as falas de `00:00:33` (“apagar tudo, menos a config”) e `00:02:34` (“apaga config”) colidem com a recomendação de backup de `00:03:09`–`00:03:24`. O material marca o fluxo como **bloqueado**; a rotina vigente precisa ser confirmada pelo responsável técnico.
2. **Matriz de atualização de componentes (PENDENTE):** `00:04:03`–`00:04:27` distingue casos (API × autorizador × “caso do SIC”) e cita que “o AWS não atualiza”. A sigla pode ser o próprio WS ou erro de reconhecimento. **Não usar como matriz de implantação.**
3. **Desfecho do incidente de tolerância (PENDENTE):** a gravação mostra a regra da EF (0–99, opcional, 2 casas decimais), a evidência de tela com `100,00` e o encaminhamento a “Michelle de negócios” (`00:07:40`), mas **não** mostra correção, reprovação ou encerramento. Confirmar o estado atual do ajuste antes de tratar como resolvido.
4. **Erro durante a cópia de arquivos (PENDENTE):** as mensagens em vermelho de `00:03:40`–`00:05:05` não são legíveis nos quadros amostrados e a avaliação “é um erro genérico, não interfere em nada” (`00:04:29`–`00:04:39`) é apenas fala, sem diagnóstico.
5. **Validação do resultado da importação (PENDENTE):** a única evidência de sucesso é a mensagem “As informações foram salvas” (`00:07:20`–`00:07:25`). Não houve reexportação, vinculação a proposta ou teste funcional do modelo `9999` (`teste_tolerancia`).
6. **Escuta humana da transcrição (PENDENTE):** a cobertura foi validada tecnicamente (nenhum trecho audível acima de `-50 dB` sem segmento de ASR; silêncio digital confirmado a partir de `00:08:28`), mas não houve escuta integral nem revisão do chat dos primeiros segundos.

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

## Pendências de `Gravando 2026-10-06 110907.mp4` (2026-10-15)

Detalhes e timestamps em [`gravando-2026-10-06-110907/incertezas.md`](gravando-2026-10-06-110907/incertezas.md).

1. **Regra do produto:** confirmar eventos elegíveis para cancelamento (liquidação/quitação/refinanciamento/estorno/cancelamento) e a razão transmitida; a fala é hesitante.
2. **Origem da despesa de seguro na operação:** não identificada. Nomes `CECOMP`, `TRDSP`, `PDT` e “CDCM” são candidatos ASR incertos; não construir consulta/rotina a partir deles.
3. **Sistema e integração:** confirmar CDC/CQ/SIC, fronteira com Autorizador, nome do plugin/serviço e contrato externo. URL, segredo e proxy foram apenas citados; não há valores publicados.
4. **Datas e parâmetros:** confirmar sintaxe/semântica de `DTN`, “PT fim”, “Gearlog”, limites do período e calendário de dia útil.
5. **Reenvio e consistência:** definir retry, idempotência, auditoria e proteção contra duplicação, sobretudo para seleção em lote.
6. **Relatório:** resolver campos, filtros, formato (fala oscila entre `RPT`/`SIG`) e padrão de emissão.
7. **Estado da entrega:** comitê, horas, urgência e release descritos são históricos e não representam aprovação/prazo atual.
8. **Privacidade/cobertura:** sistema/projeto de referência em `00:18:23.90–00:18:27.28` foi substituído; conversa paralela sobre incidente em `00:23:04.06–00:23:47.48` foi omitida. ASR 683 segmentos; MP4/EF/telas não foram revisados, e não houve teste/SQL. Manter **em revisão**.

## Pendências de `Gravando 2026-09-23 164626.mp4` (2026-10-15)

Detalhes em [`gravando-2026-09-23-164626/incertezas.md`](gravando-2026-09-23-164626/incertezas.md).

1. **Nomenclatura do objeto JSON:** “Attach documento” no ASR × `attachment_document` × `attached_document` em gravações relacionadas. Confirmar a EF/schema vigente; não escolher por inferência.
2. **Campos e contrato:** tipo, nome e usuário são citados, mas grafia, tipo de dado, origem, obrigatoriedade, nulabilidade e multiplicidade não foram validados.
3. **Sem anexos:** relato de saída `null`; confirmar se o contrato exige `null`, lista vazia ou ausência do campo.
4. **Múltiplos anexos:** fala relata dois itens no JSON após retornar/reexecutar. Confirmar persistência, ordem, duplicação e aceite em teste autorizado.
5. **Perfil GED:** mensagens envolvendo perfil/chaves e um ajuste subsequente foram reconhecidas pelo ASR, sem revisão visual; não converter números ou mudanças relatadas em configuração operacional.
6. **Retorno versus loop:** conversa não fecha o fluxo de reentrada, retry ou idempotência.
7. **Cobertura:** 396 segmentos; último cue `00:26:14.39`, áudio `00:33:59.98`, com aproximadamente `00:07:45.59` sem transcrição no final e outros intervalos sem segmentos. Revisão humana integral pendente; manter **em revisão**.
8. **Fonte primária:** o MP4 não foi baixado nem inspecionado visualmente neste lote; relatos de anexação e sucesso não foram confirmados contra tela/JSON.

## Pendências de `Como fazer EPT.mp4` (2026-10-15)

Detalhes em [`como-fazer-ept/incertezas.md`](como-fazer-ept/incertezas.md).

1. **Exemplo × exercício:** o início demonstra uma EPT/API com objetos de despesa e reaproveitamento; o final apresenta um exercício sobre recálculo/margem de tolerância. Confirmar se são projetos/EFs distintos.
2. **Template:** a fala diz que o modelo tem seis colunas, mas a enumeração não é clara. Conferir cabeçalhos oficiais, numeração de casos/etapas e regras de pré/pós-condição.
3. **API:** conferir nome/rota, parâmetros, objetos/campos/tipos/nulabilidade e cenários sem dados na EF e documentação vigentes.
4. **Reaproveitamento:** regra geral é explicada verbalmente para refinanciamento; valores numéricos são didáticos, não requisito nem massa aprovada.
5. **Margem de tolerância:** fórmula, valores mínimo/máximo, tolerância percentual, arredondamento, fronteiras, precedência e estados sem configuração não definidos.
6. **Dependência/identificador:** implementação anterior é descrita como requisito; ID ouvido pelo ASR precisa de validação antes de ser usado para localizar projeto.
7. **Demonstração da EPT:** o próprio interlocutor critica o exemplo mostrado. Não copiar seus passos sem confronto com o template e a EF atuais.
8. **Cobertura:** áudio `00:35:47.18`, último cue `00:35:43.14`, duração ASR declarada `1651.5 s`; existem intervalos sem segmentos. MP4/telas não revistos; manter **em revisão**.


## Pendências de `projeto EPT.mp4` (2026-10-15)

Detalhes em [`projeto-ept/incertezas.md`](projeto-ept/incertezas.md).

1. **Validade do ASR:** 69 dos 73 segmentos repetem “Legenda Adriana Zanotto”; revisar contra áudio antes de tratar qualquer trecho como fala ou legenda.
2. **Passes divergentes:** a referência diz que a passagem com VAD reconheceu 1 segmento e a passagem sem VAD 73. Recuperar/comparar o primeiro artefato e confirmar qual configuração, se alguma, representa a fonte.
3. **Cobertura:** MP4 não foi ouvido/visto; não declarar que o vídeo está silencioso nem que seu tema é EPT.
4. **Temporização:** duração `00:36:16.70`, cue final `00:36:29.98` (13.28 s além); `duracao_transcricao_s: 788.8` não está definido.
5. **Identidade/legenda:** nome e frase retornados pelo ASR não estão confirmados; não inferir crédito visual ou identidade pessoal.
6. **Conteúdo técnico:** nenhum sistema, processo, requisito, SQL ou procedimento pode ser extraído com segurança desta saída; não concluir até revisão humana/audiovisual.


## Pendências de `ClientSecret EWEN TREINAMENTO.mp4` (2026-10-15)

Detalhes em [`clientsecret-ewen-treinamento/incertezas.md`](clientsecret-ewen-treinamento/incertezas.md).

1. **Credencial/expiração:** fala sugere prazo longo para Client Secret; validar política vigente, menor duração, rotação, escopo, revogação e cofre seguro. Não adotar instrução oral como padrão.
2. **Privilégio:** `Supervisor` é usado no relato; confirmar necessidade, aprovação e alternativa de menor privilégio antes de conceder acesso.
3. **Client ID e terminologia:** valores lidos pelo ASR divergem em `00:15:09` e `00:21:12`; `Client Secret`/`CloudSecret` alternam. Não reutilizar valor nem grafia sem fonte autorizada.
4. **Teste de API:** produto, URL, ambiente, endpoint, método e payload não foram conferidos; resultado do teste não é demonstrado de forma verificável.
5. **Licença:** arquivo, versões, API/métodos, origem, integridade e autorização/“contrassenha” carecem de confirmação. A própria fala corrige números e uma alteração anterior de licença teria causado erro de token.
6. **Direitos por rotina:** sequência e opções `A`/`M` dependem da versão; validar com a matriz e o runbook atual. Nenhuma mudança foi executada.
7. **CTC/CIP:** menção é introdutória; o interlocutor diz que testou pouco. Obter EF/fluxo oficial antes de elaborar cenários.
8. **Cobertura/privacidade:** ASR sem VAD (649 segmentos), sem revisão audiovisual. TXT/SRT/VTT não incluem valor literal reconhecível de segredo, mas não permitem afirmar o que aparece nas telas. A transcrição integral preserva conversa pessoal, inclusive autodeclaração de saúde, conforme instrução registrada na nota de privacidade §13.


## Pendências de `explicacao mesa c6.mp4` (2026-10-15)

Detalhes em [`explicacao-mesa-c6/incertezas.md`](explicacao-mesa-c6/incertezas.md).

1. **Configuração de pastas:** a fala diz apagar tudo exceto `config`, depois preservar a pasta, e alterna entre alterar/excluir; bloquear qualquer implantação sem runbook versionado, inventário do ambiente, backup e rollback.
2. **Máquina/base/UDL:** há bases local e de servidor com caminhos/login distintos e mais de um teste concorrente. Host, proprietário, UDL, credenciais e destino não foram confirmados; não utilizar os rótulos ASR como conexão.
3. **EPT/EF:** validar o exemplo de recálculo, os processos citados, o parâmetro, fórmula/limites, template e critérios de aceite na EF vigente. Não presumir que o exemplo descrito seja regra atual.
4. **Treinamento/fluxo de teste:** sequência de produto, convênio, esteira, proposta, API e ordem simulação/inclusão precisa ser conferida com material oficial; nenhum teste ocorreu.
5. **Evidências:** esclarecer política de prints, timestamp, armazenamento/compartilhamento, dados permitidos e aprovação antes de qualquer publicação.
6. **ASR:** saída sem VAD contém quatro cues “Legenda Adriana Zanotto” (`00:13:10–00:14:40`) e grafias incertas; verificar na fonte, ainda não revisada.
7. **Cobertura:** áudio `00:57:41.57`, último cue `00:57:29.58`; outros intervalos não reconhecidos e `duracao_transcricao_s: 2802.8` sem definição. Não inferir silêncio.
8. **Privacidade e acesso:** há nomes internos, rótulos de máquina/pasta e menção genérica a login/senha; nenhum valor literal de credencial foi reconhecido no ASR. Como vídeo/telas não foram revisados, informação visual adicional continua desconhecida. Transcrição mantida conforme §13.
9. **SQL:** não há consulta literal reconhecida; menção a tabela/C-Oper não basta para criar ou executar query.

## Pendências de `recalculo.mp4` (2026-10-15)

Detalhes e timestamps em [`recalculo/incertezas.md`](recalculo/incertezas.md).

1. **Fórmula de tolerância:** exemplos com limites 1.000/3.000, valores 2.990/2.995 e percentuais 1%/10% não definem uma única regra. Confirmar base, direção, simetria, inclusividade e arredondamento na EF.
2. **Modo de atividade:** “somente recálculo” e “ambos” são comparados, mas o comportamento esperado e a diferença entre rotas não estão definidos.
3. **Resultados incompatíveis:** o ASR registra tentativas descritas como falha e, mais tarde, uma como bem-sucedida; entradas, configuração, versão e estado final não podem ser reconciliados sem fonte/evidência.
4. **Versão/ambiente:** versões antigas/novas, máquinas/servidores e bases são citados sem identificação confirmada. Não trocar versão, arquivo, servidor, configuração ou base sem runbook, autorização e rollback.
5. **Cobertura:** 1.043 segmentos ASR sem VAD; trechos não técnicos/aparente áudio de fundo e último cue `01:11:18.540`, 27,72 s além do áudio declarado `01:10:50.82`. Rever MP4/áudio integralmente.
6. **Escopo da análise:** vídeo/telas não inspecionados; nenhuma API, SQL, configuração, massa, proposta ou ambiente foi testado/alterado.

## Pendências de `dESAVERBAÇÃO.mp4` (2026-10-15)

Detalhes e timestamps em [`desaverbacao/incertezas.md`](desaverbacao/incertezas.md).

1. **Fonte primária:** objeto LFS reconhecido, mas `git-lfs` ausente e sondas ao host de conteúdo falharam; não houve download, reconstrução ou revisão audiovisual nesta sessão. O registro de execução anterior informa que o runner validou as duas partes e o original; não foi refeito aqui.
2. **Cobertura ASR:** 1.274 segmentos `large-v3`, sem VAD, sem revisão humana; último cue `01:13:37.080–01:14:07.060` excede o áudio declarado `01:13:40.67` em 26,39 s. `duracao_transcricao_s: 2678.2` não está definido.
3. **Estados e causa:** confirmar relação entre proposta averbada, cancelamento, exclusão de averbação e estado “desaverbado”; a falha inicial de elegibilidade e a descrição dos plugins não demonstram causa (`00:00:34–00:00:45`; `00:15:05–00:17:18`).
4. **Configuração/esteira:** modo manual/automático, stub, vínculo de empregador, tipos `A/N/F/P` (sem significado definido para `N`), processo `99`, alçada/fase e relação modelo/produto dependem de EF/runbook e versão; não copiar nem alterar (`00:01:36–00:05:10`; `00:29:20–00:44:01`).
5. **Consulta e retorno:** menção a SQL sem query literal (`00:24:47–00:25:44`); código “BF”/“competência”, versão e resultado final não verificados (`00:18:06–00:23:39`; `01:05:15–01:06:33`). Nenhum SQL foi executado.
6. **Ambiente e margem:** mock, massa sintética, limites de WebTabelas e qualquer integração externa precisam de validação; a fala não autoriza Dataprev/cliente/produção (`00:44:32–00:48:10`).
7. **Evidência visual:** ASR menciona um print, mas nenhuma captura foi obtida ou revisada nesta sessão. Manter **em revisão** até revisão humana/audiovisual, validação do fluxo e resolução das incertezas.
