> **Fonte textual** fornecida pelo responsável em **2026-10-15**; sem identificadores diretos a
> mascarar.

# Procedimentos — automação de testes e trilha de estudo (Oscar)

**Nada foi executado nesta análise** (nenhuma ferramenta instalada, nenhum teste automatizado, nenhum
ambiente ou configuração tocada). Os fluxos abaixo são **método derivado da conversa** — proposta e
raciocínio, não prática homologada.

## Fluxo A — Avaliar uma PoC de automação de testes (Cypress)

| Item | Conteúdo |
|---|---|
| **Objetivo** | Testar, com escopo pequeno, se a automação agiliza testes padrão sem criar dívida |
| **Pré-condições** | Processo/feature **estável** e já compreendido; aval do time; ambiente de teste isolado; critério de sucesso acordado |
| **Entradas** | Lista de testes “padrão” repetitivos (ex.: casos de API), ferramenta (Cypress, JavaScript) |
| **Fonte** | `[M09]`, `[M10]`, `[M11]`, `[M12]` |
| **Resultado esperado** | Decisão fundamentada: manter, ajustar escopo ou descartar a ferramenta |

1. **Escolha o alvo pelo conhecimento de negócio**, não pela facilidade da ferramenta: testes
   repetitivos, com resultado esperado claro e **processo já estabilizado** (`[M09]`, `[M10]`).
2. Considere o custo de aprendizagem: o time pode não ter contato prévio com a ferramenta
   (`[M11]` — “ainda não tive contato com o Cypress”).
3. Prepare o mínimo de stack necessária — no relato, **JavaScript** (`[M12]`).
4. Rode a PoC **em ambiente de teste**, sobre um caso já conhecido (bom candidato: um cenário de API
   já documentado em [`../conversa-matheus-refin-api/procedimentos.md`](../conversa-matheus-refin-api/procedimentos.md)).
5. **Validação:** a automação deve reproduzir o **mesmo resultado esperado** do teste manual e falhar
   quando o comportamento mudar (teste que nunca falha não é teste).
6. **Exceções/limites:** se o processo ainda muda com frequência, **não automatizar** — o custo de
   manutenção supera o ganho.
7. **Registro:** o resultado da PoC (o que funcionou, o que não, esforço) deve virar material do
   acervo, com ambiente, versão da ferramenta e limitações.

## Fluxo B — Transformar uma dor operacional em trilha de estudo

| Item | Conteúdo |
|---|---|
| **Objetivo** | Não depender de ajuda de terceiros para configurações recorrentes |
| **Pré-condições** | Dor identificada e recorrente; demanda real (aqui: configuração em PSA, urgente) |
| **Entradas** | Nome do sistema/parâmetro; sintoma; o que já foi tentado |
| **Fonte** | `[M20]`, `[M21]`, `[M23]`, `[M24]`, `[M25]`, `[M26]` |
| **Resultado esperado** | Pedido de ajuda qualificado **e** item aberto no acervo de lacunas |

1. Descreva o problema em termos de **configuração** (“tentando achar uma configuração no psa”,
   `[M20]`) — isso separa dificuldade de parâmetro de defeito de sistema.
2. **Peça ajuda qualificada**: pergunte quem já pegou o sistema (`[M23]`) em vez de só relatar a dor.
3. Se a resposta for “nunca” (`[M24]`), registre a **lacuna de cobertura** do time (ver
   [`incertezas.md`](incertezas.md) item 3) e leve a demanda para quem administra o sistema.
4. **Validação:** quando existir documentação/gravação sobre PSA/PEGEUT, atualizar este pacote e o
   [`../INDICE.md`](../INDICE.md).
5. **Cuidado:** “urgente” (`[M20]`) **não** autoriza alterar configuração sem seguir o procedimento
   vigente; a fonte não descreve nenhum parâmetro nem caminho.

## Fluxo C — Manter a trilha de estudo acoplada ao trabalho

| Item | Conteúdo |
|---|---|
| **Objetivo** | Estudar o que tem aplicação direta e registrar o que foi aprendido |
| **Fonte** | `[M01]`, `[M05]`, `[M06]`, `[M08]`, `[M18]` |
| **Resultado esperado** | Trilha com prioridades claras: negócio → processo → ferramenta |

1. Priorize o que **explica o negócio** (regra, cadastro, esteira, condição de crédito) — é o
   contraponto que a própria conversa destaca (`[M05]`, `[M08]`).
2. Ao estudar ferramenta (automação, IA, Cypress), ancore sempre em um **caso real da Função**
   (`[M09]`).
3. Use este repositório como plano de estudos: cada pacote de vídeo é uma trilha de processo.
4. **Validação:** a cada ciclo, registrar o que mudou de entendimento em `incertezas.md` do pacote
   correspondente — estudo que não deixa rastro se perde.

## Sequência mínima resumida

```
escolher o alvo pelo processo (não pela ferramenta)  →  checar aval e ambiente de teste
        →  PoC com critério de sucesso  →  registrar resultado  →  transformar a dor restante em trilha de estudo
```
