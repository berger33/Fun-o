> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Zé, Priscilla/Pri, Augusto, Gabriel). Não são publicadas **imagens
> de pessoas** (avatares/câmeras da reunião).

# Transcrição revisada — PROJETO 14-08.mp4

Transcrição automática (`faster-whisper`, `large-v3`; ver
[`metadados.md`](metadados.md)) revisada apenas em pontuação e termos confirmado na tela.
Falantes identificados genericamente quando a atribuição é incerta; o texto bruto está em
[`transcricao_bruta.txt`](transcricao_bruta.txt) / [`transcricao.srt`](transcricao.srt).

- **Apresentador do item 1** — conduz a reunião e apresenta a primeira EF.
- **Zé** — participante que verifica a origem do campo do CNPJ e envia o Gantt.
- **Pri (Priscilla)** — apresentaria a segunda EF; compartilha a tela no início.
- **Apresentador do item 2** — compartilha e apresenta a OS 556576 (tela compartilhada por
  **Augusto**).

## Item 1 — novo campo CNPJ do empregador no envio ao sistema externo

**[00:00:00] — Apresentador do item 1:** Então, o que a gente vai fazer, basicamente? A gente
vai implementar ali no módulo ServCom, no plugin, envio da proposta ao sistema externo um novo
campo. O que seria esse campo? É o CNPJ, que é responsável ali pelo número do cadastro
nacional da pessoa jurídica. Tá bom? Então, para compor as informações desse plugin, que
enviam informações ao sistema externo da instituição para a formalização digital, a gente vai
incluir um novo campo de CNPJ destinado a um envio do número da descrição do Cadastro
Nacional de Pessoa Jurídica do empregador. É isso.

**[00:00:47] — Zé:** Essa informação vem da consulta de margem ou a gente vai ter que puxar
baseado na origem 4 da proposta?

**[00:00:55] — Apresentador do item 1:** Na origem 4, Zé, se eu não me engano. Porque ele está
no meio do bloco lá da ETRACPD **00:00:57–00:01:01**. A consulta que a gente faz lá na consulta
de margem… Deixa eu abrir a EF aqui. Eu digo lá no layout, lá do envio.

**[00:01:10] — Zé:** Não, da ETRACPD mesmo.

**[00:01:27] — Apresentador do item 1:** A gente tem a informação de qual campo que é?

**[00:01:32] — Zé:** Isso eu não tenho.

**[00:01:33] — Apresentador do item 1:** Precisa pegar então. Só que acho que quando a gente
começar lá, é só a gente colocar lá no select **00:01:36**. É quando você pegar a semana para
a Pri, aí a gente põe na EF, Pri, também, para deixar qual o campo que a gente está enviando.
Por favor.

**[00:01:51] — Pri (Priscilla):** Oi, não entendi.

**[00:01:52] — Apresentador do item 1:** O Zé vai pegar da onde que é o campo que a gente vai
enviar a informação. Na verdade, eu perguntei para o negócio. Eu estou perguntando para o
negócio qual é o campo. Então, a gente pode até ver com alguém do empregador lá para a gente
ver se a gente consegue achar essa informação, mas aí eu teria que colocar na EF esse cara de
qualquer forma. Você vai complementar aí: `ETRACPD.<nome do campo>` **00:02:13–00:02:15**, só
para a gente ter registrado.

**[00:02:18] — Apresentador do item 1:** Qualquer um… eu não sei se tá ruim… só para mim,
gente, eu não tô ouvindo, tá um pouco abafado agora.

**[00:02:23] — Zé / participantes:** Tá ruim, tá ruim.

**[00:02:26] — Apresentador do item 1:** Porra desse notebook… tá me ouvindo?

**[00:02:35] — Zé:** Eu já falei com a infra, agora acho que eu finalmente vou arrumar essa
porra **00:02:35–00:02:40**.

**[00:02:40] — Apresentador do item 1:** A gente só vai incluir ali na última coluna depois o
nome do campo **00:02:40–00:02:43**. Tá vendo que tem vários campos `ETRACPD.<alguma coisa>`?
A gente vai colocar um `ETRACPD.<nome do campo>` ali só, só isso. É. O Zé vai ver qual é o
nome, vai mandar para a gente e a gente vai colocar depois **00:02:52–00:03:00**.

**[00:03:00] — Apresentador do item 1:** Alguém tem mais alguma dúvida?

**[00:03:05] — Participante:** Sim, aí eu posso cadastrar proposta do meu cliente com o CPF
normal dele ainda? Então eu vou ter que cadastrar usando o CNPJ?

**[00:03:13] — Apresentador do item 1:** Não, pode cadastrar normal. E aí vai entrar no
empregador então isso. Porque aí tá falando, a descrição dele é esse projeto do empregador, né?

**[00:03:20] — Participante:** Isso. Tá.

**[00:03:23] — Apresentador do item 1:** Mais alguém? Não. Então, próxima EF.

## Transição

**[00:03:36] — Apresentador do item 1:** Você não vai apresentar, Pri? A próxima EF, que
também é nossa. Mas se você não for, eu apresento aqui.

**[00:04:16] — Pri (Priscilla):** Peraí, só peraí, rapidinho. É que travou tudo. Deixa eu ver
aqui também.

**[00:04:40] — Participante:** Você tem ela fácil aí, Augusto? Minha tela tá toda travada,
gente, não tô conseguindo. O que tem aqui? Eu vou compartilhar.

**[00:04:53] — Apresentador do item 2:** É 556776… 556576.

**[00:05:02] — Apresentador do item 2:** Deixa eu abrir aqui, só um momento. Estão vendo a
minha tela?

**[00:05:26] — Participantes:** Estamos.

## Item 2 — OS 556576: campo `simulation_id`

**[00:05:28] — Apresentador do item 2:** Bom, esse item aqui também é um item simples, tá? É
uma EF de um item só. Onde é aqui no item, no projeto **556576**, tá? Onde o objetivo aqui é
viabilizar a integração de informações mediante a simulação do reaproveitamento, do
reaproveitamento lá do ProRata, né? No plugin de envio [da] proposta [a]o sistema externo.
Onde, a partir de agora, aqui no… Vamos voltar também aqui. A partir de agora, eles vão começar
a passar para nós o ID da simulação, né? Então, com isso, lá no plugin do Envio [de] Proposta
[a]o Sistema Externo, nós vamos acrescentar um novo campo, que chama **Simulation ID**, e com
isso ele vai trazer qual foi o ID da simulação do ProRata, tá?

**[00:06:16] — Apresentador do item 2:** Se aqui nós colocamos aqui o JSON, né, que eles
mandaram para nós, que vai vir assim, nós vamos enviar lá no nosso plugin de envio para o
sistema externo esse campo de Simulation ID, tá? Que tá aqui no… eita, peraí, que é gigante
esse plugin, né? Cadê a informação?

**[00:06:58] — Augusto:** Augusto, aí dentro dele vai ter só o ID, né, aquele JSON?

**[00:07:02] — Apresentador do item 2:** O JSON é o JSON que eles enviam para nós, né, do
ProRata e tudo mais, com as informações do ProRata. Colocamos aqui na EF o JSON completo do
jeito que eles passam para nós, mas o campo que nós vamos ver vai ser esse aqui, o
**Simulation ID**, que é o novo campo que a partir de agora vai ter. E aí dentro lá vai ter
esse ID que eles passam para nós no plugin. Beleza?

**[00:07:30] — Participante:** Entendi, beleza.

**[00:07:31] — Apresentador do item 2:** É isso, esse item também, ele é um item simples
também, pequeno, né. Tem alguma especificação de nova, refinanciamento, alguma coisa?

**[00:07:42] — Participante:** Ah, é reaproveitamento, né? Isso, é reaproveitamento, né, então
quando é reaproveitamento é ter todo aquele… é ter uma esquemia, toda configuração para fazer.

**[00:07:53] — Apresentador do item 2:** Não, tá bom. Aí no reaproveitamento você vai ver se
ele trouxe o campo: se ele trouxe, [envia]; vazio, ele vai enviar vazio também, tá bom? Ele vai
trazer o que veio aqui no cara, se tá aprovado, qual foi, só muda isso, vai ter só esse novo
campo aqui, tá bom? Lá no cara também. Se não for reaproveitamento, vai vir vazio esse número,
esse ID **00:08:13–00:08:16**.

**[00:08:18] — Participante:** Isso.

**[00:08:20] — Apresentador do item 2:** Tá bom? Ok, é isso.

## Encerramento

**[00:08:30] — Apresentador do item 2:** Fechamos as dúvidas, então, pessoal?

**[00:08:33] — Zé:** É, esse aí até que é relativamente simples, é só… a gente já tem o campo,
né? A gente já retorna esse campo lá, então é só levantar ele lá no build do plugin e passar
ele para frente **00:08:35–00:08:41**.

**[00:08:44] — Apresentador do item 2:** Isso, perfeito, isso mesmo.

**[00:08:47] — Apresentador do item 2:** Zé, você acha que você consegue me mandar o Gantt
desses dois projetos quando? Segunda?

**[00:08:53] — Zé:** Segunda. Tá bom.

**[00:08:54] — Apresentador do item 2:** Eu já criei o do… esse é do pacote 4, né? Isso.
Então a gente já cria ele separado lá para deixar e já vai colocando os outros projetos dele
depois. Aí Zé, quando você passar o Gantt, nos avisa para colocar certinho aqui no mapa,
valeu. Aí dá um toque no Gabriel também, para as horas dele no Gantt, tá Zé?

**[00:09:20] — Zé:** Tá bom, beleza. Valeu, valeu, pessoal.
