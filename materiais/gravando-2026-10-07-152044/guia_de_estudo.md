> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Gabriel, William, Santana). Não são publicadas **imagens de pessoas**
> (avatares/fotos de perfil), URLs de sessão nem campos de CPF/telefone/e-mail de teste.

# Guia de estudo — Gravando 2026-10-07 152044.mp4

- **Categoria:** `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `SQL`, `DÚVIDA_OU_CONFLITO`
- **Sistema:** **Autorizador Web (`WebAutorizador`)** (`Proposta Sintetizada`, `Alteração de Convênio`) e banco **`FCSMONITOREMPR`** (SSMS)
- **Assunto:** relação entre despesa e seguro na Proposta Sintetizada, localização do código da **Política de Despesa/Tarifa (`98`)** no convênio (`989898 - CONV MS`) e consulta SQL `ECONSULT` × `TBPERFCON`
- **Fonte:** `Gravando 2026-10-07 152044.mp4` (134290125 bytes), 2026-10-07 ~14:52 (BRT), duração 00:04:10.54 — SHA-256 `07fc2d87…`
- **Confiança da extração:** **alta** — áudio do orientador compreensível do início ao fim e telas do Autorizador Web nítidas em 1278×766.

## 1. Objetivo e público

- **Objetivo do vídeo:** ensinar o operador a identificar onde o **seguro** aparece na tela de
  **Proposta Sintetizada** (dentro do bloco **Despesas / Tarifas**), entender que o seguro é
  configurado como um tipo de despesa vinculada ao convênio e descobrir qual **Código de Política de
  Despesa/Tarifa** (`98`) está associado ao convênio utilizado na proposta (`989898 - CONV MS`).
- **Público/pré-requisitos:** operadores de CQ e analistas da **Função Sistemas** que configuram e
  testam propostas, seguros e políticas de despesas no **Autorizador Web**.

## 2. Conceito-chave: Despesa × Seguro no Autorizador Web (00:00:11 – 00:01:29)

- **[00:00:32 – 00:00:45]** No **Autorizador Web**, uma **despesa** pode ter vários tipos, e a
  despesa do tipo **seguro** é um desses tipos configuráveis para o convênio.
- **[00:00:51 – 00:01:26]** Na tela da proposta (`UI.PropostaSintetizada.aspx`), para a tabela/convênio
  selecionado (`989898 CONV MS`), o item **`Seguro A`** aparece dentro do quadro **Despesas / Tarifas**
  (junto com `Vlr. IOF`), com a caixa `Incluir` marcada e valor `420,00` (ver
  [`capturas/02-proposta-condicao-despesas-seguro.png`](capturas/02-proposta-condicao-despesas-seguro.png)).
  O seguro faz parte da estrutura de despesas da proposta, não sendo uma entidade separada fora daquele
  quadro.

## 3. Como descobrir o código da Política de Despesas de um Convênio (00:01:31 – 00:03:54)

Para saber qual política de despesas rege o seguro exibido em uma proposta:

1. **Conferir na proposta qual convênio/tabela está selecionado (00:02:07 – 00:02:39):**
   - Não "chutar" na pesquisa de convênios (**[00:02:26]**): olhar na aba da proposta qual linha da
     grade **Condição Escolhida** está marcada (`989898 CONV MS`).
2. **Abrir o cadastro do Convênio em outra aba do Autorizador Web (00:01:31 – 00:02:50):**
   - No menu superior, acessar `Tabelas -> Convênios` (**[00:02:00]**, ver
     [`capturas/03-menu-tabelas-convenios.png`](capturas/03-menu-tabelas-convenios.png)).
   - Na tela `Alteração de Convênio` (`UI.CD.ConvA.aspx`), informar o **Módulo** (`998`) e pesquisar/selecionar
     o **Convênio** (`989898 - CONV MS`) para abrir `UI.ConfigConvenio.aspx` (ver
     [`capturas/04-convenio-conv-ms-botao-despesas.png`](capturas/04-convenio-conv-ms-botao-despesas.png)).
3. **Consultar o botão `Despesas` dentro do Convênio (00:02:52 – 00:03:38):**
   - Na parte inferior da tela `Convênio`, clicar no botão **`Despesas`** (**[00:02:52]**).
   - No modal **`Despesas`** que se abre, ler o campo **`Cód. Política de Despesa/Tarifa:`** — no
     exemplo demonstrado, código **`98`** com descrição **`teste`** (**[00:03:07 – 00:03:21]**, ver
     [`capturas/05-modal-despesas-codigo-98.png`](capturas/05-modal-despesas-codigo-98.png)).
4. **Próximo passo indicado (00:03:40 – 00:03:54):**
   - Com o código **`98`** anotado ("abstraída essa informação"), sair do modal do convênio para ir
     consultar a **Política de Despesas e Tarifas** em si (`Tabelas -> Política de Despesas e Tarifas`).

## 4. Análise de SQL exibido na tela inicial (00:00:00)

Nos primeiros segundos (**[00:00:00 – 00:00:05]**), a janela do Teams mostra um print do SQL Server
Management Studio enviado no contexto de investigação de `"INTEGRAÇÃO DE REAPROVEITAMENTO DE SEGURO"`
(ver [`capturas/01-consulta-sql-monitor-empr.png`](capturas/01-consulta-sql-monitor-empr.png)):

```sql
--INTEGRAÇÃO DE REAPROVEITAMENTO DE SEGURO
SELECT TOP 1000 PRDESCPFCON, CSNRPROP, CSSERVER,CSRETTEXT,CSDTHRAGEN,CSSTATUS,* FROM FCSMONITOREMPR..ECONSULT(NOLOCK)
INNER JOIN FCSMONITOREMPR..TBPERFCON ON CSIDPFCON = PRIDPFCON WHERE CSNRPROP = '000033373'
--where PRDESCPFCON LIKE ('%INSS - Plugin de levantamento para exclusão de averbação%')
ORDER BY CSIDCONS DESC

USE FCSMONITOREMPR
```

- **Dialeto:** T-SQL (Microsoft SQL Server — sustentado pelo uso de `SELECT TOP 1000`, notação de
  banco `FCSMONITOREMPR..ECONSULT`, dica `(NOLOCK)`, `USE FCSMONITOREMPR` e interface SSMS).
- **Tipo de comando:** **somente leitura (`SELECT`)** (acompanhado de `USE FCSMONITOREMPR` para troca
  de contexto de banco).
- **Explicação linha a linha:**
  - `--INTEGRAÇÃO DE REAPROVEITAMENTO DE SEGURO`: comentário identificando a finalidade do diagnóstico.
  - `SELECT TOP 1000 PRDESCPFCON, CSNRPROP, CSSERVER,CSRETTEXT,CSDTHRAGEN,CSSTATUS,* FROM FCSMONITOREMPR..ECONSULT(NOLOCK)`:
    projeta até 1000 registros da tabela de consultas/eventos `ECONSULT` no banco `FCSMONITOREMPR` sem
    bloqueio compartilhado (`NOLOCK`), destacando a descrição do perfil (`PRDESCPFCON`), número da
    proposta (`CSNRPROP`), servidor (`CSSERVER`), texto de retorno (`CSRETTEXT`), data/hora de
    agendamento (`CSDTHRAGEN`), status (`CSSTATUS`) e demais colunas (`*`).
  - `INNER JOIN FCSMONITOREMPR..TBPERFCON ON CSIDPFCON = PRIDPFCON WHERE CSNRPROP = '000033373'`:
    faz junção interna com a tabela de perfis de consulta (`TBPERFCON`) pela chave de perfil
    (`CSIDPFCON = PRIDPFCON`) filtrando pelo número da proposta (`CSNRPROP = '<numero-proposta>'`;
    no editor aparece `'000033373'` e na grade de resultado aparece `'800033373'`).
  - `--where PRDESCPFCON LIKE ('%INSS - Plugin de levantamento para exclusão de averbação%')`:
    filtro alternativo comentado por descrição do plugin/serviço.
  - `ORDER BY CSIDCONS DESC`: ordena do evento mais recente para o mais antigo pelo identificador
    da consulta (`CSIDCONS`).
- **Saída demonstrada na grade (4 linhas para a proposta `800033373`, todas com `CSSTATUS = C`):**
  1. `Esteira Autorizador` (`CSIDPFCON = 410`, `CSRETTEXT = 'Esteira .Net acionada com sucesso..'`)
  2. `CPD - Averbação de Empréstimo consignado Trabalh...` (`CSIDPFCON = 610`, `CSRETTEXT = 'Finalizado - OK'`)
  3. `Averbação ON-LINE(Averbação Padrão)` (`CSIDPFCON = 6`, `CSDTHRAGEN = NULL`)
  4. `Averbação Proposta` (`CSIDPFCON = 60`, `CSDTHRAGEN = NULL`)

## 5. Erros, cuidados e ressalvas

- **Não consultar convênio por tentativa e erro ("chute"):** sempre verificar na tela da proposta
  qual código de tabela/convênio está efetivamente selecionado na simulação (**[00:02:18 – 00:02:39]**).
- **Diferença entre o convênio e a política de despesas:** o modal `Despesas` dentro de `Convênios`
  mostra apenas o **vínculo** (`Cód. Política de Despesa/Tarifa: 98`) e os `Valores de TC por Convênio`;
  para ver as regras completas da política `98`, é preciso sair dessa tela e consultar o cadastro da
  **Política de Despesas e Tarifas** (**[00:03:40 – 00:03:51]**).

## 6. Resumo em uma frase

Em **00:04:10**, o vídeo mostra no **Autorizador Web** como o seguro (`Seguro A`) integra o bloco
**Despesas / Tarifas** da **Proposta Sintetizada** e ensina o caminho passo a passo para identificar,
a partir do convênio selecionado na proposta (`989898 - CONV MS`), o **Código da Política de
Despesa/Tarifa (`98`)** no botão **Despesas** do cadastro de convênios, além de exibir uma consulta
T-SQL de rastreamento de eventos da proposta em `FCSMONITOREMPR..ECONSULT`.
