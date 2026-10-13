> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Jonas, William, Lucas). Não são publicadas **imagens de pessoas**
> (avatares/fotos de perfil), URLs de sessão, caminhos de rede/usuário nem campos de
> CPF/CNPJ/telefone/e-mail de teste (identificados como `[DADO PESSOAL OMITIDO]` quando citados).

# Glossário — Jonas EPT explicação.mp4

- **`attached_document` (bloco da EF)** — objeto do payload do envio ao sistema externo para o
  agrupamento de documentos anexados, mostrado na página de tabelas de layout da Especificação
  Funcional da OS 586780 com os campos `document_type` ("Tipo do documento") e `document_name`
  ("Nome do documento") (**[00:04:20]**). *Conflito de leitura* com a gravação anterior, que
  registrou `attachment_document` (ver [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md)).
- **Autorizador Web (`WebAutorizador`)** — sistema web (`C6/WebSite/WebAutorizador`) usado na
  demonstração nas telas `Cadastro de Decisão` (`UI.CD.Deci.aspx`), `Proposta Sintetizada`
  (`UI.PropostaSintetizada.aspx`), `ESCOLHAPCS` e `Aprovação/Consulta`
  (`UI.AprovacaoConsultaAnd.aspx`) (**[00:00:10 – 00:02:40]**).
- **`CCOMP` (`FCSPROPEMPR..CCOMP`)** — tabela do banco `FCSPROPEMPR` citada em consulta preparada
  no SSMS (`SELECT * FROM CCOMP WHERE CSNRPROP=…`), sem execução nem explicação na gravação
  (**[00:00:00]**).
- **`CLOGREFIN` / `CLOGREFIND` (`FCSPROPEMPR`)** — tabelas citadas em consultas preparadas
  (`SELECT * FROM CLOGREFIN` / `SELECT * FROM CLOGREFIND`), sem execução nem explicação
  (**[00:00:00]**); os nomes sugerem log de refinanciamento (não confirmado).
- **`corban_data` (objeto do payload)** — dados da promotora/correspondente bancário no JSON do
  envio: `id` (`"001010"` — a mesma "Origem 3" da URL da Proposta Sintetizada), `company_name`,
  `fancy_name`, `document`, endereço (**[00:04:30 – 00:05:20]**); a EF traz os campos `phone`
  ("Telefone Corban", ≤9 caracteres) e `phone_area_code` ("DDD Corban", ≤3) "de acordo com o
  cadastro da Origem 3 da proposta" (**[00:05:00]**).
- **`client` (objeto do payload)** — bloco do JSON com os dados do cliente (`id`,
  `tax_identifier`, `name`, `verification_code`, `pensioner_enrollment`, `enrollment`,
  `mother_name`, contato, nascimento, documentos e endereço). O novo agrupamento de documentos
  anexados entra **dentro dele** ("ele vai estar em client") (**[00:04:33 – 00:05:23]**).
- **EPT (planilha `EPT_586780`)** — documento de casos de teste do CQ em Excel (Modo de
  Compatibilidade), com seções "Premissas Gerais"/"Validações Básicas" e tabela de casos
  (`CT | Ref. | Descrição | Etapa | … | Resultado esperado | Status | Observações`) (**[00:05:50 – 00:08:10]**).
- **`EREAPSEG` (`FCSPROPEMPR..EREAPSEG`)** — tabela citada em consulta preparada
  (`SELECT * FROM EREAPSEG WHERE EPRNRPROP='…'`), sem execução nem explicação (**[00:00:00]**); o
  nome sugere reaproveitamento de seguro (não confirmado na gravação).
- **`ECONSULT` (`FCSMONITOREMPR..ECONSULT`)** — tabela de eventos/consultas de execução de
  serviços e plugins do monitor, consultada via SSMS filtrando pela descrição do serviço
  (`PRDESCPFCON`) e ordenando por `CSIDCONS DESC`; fornece proposta (`CSNRPROP`), servidor
  (`CSSERVER`), retorno (`CSRETTEXT`), datas (`CSDTHRAGEN`/`CSDTHRSOL`), status (`CSSTATUS`),
  usuário (`CSUSUARIO`) e número externo (`CSNREXTERNO`) (**[00:02:50 – 00:03:40]**).
- **`ECONSULTD` (`FCSMONITOREMPR..ECONSULTD`)** — tabela de **detalhe** da consulta em formato
  chave-valor (`CDIDCONS`, `CDCONTROLE`, `CDCAMPO` + coluna de conteúdo), consultada com o
  `CSIDCONS` do evento (ex.: `84942`) para obter o conteúdo enviado — inclusive o **JSON do
  payload** do envio ao sistema externo (**[00:03:11 – 00:03:42]**).
- **Especificação Funcional (EF, `DS586780.PDF`)** — documento de 41 páginas da OS 586780
  "[ÁGIL] (I) Nova Flag informativa de Docs anexados no SrvEnvioPropExt" com necessidade,
  solução proposta (item 001.1) e tabelas de layout do payload (endereço do cliente,
  `attached_document`, corban) (**[00:04:10 – 00:05:30]**).
- **Endpoints `/proposal/import` e `/proposal/update`** — fluxos da integração com o sistema
  externo citados nos cenários de teste: importação de proposta nova e atualização de proposta
  existente, ambos com documento anexado no checklist (**[00:09:00 – 00:09:30]**).
- **OS 586780 (`[ÁGIL] (I) Nova Flag informativa de Docs anexados no SrvEnvioPropExt`)** — ordem
  de serviço do item em desenvolvimento, mesma da gravação `Gravando 2026-09-22 111258`; a
  "flag informativa" corresponde ao novo agrupamento de documentos anexados no payload do
  serviço `SrvEnvioPropExt` (**[00:04:10]**).
- **Relatório de Testes (`Relatorio_de_Testes_586780`)** — documento Word no padrão "CQ -
  Controle de Qualidade / Evidências de Testes / Função Sistemas", com os cenários 001.1 de
  importação e atualização (prioridade alta), parâmetros, 8 passos e resultado esperado, usado
  como fonte para acrescentar cenários à EPT (**[00:08:27 – 00:09:30]**).
- **`ServCon` (módulo) / `SrvEnvioPropExt` (plugin)** — módulo e serviço ("Envio da Proposta ao
  Sistema Externo") onde o item 001.1 implementa o novo agrupamento, conforme a EF e a linha
  001.1 da EPT (**[00:06:00]**); o registro de execução aparece em `ECONSULT` como
  "Serviço de Envio de Proposta ao Sistema Externo" (**[00:02:50]**).
- **`SrvTok…` (`CSNREXTERNO`)** — tokens de retorno de plugins exibidos na grade `ECONSULT`
  (ex.: `SrvTok…` do `Plugin CPO - Token`), omitidos nos derivados (**[00:00:00]**).
- **`TBPERFCON` (`FCSMONITOREMPR..TBPERFCON`)** — tabela de perfis de consulta relacionada a
  `ECONSULT` por `CSIDPFCON = PRIDPFCON`, que fornece a descrição do serviço/plugin
  (`PRDESCPFCON`) (**[00:02:50]**).
