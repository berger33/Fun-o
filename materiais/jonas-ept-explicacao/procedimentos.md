# Procedimentos — Jonas EPT explicação.mp4

Passos observados na gravação, organizados como roteiro reaproveitável. Dados de teste e caminhos internos mascarados. Timestamps `HH:MM:SS` apontam o momento em que cada passo é demonstrado.

## 1. Rastrear a execução do "Serviço de Envio da Proposta ao Sistema Externo" no banco

1. Conectar o SSMS ao banco **`FCSMONITOREMPR`** do ambiente de CQ (**[00:00:00]**).
2. Executar a consulta de eventos por **nome do serviço** (junção `ECONSULT` × `TBPERFCON`), ordenada do mais recente para o mais antigo (**[00:02:50]–[00:03:40]**):

   ```sql
   SELECT TOP 100? PRDESCPFCON, CSVERPLUG, CSNRPROP, CSSERVER, CSRETTEXT, CSERRO, CSDTHRAGEN, CSSTATUS, *
   FROM FCSMONITOREMPR..ECONSULT(NOLOCK)
   INNER JOIN FCSMONITOREMPR..TBPERFCON ON CSIDPFCON = PRIDPFCON
   WHERE PRDESCPFCON LIKE ('%Servico de Envio da Proposta ao Sistema Externo%')
   ORDER BY CSIDCONS DESC
   ```

   - Filtrar por `PRDESCPFCON` (descrição do serviço) é o caminho quando não se quer filtrar por número de proposta; o filtro antigo por `CSNRPROP` fica comentado no editor (**[00:03:00]**).
   - Colunas úteis da grade: `PRDESCPFCON` (serviço), `CSNRPROP` (proposta), `CSSERVER`, `CSRETTEXT` (retorno), `CSDTHRAGEN`/`CSDTHRSOL` (data/hora agendamento/solicitação), `CSSTATUS` (`P`/`C`), `CSIDCONS` (id do evento), `CSIDPFCON` (perfil), `CSUSUARIO`, `CSNREXTERNO` (número externo/token).
3. Localizar a linha do serviço e **anotar o `CSIDCONS`** (na demonstração, `84942` — **[00:03:14]** "o ID cons desse cara").
4. Consultar o **detalhe do evento** em `ECONSULTD` pelo id (**[00:03:11]–[00:03:42]**):

   ```sql
   SELECT * FROM ECONSULTD WHERE CDIDCONS='84942'
   ```

   - `ECONSULTD` é chave-valor: `CDIDCONS` (id da consulta), `CDCONTROLE` (sequencial), `CDCAMPO` (campo) + coluna de conteúdo (ex. de campos visíveis: `DATAPREV_CNPJEMPR`, `DATAPREV_CODCATEG`, `DATAPREV_CODCBO`, `DATAPREV_CODCNAE`, `DATAPREV_DESCCBO`, `DATAPREV_DESCCNAE`) (**[00:05:40]**).
   - É onde fica o **JSON do payload** enviado ao sistema externo ("o JSON… aquilo que eu entendi vai estar aqui", **[00:03:32]–[00:03:37]**). Copiar o conteúdo e colar num editor de texto (Notepad++) para examinar (**[00:04:30]**).
5. Se necessário, o editor mantém consultas prontas no banco **`FCSPROPEMPR`** para complementar a investigação (**[00:00:00]**; sem execução demonstrada): `SELECT * FROM CLOGREFIN`; `SELECT * FROM CLOGREFIND`; `SELECT * FROM EREAPSEG WHERE EPRNRPROP='…'`; `SELECT * FROM CCOMP WHERE CSNRPROP=…` — finalidades não explicadas na gravação.

## 2. Confirmar os dados da proposta no Autorizador Web

1. Abrir a **Proposta Sintetizada** da proposta de teste (menu `Cadastro/Proposta`; a URL carrega `Origem3=001010`) e conferir os **Dados da Operação** — na demonstração: Valor Cliente 2.000,00, Valor Parcela 89,47, Valor Financiado 2.078,59 (**[00:01:50]–[00:02:20]**).
2. A tela `Aprovação/Consulta` lista o evento do serviço externo para a proposta (linha `ENVIA SIST EXT`) (**[00:02:40]**).
3. O payload copiado do banco deve **conferir** com esses valores (no vídeo: `contract_amount 2078.59`, `contract_parcel_amount 89.47`, `contract_net_amount 2000.0`, `contract_parcel_quantity 30`) (**[00:04:30]–[00:05:20]**).

## 3. Posicionar o novo agrupamento no payload (item OS 586780)

1. Abrir a **Especificação Funcional** (`DS586780.PDF`, 41 páginas) na página de tabelas de layout e localizar o bloco "**Início do objeto `attached_document`**" com os campos `document_type` (Tipo do documento) e `document_name` (Nome do documento) — gravação também mostra páginas de campos de endereço do cliente e de **corban** (`phone` "Telefone Corban" ≤9 caracteres, `phone_area_code` "DDD Corban" ≤3, origem "De acordo com o cadastro da Origem 3 da proposta") (**[00:04:10]–[00:05:30]**).
2. No payload JSON, o agrupamento entra **dentro do objeto `client`** ("acima de client / ele vai estar / em client… então ele entraria aqui, nessas novas informações") (**[00:04:33]–[00:05:23]**).
3. Conferir que as demais estruturas não mudam: o cenário de teste cita `corbanData`, `Credor associatedProposals`, `last_ConsultINSS` e `Insurance_reuse` (**[00:09:20]**).

## 4. Preencher a EPT (planilha de casos de teste)

1. Abrir a planilha **`EPT_586780`** (Excel, Modo de Compatibilidade) na pasta compartilhada da equipe (`Mesa_C6`) (**[00:05:50]**).
2. No cabeçalho da primeira linha do caso, preencher: **número do projeto**, **item da EF** e **Etapa** — a etapa "pode ser bem genérica" (**[00:05:52]–[00:06:11]**).
3. Usar a linha de caso **001.1** já redigida: "Implementar no módulo 'ServCon', no serviço (plugin) 'Envio da Proposta ao Sistema Externo', novo agrupamento responsável por identificar documentação anexa para compor as informações do cliente" (**[00:06:00]**).
4. Nas pré-condições, registrar direitos de acesso no módulo Web Autorizador e, em `Versões`, comparar a versão entregue na ficha da rotina (**[00:08:10]**).
5. Para as etapas que envolvem anexo de documento, usar a rotina **"Anexar/Consultar Documentação" do Autorizador** ("eu posso no autorizador no anexar documento", **[00:07:54]**; rotina detalhada na gravação `Gravando 2026-09-22 111258`).

## 5. Acrescentar cenário de teste a partir do Relatório de Testes

1. Na "pasta doc" do compartilhamento (`Mesa_C6`), abrir **`Relatorio_de_Testes_586780`** (Word) — junto dele está o PDF `D586780` da EF (**[00:08:27]–[00:08:30]**).
2. Ler o documento e **acrescentar à EPT** o cenário válido para o teste ("dá uma lida, e acrescenta esse cenário… primeiro ponto, acrescenta esse cenário") (**[00:08:32]–[00:08:38]**).
3. Cenários disponíveis no relatório (**[00:09:00]–[00:09:30]**):
   - **Importação:** proposta do módulo ServCon enviada pelo fluxo `/proposal/import` com ao menos um documento anexado no checklist;
   - **Atualização:** proposta já existente atualizada pelo fluxo `/proposal/update` com documento anexado (prioridade alta; proposta com exatamente um anexo; usuário autenticado com privilégios compatíveis com os direitos de origem).
4. Executar pelos **8 passos** do relatório (garantir proposta; garantir anexo; acionar endpoint; capturar requisição do plugin; validar agrupamento em `Client`; conferir campos do documento e usuário; checar regressão dos demais blocos; validar resposta HTTP) e conferir o **resultado esperado**: `200 OK` com `success=true`, `type=ok`, `message=proposal imported`; em falha de validação, `400 BadRequest`/`409 Conflict` (**[00:09:20]**).
5. Ajuste pendente apontado na fala: a parte do **número da proposta** no envio ao sistema externo ("a única coisa que a gente tem que ajustar é aquela parte do… número da proposta… mandar ela pro sistema externo", **[00:09:31]–[00:09:39]** — ajuste exato não detalhado; ver [`incertezas.md`](incertezas.md) item 10).
6. Ao final, o responsável manda a planilha/documento ao colega ("aqui eu vou mandar pra você", **[00:09:42]**).

## 6. Referência cruzada

- Especificação da OS 586780 e rotina de anexar documento: [`../gravando-2026-09-22-111258/procedimentos.md`](../gravando-2026-09-22-111258/procedimentos.md).
- Consulta `ECONSULT` por número de proposta (mesma tabela, outro filtro): [`../gravando-2026-10-07-152044/procedimentos.md`](../gravando-2026-10-07-152044/procedimentos.md).
- Compartilhamentos de rede da equipe (`Mesa_C6`, UDL Base): [`../gravando-2026-07-07-155307/procedimentos.md`](../gravando-2026-07-07-155307/procedimentos.md).
