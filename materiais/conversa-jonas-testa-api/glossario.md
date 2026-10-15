> **Fonte textual** fornecida pelo responsável em **2026-10-15**; CPF e hospedeiros de rede
> mascarados. Nomes de operadores da Função preservados conforme autorização registrada em
> [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md).

# Glossário — depuração no Test API (Jonas)

| Termo / sigla | Significado sustentado pela fonte | Categoria | Âncora |
|---|---|---|---|
| **`FIApiAutIncluirProposta`** | Nome do serviço/modelo da API de **inclusão de proposta** do Autorizador; aparece no texto do erro (`FIApiAutIncluirProposta.Models.SubTipoRefin`) e nos dois caminhos de endpoint. | SISTEMAS | `[M04]`, `[M05]`, `[M13]` |
| **Test API** | Ferramenta de envio de payload à API; grafada pelo operador como “testa api”. Tem **campos próprios**, o que motivou a pergunta de `[M07]`. | SISTEMAS | `[M07]` |
| **Autorizador** | Sistema onde a proposta é simulada e de onde sai o payload; funciona como referência do teste (conversa irmã, `[M05]`). | SISTEMAS | contexto (`[M01]`) |
| **Refin / Refinanciamento** | Operação tratada na conversa; o nó do payload é `OperacoesRefin`. | NEGOCIO | `[M13]`, `[M14]` |
| **`OperacoesRefin`** | Bloco do payload de refin; contém a lista de operações de origem e o campo `SubTipoRefin`. | NEGOCIO / SISTEMAS | `[M13]` |
| **`SubTipoRefin`** | Campo do bloco `OperacoesRefin` que **não aceita `null`** no modelo — causa direta do erro colado. Valor candidato: `"NaoDefinido"` (hipótese). | SISTEMAS / DÚVIDA_OU_CONFLITO | `[M13]`, `[M14]` |
| **`NumeroOperacao`** | Campo com o número da operação de origem; ao ser removido, a API **pede** o número da operação — é indispensável no fluxo. | NEGOCIO / SISTEMAS | `[M06]`, `[M16]` |
| **“Mesa C6” / “Regressivo 540791”** | Área/caminho onde há uma publicação do endpoint (`Mesa C6/Regressivo 540791/…`). “Regressivo” tem número associado; a semântica não é explicada na fonte. | INFRA_E_ACESSO / DÚVIDA_OU_CONFLITO | `[M04]` |
| **`C6/Api`** | Caminho alternativo de publicação do mesmo endpoint (`…/C6/Api/FIApiAutIncluirProposta/`). | INFRA_E_ACESSO | `[M05]` |
| **`Modelo de entrada de dados inválido`** | Prefixo da mensagem de erro: o corpo recebido não corresponde ao modelo esperado pela API. | SISTEMAS | `[M13]` |
| **`Error converting value {null} to type '…Models.SubTipoRefin'`** | Erro de **desserialização** do corpo: chegou `null` em campo de enum não anulável. | SISTEMAS | `[M13]` |
| **`Path` / `line 1, position 1117`** | Localização do campo no JSON (caminho lógico e posição no corpo minificado) — usados para achar o ponto exato da correção. | SISTEMAS | `[M13]` |
| **`CODIGO: 100000002`** | Código do erro de modelo retornado pela API. **Sem catálogo na fonte** — não interpretar além do texto. | SISTEMAS / DÚVIDA_OU_CONFLITO | `[M13]` |
| **“Tirar o campo”** | Técnica de diagnóstico: remover um campo do payload para observar a crítica e isolar a causa. | PROCESSOS | `[M06]`, `[M09]`, `[M11]`, `[M14]` |
| **Incidente** | Classificação de falha. Jonas levanta a hipótese (“parece incidente”) **antes** de o grupo confirmar. | PROCESSOS | `[M15]` |
| **Santana** | Colega da frente de **API** do projeto, envolvido no caso pelo próprio operador. | PROCESSOS | `[M22]` |

## Nota de escopo

Os nomes de campo e os trechos de erro foram preservados **exatamente** como aparecem na fonte —
inclusive o erro gramatical do retorno da API (“Modelo de entrada de dados inválido”) e os erros de
digitação do interlocutor (“conegue”, “operaão”, “númeo”). Corrigir isso destruiria a evidência de
que o texto é literal.
