# Metadados — conversa de refinanciamento pela API (Matheus)

- **Tipo de fonte:** conversa (texto) — recorte de chat de trabalho, sem mídia
- **Arquivo/registro de origem:** recorte textual fornecido pelo responsável (operador **William**) em
  **2026-10-15**, no contexto do pedido de análise de conversas de trabalho
- **Slug em `materiais/`:** `materiais/conversa-matheus-refin-api/`
- **Participantes:** **Matheus** (tester/analista, autor das orientações) e **William** (operador em
  treinamento, autor do payload). Nomes preservados conforme diretriz registrada em
  [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md).
- **Extensão do recorte:** 22 mensagens (âncoras `[M01]`–`[M22]`) + 1 payload JSON embutido em `[M07]`
  (~120 linhas). **Recorte parcial** em ambas as pontas.
- **Data/hora:** **não registradas** — o chat não traz carimbo de tempo. Nenhum horário foi inferido.
- **Natureza da evidência:** texto digitado (a maior parte) e **um anexo/imagem referenciado em
  `[M19]` que não foi fornecido**; em `[M01]` há referência a um contrato/arquivo enviado antes do
  recorte, também não fornecido.
- **Categorias aplicáveis:** `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `DÚVIDA_OU_CONFLITO`. **Sem SQL
  executável** (apenas a menção de `[M14]`, registrada no índice de SQL como “menção, sem texto”).
- **Sistemas/artefatos citados:** API de inclusão de proposta (`FIApiAutIncluirProposta`), Test API,
  Autorizador (tela de simulação), consulta à base (tabela referida como `coper`), payload JSON.
- **Confiança da extração:** **média-alta** para a estrutura do payload (JSON integral e legível) e
  para as regras ensinadas (fala direta do tester); **baixa** para reprodutibilidade operacional
  (ambiente, versão, nome de tabela e comportamento visual não demonstrados) — ver
  [`incertezas.md`](incertezas.md).
- **Método de análise:** leitura integral do recorte, extração do payload para bloco de código,
  mascaramento de identificadores diretos, cruzamento com os pacotes
  [`../conversa-jonas-testa-api/`](../conversa-jonas-testa-api/) (mesma API) e
  [`../gravando-2026-10-07-152044/`](../gravando-2026-10-07-152044/) (convênio/produto) do acervo.
  Nenhum sistema, API, banco, tela ou massa foi acessado ou alterado nesta análise.
- **Varredura de privacidade:** feita com `tools/validar_materiais.py` (CPF/CNPJ, e-mail, telefone,
  segredos). Os identificadores diretos foram substituídos por `[DADO PESSOAL OMITIDO]`; a lista
  completa do que foi mascarado está em [`incertezas.md`](incertezas.md) item 6.
- **Capturas:** nenhuma (ver [`capturas.md`](capturas.md)).
- **Estado:** `em revisão` — ver [`../../STATUS.md`](../../STATUS.md).
- **Limitações:** recorte parcial sem data/hora; ausência de telas, de mensagem de erro e de confirmação
  de sucesso; nomes de tabela/campos do payload são exatamente os digitados, sem conferência na EF da
  API.
