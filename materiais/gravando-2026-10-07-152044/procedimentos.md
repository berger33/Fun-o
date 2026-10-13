> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Gabriel, William, Santana). Não são publicadas **imagens de pessoas**
> (avatares/fotos de perfil), URLs de sessão nem campos de CPF/telefone/e-mail de teste.

# Procedimentos — Gravando 2026-10-07 152044.mp4

## Fluxo A — Identificar o Código da Política de Despesa/Tarifa vinculada ao Convênio de uma Proposta (00:00:06 – 00:03:54)

- **Sistema / Módulo:** **Autorizador Web (`WebAutorizador`)** — versão `26.0929.124.7113`
- **Objetivo:** descobrir qual código de **Política de Despesa/Tarifa** configura as despesas e o
  seguro (`Seguro A`) apresentados em uma proposta no **Autorizador Web**.
- **Pré-condições:**
  - Proposta aberta na tela **Proposta Sintetizada** (`MenuWeb/Cadastro/Proposta/UI.PropostaSintetizada.aspx`)
    com cálculo/simulação realizado **[00:00:06 – 00:00:55]**.
  - Usuário autenticado com acesso ao menu `Tabelas -> Convênios` (no vídeo, usuário `SUPERVISOR`)
    **[00:02:00]**.
- **Sequência numerada:**
  1. Na tela **Proposta Sintetizada** (`UI.PropostaSintetizada.aspx`), localizar o quadro
     **Condição Escolhida** e verificar qual **Tabela / Convênio** está marcada (no vídeo,
     `989898 - CONV MS`), bem como o quadro lateral **Despesas / Tarifas** onde aparecem `Vlr. IOF`
     (`53,04`) e `Seguro A` (`420,00`, com `Incluir` marcado) **[00:00:11 – 00:00:55; 00:02:18 – 00:02:39]**
     (ver [`capturas/02-proposta-condicao-despesas-seguro.png`](capturas/02-proposta-condicao-despesas-seguro.png)).
  2. Manter a aba da proposta aberta e usar uma segunda aba do **Autorizador Web** para consulta
     **[00:01:31 – 00:01:55]**.
  3. No menu principal superior do **Autorizador Web**, acessar **`Tabelas -> Convênios`**
     (subopção de alteração/consulta que abre `MenuWeb/Tabelas/Convenio/UI.CD.ConvA.aspx`)
     **[00:01:55 – 00:02:05]** (ver [`capturas/03-menu-tabelas-convenios.png`](capturas/03-menu-tabelas-convenios.png)).
  4. Na tela **Alteração de Convênio**, informar o **Módulo** (`998`) e selecionar o **Convênio**
     exato utilizado na proposta (`989898 - CONV MS`), clicando em **Confirmar** para abrir a tela
     **Convênio** (`UI.ConfigConvenio.aspx`) **[00:02:07 – 00:02:50]** (ver
     [`capturas/04-convenio-conv-ms-botao-despesas.png`](capturas/04-convenio-conv-ms-botao-despesas.png)).
  5. Na parte inferior da tela **Convênio**, clicar no botão **`Despesas`** **[00:02:52 – 00:03:07]**.
  6. No modal **Despesas** exibido, ler o campo **`Cód. Política de Despesa/Tarifa:`** (no vídeo,
     código **`98`** e descrição **`teste`**) **[00:03:07 – 00:03:23]** (ver
     [`capturas/05-modal-despesas-codigo-98.png`](capturas/05-modal-despesas-codigo-98.png)).
  7. Anotado o código da política (`98`), fechar/voltar do modal do convênio para, na etapa seguinte,
     consultar diretamente o cadastro da **Política de Despesas e Tarifas** **[00:03:36 – 00:03:54]**.
- **Resultado esperado:** identificação exata do código da política de despesas (`98`) vinculada ao
  convênio da proposta (`989898`), permitindo auditar suas regras no cadastro próprio de políticas.
- **Exceções e cuidados:**
  - Não pesquisar um convênio aleatório na lista de pesquisa (`000001`, `000012`, etc.) sem antes
    conferir na aba da proposta qual convênio está selecionado na simulação **[00:02:18 – 00:02:39]**.

## Fluxo B — Consulta SQL de monitoramento de esteira/averbação da proposta (00:00:00)

- **Ambiente:** SQL Server Management Studio (SSMS), banco **`FCSMONITOREMPR`**.
- **Objetivo:** consultar os registros de execução de plugins/etapas da esteira e averbação para o
  número de uma proposta (`CSNRPROP`), no contexto de verificação de integração/reaproveitamento de
  seguro **[00:00:00]** (ver [`capturas/01-consulta-sql-monitor-empr.png`](capturas/01-consulta-sql-monitor-empr.png)).
- **Consulta demonstrada (somente leitura — `SELECT`):**
  ```sql
  --INTEGRAÇÃO DE REAPROVEITAMENTO DE SEGURO
  SELECT TOP 1000 PRDESCPFCON, CSNRPROP, CSSERVER,CSRETTEXT,CSDTHRAGEN,CSSTATUS,* FROM FCSMONITOREMPR..ECONSULT(NOLOCK)
  INNER JOIN FCSMONITOREMPR..TBPERFCON ON CSIDPFCON = PRIDPFCON WHERE CSNRPROP = '000033373'
  --where PRDESCPFCON LIKE ('%INSS - Plugin de levantamento para exclusão de averbação%')
  ORDER BY CSIDCONS DESC
  ```
- **Conferência do resultado:** verificar as linhas retornadas por `CSIDCONS DESC`, observando a
  etapa (`PRDESCPFCON`), o status (`CSSTATUS`, ex.: `C`), o retorno (`CSRETTEXT`) e a data/hora de
  agendamento (`CSDTHRAGEN`) **[00:00:00]**.
