# Guia de estudo — conversa sobre refinanciamento pela API (Matheus)

- **Categoria:** `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `DÚVIDA_OU_CONFLITO` (sem `SQL` executável: há
  **menção** a um `select`, sem comando, esquema ou dialeto — ver [`../SQL/INDICE_SQL.md`](../SQL/INDICE_SQL.md))
- **Sistema:** Função Sistemas — **API de inclusão de proposta** (`FIApiAutIncluirProposta`) e
  **Autorizador** (tela de simulação de proposta), com apoio de consulta à base
  (`select` na tabela referida como `coper`, `[M14]`)
- **Assunto:** como montar e depurar um envio de **proposta de refinanciamento** pela API; por que a
  simulação no Autorizador é o oráculo do teste; como identificar contratos elegíveis (operação não
  quitada, contrato “marcável” na simulação); estrutura completa do payload de entrada.
- **Fonte:** recorte textual de conversa de trabalho com o tester **Matheus**, fornecido pelo
  responsável em **2026-10-15**; âncoras `[Mnn]` conforme [`../CONVENCOES_FONTES_TEXTUAIS.md`](../CONVENCOES_FONTES_TEXTUAIS.md)
- **Confiança da extração:** média-alta para a **estrutura do payload** (o JSON foi colado integral e
  é integralmente legível) e para as **regras ensinadas** (faladas de forma direta pelo tester);
  **baixa** para reprodução operacional (ambiente, versão da API, nome/colunas da tabela `coper`,
  texto do erro de “operação quitada” e a tela de contratos em vermelho **não** foram demonstrados).

## 1. Contexto

O operador **William** estava tentando incluir uma proposta de **refinanciamento** pela API
(`FIApiAutIncluirProposta`) e não conseguia concluir; o tester **Matheus** rodou a simulação com o
mesmo contrato (`[M01]`), avaliou o JSON enviado, apontou erros de dado e ensinou o método de teste
que usa no dia a dia. A conversa termina com um plano de ação (`[M22]`), sem confirmação de sucesso.

Três entregas didáticas:

1. **Método de teste (o mais valioso):** ao preparar um refin pela API, **simular a mesma proposta no
   Autorizador** e comparar (`[M05]`, `[M16]`). O Autorizador funciona como *oráculo*: mostra o que o
   negócio espera e quais contratos podem ser usados.
2. **Elegibilidade dos contratos de origem:** existe **operação já quitada** que inviabiliza o refin
   (`[M13]`); na simulação, contratos **em vermelho** não podem ser usados e só os **marcáveis**
   entram (`[M16]`, `[M17]`, `[M18]`). O caminho indicado para investigar é consultar a base por CPF
   (`[M14]`).
3. **Disciplina de dados do teste:** matrícula incorreta passa e a proposta “dá certo”, mas o dado
   está errado (`[M02]`, `[M03]`); e **dado errado em proposta de teste não é incidente** (`[M04]`).

## 2. Linha de raciocínio da conversa

| Âncora | O que acontece | O que se aprende |
|---|---|---|
| `[M01]`–`[M04]` | Tester reproduz o cenário, aponta matrícula incorreta no JSON, mas confirma que a inclusão funcionou; descarta a hipótese de incidente | O envio **passou** com dado cadastral errado → validação de matrícula não bloqueia a inclusão. Erro de dado de teste **não** é incidente |
| `[M05]`, `[M06]`, `[M16]` | Dica de método: simular também no Autorizador | O Autorizador é a referência funcional do teste de API |
| `[M07]`–`[M10]` | Envio do JSON “mais recente”; operador relata que fechou a tela sem salvar e recuperou o conteúdo do bloco de notas | Risco de **payload desatualizado**: a tela de simulação é a fonte do JSON, então copiar antes de salvar/fechar envia dados velhos |
| `[M11]`–`[M13]` | Tester executa a consulta e conclui: há **operação quitada** na proposta de refin | O refin só aceita operações elegíveis; contrato liquidado bloqueia o cenário |
| `[M14]`, `[M15]` | “dar um select na coper com seu cpf” | Caminho de investigação por CPF na base, para listar as operações do cliente |
| `[M16]`–`[M18]` | Instrução de leitura da tela de simulação: contratos em vermelho não servem; usar só os marcáveis | A simulação **mostra** a elegibilidade; o vermelho é o sinal visual |
| `[M19]`–`[M22]` | Exemplificação por imagem (não fornecida) e plano de ação | Ver [`incertezas.md`](incertezas.md) item 2 |

## 3. Anatomia do payload de refinanciamento (o núcleo do material)

Bloco a bloco, com o significado sustentado pela fonte (`[M07]`). O JSON completo, mascarado, está em
[`transcricao.md`](transcricao.md).

### 3.1 Cabeçalho da operação

| Campo | Valor no teste | Leitura |
|---|---|---|
| `AssumirCliente` | `"Informado"` | Indica que o dado do cliente foi informado no payload |
| `CPF` | *(mascarado)* | CPF do proponente, também repetido em `DadoCadastral.CPF` |
| `CodigoCliente` | `"null"` (string) | Inconsistência da fonte; não corrigida |
| `TipoOperacao` | `"Refinanciamento"` | Discriminante do fluxo — é o que diferencia este envio de uma proposta nova |
| `TipoFormalizacao` | `"DIGITAL"` | Modalidade de formalização |
| `CodigoSubtipoFormalizacao` | `1` | Subtipo numérico da formalização |
| `NumeroPropostaExterno`, `NumeroOferta`, `Plataforma`, `CodServico`, `PIS`, `CodigoCBC` | `null` | Campos não usados nesta operação |
| `CodVerba` | `""` | Vazio (string), não nulo |

### 3.2 `Origens` — as seis origens da proposta

`CodigoOrigem1` a `CodigoOrigem6` identificam as origens (1–6) e `CodigoOrigem3O` aparece como campo
**extra**, específico: nesta tentativa, `CodigoOrigem3O` = `"000202"` enquanto `CodigoOrigem3` =
`"001010"`. `NumeroCPFCertificado` e `NomeCertificado` ficaram nulos. A semântica de “origem 3” já
aparece em outra fonte do acervo como a **promotora/correspondente** (*corban*) — ver
[`../jonas-ept-explicacao/glossario.md`](../jonas-ept-explicacao/glossario.md) (`corban_data` /
`id "001010"` = Origem 3).

### 3.3 `CondicaoCredito` — a condição financeira negociada

| Campo | Valor no teste | Leitura |
|---|---|---|
| `CodigoConvenio` / `CodigoProduto` | `"989898"` / `"009898"` | Convênio e produto do teste (o convênio `989898 - CONV MS` já aparece em [`../gravando-2026-10-07-152044/guia_de_estudo.md`](../gravando-2026-10-07-152044/guia_de_estudo.md)) |
| `QuantidadeParcelas` | `36` | Prazo |
| `ValorSolicitado` / `ValorPrincipal` / `ValorCliente` / `ValorParcela` / `ValorIOF` | `3222` / `4525.56` / `2836` / `125.71` / `17.61` | Valores da condição; `ValorParcela` = 125,71 e `MetaCalculo` = `"ValorParcela"` (a meta de cálculo é a parcela) |
| `DataPrimeiroVencimento` / `DataUltimoVencimento` | `07/09/2027` / `07/08/2030` | Datas no formato `dd/MM/aaaa` |
| `TaxaCETAM` / `TaxaCLAM` | `2.73` / `1.7` | Taxas mensais (CET e “CL” — expansão não confirmada na fonte) |
| `MeioLiberacaoCliente` | `"001"` | Forma de liberação |
| `ValorFGTS`, `ValorGarantiaFGTS`, `Despesas` | `null` | Não usados neste cenário |

### 3.4 `OperacoesRefin` — a(s) operação(ões) refinanciada(s)

```json
"OperacoesRefin": {
    "OperacoesRefin": [ { "NumeroOperacao": "800033329-7" } ],
    "SubTipoRefin": "NaoDefinido"
}
```

- A coleção interna se chama `OperacoesRefin` dentro do bloco `OperacoesRefin` (nome repetido).
- `NumeroOperacao` identifica o contrato de origem — **é o campo que precisa apontar para uma operação
  elegível** (não quitada, “marcável” na simulação — `[M13]`, `[M16]`–`[M18]`).
- `SubTipoRefin` = `"NaoDefinido"` **não é “campo vazio”**: é o valor literal que funcionou aqui. Em
  outra conversa, remover/deixar nulo esse campo faz a API recusar o modelo — ligação registrada como
  **hipótese** em [`../conversa-jonas-testa-api/incertezas.md`](../conversa-jonas-testa-api/incertezas.md).

### 3.5 `Pagamento` e `DadoCadastral`

- `Pagamento`: banco, agência (com dígito), tipo de conta e conta (com dígito) — dados de crédito
  **da operação**, distintos dos dados bancários do cadastro.
- `DadoCadastral`: identificação (`TipoPessoa`, `CPF`, `Nome`, `Grupo`), documento (`TipoDocumento`,
  `UFDocumento`, `DataEmissaoDocumento`, `OrgaoEmissorDocumento`), dados pessoais
  (`DataNascimento`, `Sexo`, `NomePai`, `NomeMae`, `Escolaridade`, `Naturalidade`), contato
  (`Email`, `Telefones`), `PEP`, `Conjuge` e dois campos de **senha** (`SenhaAverbacao`,
  `SenhaConsultaMargem` — nulos aqui; são campos do contrato, não credenciais do integrador).
- Sub-blocos: `DadoEndereco` (`Enderecos` com CEP, logradouro, número, complemento, bairro, cidade,
  UF, zona, além de tempo de residência atual/anterior), `DadoProfissional` (**`EmpresaCNPJ`,
  `Profissao`, `Cargo`, `DataAdmissao`, `NumeroMatricula`** — o campo do erro em `[M02]`),
  `DadosBancarios`, `Referencias` (referência pessoal com telefone) e `DadoBeneficio`.
- **Regra prática que sai daqui:** o envio **não valida** o dado de matrícula de forma bloqueante
  (`[M02]`+`[M03]`). Consequência: uma proposta pode “passar” com dado cadastral errado — em teste,
  corrija e siga (`[M03]`); em produção, esse é um risco a considerar.

### 3.6 Blocos opcionais e de extensão

`CondicaoRefinanciamentoConjunto`, `LiberacoesAdicionais`, `OperacoesPortabilidade`,
`ReaproveitamentoSeguro` e `Garantias` foram enviados como `null`. Eles **existem** no contrato da API:
são os pontos de extensão para refinanciamento conjunto, liberações adicionais, portabilidade,
reaproveitamento de seguro (funcionalidade monitorada em outros materiais do acervo — ver
[`../gravando-2026-10-07-152044/glossario.md`](../gravando-2026-10-07-152044/glossario.md)) e garantias.

## 4. Conceitos que o material consolida

1. **API + Autorizador andam juntos.** A API não é testada “no escuro”: a simulação no Autorizador
   dá a condição esperada e a lista de contratos válidos (`[M05]`, `[M16]`).
2. **Elegibilidade é pré-condição de negócio, não bug.** Operação quitada inviabiliza o cenário
   (`[M13]`); a tela marca o que não serve (`[M16]`–`[M18]`).
3. **Payload é artefato versionável.** Se a tela não foi salva, o JSON copiado é o antigo (`[M07]`) —
   guardar o payload em arquivo (bloco de notas, no relato) é o que salvou a tentativa.
4. **Triagem de falha antes de escalar.** Erro de dado de teste ≠ incidente (`[M04]`); a escalada
   correta (grupo/pareamento com o responsável pela API) aparece na conversa irmã
   [`../conversa-jonas-testa-api/guia_de_estudo.md`](../conversa-jonas-testa-api/guia_de_estudo.md).
5. **Consultar a base é parte do diagnóstico.** Antes de insistir no payload, olhe as operações do
   cliente (`[M14]`).

## 5. Erros, riscos e cuidados

- **Não reutilizar estes valores como regra de negócio.** Taxas, prazos, valores e códigos são de
  **uma tentativa de teste**; servem para reconhecer a forma do payload.
- **Não usar os campos pessoais como massa de teste.** Os identificadores foram mascarados aqui por
  política; reutilizar CPF/nome/telefone de pessoas reais em massa de teste é o oposto do que se quer.
- **Não executar o `select` em ambiente indevido.** A conversa diz “dar um select na coper”; o alvo
  (base/ambiente), o nome exato da tabela e as colunas **não** foram ditos. Consulta de leitura só no
  ambiente de teste, conforme runbook — ver [`incertezas.md`](incertezas.md) itens 1 e 2.
- **Não existe captura de tela** desta conversa que comprove o comportamento visual dos contratos em
  vermelho (a imagem citada em `[M19]` não foi fornecida).
- **Ordem das mensagens não é cronologia**: não inferir prazo entre `[M07]` e `[M22]`.

## 6. Resumo de uma linha

Para testar refin pela API: monte o payload espelhando a simulação do Autorizador, use **apenas
operações elegíveis** (confira na tela e, se preciso, na base por CPF), confira matrícula/dados
cadastrais antes de concluir — e trate erro de dado de teste como ajuste, não como incidente.
