> **Fonte textual** fornecida pelo responsável em **2026-10-15**; identificadores diretos e
> hospedeiros de rede interna mascarados. Nomes de operadores da Função preservados conforme
> autorização registrada em [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md).

# Procedimentos — depuração no Test API (Jonas)

Reproduzem o que a conversa ensina. **Nada foi executado nesta análise** (nenhuma chamada de API,
nenhum teste, nenhuma alteração). Os fluxos são **método relatado**, não runbook homologado.

## Fluxo A — Diagnosticar crítica de modelo no Test API

| Item | Conteúdo |
|---|---|
| **Objetivo** | Descobrir qual campo faz a API recusar o corpo, sem tentativa às cegas |
| **Pré-condições** | Payload de refin conhecido (ideal: capturado da simulação do Autorizador); acesso ao Test API no ambiente correto (Fluxo B) |
| **Entradas** | JSON de entrada; retorno com `MENSAGEM`/`CODIGO` |
| **Fonte** | `[M06]`, `[M07]`, `[M09]`, `[M11]`, `[M13]`, `[M14]`, `[M16]` |
| **Resultado esperado** | Campo culpado identificado com a mensagem de erro como evidência |

1. Confirme se os campos foram preenchidos **na própria ferramenta Test API** — a pergunta que Jonas
   faz antes de qualquer hipótese (`[M07]`).
2. **Reduza o payload ao mínimo**: preencha **somente o número da operação** (`[M11]`) e **deixe de
   fora** o campo sob suspeita (`[M09]`).
3. Envie e **leia a crítica por inteiro**: `Modelo de entrada de dados inválido` +
   `Error converting value {null} to type '…Models.SubTipoRefin'` +
   `Path 'OperacoesRefin.SubTipoRefin'` + `line 1, position 1117` + `CODIGO` (`[M13]`).
4. Localize o campo indicado no `Path` no JSON **minificado** enviado; use `line`/`position` para
   achar a posição.
5. **Reintroduza um campo por vez**, observando quando a crítica muda (`[M14]`).
6. **Validação:** o diagnóstico termina quando a API deixa de recusar o **modelo** (o corpo é aceito
   e a resposta passa a tratar de negócio) ou quando se chega a um campo **indispensável**.
7. **Exceção/limite:** removendo `NumeroOperacao`, a API **pede o número da operação** (`[M16]`) —
   não há mais o que remover; pare de ajustar payload e vá para o Fluxo C.
8. **Correção apontada pela evidência:** `SubTipoRefin` deve ir **preenchido com valor válido**; a
   conversa irmã mostra `"NaoDefinido"` em um envio que passou — **hipótese a confirmar**
   ([`incertezas.md`](incertezas.md) item 2).

## Fluxo B — Confirmar o endpoint/ambiente antes de testar

| Item | Conteúdo |
|---|---|
| **Objetivo** | Evitar depurar payload quando o problema é o caminho de publicação usado |
| **Pré-condições** | Payload pronto; intenção de testar refin pela API |
| **Entradas** | URL completa do endpoint em uso |
| **Fonte** | `[M03]`, `[M04]`, `[M05]` |
| **Resultado esperado** | Caminho/ambiente declarado antes de qualquer conclusão sobre payload |

1. Anote **o caminho completo** do endpoint usado (é a primeira coisa que Jonas pede: `[M03]`).
2. Compare com os caminhos conhecidos no acervo:
   - `http://<servidor>/Mesa C6/Regressivo 540791/FIApiAutIncluirProposta/` (`[M04]`);
   - `http://<servidor>/C6/Api/FIApiAutIncluirProposta/` (`[M05]`).
3. Se os caminhos diferirem, trate como **publicações distintas**: informe a URL ao pedir ajuda
   (`[M01]`–`[M05]` mostram o operador relatando que trocou de caminho justamente por não estar
   conseguindo).
4. **Validação:** antes de escalar, ambos os lados (quem reporta e quem ajuda) devem estar falando do
   **mesmo** endpoint.
5. **Cuidado:** a fonte **não** confirma qual publicação é a vigente — não padronizar por conta
   própria ([`incertezas.md`](incertezas.md) item 4).

## Fluxo C — Classificar e escalar a falha

| Item | Conteúdo |
|---|---|
| **Objetivo** | Encaminhar o problema pelo caminho que a equipe usa, com reprodução por outra pessoa |
| **Pré-condições** | Payload reduzido ao mínimo (Fluxo A) e campo indispensável identificado |
| **Entradas** | Mensagem de erro; endpoint; tentativas feitas; payload mínimo |
| **Fonte** | `[M15]`, `[M17]`, `[M18]`, `[M22]`, `[M24]` |
| **Resultado esperado** | Caso visível para o time, com alguém reproduzindo e o dono da API envolvido |

1. Forme a hipótese e nomeie-a como tal: “parece incidente” (`[M15]`) — **hipótese**, não conclusão.
2. **Leve ao grupo** para ver se outra pessoa consegue ajudar (`[M17]`).
3. **Reproduza em paralelo** — a mesma pessoa que orienta tenta do lado dela (`[M18]`, `[M24]`).
4. **Envolva o dono da frente de API** (Santana chama para ver junto, `[M22]`).
5. **Validação:** a escalada só está completa quando há descrição do erro (**texto do retorno**), do
   **endpoint** e do **payload mínimo** que reproduz.
6. **Exceção:** se a causa for **dado de teste** (massa inválida, contrato quitado), **não** é
   incidente — ver Fluxo D de
   [`../conversa-matheus-refin-api/procedimentos.md`](../conversa-matheus-refin-api/procedimentos.md).

## Fluxo D — Conferir aderência entre a proposta criada e o payload

| Item | Conteúdo |
|---|---|
| **Objetivo** | Evitar erro de pareamento entre a proposta existente e os dados enviados |
| **Pré-condições** | Proposta criada no sistema; payload montado a partir dela |
| **Entradas** | Identificação da proposta (cliente/CPF) e o payload enviado |
| **Fonte** | `[M01]`, `[M02]` (registro mascarado) |
| **Resultado esperado** | Payload apontando para o **mesmo** cliente/proposta do cenário |

1. Antes de enviar, confira que o **cliente do payload** é o mesmo da **proposta criada** (`[M01]`).
2. Não reutilize payload de outro cenário: a troca de CPF aparece como fonte de confusão na conversa
   (`[M01]`, `[M02]`).
3. **Validação:** CPF/nome na proposta = CPF/nome no payload (ou o identificador de proposta usado
   pelo fluxo).
4. **Observação:** a fonte **não** afirma que o CPF diverge no envio do Test API nem que isso gere erro
   — é conferência preventiva, marcada como **[inferência]**.

## Sequência mínima resumida

```
pegar/validar o endpoint  →  reduzir o payload ao mínimo  →  enviar no Test API
     →  ler MENSAGEM/PATH/CODIGO  →  reintroduzir campo a campo  →  travar no campo indispensável
     →  mandar no grupo + reproduzir em paralelo + envolver o dono da API
```
