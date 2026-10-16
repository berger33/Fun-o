> **Fonte textual** fornecida pelo responsável em **2026-10-15**; identificadores diretos mascarados.
> Nomes de operadores da Função preservados conforme autorização registrada em
> [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md).

# Glossário — refinanciamento pela API (Matheus)

| Termo / sigla | Significado sustentado pela fonte | Categoria | Âncora |
|---|---|---|---|
| **`FIApiAutIncluirProposta`** | Endpoint/modelo de **inclusão de proposta** do Autorizador (o nome aparece por extenso na conversa irmã; aqui o fluxo é o mesmo). | SISTEMAS | `[M05]`, `[M10]` (contexto) |
| **Test API** | Ferramenta usada para enviar o payload à API de inclusão em teste — grafada “testa api” pelo operador. | SISTEMAS | `[M10]` |
| **Autorizador** | Sistema onde a proposta é **simulada**; funciona como referência (*oráculo*) do teste de API. | SISTEMAS | `[M05]`, `[M16]` |
| **Refin / Refinanciamento** | Operação em que uma proposta nova quita/absorve operações anteriores do cliente. Discriminada no payload por `TipoOperacao` = `"Refinanciamento"`. | NEGOCIO | `[M05]`, `[M07]` |
| **`OperacoesRefin`** | Bloco do payload que lista as **operações de origem** do refin; a coleção interna de mesmo nome guarda `NumeroOperacao`. | NEGOCIO / SISTEMAS | `[M07]` |
| **`NumeroOperacao`** | Identificador do contrato de origem (ex.: `"800033329-7"` no teste). | NEGOCIO | `[M07]` |
| **`SubTipoRefin`** | Campo de subtipo do refin, com valor `"NaoDefinido"` neste envio. Ver ligação com o erro de modelo na conversa irmã. | NEGOCIO / SISTEMAS | `[M07]` |
| **Operação quitada** | Contrato já liquidado; **não pode** ser usado como origem em proposta de refin. | NEGOCIO | `[M13]` |
| **Contrato “em vermelhinho” / “que dá para marcar”** | Sinalização visual na simulação: vermelho = não utilizável; marcável = utilizável no cenário. | SISTEMAS / PROCESSOS | `[M16]`, `[M17]`, `[M18]` |
| **`coper`** | Tabela referida oralmente para conferir as operações do cliente por CPF. Grafia aproximada; nome/colunas **não confirmados**. | SQL / DÚVIDA_OU_CONFLITO | `[M14]` |
| **`CondicaoCredito`** | Bloco do payload com convênio, produto, prazo, valores, datas de vencimento e taxas. | NEGOCIO | `[M07]` |
| **`MetaCalculo`** | Campo que indica o que é calculado/metas do cálculo — no teste, `"ValorParcela"`. Expansão não explicada na fonte. | NEGOCIO / DÚVIDA_OU_CONFLITO | `[M07]` |
| **`TaxaCETAM` / `TaxaCLAM`** | Taxas informadas na condição (2,73 e 1,7 no teste). Expansão das siglas **não confirmada** na fonte. | NEGOCIO / DÚVIDA_OU_CONFLITO | `[M07]` |
| **`Origens` (`CodigoOrigem1`…`6`, `CodigoOrigem3O`)** | Origens cadastrais da proposta; `CodigoOrigem3` = `"001010"` (promotora/*corban* em outra fonte do acervo) e `CodigoOrigem3O` = `"000202"` no teste. | NEGOCIO / SISTEMAS | `[M07]` |
| **`DadoCadastral`** | Bloco de identificação e cadastro do proponente, com sub-blocos `Telefones`, `DadoEndereco`, `DadoProfissional`, `DadosBancarios`, `Referencias` e `DadoBeneficio`. | SISTEMAS | `[M07]` |
| **`NumeroMatricula`** | Campo do sub-bloco `DadoProfissional` apontado como **incorreto** no envio revisado. | NEGOCIO / PROCESSOS | `[M02]`, `[M07]` |
| **`AssumirCliente`** | Campo de cabeçalho com valor `"Informado"` neste envio; a semântica exata não foi explicada na fonte. | DÚVIDA_OU_CONFLITO | `[M07]` |
| **`PEP`** | Campo booleano do cadastro (`false` no teste); sigla não expandida na fonte (pessoa exposta politicamente, por uso corrente — **não confirmado aqui**). | NEGOCIO / DÚVIDA_OU_CONFLITO | `[M07]` |
| **`SenhaAverbacao` / `SenhaConsultaMargem`** | Campos **do cadastro/proposta** enviados nulos neste teste. Não são credenciais do integrador e nenhum valor é reproduzido. | SISTEMAS / INFRA_E_ACESSO | `[M07]` |
| **Incidente** | Classificação formal de falha; **não** se aplica a erro de dado em proposta de teste. | PROCESSOS | `[M04]` |
| **Payload (JSON)** | Corpo de entrada da API; aqui, artefato copiado da simulação do Autorizador e transportado em bloco de notas. | SISTEMAS / PROCESSOS | `[M07]` |

## Nota de escopo do glossário

Os nomes de campo foram preservados exatamente como aparecem no payload (`PascalCase` sem acento),
porque é assim que eles devem ser digitados na API. **Nenhum valor identificador de pessoa** é
reproduzido; `[DADO PESSOAL OMITIDO]` aparece no lugar (ver [`incertezas.md`](incertezas.md) item 6).
