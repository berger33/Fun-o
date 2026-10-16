> **Fonte textual** fornecida pelo responsável em **2026-10-15** (recorte de conversa de trabalho,
> sem carimbo de data/hora). **Identificadores diretos mascarados** (`[DADO PESSOAL OMITIDO]`):
> CPF, CNPJ, RG/documento, telefone, e-mail, matrícula, endereço/CEP e nomes de familiares e de
> terceiros citados no payload. Nomes de operadores da Função preservados conforme autorização
> registrada em [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md). Nenhum segredo, senha,
> token ou contrato real é publicado.

# Transcrição — conversa de refinanciamento pela API (Matheus)

- **Natureza da fonte:** conversa escrita (chat), com **payload JSON colado** por um dos
  participantes. Há referência a um contrato/anexo enviado antes do recorte (`[M01]`), que **não**
  faz parte deste material.
- **Âncoras:** `[Mnn]` = índice da mensagem **na ordem em que o recorte foi fornecido**. A ordem não
  representa intervalo de tempo; o chat não traz carimbo de data/hora.
- **Autoria:** atribuída quando o recorte indica (citação/contexto). Mensagens curtas de reação sem
  autoria determinável estão marcadas como `autoria não determinada`.

---

## Bloco 1 — Revisão do primeiro envio (reação do tester)

- **[M01] Matheus:** "simulei com esse contrato aqui"
  *(refere-se a um contrato/anexo enviado antes deste recorte — imagem ou arquivo não fornecido)*
- **[M02] Matheus:** "sua matricula ou pelo menos essa matricula que vc mandou ai no json ainda esta incorreta"
- **[M03] Matheus:** "ajeita isso ai, mas esta dando certo tranquilo"
- **[M04] Matheus:** "kkkk nao é incidente"

## Bloco 2 — Dica de método: usar o Autorizador como oráculo

- **[M05] Matheus:** "uma dica: quando vc for fazer uma proposta refin pela api, vai simulando tbm pelo autorizador"
- **[M06] Matheus:** "ajuda mt"

## Bloco 3 — Envio do payload atualizado (William)

- **[M07] William:** "o json que mandei agora agora realmente não foi o mais recente, eu tinha fechado
  a tela e nao salvei as ultimas alterações, mas tinha copiado no bloco de notas esse é o mais
  recente:," — seguido do payload JSON reproduzido abaixo (§Payload).
- **[M08] Matheus:** "Deixa eu ver o que faltou"
- **[M09] William:** "pior que no meio das tentativas eu fiz isso" *(referindo-se à dica de `[M05]`)*
- **[M10] William:** "consigo simular pelo autorizador normalmente, mas pelo testa api que ainda to apanhando pra fazer o refin"

## Bloco 4 — Diagnóstico: operação já quitada

- **[M11] Matheus:** "rodei auqi" / "aqui\*\*"
- **[M12] Matheus:** "hmm"
- **[M13] Matheus:** "vi que vc esta com uma operação ja quitada em uma proposta refin"
- **[M14] Matheus:** "dar um select na coper com seu cpf"
- **[M15] Matheus:** "aquele que te mandei acima" *(autoria inferida; referência ambígua — ver
  [`incertezas.md`](incertezas.md) item 3)*

## Bloco 5 — Como escolher os contratos elegíveis

- **[M16] Matheus:** "simula tbm pelo autorizador... vc vai notar que tem uns contratos em vermelhinho que nao dar para usar"
- **[M17] Matheus:** "ai vc nao usa esses"
- **[M18] Matheus:** "usa somente os que dao para marcar"
- **[M19] autoria não determinada:** "tipo noa usa esses" *(texto que acompanha uma imagem de
  exemplo citada na conversa — **imagem não fornecida neste recorte**)*
- **[M20] autoria não determinada:** "não"
- **[M21] autoria não determinada:** "hmm"
- **[M22] William:** "vou tentar fazer isso"

---

## Payload JSON enviado em `[M07]` (identificadores mascarados)

> **Leitura:** este é o corpo enviado para a inclusão de proposta de **refinanciamento**. Os valores
> de negócio (prazos, taxas, códigos de produto/convênio, valores) foram preservados porque são o
> objeto do teste; os campos que identificam a pessoa foram substituídos por
> `[DADO PESSOAL OMITIDO]`. O campo `NumeroMatricula` de `[M02]` **é exatamente o que o tester
> apontou como incorreto** — o valor não é reproduzido aqui.

```json
{
    "AssumirCliente": "Informado",
    "CPF": "[DADO PESSOAL OMITIDO]",
    "CodigoCliente": "null",
    "NumeroPropostaExterno": null,
    "NumeroOferta": null,
    "Plataforma": null,
    "TipoOperacao": "Refinanciamento",
    "CodVerba": "",
    "CodServico": null,
    "PIS": null,
    "TipoFormalizacao": "DIGITAL",
    "CodigoSubtipoFormalizacao": 1,
    "CodigoCBC": null,
    "Origens": {
        "CodigoOrigem1": "000001",
        "CodigoOrigem2": "000001",
        "CodigoOrigem3": "001010",
        "CodigoOrigem4": "001010",
        "CodigoOrigem5": "001010",
        "CodigoOrigem6": "000001",
        "CodigoOrigem3O": "000202",
        "NumeroCPFCertificado": null,
        "NomeCertificado": null
    },
    "CondicaoCredito": {
        "CodigoConvenio": "989898",
        "CodigoProduto": "009898",
        "QuantidadeParcelas": 36,
        "ValorSolicitado": 3222,
        "ValorPrincipal": 4525.56,
        "ValorParcela": 125.71,
        "ValorIOF": 17.61,
        "ValorCliente": 2836,
        "DataPrimeiroVencimento": "07/09/2027",
        "DataUltimoVencimento": "07/08/2030",
        "TaxaCETAM": 2.73,
        "TaxaCLAM": 1.7,
        "MeioLiberacaoCliente": "001",
        "MetaCalculo": "ValorParcela",
        "ValorFGTS": null,
        "ValorGarantiaFGTS": null,
        "Despesas": null
    },
    "CondicaoRefinanciamentoConjunto": null,
    "LiberacoesAdicionais": null,
    "OperacoesRefin": {
        "OperacoesRefin": [
            {
                "NumeroOperacao": "800033329-7"
            }
        ],
        "SubTipoRefin": "NaoDefinido"
    },
    "OperacoesPortabilidade": null,
    "Pagamento": {
        "NumeroBanco": "336",
        "NumeroAgencia": "0001",
        "DigitoAgencia": "1",
        "TipoConta": "ContaCorrenteIndividual",
        "NumeroConta": "12345",
        "DigitoConta": "1"
    },
    "DadoCadastral": {
        "TipoPessoa": "Fisica",
        "CPF": "[DADO PESSOAL OMITIDO]",
        "Nome": "WILLIAM TESTE",
        "Grupo": "001",
        "Nacionalidade": "Brasileira",
        "TipoDocumento": "RG",
        "NumeroDocumento": "[DADO PESSOAL OMITIDO]",
        "UFDocumento": "SP",
        "DataEmissaoDocumento": "11/09/2025",
        "OrgaoEmissorDocumento": "SSP",
        "EstadoCivil": "Solteiro",
        "QuantidadeDependentes": 0,
        "DataNascimento": "11/09/1991",
        "Sexo": "Masculino",
        "ValorRenda": 50000,
        "ValorRendaOutros": 0,
        "NomePai": "[DADO PESSOAL OMITIDO]",
        "NomeMae": "[DADO PESSOAL OMITIDO]",
        "Escolaridade": "Superior",
        "Naturalidade": "Brasileira",
        "NaturalidadeUF": "SP",
        "Email": "[DADO PESSOAL OMITIDO]",
        "NomeRecado": null,
        "PEP": false,
        "SenhaAverbacao": null,
        "SenhaConsultaMargem": null,
        "DataContracheque": null,
        "IdentidadeMilitar": null,
        "ValidarUFOM": null,
        "Conjuge": null,
        "Telefones": {
            "Telefones": [
                {
                    "Tipo": "Celular",
                    "DDD": "[DADO PESSOAL OMITIDO]",
                    "NumeroTelefone": "[DADO PESSOAL OMITIDO]"
                }
            ]
        },
        "DadoEndereco": {
            "TipoEnderecoCorrespondencia": "Residencial",
            "TipoResidencia": "Propria",
            "ValorAluguel": null,
            "ResidenciaAtualAnos": "20",
            "ResidenciaAtualMeses": "3",
            "ResidenciaAnteriorAnos": "12",
            "ResidenciaAnteriorMeses": "0",
            "Enderecos": {
                "Enderecos": [
                    {
                        "Tipo": "Residencial",
                        "CEP": "[DADO PESSOAL OMITIDO]",
                        "Logradouro": "[DADO PESSOAL OMITIDO]",
                        "Numero": "[DADO PESSOAL OMITIDO]",
                        "Complemento": "[DADO PESSOAL OMITIDO]",
                        "Bairro": "[DADO PESSOAL OMITIDO]",
                        "Cidade": "[DADO PESSOAL OMITIDO]",
                        "UF": "SP",
                        "Zona": "ZonaUrbana"
                    }
                ]
            }
        },
        "DadoProfissional": {
            "EmpresaNome": "Empresa",
            "EmpresaCNPJ": "[DADO PESSOAL OMITIDO]",
            "TipoInscricaoEmpresa": "CNPJ",
            "Profissao": "TI",
            "Cargo": "Analista de Sistemas",
            "DataAdmissao": "11/10/2013",
            "NumeroMatricula": "[DADO PESSOAL OMITIDO]",
            "NumeroMatriculaInstituidor": null,
            "CodigoNaturezaOcupacao": null,
            "TipoBeneficio": null,
            "EmpresaAnteriorNome": null,
            "EmpresaAnteriorDataAdmissao": null,
            "EmpresaAnteriorDataDemissao": null,
            "OutrasRendasNome": null,
            "OutrasRendasCNPJ": null,
            "OutrasRendasDataAdmissao": null,
            "OutrasRendasCargo": null,
            "OutrasRendasCodigoNaturezaOcupacao": null
        },
        "DadosBancarios": {
            "DadoBancario": [
                {
                    "Compensacao": "001",
                    "Banco": "1",
                    "Agencia": "1",
                    "AgenciaDigito": "1",
                    "TipoConta": "ContaCorrenteIndividual",
                    "Conta": "12345",
                    "ContaDigito": "1",
                    "AgenciaNome": "0001",
                    "AgenciaEndereco": "teste rua",
                    "DataAbertura": null,
                    "Cartao": null
                }
            ]
        },
        "Referencias": {
            "Referencias": [
                {
                    "Tipo": "Pessoal",
                    "TipoReferenciaTelefone": "Celular",
                    "Nome": "[DADO PESSOAL OMITIDO]",
                    "DDD": "[DADO PESSOAL OMITIDO]",
                    "NumeroTelefone": "[DADO PESSOAL OMITIDO]"
                }
            ]
        },
        "DadoBeneficio": {
            "Agencia": "0001",
            "AgenciaDigito": "1",
            "Banco": "1",
            "Conta": "012345",
            "ContaDigito": "1",
            "RecebeBeneficioCartao": false,
            "BeneficioUF": "SP"
        }
    },
    "DadoRepresentanteLegal": {
        "PossuiRepresentanteLegal": false,
        "CPFRepresentanteLegal": null,
        "NomeRepresentanteLegal": null,
        "DataFimRepresentanteLegal": null,
        "RepresentanteCPFTitularContaBeneficio": "NaoDefinido"
    },
    "ReaproveitamentoSeguro": null,
    "Garantias": null
}
```

### Observações de leitura do payload

- O bloco `OperacoesRefin` traz **uma** operação (`NumeroOperacao`) e `SubTipoRefin` = `"NaoDefinido"`.
  Este valor é relevante: em outra conversa do acervo, enviar `SubTipoRefin` nulo/ausente provoca erro
  de conversão do modelo — ver [`../conversa-jonas-testa-api/incertezas.md`](../conversa-jonas-testa-api/incertezas.md).
- `TipoOperacao` = `"Refinanciamento"` e `TipoFormalizacao` = `"DIGITAL"` são os valores usados nesta
  tentativa; não há catálogo de valores na fonte.
- Os blocos opcionais (`CondicaoRefinanciamentoConjunto`, `LiberacoesAdicionais`,
  `OperacoesPortabilidade`, `ReaproveitamentoSeguro`, `Garantias`, `Despesas`) foram enviados como
  `null` nesta tentativa — **não enviar esses blocos é diferente de enviá-los nulos**; ver
  [`incertezas.md`](incertezas.md) item 5.
- O JSON colado tem `"CodigoCliente": "null"` (string `"null"`) enquanto os demais vazios usam o
  valor nulo do JSON. É uma inconsistência **da fonte**, registrada e não corrigida.

## Observações de qualidade

- O recorte não contém data/hora, e a conversa é claramente **parcial**: começa com uma resposta a
  algo enviado antes (`[M01]`) e termina com um plano de ação (`[M22]`).
- Nenhuma mensagem de erro da API é reproduzida nesta conversa (diferente da conversa com Jonas).
- Nenhum segredo, senha ou token aparece no recorte.
