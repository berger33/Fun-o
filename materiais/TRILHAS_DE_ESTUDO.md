# Trilhas de estudo — o que estudar a partir das conversas (2026-10-15)

Consolida, em **ordem de execução**, o que as cinco conversas de trabalho revelaram sobre competências a
desenvolver e onde cada assunto se apoia no restante do acervo. Cada trilha sai de uma **necessidade
nomeada na fonte** — não é lista genérica de cursos.

> **Origem:** [`conversa-matheus-refin-api/`](conversa-matheus-refin-api/LEIA-ME.md),
> [`conversa-jonas-testa-api/`](conversa-jonas-testa-api/LEIA-ME.md),
> [`conversa-cler-artefatos-acesso/`](conversa-cler-artefatos-acesso/LEIA-ME.md),
> [`conversa-oscar-automacao-testes/`](conversa-oscar-automacao-testes/LEIA-ME.md) e
> [`conversa-gabriel-comunicacao-estudos/`](conversa-gabriel-comunicacao-estudos/LEIA-ME.md).
> **Regra de ouro que atravessa tudo:** *processo e regra de negócio primeiro; ferramenta depois*
> (`[P12]` da conversa com Gabriel; `[M05]`, `[M08]` da conversa com Oscar).

## Trilha 1 — Testar refinanciamento pela API (prioridade alta: é a dor atual)

| Ordem | Assunto | Onde estudar | Como saber que aprendeu |
|---|---|---|---|
| 1.1 | Fluxo do refin e papel das operações de origem | [`conversa-matheus-refin-api/guia_de_estudo.md`](conversa-matheus-refin-api/guia_de_estudo.md) §3.4 | Explicar por que uma operação quitada inviabiliza o cenário (`[M13]`) |
| 1.2 | Payload campo a campo (cabeçalho, origens, condição de crédito, pagamento, cadastro) | idem §§3.1–3.6 | Montar o payload a partir da simulação do Autorizador |
| 1.3 | Mensagem de erro de modelo e como lê-la | [`conversa-jonas-testa-api/guia_de_estudo.md`](conversa-jonas-testa-api/guia_de_estudo.md) §3 | Localizar campo pelo `Path` e `position` sem tentativa às cegas |
| 1.4 | Método de isolamento de campo no Test API | [`conversa-jonas-testa-api/procedimentos.md`](conversa-jonas-testa-api/procedimentos.md) Fluxo A | Reduzir o payload e reintroduzir campo a campo |
| 1.5 | Elegibilidade de contratos na tela de simulação | [`conversa-matheus-refin-api/procedimentos.md`](conversa-matheus-refin-api/procedimentos.md) Fluxo B | Distinguir contrato utilizável de inutilizável antes de montar o cenário |
| 1.6 | Comparação com os contratos já documentados do envio ao sistema externo | [`jonas-ept-explicacao/guia_de_estudo.md`](jonas-ept-explicacao/guia_de_estudo.md) §§3–6 | Ligar payload → monitor (`ECONSULT`/`ECONSULTD`) |

**Lacunas desta trilha:** catálogo de erros da API (`100000002`), enum completo de `SubTipoRefin`,
ambiente/tabela `coper`, publicação vigente do endpoint. **Peça validação** antes de fixar qualquer uma
delas ([`CONFLITOS_E_VALIDACAO.md`](CONFLITOS_E_VALIDACAO.md)).

## Trilha 2 — Automação de testes (Cypress + API)

Sai da proposta de `[M09]`–`[M12]` (conversa com Oscar) e do acervo de API.

| Ordem | Assunto | Onde estudar | Observação |
|---|---|---|---|
| 2.1 | Fundamentos de teste de API: entrada, contrato, massa, resultado esperado | [`conversa-jonas-testa-api/`](conversa-jonas-testa-api/) e [`conversa-matheus-refin-api/`](conversa-matheus-refin-api/) | base já existente no acervo |
| 2.2 | **JavaScript** — base para o Cypress | **lacuna** — sem material no acervo | incluir na fila de estudo |
| 2.3 | **Cypress**: seletores, comandos, interceptação de requisição, estabilidade de teste | **lacuna** — a fonte só cita o nome (`[M09]`) | pedir/obter material próprio |
| 2.4 | Escolher o alvo: teste repetitivo, estável e com resultado esperado claro | [`conversa-oscar-automacao-testes/procedimentos.md`](conversa-oscar-automacao-testes/procedimentos.md) Fluxo A | nunca começar por processo em mudança |
| 2.5 | Relação com a EPT: automatizar cenários já escritos em planilha de CQ | [`como-fazer-ept/guia_de_estudo.md`](como-fazer-ept/guia_de_estudo.md) e [`jonas-ept-explicacao/`](jonas-ept-explicacao/) | ponte entre CQ e automação |

**Regra de segurança:** PoC **não aprovada** na fonte; ambiente de teste e aval do time são
pré-requisito. Nada aqui autoriza introduzir ferramenta em ambiente de trabalho
([`conversa-oscar-automacao-testes/incertezas.md`](conversa-oscar-automacao-testes/incertezas.md) item 2).

## Trilha 3 — IA aplicada às rotinas (RAG, automação assistida)

Sai da trilha declarada em `[P12]` (conversa com Gabriel): hackathon de IA da Oracle, certificação de
**Fundamentos de IA e RAG**, prática de **testes automatizados com IA** em projetos pessoais.

| Ordem | Assunto | Por quê | Onde encaixa |
|---|---|---|---|
| 3.1 | Fundamentos de IA e RAG (já certificado) | base declarada | manter prática ativa |
| 3.2 | **Modelagem de processo antes de automatizar** | pré-requisito declarado pelo próprio autor: “compreenda muito bem todos os processos daqui” | este acervo é a fonte: cada pacote é um processo documentado |
| 3.3 | EPT: estrutura, colunas e critérios | candidato natural a geração assistida | [`jonas-ept-explicacao/guia_de_estudo.md`](jonas-ept-explicacao/guia_de_estudo.md) §5 |
| 3.4 | Documentação de sistema como base de conhecimento (SIC/GED/API) | alimenta qualquer assistente que “entenda as rotinas” | [`SISTEMAS/INDICE_SISTEMAS.md`](SISTEMAS/INDICE_SISTEMAS.md) |
| 3.5 | Pedir orientação a quem já é referência | o pedido de “dicas de conteúdo” é explícito em `[P12]` | conversa com o analista |

## Trilha 4 — Ambiente, artefatos e acesso

Sai da conversa com Cler. **Trilha curta e bloqueada por informação** — o primeiro passo é perguntar, não
estudar.

| Ordem | Assunto | Situação |
|---|---|---|
| 4.1 | O que é **UDL**, conteúdo e canal oficial de obtenção | **lacuna** — nenhuma fonte do acervo define |
| 4.2 | **SETHI**: o que é e como se ambienta (usa `DIG A`?) | **lacuna** — relato oral, a validar |
| 4.3 | Obtenção de pacote de módulo (ex.: **Web Empregador**) | procedimento **parcial**: quem tem / quem conhece / download autorizado |
| 4.4 | Rotina de “subir base” e trocar pasta compartilhada | já mapeada em [`gravando-2026-07-07-155307/`](gravando-2026-07-07-155307/) — conferir antes de mexer |

## Trilha 5 — Comunicação e trabalho em equipe

Sai da conversa com Gabriel.

| Ordem | Assunto | Como praticar |
|---|---|---|
| 5.1 | Explicar perfil de comunicação (objetividade, feedback direto, literalidade) | roteiro de [`conversa-gabriel-comunicacao-estudos/procedimentos.md`](conversa-gabriel-comunicacao-estudos/procedimentos.md) |
| 5.2 | Escolher canal e formato por interlocutor | mensagens de autodescrição ganham com **resumo + tópicos** (`[P11]` fala do “textão”) |
| 5.3 | Pedir ajuda cedo, sem medo de incomodar | receio explícito em `[P5]`; porta aberta em `[P1]` |
| 5.4 | Escalar dúvida técnica pelo caminho certo | padrões em [`conversa-jonas-testa-api/procedimentos.md`](conversa-jonas-testa-api/procedimentos.md) Fluxo C e [`conversa-cler-artefatos-acesso/`](conversa-cler-artefatos-acesso/) |
| 5.5 | Registrar o que foi combinado | nenhum acordo sobrevive sem registro — ver [`conversa-gabriel-comunicacao-estudos/incertezas.md`](conversa-gabriel-comunicacao-estudos/incertezas.md) item 4 |

## Trilha 6 — Lacunas de sistema que o acervo ainda não cobre

| Lacuna | Origem | O que pedir |
|---|---|---|
| **PSA / PEGEUT** | `[M20]`–`[M26]` (Oscar) | gravação/treinamento de configuração |
| **SETHI / DIG** | `[M08]`, `[M14]` (Cler) | material de ambientação |
| **JavaScript / Cypress** | `[M09]`–`[M12]` (Oscar) | curso/material próprio (fora do acervo interno) |
| Catálogo de erros da API de inclusão | `[M13]` (Jonas) | documento de contrato/erros com o time de API |
| Tela de simulação de refin (contratos inutilizáveis) | `[M16]`–`[M19]` (Matheus) | demonstração em gravação, sanitizada |

## Como usar estas trilhas

1. **Escolha uma trilha por vez** e marque o item que está em andamento.
2. Cada item aponta para o **documento-fonte** dentro do acervo: estude no material, não em anotação solta.
3. Ao concluir um item, atualize o `incertezas.md` do pacote correspondente com o que ficou esclarecido —
   é assim que uma dúvida deixa de ser dúvida.
4. **Não** avance para ferramenta (Cypress, IA) sem ter fechado a parte de **processo** daquele assunto:
   é a ordem que as próprias conversas defendem.
