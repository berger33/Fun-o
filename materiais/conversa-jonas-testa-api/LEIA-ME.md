# Materiais da conversa — depuração no Test API (Jonas)

Pacote derivado de um **recorte de conversa de trabalho** com **Jonas** (tester e futuro analista),
em que o operador **William** relata o que acontece ao tentar incluir uma **proposta de
refinanciamento** pela API `FIApiAutIncluirProposta` usando o **Test API**.

- **Fonte:** recorte textual de chat fornecido pelo responsável em **2026-10-15** (sem carimbo de
  data/hora). Não é gravação: a rastreabilidade usa **âncoras `[Mnn]`** — ver
  [`../CONVENCOES_FONTES_TEXTUAIS.md`](../CONVENCOES_FONTES_TEXTUAIS.md).
- **Documentos:** [`transcricao.md`](transcricao.md), [`guia_de_estudo.md`](guia_de_estudo.md),
  [`procedimentos.md`](procedimentos.md), [`perguntas.md`](perguntas.md), [`glossario.md`](glossario.md),
  [`incertezas.md`](incertezas.md), [`metadados.md`](metadados.md), [`capturas.md`](capturas.md).
- **Valor principal:** é o material do acervo que **explica uma mensagem de erro real da API de
  inclusão** (`Error converting value {null} to type '…Models.SubTipoRefin'`) e o **método de
  isolamento de campo** usado para chegar lá, além do critério de **quando escalar** (grupo + par com
  o responsável da API).
- **Privacidade:** CPF citado em `[M01]` mascarado; nomes de rede/servidor substituídos por
  `<servidor>`; nenhum segredo, token ou credencial aparece na fonte.
- **Estado:** `em revisão` em [`../../STATUS.md`](../../STATUS.md) — o par requisição/resposta não é
  reconstruível a partir do recorte e o desfecho do caso (escalada com Santana) não aparece.
