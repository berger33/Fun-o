# Transcrição — Jonas EPT explicação.mp4

Fala com timestamps `HH:MM:SS` (tempo do arquivo). Transcrição automática (`faster-whisper`, `large-v3`, idioma `pt`) **revisada contra a tela** nos pontos listados em *Notas de revisão*; a fala é esparsa (91 segmentos em 10:25 — a demonstração é essencialmente de tela). Indicações visuais entre colchetes resumem o que a tela mostra no momento (leitura por OCR dos quadros). Falantes: **Jonas** conduz compartilhando a tela; o interlocutor agradece ao final. Nomes completos de participantes e dados pessoais de clientes de teste omitidos.

> Transcrição automática é insumo, não verdade. Trechos com fala travada, expressões truncadas e jargão corrompido estão preservados como foram transcritos, com correção indicada nas notas.

## Trechos transcritos

### 00:00:00 – 00:01:20 (SSMS e telas do Autorizador Web)

- `[00:00:00]` porque a gente pode até fazer uma aqui
- `[00:00:03]` só pra você ter uma ideia de como é que vai funcionar
- `[00:00:05]` deixa mais a parte
- `[00:00:09]` pra você ter uma visão mais ampla desse cara
- `[00:00:11]` cadastro manual
  - *[tela `00:00:00`: SSMS — `SQLQuery1.sql` conectado a `FCSMONITOREMPR` do ambiente de CQ, com as consultas já preparadas (ver guia §3) e grade de resultados de `ECONSULT` com execuções de plugins (`Plugin CPO - Token`, `CFD - Plugin de Levantamento para Exclusão de Av…`)]*
  - *[tela `00:00:10`: Autorizador Web (BANCO FICSA) — tela `Cadastro de Decisão` (`UI.CD.Deci.aspx`, código 21777)]*
  - *[tela `00:00:20`–`00:01:10`: Autorizador Web — `Proposta Sintetizada` (`UI.PropostaSintetizada.aspx?Origem3=001010`) com cliente de teste (nome/documento omitidos), matriz `0001 - BANCO FUNÇÃO S/A`, botão `Enviar Token`, mensagens "Aguarde" e "7 tentativas…" — fala correspondente ausente]*

### 00:01:18 – 00:02:30 (chat do Teams e proposta)

- `[00:01:18]` Boa, vou tirar com ela
  - *[tela `00:01:20`–`00:01:40`: Teams — canais `Canal C6 - CQ`, `MESA C6 - Equipe CQ`, `MESA C6 - Equipe CQ + DEV`; mensagens sobre filtro de CPF/CNPJ em tabela e sobre a EPT ("Eu vou fazer a EPT dele")]*

- `[00:02:23]` Se não precisa nem
  - *[tela `00:01:50`–`00:02:20`: `Proposta Sintetizada` — "As informações foram salvas"; quadro `Condição Escolhida` (tabelas `0002 Conv Pond AP`, `000012 Crev AFI TESTE`, `000200 CONVENIO FORT…`) e `Dados da Operação` (Valor Cliente `2.000,00`, Valor Parcela `89,47`, Valor Financiado `2.078,59`) — mesmos valores do payload JSON exibido depois em `00:04:30`]*
  - *[tela `00:02:30`: tela `ESCOLHAPCS` (`Esteira/Processos/Web/INTERNO/ESCOLHAPCS.aspx`)]*

### 00:02:33 – 00:04:10 (o sistema externo e a consulta no banco)

- `[00:02:33]` O sistema externo
- `[00:02:40]` Cara, pelo que eu recordo, sim
- `[00:02:48]` Deixa eu só ver aqui
- `[00:02:50]` Boa, aqui
- `[00:02:52]` O que que acontece? Aqui ele já assinou o plugin *(ver Notas de revisão 2)*
- `[00:02:55]` A gente vira de proposta *(ver Notas de revisão 3: "o envio de proposta")*
- `[00:02:57]` Ao sistema externo
- `[00:02:58]` Como que a gente vai consultar
- `[00:03:01]` Esse
- `[00:03:02]` essas informações
- `[00:03:07]` tem esse CSI de cons *(ver Notas de revisão 4)*
- `[00:03:09]` tá vendo?
- `[00:03:11]` aí a gente vai na IconSuiteD *(ver Notas de revisão 5: `ECONSULTD`)*
- `[00:03:12]` passa aqui, ó
- `[00:03:14]` o ID cons desse cara *(o valor `CSIDCONS = 84942` da linha do "Serviço de Envio de Proposta ao Sistema Externo")*
- `[00:03:16]` aí aqui, ó
  - *[tela `00:02:50`–`00:03:40`: SSMS executando a consulta `ECONSULT` × `TBPERFCON` filtrada por `PRDESCPFCON LIKE ('%Servico de Envio da Proposta ao Sistema Externo%')` com `ORDER BY CSIDCONS DESC`; a grade traz na primeira linha o "Serviço de Envio de Proposta ao Sistema Externo" com `CSIDCONS 84942`, usuário `JAFONSO` e timestamps `2026-09-23 09:30`; abaixo, no editor, `SELECT * FROM ECONSULTD WHERE CDIDCONS='84942'`]*
- `[00:03:32]` o Jason *(ver Notas de revisão 6: JSON)*
- `[00:03:33]` Jason
- `[00:03:37]` aquilo que eu entendi vai estar aqui
- `[00:03:42]` tá?
- `[00:03:42]` vamos pegar ele
- `[00:03:55]` vamos ver se ele tá muito
- `[00:04:00]` quer ver que eu tô colocando errado
  - *[tela `00:03:40`–`00:04:00`: consulta `ECONSULTD` executada com o id `84942`; filtro ajustado no editor (antes `915516`, depois `84942`)]*

### 00:04:10 – 00:05:35 (Especificação Funcional e payload JSON)

- `[00:04:33]` se eu não me engano era para ele estar dentro de cliente não era não mas para cima *(o agrupamento de documentos anexados dentro do objeto `Client` do payload)*
- `[00:05:01]` acima de client
- `[00:05:04]` ele vai estar
- `[00:05:06]` em client
- `[00:05:08]` bom, mas é basicamente
- `[00:05:17]` eu acho que aqui ele perdeu *(ver Notas de revisão 7)*
- `[00:05:19]` ele tá lá em digital *(expressão incerta — ver [`incertezas.md`](incertezas.md) item 4)*
- `[00:05:20]` então ele entraria aqui
- `[00:05:23]` nessas novas informações
- `[00:05:24]` aí só escreve você que mandou *(trecho truncado, sentido incerto)*
  - *[tela `00:04:10`: Edge com o PDF da Especificação Funcional da OS 586780 (41 páginas) — página de tabela de layout com campos de endereço do cliente; em `00:04:20`, o bloco "Início do objeto `attached_document`" com `document_type` (Tipo do documento) e `document_name` (Nome do documento); em `00:05:00`, página com campos da promotora/corban (`phone` "Telefone Corban" até 9 caracteres, `phone_area_code` "DDD Corban" até 3, "De acordo com o cadastro da Origem 3 da proposta")]*
  - *[tela `00:04:30`–`00:05:20`: Notepad++ (aba não salva "*new 8*") com o payload JSON completo do envio (191 linhas): campos de contrato (`contract_amount 2078.59`, `contract_parcel_amount 89.47`, `contract_net_amount 2000.0`, `contract_parcel_quantity 30`, `last_parcel_date`, taxas de juros, `bank_code`, `agency_number`, `account_number`, `proposal_hash_id`, `loan_track_status_code`, `contract_parcels/guarantee/insurance null`), objeto `client { id, tax_identifier, name, … }` e objeto `corban_data { id "001010", company_name, fancy_name, document, endereço }` — valores de dados pessoais omitidos aqui de propósito]*
- `[00:05:35]` aí dá pra corrigir
- `[00:05:39]` tem mais uma coisinha pra ajustar
- `[00:05:47]` nessa primeira linha
- `[00:05:49]` mas eu já vi aqui
- `[00:05:52]` que acho que é o número da EF *(ver Notas de revisão 8)*
- `[00:05:53]` é, exato
- `[00:05:56]` tipo, aqui você põe
- `[00:05:57]` o número do projeto
- `[00:05:59]` certo? e aqui
- `[00:06:01]` o item da EF
- `[00:06:03]` é, aí
- `[00:06:05]` o que você pode fazer?
- `[00:06:08]` a etapa
- `[00:06:09]` a etapa lá do
- `[00:06:11]` como que a gente pode fazer ela já tô te chamando aqui pra falar tipo é pode ser bem genérica sabe *(trecho travado; sentido: a coluna "Etapa" pode ser preenchida de forma genérica)*
  - *[tela `00:05:50`: Excel `EPT_586780` (Modo de Compatibilidade) — seções "Premissas Gerais", "Validações Básicas"; em `00:06:00`, a tabela de casos de teste com colunas `CT | Ref. | Descrição | Etapa | … | Resultado esperado | Status | Observações` e a linha "001.1 - Implementar no módulo 'ServCon', no serviço (plugin) 'Envio da Proposta ao Sistema Externo', novo agrupamento responsável por identificar documentação anexa para compor as informações do cliente" sob o título "C6 Consig - 586780 - [ÁGIL] (I) Nova Flag informativa de Docs anexados no SrvEnvioPropExt"; pré-condição "Usuário deve possuir direitos de acesso… no módulo Web Autorizador… configurado"; também visível outro item "C6 Consig - 59??8? - [ÁGIL] (I) …abilidade de Consulta de Saldo…" (leitura parcial)]*

### 00:07:38 – 00:09:10 (etapa genérica, rotina de anexar documento e a pasta doc)

- `[00:07:38]` tipo vou tá te mandando aí não sei se eu posso dizer bem mas pode ser bem genérica nem eu sei
- `[00:07:44]` ao certo como que é essa configuração mas a gente já mostrou lá na hora e a gente vê ó aí tem esse
- `[00:07:54]` aqui ó que aí a gerou para mas de resto certo eu posso no autorizador no anexar documento já *(trecho travado; "no autorizador no anexar documento" = rotina Anexar/Consultar Documentação do Autorizador; resto incerto — ver [`incertezas.md`](incertezas.md) item 8)*
- `[00:08:17]` que já é uma já tá uma boa esses processos mas as etapas mas pega aqui esse bloco anexei lá na *(trecho travado; ver Notas de revisão 9)*
- `[00:08:27]` tá aqui na pasta doc
- `[00:08:30]` pega ele
- `[00:08:32]` dá uma lida
- `[00:08:33]` e acrescenta esse cenário
- `[00:08:36]` primeiro ponto, acrescenta esse cenário
- `[00:08:38]` pega esse doc
- `[00:09:08]` e dá uma lida nele aqui
  - *[tela `00:07:00`–`00:07:20`: Teams — chat com William ("consegue falar?", "eu te mostro aqui melhor do que ficar mandando msg")]*

### 00:09:11 – 00:10:25 (Relatório de Testes e encerramento)

- `[00:09:11]` de repente
- `[00:09:13]` esses
- `[00:09:16]` caras que tem a gera aqui *(trecho truncado, sentido incerto)*
- `[00:09:16]` é de 880, ou é muito bom ou não é muito bom *(expressão incerta — ver [`incertezas.md`](incertezas.md) item 9)*
- `[00:09:18]` beleza, vai deixar
- `[00:09:20]` a gente chega a ver, mas dá uma olhada
- `[00:09:22]` de repente tem alguma coisa documentada
- `[00:09:24]` que a gente pode acrescentar
- `[00:09:25]` alguma coisa
- `[00:09:27]` se dá pra ajustar alguma coisa
- `[00:09:29]` se ela colocou de uma forma diferente *(“ela” = autora do documento de teste; nome não dito)*
- `[00:09:31]` perfeito, a única coisa que a gente tem que ajustar é aquela parte do
- `[00:09:36]` inaúmero proposta, né *(ver Notas de revisão 10: "o número da proposta")*
- `[00:09:39]` tá
- `[00:09:39]` mandar ela pro sistema externo
- `[00:09:42]` exato, aqui eu vou mandar pra você aqui
- `[00:10:12]` por enquanto é isso, qualquer coisa
- `[00:10:14]` aí pode dar um toque
- `[00:10:15]` Maravilha
- `[00:10:16]` Pode deixar, você que finalizou
- `[00:10:18]` Obrigado Jonas
- `[00:10:20]` Demorou, tamo junto, valeu
  - *[tela `00:08:30`: Explorador de Arquivos na pasta compartilhada de rede (`Mesa_C6`) com `D586780` (PDF, 365 KB) e `Relatorio_de_Testes_586780` (Word, 99 KB); caminho do servidor mascarado nos derivados]*
  - *[tela `00:09:00`–`00:09:30`: Word `Relatório de Testes` (CQ - Controle de Qualidade / Evidências de Testes / Função Sistemas) com os cenários de teste da OS 586780 — "001.1 - Cenário 1 - Importação de proposta com documentos anexados deve preencher o [agrupamento]" (proposta enviada pelo fluxo `/proposal/import` com ao menos um documento anexado no checklist) e o cenário de atualização ("Uma proposta já existente será atualizada pelo fluxo `/proposal/update`"), com `Prioridade: Alta`, `Situação:`, `Parâmetros` (Endpoint `/proposal/update`; proposta existente com exatamente um documento anexado no checklist; usuário autenticado com privilégios compatíveis com os direitos de origem; proposta preparada sem anexos no checklist; proposta preparada com um documento anexado pelo mesmo fluxo funcional da rotina de anexação do módulo Autorizador), `Objetivo`, 8 passos de execução e `Resultado Esperado` — detalhados no guia §6; anotação no documento: "ler doc gerado pela [colega] e verificar se tem algum cenário válido para o nosso teste"]*
  - *[tela `00:09:40`–`00:10:10`: Excel da EPT e Teams; encerramento]*

## Notas de revisão (termos corrigidos ou marcados contra a tela)

1. **"IconSuiteD" → `ECONSULTD`** (`00:03:11`): a tela mostra a consulta `SELECT * FROM ECONSULTD WHERE CDIDCONS='84942'` — a fala se refere à tabela de detalhe de `ECONSULT`. A grafia "IconSuiteD" é erro do ASR.
2. **"aqui ele já assinou o plugin"** (`00:02:52`): provavelmente "aqui ele já chamou o plugin" (a grade mostra o registro da execução do serviço) — "assinou" pode ser erro do ASR; não confirmado.
3. **"A gente vira de proposta"** (`00:02:55`): lê-se "o envio de proposta" ao sistema externo, pelo contexto e pela tela (`Servico de Envio da Proposta ao Sistema Externo`).
4. **"tem esse CSI de cons"** (`00:03:07`): leitura incerta; pelo contexto da tela, refere-se ao registro de **consulta** em `ECONSULT` (a fala continua "aí a gente vai na ECONSULTD"). Não confundir com o sistema SIC citado em outra gravação.
5. **`ECONSULTD`** (`00:03:11`): confirmado na tela; tabela de detalhe (chave-valor) da consulta, colunas visíveis `CDIDCONS` (leitura aproximada), `CDCONTROLE`, `CDCAMPO` e coluna de conteúdo (leitura parcial).
6. **"Jason" → JSON** (`00:03:32`–`00:03:33`): a tela mostra o payload JSON em `ECONSULTD`/Notepad++.
7. **"eu acho que aqui ele perdeu"** (`00:05:17`): trecho truncado; provavelmente sobre a posição do agrupamento no payload ("ele perdeu" pode ser "ele ficou"), não confirmado.
8. **"acho que é o número da EF"** (`00:05:52`): EF = Especificação Funcional; a fala seguinte distingue "número do projeto" e "item da EF" no preenchimento da EPT.
9. **"pega aqui esse bloco anexei lá na"** (`00:08:17`): trecho travado; possivelmente "esse bloco, anexa ele lá na [EPT]" ou "o bloco 'anexo'"; o contexto (pega o documento na pasta doc e acrescenta o cenário) é confirmado pela tela e pela fala seguinte.
10. **"inaúmero proposta"** (`00:09:36`): lê-se "o número da proposta" — o ajuste citado é sobre o número da proposta ser enviado ao sistema externo (ver [`incertezas.md`](incertezas.md) item 10).

Termos mantidos como transcritos por falta de confirmação: "deixa mais a parte" (`00:00:05`), "cadastro manual" (`00:00:11`), "Boa, vou tirar com ela" (`00:01:18`), "é de 880, ou é muito bom ou não é muito bom" (`00:09:16`).
