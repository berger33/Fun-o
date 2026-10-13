> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Glauco, William e equipe CQ 1). Não são publicadas **imagens de
> pessoas** (avatares/câmeras da reunião).

# Transcrição — Liberação padrão - Glauco.mp4

A gravação registra **00:05:16.50** da reunião `Daily - CQ 1` em **2026-05-06**, na qual **Glauco**
apresenta para **William** e para a equipe o uso da planilha **`Liberacao_Padrao_V30.xlsx`** para
executar e evidenciar testes de **disponibilização / liberação padrão** (exemplificando com uma
entrega inicial completa de `Plugin` para **Portobank**).

## Bloco 1 — Contexto: chegada das demandas de disponibilização padrão (00:00:00 – 00:00:28)

- **00:00:00 — Glauco:** "[...] uma OS Função antiga e disponibilizar. Esse tipo a gente não fazia aqui. Acho que o pessoal também nem sabe. Até os mais experientes acho que não sabem esse tipo de disponibilização, entendeu?"
- **00:00:13 — William:** "Perfeito."
- **00:00:14 — Glauco:** "A gente vai começar a fazer aqui. Meio que saiu lá do Galo e vai vir para a gente. Já deixa eu até explicar, então, mais ou menos aqui rapidinho para o pessoal como que vai funcionar — até para você mesmo, mas é assim..."

## Bloco 2 — Estrutura da planilha `Liberacao_Padrao_V30.xlsx` e filtro por Artefato (00:00:29 – 00:01:27)

- **00:00:29 — Glauco:** "A gente tem essa planilha aqui, pessoal. Vocês estão vendo minha tela aí?"
- **00:00:33 — William:** "Sim."
- **00:00:33 — Glauco:** "A gente tem essa planilha. Essa planilha é a **planilha de disponibilização padrão**. O que a gente faz? A gente ignora todos esses campos aqui embaixo, que são abas de cálculo [`Planilha1`, `Planilha2`, `Esforço Padrão`, `Esforço Liberações`, `Liberações`], e deixa somente nessa aba aqui de **`Cenários`**."
- **00:00:50 — Glauco:** "E aí a gente tem que ver o que nós estamos testando. Por exemplo, se nós estamos testando um **website** [`Web Site .Net`], a gente vai marcar aqui o website que a gente está testando."
- **00:01:02 — Glauco:** "Se a gente está testando, sei lá, um **plugin** [`Plugin`], a gente coloca aqui o plugin. Conforme o que a gente marcar aqui, vai ser demonstrado o que a gente precisa estar testando."
- **00:01:14 — Glauco:** "Então, basicamente, é só seguir esses processos aqui que está sendo pedido na planilha e vida que segue. É basicamente isso aqui que a gente precisa testar e também **evidenciar**."

*(Indicação visual: em **00:00:50**, a planilha exibe `Web Site .Net` filtrado — 19 de 162 registros,
ver [`capturas/01-planilha-liberacao-padrao-website-net.png`](capturas/01-planilha-liberacao-padrao-website-net.png).
Em **00:01:06**, Glauco abre o filtro da coluna `Artefato` e marca `Plugin` — 7 de 162 registros,
ver [`capturas/02-filtro-artefatos-planilha.png`](capturas/02-filtro-artefatos-planilha.png) e
[`capturas/03-cenarios-plugin-7-registros.png`](capturas/03-cenarios-plugin-7-registros.png).)*

## Bloco 3 — O que exige evidência × o que é apenas conferência (00:01:28 – 00:01:59)

- **00:01:28 — Glauco:** "Alguns são muito mais simples. Por exemplo, se a gente for testar um **plugin**, é basicamente só mostrar ele **instalado e rodando**. Está rodando, basicamente é isso."
- **00:01:42 — Glauco:** "O restante, tem coisas aqui que a gente precisa analisar se precisa colocar evidência; às vezes não. Por exemplo, `Lista de plugins conforme a planilha disponível` [linha 87]: tem que colocar evidência disso? É só uma **conferência** para a gente ver se está ok. Então, alguns vai a evidência, outras coisas não vão."

## Bloco 4 — Colunas de modalidade de entrega, exemplo Portobank e ressalva sobre procedures C e W (00:02:00 – 00:02:59)

- **00:02:00 — Glauco:** "E aqui do lado [colunas `G` a `J`] tem também o que a gente está fazendo: se o cliente já tem o módulo [`Testar se o cliente já tiver o módulo?`], se é uma **entrega inicial completa** [`Entrega inicial - Completo`] e tudo mais."
- **00:02:10 — Glauco:** "Nesse caso do **William**, a gente coloca... deixa eu ver aqui o que é o dele aqui... **Portobank**, **liberação do módulo padrão**. É, o cliente **não tem**. Então vai ser essa **entrega inicial completa**."
- **00:02:25 — Glauco:** "Aí você marca aqui como **`Sim`** essa `Entrega inicial - Completo` aqui, e aí a gente vê aqui o que o cara vai testar."
- **00:02:31 — Glauco:** "No caso do **plugin**, seria só mostrar ele aberto [linha 84: `Instalação / Evidências`] e **criação com C** [linha 86: `Criação de procedures: .NET - com a opção C, sem erros.`]."
- **00:02:35 — Glauco:** "**Isso aqui está desatualizado**: precisa também fazer a **criação com W** — na verdade, só **conferir se o W existe lá**, para ver se está tudo certinho. Fechou? Belezinha?"
- **00:02:48 — William:** "Boa, isso que eu ia pedir."
- **00:02:51 — Glauco:** "Tá bom, aí deu para entender? Caso não, eu te explico melhor depois, se precisar. Fechou?"

*(Indicação visual: em **00:02:25 – 00:02:35**, Glauco filtra a coluna `G` (`Entrega inicial - Completo`)
para `Sim`, restando apenas 2 de 162 registros para `Plugin`: linha `84` (`Instalação / Evidências`) e
linha `86` (`Criação de procedures: .NET - com a opção C, sem erros.`) — ver
[`capturas/04-colunas-entrega-inicial-completo-sim.png`](capturas/04-colunas-entrega-inicial-completo-sim.png).)*

## Bloco 5 — Priorização do dia para William e status do Função / Azure 53 e 54 (00:03:00 – 00:03:35)

- **00:03:01 — Glauco:** "Beleza. E aí, por hoje você pode fazer isso daí, tá? Tinha pedido pra você iniciar a sua outra Função, mas por hoje você pode iniciar esse cara aí, fechou?"
- **00:03:13 — Glauco:** "Beleza, acho que a princípio é isso com você, mano. Belezinha? Bom dia, viu?"
- **00:03:19 — William:** "Ô Glauco [transcrito como 'O que foi logo?'], o Função então não inicio ainda, né? O **Função Azul** [Azure] **53, 54** já finalizou."
- **00:03:27 — Glauco:** "Ah, tá, beleza! Está finalizado."
- **00:03:33 — Glauco:** "Fechou, William. Obrigado, viu? Bom dia, bom trabalho."

## Bloco 6 — Envio e download da planilha no chat da Daily (00:03:36 – 00:05:16)

*(Sem fala relevante no áudio; em **00:04:05 – 00:05:16**, Glauco envia o arquivo
`Liberacao_Padrao_V30.xlsx` no chat `Daily - CQ 1` às `10:07`, e William baixa o arquivo na sua
máquina como `Liberacao_Padrao_V30 21.xlsx`.)*

## Leitura de tela (não falada)

1. **[00:00:40 – 00:02:45, `Liberacao_Padrao_V30.xlsx`, aba `Cenários`]**
   - **Orientações gerais (linhas 1–6):**
     - `* Esta planilha contempla todos os processos que devem ser realizadas durante testes de disponibilização padrão.`
     - `* As colunas G e H são preenchidas pelo analista, não a altere e valide somente o que estiver como "Sim".`
     - `* Evidenciar todos os processos efetuados.`
     - `* A coluna "Status" facilita o uso, não precisa enviar para o analista e nem publicar em nenhum lugar, a menos que ele te peça.`
     - `* Caso se depare com um módulo que não há processo na planilha, avise o seu analista.`
   - **Legenda de `Status` (colunas E–G, linhas 1–8):**
     - `Não se aplica - Não serve para o módulo`
     - `Pendente – Não testado`
     - `And – Testes iniciados e em andamento`
     - `NOK – Com erro`
     - `OK – Validado com sucesso`
     - `Evidenciado – Validado e documento OK`
     - `OK + Evidenciado (Geral)`
   - **Opções visíveis no filtro `Artefato` (00:01:06):** `Linha de comando .Net`, `Linha de comando Delphi`,
     `Plugin`, `Relatório`, `Todos - Tema / Reg / FiMenu`, `Web Aut SubSite CP`, `Web Aut SubSite Empr`,
     `Web Aut SubSite FGTS`, `Web Aut SubSite Veic`, `Web Autorizador de Acordos`, `Web Site .Net`.
   - **Colunas da tabela (linha 16):** `A: Artefato`, `B: Processo`, `C: Status`, `D: Esforço unitário`,
     `E: Ciclos`, `F: Esforço total`, `G: Entrega inicial - Completo`, `H: Testar se o cliente já tiver o módulo?`,
     `I: Fluxo Limpo Versão Padrão`, `J: Entrega inicial - Reduzido`.
   - **Processos de `Web Site .Net` visíveis (linhas 17–21):**
     - `17`: `Instalação / Evidências` (`0:10:00`, 1 ciclo)
     - `18`: `Configurar alias específico do cliente na tabela TPARWFIUTIL, campo PWALIAS, e regularizar a estrutura via WFIUTIL.` (`0:08:00`, 1 ciclo)
     - `19`: `Criação de procedures: .NET - com a opção C, sem erros.` (`0:10:00`, 1 ciclo)
     - `20`: `Cadastro de rotinas no acesso (.NET - Via FI.SQLResutil - Deletar da tabela TRTHB os registros referentes ao site atual antes) - após o cadastro, checar se as rotinas aparecem no WebAcesso, rotina de cadastro de direitos.` (`0:10:00`, 1 ciclo)
     - `21`: `Cadastro de rotinas no acesso (.NET - Via rotina da Aplicação, geralmente no menu Serviços - Deletar da tabela TRTHB os registros referentes ao site atual antes) - após o cadastro, checar se as rotinas aparecem no WebAcesso, rotina de cadastro de direitos.` (`0:10:00`, 1 ciclo)
   - **Processos de `Plugin` visíveis (linhas 84–88):**
     - `84`: `Instalação / Evidências` (`0:06:00`, 1 ciclo — `Sim` nas colunas `G`, `H`, `I`, `J`)
     - `85`: `Configurar alias específico do cliente na tabela TPARWFIUTIL, campo PWALIAS, e regularizar a estrutura via WFIUTIL.` (`0:00:00`, `Não` nas colunas `G`, `H`, `I`, `J`)
     - `86`: `Criação de procedures: .NET - com a opção C, sem erros.` (`0:08:00`, 1 ciclo — `Sim` nas colunas `G`, `H`, `I`, `J`)
     - `87`: `Lista de plugins conforme planilha disponível nas ocorrências da OS de projeto (ou subprojeto, checar nos dois), não pode haver nem mais e nem menos plugins. Caso não exista lista de plugins na planilha, considerar o que foi liberado como correto.` (`0:12:00`, `Não` nas colunas `G`, `H`, `I`, `J`)
     - `88`: `Caso existir, ler o ESCOPO (EF/DT) e validar a inclusão/remoção de plugins ou a alteração que estiver descrita.` (`0:05:00`, `Não` em `G`, `Sim` em `H`, `Não` em `I` e `J`)
