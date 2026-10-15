# Guia de estudo — automação de testes e trilha de estudo (Oscar)

- **Categoria:** `PROCESSOS`, `SISTEMAS`, `NEGOCIO`, `DÚVIDA_OU_CONFLITO` (sem `SQL`)
- **Sistema:** Função Sistemas — alvos da automação proposta (**testes padrão** e **testes de API**) e
  **PSA/PEGEUT** (configuração de pauta/esteira, segundo o contexto)
- **Assunto:** como decidir **o que automatizar** em um time de CQ; proposta de PoC com **Cypress**;
  **regra de negócio** como competência que não se terceiriza para ferramenta; e uma **lacuna** de
  conhecimento registrada (PSA/PEGEUT).
- **Fonte:** recorte textual de conversa de trabalho com **Oscar**, fornecido pelo responsável em
  **2026-10-15**; âncoras `[Mnn]` conforme [`../CONVENCOES_FONTES_TEXTUAIS.md`](../CONVENCOES_FONTES_TEXTUAIS.md)
- **Confiança da extração:** **alta** para o **conteúdo das opiniões e da proposta** (transcritas
  literalmente); **baixa** para contexto operacional — a fonte **não** diz o que é PSA nem PEGEUT, não
  informa qual sistema é alvo da PoC, não tem data e não atribui autoria com segurança.

## 1. Contexto

Duas conversas curtas entre colegas de trabalho. Na primeira (`[M01]`–`[M17]`), o assunto é **estudo e
competência técnica**: o que vale mais — saber programar, saber automação ou entender a **regra de
negócio** — e, no meio, surge uma **proposta de melhoria** para a Função. Na segunda (`[M18]`–`[M26]`),
o tema é um **problema operacional urgente** de configuração em **PSA/PEGEUT**.

## 2. O que a conversa ensina

### 2.1 Automação não substitui conhecimento de negócio (`[M01]`–`[M05]`, `[M08]`)

| Âncora | Fala | Leitura |
|---|---|---|
| `[M01]`, `[M02]` | “acabo estudando muito pouco código e mais automação, aplicações, coisas de ia”; “pessoas que usem essas ferramentas” | Autocrítica: o estudo migrou para **automação/aplicações/IA** |
| `[M04]`, `[M05]` | “tenho esse pensamento tbm”; “mas ao mesmo tempo gente que entende regra de negócio” | O contraponto que sustenta a relevância do profissional: **quem entende a regra** |
| `[M08]` | “sim, isso vai ser cada vez mais necessário” | **[inferência]** Competência que tende a valorizar, não a ser substituída pela ferramenta |

**Consequência para o estudo:** ferramenta (Cypress, IA, automação) é meio; **processo e regra de
negócio** são o que define o que testar, o que é resultado esperado e o que é falha. Esse princípio
aparece também na conversa com Gabriel: para automatizar/gerar EPTs com IA, primeiro é preciso
**compreender bem os processos** ([`../conversa-gabriel-comunicacao-estudos/guia_de_estudo.md`](../conversa-gabriel-comunicacao-estudos/guia_de_estudo.md)).

### 2.2 Proposta de PoC com Cypress na Função (`[M09]`–`[M12]`)

- **Objetivo declarado:** “agilizar alguns testes padrão / tipo api e etc” (`[M09]`, `[M10]`).
- **Stack informada:** **JavaScript** (`[M12]`).
- **Estado de conhecimento do time:** a outra parte “ainda não tive contato com o Cypress” (`[M11]`).
- **[inferência]** É uma **ideia a experimentar** (“ver se funciona”), não um plano aprovado — o
  material registra como **proposta**, jamais como prática vigente.
- **Ligação com o acervo:** o conhecimento acumulado de **API** (conversas sobre
  `FIApiAutIncluirProposta`, Test API e payload de refin — [`../conversa-matheus-refin-api/`](../conversa-matheus-refin-api/)
  e [`../conversa-jonas-testa-api/`](../conversa-jonas-testa-api/)) é exatamente a matéria-prima de
  “testes padrão de API”. Automatizar antes de entender o contrato da API só automatiza o erro.

### 2.3 Lacuna identificada: PSA/PEGEUT (`[M20]`–`[M26]`)

| Âncora | Fala | Leitura |
|---|---|---|
| `[M20]`, `[M21]` | “tentando achar uma configuração no psa meio urgente”; “assumi a pauta de colega, e psa ta um porre” | Configuração de PSA é **difícil e demorada**; a demanda chegou por **assunção de pauta de colega** |
| `[M22]` | “Tranquilo! Vou dar um salve por aqui” | Pedido de ajuda a terceiros dentro do time |
| `[M23]`, `[M24]` | “por acaso já pegou psa?” / “nunca” | **Ninguém** na conversa tem experiência com PSA |
| `[M25]`, `[M26]` | “po psa/pegeut” / “chato pra algumas config” | A dor está na **configuração**, e PSA/PEGEUT aparecem associados |

**Ação decorrente:** PSA/PEGEUT entra na **lista de lacunas de cobertura** do acervo, com pedido de
material (ver [`incertezas.md`](incertezas.md) item 3 e
[`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md)).

### 2.4 Um sinal de método (`[M18]`)

“As conexões que o arena oferece se vc ficar atualizando kkkk” — registro de que ferramentas de
assistente **com conectores** já fazem parte da rotina de trabalho/estudo. **[inferência]** Vale como
inventário de ferramenta, não como fonte técnica: nada nesta conversa ensina a configurar nada.

## 3. Trilha de estudo que se deriva desta conversa

| Etapa | Conteúdo | Como fechar o ciclo no acervo |
|---|---|---|
| 1 | **Fundamentos de teste de API** — entrada, contrato, mensagens de erro, massa de teste | Já coberto em [`../conversa-jonas-testa-api/`](../conversa-jonas-testa-api/) e [`../conversa-matheus-refin-api/`](../conversa-matheus-refin-api/) |
| 2 | **JavaScript para automação** (base do Cypress) | **Lacuna** — sem material no acervo |
| 3 | **Cypress** — seletores, comandos, testes de UI e de requisição; critérios de estabilidade | **Lacuna** — a fonte só cita o nome |
| 4 | **O que automatizar primeiro** — testes “padrão”, repetitivos e estáveis; nunca processo que ainda está mudando | Regra derivada de `[M09]`–`[M11]` |
| 5 | **Regra de negócio da Função** — convênio, produto, esteira, condições de crédito | Já coberto em [`../GLOSSARIO_GERAL.md`](../GLOSSARIO_GERAL.md) e nos guias dos vídeos |

> **Ordem importa:** a própria conversa sugere que a competência de negócio é a que se valoriza
> (`[M05]`, `[M08]`). Automatizar sem entender isso produz teste que passa e sistema que erra.

## 4. Riscos e cuidados

- **Não tratar a PoC como aprovada.** `[M09]` é intenção de quem estuda o assunto; não há aprovação,
  escopo, ambiente ou prazo na fonte.
- **Não automatizar ambiente de produção** nem introduzir ferramenta nova sem aval do time — a fonte
  não menciona autorização de nenhum tipo.
- **Não usar PSA/PEGEUT como se soubéssemos o que é.** A conversa prova apenas que **existem**, que
  **dão trabalho** e que **ninguém ali tem experiência**.
- **Autoria das falas não é confiável**: o recorte não marca quem disse o quê — não citar pessoas nas
  conclusões (ver [`incertezas.md`](incertezas.md) item 1).

## 5. Resumo de uma linha

Ferramenta nova (Cypress) é bem-vinda para **testes padrão/API** — desde que o alvo seja escolhido por
quem **entende a regra de negócio**, que a PoC seja autorizada, e que as lacunas reais do time
(**PSA/PEGEUT**, JavaScript/Cypress) entrem em uma **trilha de estudo explícita**.
