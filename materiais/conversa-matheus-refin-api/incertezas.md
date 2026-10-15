# Incertezas e pendências — refinanciamento pela API (Matheus)

## 1. Tabela `coper` — nome, ambiente e colunas desconhecidos (âncora `[M14]`)

- A fonte diz apenas “dar um select na **coper** com seu cpf”. Não informa **ambiente/base**,
  **esquema**, **colunas** nem o **dialeto**.
- A grafia é oral/coloquial: pode corresponder a `COPER`, `COPERACAO`, `C-OPER` ou outro nome. O
  índice de SQL do acervo já registra uma menção a “**C-Oper**” em outra fonte, sem confirmar
  (`../SQL/INDICE_SQL.md`).
- **Validação humana necessária:** confirmar o nome real da tabela e o ambiente de teste correto
  antes de qualquer uso. **Nenhuma consulta foi executada nesta análise.**

## 2. Imagem de exemplo citada em `[M19]` não fornecida

- `[M19]` (“tipo noa usa esses”) acompanha, no original, uma imagem de exemplo de contratos não
  utilizáveis. A imagem **não** faz parte do recorte entregue.
- Consequência: o **critério visual** (“em vermelhinho”) está registrado por **fala**, não por
  evidência de tela. Não há captura alguma neste pacote (ver [`capturas.md`](capturas.md)).

## 3. Alcance de “aquele que te mandei acima” (`[M15]`)

- A mensagem pode se referir ao **CPF** (usado no filtro do `select`) ou à **matrícula** mencionada em
  `[M02]`. As duas leituras cabem no texto.
- A interpretação adotada em [`procedimentos.md`](procedimentos.md) Fluxo B (filtro por CPF) é a mais
  coerente com o verbo “dar um select … com seu cpf” de `[M14]`, mas **não é conclusiva**.

## 4. Comportamento de “operação quitada” não demonstrado (`[M13]`)

- Não há mensagem de erro, tela ou retorno JSON reproduzido. Não se sabe **onde** o bloqueio ocorre
  (na API, na simulação, na esteira) nem se há diferença entre ambientes.
- **Validar** com quem conhece a API de inclusão antes de usar “operação quitada” como explicação
  padrão de falha.

## 5. Bloco nulo × bloco ausente

- Vários blocos foram enviados como `null` (`CondicaoRefinanciamentoConjunto`,
  `LiberacoesAdicionais`, `OperacoesPortabilidade`, `ReaproveitamentoSeguro`, `Garantias`,
  `Despesas`). A conversa irmã mostra que **remover** um campo pode gerar erro de conversão do modelo
  — portanto **não** é equivalente omitir e enviar nulo. Nenhum teste foi feito para separar os casos.

## 6. Mascaramento aplicado nesta publicação (registro do que foi omitido)

Identificadores diretos substituídos por `[DADO PESSOAL OMITIDO]` no payload e nos textos:
CPF (duas ocorrências), número de documento de identidade, e-mail, telefones (proponente e
referência pessoal), DDDs, matrícula, CNPJ da empresa, CEP, logradouro, número, complemento, bairro e
cidade do endereço, e nomes de pais e de terceiros citados como referência.

- **Nada disso era conteúdo de estudo:** os nomes dos campos e a lógica do payload foram preservados
  integralmente. A versão íntegra, se preservada, fica em `restrito/` (fora do Git) — ver
  [`../PRIVACIDADE_E_RETENCAO.md`](../PRIVACIDADE_E_RETENCAO.md).
- **Pendência:** se algum dia este material for usado como **massa de teste reutilizável**, gerar
  massa **nova e sintética**; não reaproveitar dados de pessoa real.

## 7. Valores de negócio não são regra

- Prazos, taxas, valores e códigos de convênio/produto do payload são de **uma tentativa de teste**.
  Nada nesta conversa os apresenta como parâmetro vigente. Não usar como referência de cálculo nem
  como expectativa de homologação.

## 8. Catálogos não fornecidos

- Não há, na fonte, catálogo de valores para `TipoOperacao`, `SubTipoRefin`, `TipoFormalizacao`,
  `CodigoSubtipoFormalizacao`, `MeioLiberacaoCliente`, `MetaCalculo`, `Origem3O` nem expansão de
  `TaxaCETAM`/`TaxaCLAM`/`PEP`/`CLAM`.

## 9. Recorte parcial, sem data/hora

- A conversa começa respondendo a algo enviado antes (`[M01]`) e termina em plano de ação (`[M22]`),
  sem confirmação de sucesso. **Não há carimbo de data/hora** em nenhuma mensagem: nada aqui permite
  datar o episódio nem medir intervalos.

## 10. Versão da API e ambiente não informados

- O recorte não diz **qual** endpoint/ambiente o operador usava (a conversa irmã mostra que existem
  ao menos dois caminhos diferentes). Sem isso, a reprodutibilidade é limitada.

## 11. Inconsistência preservada

- `"CodigoCliente": "null"` (string) no payload enviado. Pode ser ruído de ferramenta, mas **não** foi
  corrigido na transcrição — a fonte é a fonte.
