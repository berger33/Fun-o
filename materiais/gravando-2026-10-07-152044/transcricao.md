> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Gabriel, William, Santana). Não são publicadas **imagens de pessoas**
> (avatares/fotos de perfil), URLs de sessão nem campos de CPF/telefone/e-mail de teste.

# Transcrição — Gravando 2026-10-07 152044.mp4

A gravação registra **00:04:10.54** de uma instrução prática no **Autorizador Web**
(`WebAutorizador`) sobre como identificar a **despesa do tipo seguro** em uma proposta de
refinanciamento e rastrear, pelo cadastro do **Convênio** (`989898 - CONV MS`), qual é o **Código
da Política de Despesa/Tarifa** (`98`) vinculada àquele convênio.

## Bloco 1 — Contexto inicial no Teams: reaproveitamento de seguro e consulta SQL (00:00:00 – 00:00:05)

*(Indicação visual antes do início da fala: em **00:00:00**, a tela exibe a conversa de Teams com
**Gabriel** contendo relato sobre teste de reaproveitamento de seguro em refinanciamento e um
recorte de consulta no SQL Server Management Studio sobre a base `FCSMONITOREMPR` — detalhada na
seção "Leitura de tela" abaixo e em [`capturas/01-consulta-sql-monitor-empr.png`](capturas/01-consulta-sql-monitor-empr.png).)*

## Bloco 2 — Despesa × Seguro na tela de Proposta Sintetizada (00:00:06 – 00:01:30)

- **00:00:06 — Orientador:** "Então, você está aí nessa tela, certo?"
- **00:00:11 — Orientador:** "O que é uma despesa, você sabe? O que é um seguro, você sabe o que é? Aí na tela, onde fica?"
- **00:00:27 — Orientador:** "Beleza? Você sabe qual é a diferença?"
- **00:00:32 — Orientador:** "Assim, a despesa, uma despesa, são vários tipos, né? Então, a despesa do tipo **seguro** é um tipo da guia, tá?"
- **00:00:45 — Orientador:** "Então, você consegue configurar diversos tipos de despesas do convênio, certo?"
- **00:00:51 — Orientador:** "Então, no caso aí, você tá usando essa aí, certo? `989898` [transcrito como '9998'], **Seguro A**, despesa, beleza?"
- **00:01:01 — Orientador:** "Beleza. Acho que não... eu não tenho certeza."
- **00:01:09 — Orientador:** "Ele faz parte, ele complementa, mas não é à parte. Ele não é uma despesa [isolada]; ele, tipo, tá junto aí: ele faz parte da despesa, mas não é uma despesa apartada. Você vai ver."
- **00:01:29 — Orientador:** "Beleza, então."

*(Indicação visual: entre **00:00:20** e **00:01:20**, o navegador exibe a tela
`UI.PropostaSintetizada.aspx` do **Autorizador Web** com a condição `989898 CONV MS` marcada e o
quadro **Despesas / Tarifas** contendo `Vlr. IOF` = `53,04` e `Seguro A` marcado em `Incluir` com
valor `420,00` — ver [`capturas/02-proposta-condicao-despesas-seguro.png`](capturas/02-proposta-condicao-despesas-seguro.png).)*

## Bloco 3 — Abertura de outra aba do Autorizador Web e identificação do convênio usado (00:01:31 – 00:02:50)

- **00:01:31 — Orientador:** "Duplica a tela do Autorizador. Vamos abrir a tela do Autorizador [transcrito como 'doutor Isabel']."
- **00:01:36 — Orientador:** "Já tem uma aberta aí. Mantenha essa tela aí. Isso, então deixa só uma. Vamos ver outra tela aí, outra tela."
- **00:01:55 — Orientador:** "Beleza, então vamos consultar o **convênio**."
- **00:02:07 — Orientador:** "Qual convênio que você quer consultar aí? Você quer consultar o convênio que você tá usando."
- **00:02:18 — Orientador:** "Qual convênio você vai usar pra fazer? Não quero que você chute, me fala."
- **00:02:33 — Orientador:** "É o `000012` [transcrito como '0012']? É ele que tá selecionado aí?"
- **00:02:39 — Orientador:** "Isso."
- **00:02:50 — Orientador:** "Beleza."

*(Indicação visual: em **00:02:00**, o operador abre na primeira aba do **Autorizador Web** o menu
`Tabelas -> Convênios` — ver [`capturas/03-menu-tabelas-convenios.png`](capturas/03-menu-tabelas-convenios.png).
Em **00:02:20 – 00:02:40**, volta à aba da proposta para conferir qual tabela/convênio está marcado
na grade `Condição Escolhida` — inicialmente havia testado `000200 CONVENIO PORT` / `989898 CONV MS` —
e em seguida pesquisa o convênio `989898` na tela `Alteração de Convênio` no módulo `998`.)*

## Bloco 4 — Botão Despesas dentro do Convênio e descoberta do código 98 (00:02:52 – 00:04:10)

- **00:02:52 — Orientador:** "Aí, tá vendo que tem um botão que se chama **Despesas**?"
- **00:03:07 — Orientador:** "Isso, tá vendo? Tá ali, ó: **Código de despesas** [na tela: `Cód. Política de Despesa/Tarifa:`]."
- **00:03:10 — Orientador:** "Qual código que tá aí, que eu não tô enxergando? Tá muito pequeno."
- **00:03:16 — Orientador:** "**`98`**."
- **00:03:17 — Orientador:** "Beleza. Então, você vai lá consultar esse código. Então, a gente já sabe que o código dele é **`98`**, beleza? Então, você já tem uma informação dessa parte aí."
- **00:03:34 — Orientador:** "Então, beleza. Agora, você já abstraiu essa informação, certo? Agora sai dessa tela."
- **00:03:41 — Orientador:** "Agora a gente quer ver a **política em si**. A gente sabe que a despesa é **`98`**, agora a gente quer ver a política."
- **00:03:51 — Orientador:** "Então pode ir... agora essa não é a sua, pode voltar pra tela."

*(Indicação visual: em **00:03:00 – 00:03:38**, abre-se o modal **Despesas** do convênio `989898 CONV MS`,
exibindo `Cód. Política de Despesa/Tarifa: 98 | teste` e a seção `Valores de TC por Convênio` — ver
[`capturas/05-modal-despesas-codigo-98.png`](capturas/05-modal-despesas-codigo-98.png). Em **00:03:54 – 00:04:05**,
o operador fecha o modal, retorna à tela principal do convênio `989898 CONV MS` — ver
[`capturas/04-convenio-conv-ms-botao-despesas.png`](capturas/04-convenio-conv-ms-botao-despesas.png) — e
volta para `Alteração de Convênio` em **00:04:10**.)*

## Leitura de tela (não falada)

1. **[00:00:00, chat do Teams com Gabriel]**
   - Texto da mensagem visível acima da imagem:
     `"Não mostrou o reaproveitamento, estou criando uma nova proposta primeiro pra deixar no jeito para refinanciar e entender o que faltou. As configs reaproveitamento na configuração de refinanciamento está certa."`
   - Consulta SQL visível na imagem anexada ao chat (SSMS, banco `FCSMONITOREMPR`):
     ```sql
     --INTEGRAÇÃO DE REAPROVEITAMENTO DE SEGURO
     SELECT TOP 1000 PRDESCPFCON, CSNRPROP, CSSERVER,CSRETTEXT,CSDTHRAGEN,CSSTATUS,* FROM FCSMONITOREMPR..ECONSULT(NOLOCK)
     INNER JOIN FCSMONITOREMPR..TBPERFCON ON CSIDPFCON = PRIDPFCON WHERE CSNRPROP = '000033373'
     --where PRDESCPFCON LIKE ('%INSS - Plugin de levantamento para exclusão de averbação%')
     ORDER BY CSIDCONS DESC

     USE FCSMONITOREMPR
     ```
   - Grade de resultados na imagem (para `CSNRPROP = '800033373'`): 4 linhas com `CSSTATUS = 'C'`
     (`Esteira Autorizador` / `CSIDPFCON = 410`; `CPD - Averbação de Empréstimo consignado Trabalh...` / `610`;
     `Averbação ON-LINE(Averbação Padrão)` / `6`; `Averbação Proposta` / `60`).
2. **[00:00:20 – 00:01:40, `UI.PropostaSintetizada.aspx`]**
   - Cabeçalho da Proposta: Promotora `001010 - PROMOTORA CP REGRESS`, Tipo de Operação `Refinanciamento`,
     Tipo de Produto `0001 - Crédito Consignado`, Grupo de Convênio `PRIVADO`, Empregador `001010 - Regressivo`,
     Órgão `001010 - INSS REGRESSIVO CP`, Matriz `000001 - BANCO FUNCAO S/A`, Regional `000001 - Regional Função`,
     Tipo de Formalização `digital`, Subtipo `1 - DIG - DIGITAL`.
   - Campos cadastrais de teste do cliente (CPF, celular, e-mail e token fictícios de teste):
     omitidos do texto derivado (`[DADO PESSOAL OMITIDO — dados fictícios de teste]`).
   - Condição escolhida (`989898 CONV MS`): `Tx. Jr. a.m. = 1,7000`, `Vlr Parc = 133,32`, `Vlr Sol = 3.500,00`,
     `Vlr Cli = 1.209,07`; `Despesas / Tarifas`: `Vlr. IOF = 53,04` (`Fin. = X`), `Seguro A = 420,00` (`Incluir` marcado),
     `Liberado = 3.500,00`.
3. **[00:02:00 – 00:04:10, `UI.CD.ConvA.aspx` e `UI.ConfigConvenio.aspx`]**
   - Módulo `998`, Código `989898`, Descrição `CONV MS`, Situação `Alteração`.
   - Tipos de operação habilitados (`Nova`, `Refinanciamento`, `Renegociação`, `Portabilidade`), todos com Produto `009898 - PRODUTO MS`.
   - Modal `Despesas`: `Cód. Política de Despesa/Tarifa: 98` (`teste`).
