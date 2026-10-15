> **Fonte textual** fornecida pelo responsável em **2026-10-15**; identificadores diretos mascarados.
> Nomes de operadores da Função preservados conforme autorização registrada em
> [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md).

# Procedimentos — refinanciamento pela API (Matheus)

Os fluxos abaixo reproduzem o que a conversa ensina. **Nenhum passo foi executado nesta análise**
(nem API, nem SQL, nem tela de sistema). Ambiente, versão e nomes exatos de tabela **não** foram
informados na fonte — a validação é humana e obrigatória antes do uso (ver [`incertezas.md`](incertezas.md)).

## Fluxo A — Usar o Autorizador como oráculo do teste de API

| Item | Conteúdo |
|---|---|
| **Objetivo** | Garantir que o payload de refin enviado à API reflita a condição de negócio esperada |
| **Pré-condições** | Cliente/massa de teste disponível; acesso ao Autorizador; acesso ao Test API; cenário de refinanciamento definido |
| **Entradas** | CPF/número do cliente de teste; contrato(s) de origem; condição de crédito pretendida |
| **Fonte** | `[M05]`, `[M06]`, `[M16]` |
| **Resultado esperado** | Payload enviado com a mesma condição mostrada na simulação, e resposta da API comparável à tela |

1. Abra o **Autorizador** e **simule** a proposta de refinanciamento do cenário (`[M05]`).
2. Leia na simulação a **condição de crédito** e a **lista de contratos** do cliente (`[M16]`).
3. Monte o payload de `FIApiAutIncluirProposta` espelhando a simulação (`[M05]`, estrutura em
   [`transcricao.md`](transcricao.md)).
4. **Guarde o payload** (arquivo/bloco de notas) **antes** de fechar a tela de simulação (`[M07]` —
   o operador fechou sem salvar e reenviou um JSON antigo).
5. Envie pelo **Test API** e compare resposta × simulação (`[M10]`).
6. **Validação:** os valores de contrato/parcela e as datas do payload devem corresponder aos da
   simulação; divergência é indício de payload desatualizado (`[M07]`).
7. **Exceções:** se a API recusar o modelo, ver o Fluxo C e a conversa irmã
   [`../conversa-jonas-testa-api/procedimentos.md`](../conversa-jonas-testa-api/procedimentos.md).

## Fluxo B — Selecionar operações elegíveis para o refinanciamento

| Item | Conteúdo |
|---|---|
| **Objetivo** | Escolher contratos de origem que o negócio aceita em um refin |
| **Pré-condições** | Cliente com mais de uma operação; simulação aberta; acesso de leitura à base de teste |
| **Entradas** | CPF do cliente de teste; lista de operações exibida na simulação |
| **Fonte** | `[M13]`, `[M14]`, `[M16]`, `[M17]`, `[M18]` |
| **Resultado esperado** | Payload com `OperacoesRefin` contendo **somente** operações elegíveis |

1. Na simulação, observe a lista de contratos do cliente (`[M16]`).
2. **Descarte** os contratos apresentados em vermelho — não é possível usá-los (`[M16]`, `[M17]`).
3. Trabalhe **apenas** com os contratos que permitem ser marcados (`[M18]`).
4. Havendo dúvida sobre o estado das operações, **consultar a base por CPF** — o tester indica “dar um
   select na coper com seu cpf” (`[M14]`). **Alvo/ambiente não informados**; consulta somente de
   leitura e apenas em ambiente de teste — ver [`incertezas.md`](incertezas.md) itens 1 e 2.
5. Verifique se alguma das operações do refin está **quitada**: isso inviabiliza a proposta
   (`[M13]`).
6. Monte `OperacoesRefin.OperacoesRefin[].NumeroOperacao` com as operações válidas (`[M07]`).
7. **Validação:** a contagem de operações no payload deve ser a mesma das operações marcadas na
   simulação (`[M16]`–`[M18]`).
8. **Exceção conhecida:** todas as operações do cenário quitadas → trocar de cliente/massa; a fonte
   não descreve contorno dentro do mesmo contrato (`[M13]`).

## Fluxo C — Corrigir dado cadastral e reenviar

| Item | Conteúdo |
|---|---|
| **Objetivo** | Corrigir inconsistência de dado cadastral antes de considerar o teste concluído |
| **Pré-condições** | Payload já enviado e resposta recebida |
| **Entradas** | JSON enviado; tela de simulação |
| **Fonte** | `[M02]`, `[M03]`, `[M07]` |
| **Resultado esperado** | Payload novo, com o dado corrigido, e histórico do envio antigo descartado |

1. Compare o payload enviado com a tela de simulação, campo a campo — em especial
   `DadoCadastral.DadoProfissional.NumeroMatricula` (`[M02]`).
2. Corrija o dado **na simulação**, salve a tela e **recapture** o payload (`[M07]`).
3. Reenvie pelo Test API (`[M10]`).
4. **Validação:** conferir que o payload reenviado é o novo (não o antigo de bloco de notas) —
   comparar ao menos matrícula, contratos e valores (`[M07]`).
5. **Observação de negócio:** a inclusão **passa** mesmo com matrícula incorreta (`[M03]`) — a
   ausência de erro **não** é prova de dado correto.

## Fluxo D — Triagem da falha antes de escalar

| Item | Conteúdo |
|---|---|
| **Objetivo** | Não abrir incidente por erro de massa de teste e escalar pelo canal certo |
| **Pré-condições** | Envio rejeitado ou comportamento inesperado |
| **Entradas** | Mensagem de erro; payload; comparação com a simulação |
| **Fonte** | `[M04]`, `[M05]`, `[M11]`–`[M13]` |
| **Resultado esperado** | Classificação correta (dado de teste × falha de sistema) e encaminhamento registrado |

1. Verifique se o erro vem de **dado de teste** (matrícula, contrato quitado, massa inválida) — nesse
   caso **não é incidente** (`[M04]`): corrija e siga.
2. Verifique se o erro vem da **API** (modelo, contrato de entrada) — nesse caso use o fluxo de
   escalada da conversa irmã (`manda no grupo` / pareamento com o responsável pela API —
   [`../conversa-jonas-testa-api/procedimentos.md`](../conversa-jonas-testa-api/procedimentos.md) Fluxo C).
3. Compare sempre com a simulação do Autorizador antes de concluir que o sistema está errado
   (`[M05]`, `[M16]`).
4. Registre a conclusão do teste com o payload efetivamente enviado (`[M07]`).

## Sequência mínima resumida (para o dia a dia)

```
simular no Autorizador  →  escolher só contratos elegíveis  →  montar payload
        →  guardar payload  →  enviar pelo Test API  →  comparar com a simulação
        →  corrigir dado de teste (sem incidente)  →  escalar só o que for de API
```
