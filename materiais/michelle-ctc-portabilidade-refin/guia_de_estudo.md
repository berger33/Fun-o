# Guia de estudo — MICHELLE CTC PORTABILIDADE REFIN.mp4

- **Categoria:** `PROCESSOS`, `SISTEMAS`, `NEGOCIO`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO` (sem SQL demonstrado)
- **Sistema:** esteiras (modelos de decisão) de portabilidade e de refinanciamento no ecossistema Autorizador/CTC da Função Sistemas; nenhuma tela de produto é aberta — a única imagem exibida é um fluxograma exportado (`…portabilidade-Refin - Port.drawio.png`) desenhado para **outro cliente**.
- **Assunto:** como o acionamento (`CTC – Aciona Esteira de Refinanciamento`) e a espera (`CTC – Aguarda Analise do Refin de Portabilidade`) coordenam proposta de portabilidade e proposta de refim; e o desenho de um teste para verificar se a portabilidade pode avançar sem dependência do refim.
- **Fonte:** `MICHELLE CTC PORTABILIDADE REFIN.mp4` — 473540507 bytes; SHA-256 `621565bd…`; duração `00:16:56.62` (fala até `00:16:50.26`).
- **Confiança da extração:** **média** no visual (rótulos e nuvens do fluxograma lidos dos quadros, com timestamp); **média/baixa** na fala (ASR automático, termos conferidos contra a tela quando possível); **baixa** na regra de sincronização entre as propostas (a conversa não conclui e nenhum teste é executado).

> **Publicação autorizada pelo responsável em 2026-10-13** (dados declarados fictícios/de teste; nomes de operadores preservados). Este lote foi analisado a partir da **fonte primária**, com bytes conferidos. As capturas publicadas são recortes do fluxograma: sem participantes da reunião, sem barra de tarefas e sem títulos com nomes completos.

> ⚠️ **Cautela central desta gravação:** a apresentadora declara duas vezes que o desenho de esteira exibido **é de outro cliente e não é exatamente o do C6** (`00:00:05–00:00:23`; `00:15:34–00:16:07`). Os nomes de processos lidos da tela são, portanto, o vocabulário do exemplo — servem para entender o mecanismo, **não** como configuração vigente do cliente-alvo.

## 1. Objetivo e público

A gravação é uma reunião de trabalho em que Michelle explica, sobre um fluxograma de exemplo, o mecanismo que coordena uma proposta de portabilidade e seu refinanciamento (“refim”) vinculado, e combina com Santana (Matheus) e William um teste para responder a uma dúvida do banco/cliente. Serve a quem precisa:

1. entender **por que** a portabilidade, no desenho, não avança antes de o refim ser validado (consistência de valores da CCB — `00:03:36–00:04:59`);
2. reconhecer os dois processos rosa do desenho que fazem a coordenação — **acionar** a esteira do refim (`CTCACIPROPREF`) e **segurar** a portabilidade (`CTCAGANREFIN`) — e o que as anotações do desenho dizem sobre eles;
3. saber **como o teste foi desenhado verbalmente** (duas propostas, duas esteiras, parada na análise de crédito) e, sobretudo, o que **não** ficou decidido (dependência × independência; etapa de espera correta para o C6).

Não é um runbook: nenhuma esteira é configurada, nenhum teste é executado e o desenho mostrado não é o do cliente-alvo.

## 2. Conhecimento sustentado pela gravação

### 2.1 O desenho exibido (fonte visual, `00:00:05–00:16:50`)

- A imagem compartilhada o tempo todo é um fluxograma exportado de uma ferramenta de desenho (arquivo `…portabilidade-Refin - Port.drawio.png`, aberto no visualizador de fotos; título legível em parte em `00:07:10`).
- O desenho tem **duas faixas horizontais** (visíveis no zoom afastado de `00:07:00–00:09:20`), com conectores tracejados entre elas; os rótulos verticais das faixas não são legíveis nos quadros amostrados. Pela sequência das caixas e pela fala, a faixa percorrida primeiro é a da **portabilidade** e a outra, a do **refinanciamento da portabilidade**.
- A apresentadora reforça a natureza do desenho no início e no fim: “é um desenho de uma esteira que foi eu que fiz… **Não é exatamente do C6, é um outro cliente** que eu trabalhava na fábrica… é uma jornada de contratação” (`00:00:05–00:00:18`) e “não precisa se prender a isso não… é só um exemplo de como funciona cada processo de portabilidade” (`00:15:57–00:16:07`).

### 2.2 Faixa da portabilidade até a decisão (tela, `00:00:36–00:01:00`)

Sequência legível no desenho (caixas verdes) e nuvens de anotação transcritas dos quadros:

1. **`Envio/Aguarda Retorno da Núclea`** — precedida por `Notifica Requisição da Núclea` e `Acionamento de Callback (ACNCALLBACK)` (região visível em `00:02:50`).
2. **`CTC – Atualizar Proposta com NU da Portabilidade`** — nuvem: “Processo sem tela responsável por atualizar o número único retornado pela Núclea”.
3. **`CTC - Verificação de Alteração de Saldo e Prazo`** — nuvem: “Processo sem Tela que tem a finalidade de comparar o saldo e o prazo retornado pela Núclea, com os valores digitados na proposta, direcionando a proposta para a situação de pendente caso houver divergência, este processo é importante na esteira pois também atualiza os dados bancários da Instituição originadora.”
4. **`Pendente` → `Recálculo de PMT e Prazo da Portabilidade`** — nuvem: “Processo sem Tela que visa recalcular de acordo com dados retornados pela Núclea os valores da proposta variando a quantidade de parcela e taxa para encontrar o valor da parcela”.
5. **Losango `Tem Refin Vinculado?`** — nuvem lateral: “Caso não exista refin vinculado a proposta seguirá o fluxo de uma portabilidade "pura".” (captura [`01`](capturas/01-tem-refin-vinculado-aciona.png)).

A fala resume esse trecho como “a proposta é cadastrada… passa todo aquele processo… vai lá para o CTC, verifica saldo, volta, faz todo aquele trâmite” (`00:00:36–00:00:51`). Note a grafia do desenho: **Núclea** (a fala usa “CIP” em `00:04:01`; o próprio desenho também usa “CIP” na faixa do refim — §2.5).

### 2.3 O acionamento do refim — `CTCACIPROPREF` (tela + fala, `00:01:00–00:02:40`)

- No ramo **Sim** do losango está a caixa rosa **`CTC – Aciona Esteira de Refinanciamento`** com o mnemônico **`CTCACIPROPREF`** (capturas 01 e 02).
- A nuvem ligada à caixa (transcrição literal do quadro de `00:02:25`): “Processo sem Tela que verificará a última proposta de portabilidade que passar pelo processo, caso seja a última proposta será realizado o acionamento da proposta de refinanciamento. Importante o parâmetro de rotina **"G_AVERERR"** deve estar desligado, a fim de não validar a averbação no momento de andar a esteira de refim.”
- A fala confirma os dois comportamentos: (a) **várias portabilidades para um mesmo refinanciamento** — “todas as portabilidades têm que ter passado nele aqui pra ele poder andar o refim” (`00:02:00–00:02:22`); (b) o refim “não pode estar averbada” (ASR: “verbada”, `00:02:24–00:02:30`) — coerente com o parâmetro citado na nuvem.
- Esclarecimento posterior, atribuído ao Zé: o processo **só aciona, não valida** para “ficar parado” — quem define a parada é a **próxima etapa configurada na esteira**: “é só ele configurar a próxima etapa aqui como verdadeira, se ‘aguarda a alteração unificada’, e ele fica parado ali, até que eles movimentem” (`00:05:31–00:06:00`). Essa é a base da hipótese de que o problema do cliente seria de **configuração**, não de fonte (“não tem nada no fonte [ASR: “font”] que impeça fazer isso… alguma coisa ele tá configurando errado”, `00:14:07–00:14:18`).

### 2.4 A espera da portabilidade — `CTCAGANREFIN` (tela + fala, `00:03:02–00:04:59`)

- Depois do acionamento, a faixa da portabilidade chega à segunda caixa rosa: **`CTC – Aguarda Analise do Refin de Portabilidade`**, mnemônico **`CTCAGANREFIN`** (captura [`03`](capturas/03-aguarda-analise-refin.png)).
- Nuvem ligada à caixa: “Processo sem Tela que permite o bloqueio da proposta de portabilidade de acordo com a situação da proposta de refinanciamento vinculada a ela”.
- A fala descreve o comportamento pretendido no caminho “normal” (tela de cadastro): o processo “joga para lá, ele vai andar o refim e ele para a proposta aqui, até que todas as propostas de refinanciamento estejam, por exemplo, com status de **integrada**” (`00:03:15–00:03:36`). O status “integrada” é **só falado** — não aparece como texto legível no desenho.
- **Justificativa de negócio (fala):** se a portabilidade andasse antes, “ele fez o cadastro da CCB, a CCB saiu com valores diferentes”; por isso o desenho quer o refim **validado antes** de a portabilidade continuar (`00:03:36–00:04:59`).
- A **tela unificada do C6** é apresentada como o caso divergente: “hoje o C6… tem uma tela unificada que… faz o refim e a portabilidade juntos”; para ela, a fala usa o nome **“aguarda alteração unificada”** (`00:02:40–00:03:15`). ⚠️ Nos quadros, **nenhuma caixa com esse nome é enquadrada ou legível** (a câmera permanece sobre `Tem Refin Vinculado?`/`Aciona` nesse intervalo); trate o nome como referência verbal ao comportamento desejado no C6, não como caixa confirmada do desenho.

### 2.5 Faixa do refinanciamento (tela, `00:04:00–00:04:55` e `00:15:00–00:16:40`)

Sequência legível na outra faixa (captura [`04`](capturas/04-inicio-esteira-refim.png)):

1. Círculo **`Início da Esteira`** → **`Analise de Crédito`** → losango **`Existe regras de validação?`** — **Sim** → `Reprova Proposta` → `Acionamento de Callback (ACNCALLBACK)` (nuvem: “Callback para informar a reprovação das propostas”); **Não** → segue.
2. Caixa rosa anotada: **“Parada na esteira para evitar andamento enquanto não retorna o saldo”** (é uma anotação do desenho, não o nome de um processo).
3. **`CTC - Validação de Refinanciamento de Portabilidade Após retorno da CIP (AJREFPORT)`** — nuvem: “Processo **Com Tela** que demostra os valores de portabilidade após o retorno da CIP permitindo alterar os valores da proposta”; ramo para `Reprova Proposta`.
4. **`Notifica as Condições Aprovadas`** → losango **`Condições aprovadas?`** → **Sim** → **`Notifica a geração de documentos no SIC (CCB)`** → `Notifica a etapa de Anexar Arquivos/Formalização da Proposta` → losango `Doc. Obrigatórios Anexados?` (trecho visível em `00:07:05`).

Os conectores **tracejados** entre as faixas (a partir de `CTC – Aciona…` e chegando a `CTC – Aguarda Analise…`) são a representação gráfica do acionamento e da espera entre as duas propostas.

### 2.6 O que o cliente quer mudar (o problema, `00:05:09–00:08:36`)

- O banco quer que **todas** as propostas — vindas da tela unificada ou da tela de cadastro — caiam no **mesmo** processo de espera, em vez de a portabilidade parar no “aguarda análise” do desenho (`00:05:09–00:05:29`).
- O comportamento esperado, na formulação da reunião: depois do acionamento, conseguir **andar a portabilidade sem dependência** do refim (“Eu não tenho que ter dependência, porque hoje esses processos têm dependência… Ele não quer, ele quer continuar andando a esteira de portabilidade”, `00:07:50–00:08:19`).
- O cliente relatou **não conseguir** fazer isso funcionar (`00:06:00–00:06:15`; `00:13:55–00:14:06`); a hipótese de trabalho é **erro de configuração da esteira** no cliente (`00:14:07–00:14:18`). Nenhuma das duas afirmações é verificada na gravação.

### 2.7 O teste combinado (não executado, `00:06:22–00:16:39`)

Síntese do combinado verbal (detalhe e bloqueios em [`procedimentos.md`](procedimentos.md)):

- Cadastrar uma **portabilidade com refim** na tela de cadastro normal: ao gravar a portabilidade, um **pop-up** pergunta se quer fazer o refinanciamento; ao final, o sistema mostra **dois números de proposta** (`00:12:48–00:13:18`).
- Como a equipe “não tem esteiras separadas” por tipo de proposta (`00:11:18–00:11:29`), o teste exige **duas esteiras** (na prática: convênios/produtos diferentes para portabilidade e refim — `00:11:00–00:11:57`).
- Andar com as duas propostas **até a análise de crédito**; deixar o refim **parado na análise**; na esteira da portabilidade, colocar o processo de acionamento seguido da etapa de espera em discussão (“aguarda tela unificada”) — pulando os processos de CTC de envio/atualização, porque “eu não consigo fazer CTC hoje” (`00:06:39–00:07:47`; `00:09:23–00:09:50`).
- Monte uma **“esteirinha bem pequenininha”**: análise de crédito + os processos obrigatórios citados (aciona refim; aguarda) e, se necessário, notificação de condições/liberação; **não** incluir os processos do CTC “do meio” (ASR: “do MEI”, `00:15:17–00:15:28`), porque a equipe não consegue “bater lá” (sem configuração/acesso à integração real).
- A execução fica com **Santana**, acompanhando **William** (“nosso menino novo… tá aprendendo”) e reportando por mensagem (`00:08:47–00:09:23`; `00:13:36–00:13:45`). Não é urgente (“Não tem pressa”, `00:13:47–00:13:54`); o desenho será enviado (“eu mando pra vocês”, `00:15:29–00:15:34`).

## 3. Leitura operacional segura

1. **Não copie o desenho para o C6.** Ele é, por declaração da autora, de outro cliente e apenas ilustra o mecanismo. Obtenha o fluxo vigente do cliente-alvo antes de qualquer configuração.
2. **Use os dois processos rosa como vocabulário do mecanismo, não como mnemônicos confirmados do ambiente:** `CTC – Aciona Esteira de Refinanciamento (CTCACIPROPREF)` e `CTC – Aguarda Analise do Refin de Portabilidade (CTCAGANREFIN)` foram **lidos da tela**, mas pertencem ao desenho de exemplo.
3. **A regra de dependência não foi decidida nesta reunião.** Há duas formulações no mesmo vídeo (portabilidade espera o refim “integrado” × portabilidade anda sem dependência). Registrar como `DÚVIDA_OU_CONFLITO` até decisão de negócio — ver [`incertezas.md`](incertezas.md) §2.
4. **“Pular o CTC” é limitação do ambiente de teste daquela conversa**, não autorização para contornar a integração em qualquer ambiente real; qualquer simulação exige sandbox aprovado.
5. O parâmetro de rotina lido na nuvem (**`G_AVERERR`**) faz parte da anotação do desenho de exemplo; não altere parâmetros em ambiente algum com base apenas nesta gravação.

## 4. Resumo

| Pergunta | Resposta sustentada |
|---|---|
| O desenho é do C6? | **Não** — outro cliente, só exemplo (`00:00:05–00:00:23`). |
| Quem aciona a esteira do refim? | No desenho, `CTC – Aciona Esteira de Refinanciamento (CTCACIPROPREF)`, quando a **última** portabilidade vinculada passa por ele (`00:02:00–00:02:25`). |
| Quem segura a portabilidade? | No desenho, `CTC – Aguarda Analise do Refin de Portabilidade (CTCAGANREFIN)`, conforme a situação do refim vinculado (`00:03:15–00:03:36`). |
| Por que segurar? | Para não gerar/avançar a **CCB** com valores divergentes do refim (`00:03:36–00:04:59`). |
| O que o banco quer? | Unificar a espera (tela unificada = tela de cadastro) e andar a portabilidade **sem dependência** (`00:05:09–00:08:19`). |
| O teste foi executado? | **Não** — foi apenas desenhado e delegado (`00:08:47–00:09:23`). |
| Houve SQL, tela de sistema ou configuração? | **Não** — só o fluxograma compartilhado (`00:00:00–00:16:56`). |
