# Metadados — depuração no Test API (Jonas)

- **Tipo de fonte:** conversa (texto) — recorte de chat de trabalho, sem mídia
- **Arquivo/registro de origem:** recorte textual fornecido pelo responsável (operador **William**) em
  **2026-10-15**
- **Slug em `materiais/`:** `materiais/conversa-jonas-testa-api/`
- **Participantes:** **Jonas** (tester/futuro analista, conduz o diagnóstico) e **William** (operador
  que testa). **Santana** é citado como envolvido na frente de API. Nomes preservados conforme
  diretriz registrada em [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md).
- **Extensão do recorte:** 24 mensagens (âncoras `[M01]`–`[M24]`), incluindo **um retorno de API
  colado** (`[M13]`) e **duas URLs internas** (`[M04]`, `[M05]`).
- **Data/hora:** **não registradas** — o chat não traz carimbo de tempo; nenhum horário foi inferido.
- **Natureza da evidência:** texto digitado; **um trecho de retorno de sistema reproduzido literalmente**
  (fonte de maior valor probatório neste pacote).
- **Categorias aplicáveis:** `SISTEMAS`, `PROCESSOS`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO`. **Sem SQL.**
- **Sistemas/artefatos citados:** API `FIApiAutIncluirProposta` (duas publicações: área “Mesa C6 /
  Regressivo 540791” e `C6/Api`), **Test API**, Autorizador (origem do payload), grupo de comunicação
  da equipe.
- **Confiança da extração:** **alta** para o texto do erro e para o encaminhamento/escalada (explícitos
  na fonte); **média** para o método de isolamento (descrito em instruções curtas, sem requisições);
  **baixa** para reprodutibilidade (endpoint vigente, versão da API, enum do campo e desfecho não
  conhecidos) — ver [`incertezas.md`](incertezas.md).
- **Método de análise:** leitura integral do recorte; preservação literal das mensagens (inclusive
  erros de digitação e o texto do erro da API); mascaramento de CPF e de hospedeiros; cruzamento com
  [`../conversa-matheus-refin-api/`](../conversa-matheus-refin-api/) (payload de refin que passou) e com
  [`../gravando-2026-07-07-155307/`](../gravando-2026-07-07-155307/) (frente de API / Santana).
  Nenhuma API, sistema, banco ou tela foi acessado nesta análise.
- **Varredura de privacidade:** executada com `tools/validar_materiais.py`; sem achados nos derivados
  (o CPF foi mascarado antes da auditoria; a lista do que foi omitido está em
  [`incertezas.md`](incertezas.md) item 6).
- **Capturas:** nenhuma (ver [`capturas.md`](capturas.md)).
- **Estado:** `em revisão` — ver [`../../STATUS.md`](../../STATUS.md).
- **Limitações:** recorte parcial e fora de ordem cronológica garantida; sem requisição, sem tela, sem
  desfecho; nomes de servidor mascarados.
