> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Gabriel, William, Santana). Não são publicadas **imagens de pessoas**
> (avatares/fotos de perfil), URLs de sessão nem campos de CPF/telefone/e-mail de teste.

# Perguntas e respostas — Gravando 2026-10-07 152044.mp4

1. **Onde fica a informação de seguro na tela de Proposta Sintetizada do Autorizador Web? (00:00:11 – 00:00:55)**
   Fica no quadro **Despesas / Tarifas** (ao lado de **Condição Escolhida** e abaixo de **Dados da Operação**),
   onde aparecem `Vlr. IOF` e a linha do seguro (`Seguro A` ou `SEGUROS`), com a caixa `Incluir` e o
   respectivo valor (**[00:00:16 – 00:00:55]**).

2. **Qual é a relação conceitual entre "despesa" e "seguro" explicada pelo orientador? (00:00:32 – 00:01:26)**
   Existem vários tipos de despesa configuráveis no convênio, e o **seguro** é um tipo de despesa
   da guia; portanto, ele faz parte da estrutura de despesas da operação, e não de um cadastro
   isolado fora das despesas (**[00:00:32 – 00:01:25]**).

3. **Qual tabela/convênio estava selecionada na Proposta Sintetizada no exemplo analisado? (00:00:51 – 00:01:00)**
   A tabela/convênio **`989898 - CONV MS`**, exibindo `Seguro A` com valor `420,00` e `Vlr. IOF` com
   valor `53,04` (**[00:00:55]**).

4. **Por que o orientador pede para duplicar/usar outra aba do Autorizador Web? (00:01:31 – 00:01:55)**
   Para manter a tela da **Proposta Sintetizada** aberta em uma aba (preservando os dados e podendo
   conferir qual convênio está marcado) enquanto usa a outra aba para consultar o cadastro do
   **Convênio** (**[00:01:31 – 00:01:55]**).

5. **Qual caminho de menu do Autorizador Web leva à consulta/alteração de convênios? (00:01:55 – 00:02:05)**
   Menu superior **`Tabelas -> Convênios`**, que direciona para a tela `Alteração de Convênio`
   (`UI.CD.ConvA.aspx`, **[00:02:00]**).

6. **Por que o orientador adverte "Não quero que você chute, me fala" ao pesquisar o convênio? (00:02:18 – 00:02:39)**
   Porque o operador deve consultar exatamente o convênio que está selecionado na proposta em teste
   (conferindo na aba da proposta se é `000012`, `000200` ou `989898`), evitando abrir um convênio
   diferente daquele usado na simulação (**[00:02:12 – 00:02:39]**).

7. **Dentro da tela de configuração do Convênio (`UI.ConfigConvenio.aspx`), qual botão abre o vínculo de despesas? (00:02:52 – 00:03:07)**
   O botão **`Despesas`**, localizado no grupo de botões inferiores da tela `Convênio` (entre
   `Origens` e `Portabilidade`, **[00:02:52]**).

8. **Qual informação é obtida ao abrir o modal `Despesas` do convênio `989898 - CONV MS`? (00:03:07 – 00:03:23)**
   O campo **`Cód. Política de Despesa/Tarifa:`**, que no convênio `989898` está preenchido com o
   código **`98`** (`teste`) (**[00:03:08 – 00:03:21]**).

9. **Após descobrir que o código da despesa no convênio é `98`, qual é o próximo passo indicado? (00:03:36 – 00:03:54)**
   Sair do modal do convênio e ir consultar o cadastro da **Política de Despesas e Tarifas** em si
   para inspecionar as regras do código `98` (**[00:03:40 – 00:03:51]**).

10. **O que faz a consulta SQL em `FCSMONITOREMPR..ECONSULT` exibida no início do vídeo? (00:00:00)**
    Realiza um `SELECT TOP 1000` na tabela `FCSMONITOREMPR..ECONSULT(NOLOCK)` com `INNER JOIN` em
    `FCSMONITOREMPR..TBPERFCON` (`ON CSIDPFCON = PRIDPFCON`), filtrando pelo número da proposta
    (`WHERE CSNRPROP = '...'`) e ordenando por `CSIDCONS DESC`, para listar as etapas de esteira e
    averbação executadas para aquela proposta (**[00:00:00]**).
