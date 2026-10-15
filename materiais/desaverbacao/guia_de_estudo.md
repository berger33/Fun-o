> **Leitura preliminar de ASR.** O vídeo, o áudio e as telas não foram revistos nesta sessão. Este guia distingue o que o ASR registra da síntese didática; não é regra de negócio aprovada nem instrução para alterar sistemas.

# Guia de estudo — `dESAVERBAÇÃO.mp4`

- **Categoria:** `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO`; SQL apenas mencionado, sem consulta reproduzida.
- **Sistema:** Autorizador, Web Empregador/Empregador Online, Consignado Privado, esteira e plugin/stub segundo o ASR; nomes oficiais, telas e arquitetura não foram verificados.
- **Assunto:** conversa de treinamento/depuração sobre cancelar uma proposta e solicitar a exclusão/desaverbação de uma operação, incluindo parâmetros, decisão da esteira e conferência do retorno.
- **Fonte:** transcrição automática `faster-whisper large-v3`, copiada da referência `arena/17453ccc-fun-o`; não revisada contra o áudio ou vídeo nesta sessão.
- **Confiança da extração:** **baixa** para detalhes técnicos e sequência operacional; o tema geral é recorrente no ASR, mas nomes, siglas, valores, estados e resultados não foram conferidos na fonte primária.
- **Cobertura declarada:** 1.274 segmentos; áudio informado `01:13:40.67`. Último cue `01:13:37.080–01:14:07.060`, 26,39 s além da duração informada. Não inferir silêncio ou cobertura audiovisual integral.
- **Estado:** **em revisão**. Revisão humana/visual e validação da EF/runbook pendentes.

## 1. Tema e contexto relatado

**Fala ASR:** no começo, um interlocutor diz que a proposta deve estar averbada antes da exclusão de averbação (`00:00:34–00:00:45`). Mais tarde, a conversa descreve cancelar uma proposta, localizar o pedido/retorno e conferir o status de uma operação (`00:13:33–00:17:18`; `01:03:19–01:06:33`).

**Síntese:** a gravação parece acompanhar um cenário de teste de cancelamento/desaverbação de consignado. A fala mistura cadastro da proposta, configuração do empregador, esteira, serviços de exclusão e acompanhamento da operação. Não é possível confirmar se “cancelamento de proposta”, “exclusão de averbação” e “desaverbação” são sinônimos ou etapas distintas no contrato atual.

## 2. Parâmetros e preparação descritos

- **Fala ASR:** os interlocutores chamam de “modelo de averbação” uma rotina que identificam como cadastro de parâmetros do Consignado Privado; distinguem-na dos parâmetros gerais/horários de serviço (`00:01:36–00:03:44`).
- **Fala ASR:** mencionam um link de stub e vínculo com empregador; um valor numérico é sugerido para esse vínculo (`00:03:00–00:04:01`). Não reutilizar esse valor sem confirmação documental.
- **Fala ASR:** discutem se o tipo de exclusão deveria estar manual ou automático, e falam em alterar a configuração (`00:04:22–00:05:10`; `00:13:33–00:13:47`). O trecho não demonstra uma regra aprovada nem permite concluir que essa alteração resolveu o problema.
- **Síntese:** antes de qualquer teste, identificar a tela/campo corretos, o contrato do stub, o empregador de teste e a configuração prevista na EF/runbook. Não copiar configurações da gravação.

## 3. Falha inicial e investigação

- **Fala ASR:** após uma tentativa, a mensagem reconhecida é “Proposta não se encontra na situação para ser escolhida” (`00:15:05–00:15:19`).
- **Fala ASR:** um participante descreve dois componentes: um plugin de levantamento que localizaria propostas em situações como liquidada, cancelada ou reprovada; depois haveria um serviço de exclusão (`00:15:42–00:16:11`). Em seguida, a conversa situa propostas canceladas/integradas em outra rotina (`00:16:54–00:17:18`).
- **Síntese:** o erro pode estar relacionado à elegibilidade/estado e ao percurso da esteira, mas o ASR não traz evidência suficiente para atribuir causa. A separação entre seleção/levantamento e envio da exclusão é apenas uma descrição oral a confirmar.
- **Fala ASR:** são revisitados retornos do stub, um código de sucesso, “BF”/“competência” e versão do plugin; os participantes demonstram dúvida sobre o que explica a falha (`00:18:06–00:23:39`). Não há resultado que estabeleça um código ou versão corretos.

## 4. Convênio, produto e esteira

- **Fala ASR:** os interlocutores dizem consultar convênio e produto para conferir a forma de recebimento “desconto em folha” (`00:24:47–00:28:52`). A fala menciona uma consulta SQL e os nomes reconhecidos como `Cprop`, `ppcodicomv` e `ppcodprd` (`00:24:47–00:25:44`); a consulta não aparece no TXT ASR.
- **Fala ASR:** a árvore de decisão é chamada de esteira; a rotina “Relacionamento modelo versus produto” é descrita como lugar para desvincular/revincular a esteira durante a alteração (`00:29:20–00:31:17`; `00:43:21–00:44:01`).
- **Fala ASR:** são discutidos tipos de decisão `A`, `P` e `F`; o interlocutor associa `A` a avançar automaticamente, `P` a escolher/aguardar processo e `F` a finalizar atividade. As explicações aparecem em contexto de demonstração oral da tela (`00:32:33–00:40:44`).
- **Fala ASR:** a conversa descreve adicionar um processo de cancelamento com código `99`, tipo `F`, e um processo automático associado, e depois restaurar o vínculo do produto à esteira (`00:40:46–00:44:01`). Isso é um relato de configuração daquela sessão, não recomendação para outro ambiente.

**Síntese didática:** separar o diagnóstico em quatro camadas — estado da proposta, configuração de exclusão/retorno, decisão/ordem da esteira e retorno do serviço. Registrar cada camada independentemente em uma EPT aprovada; não deduzir que os valores/códigos da gravação constituam padrão.

## 5. Margem e ambiente de teste

**Fala ASR:** os interlocutores dizem que o cenário é “mocado” e que não consumiria a margem de cliente como uma chamada real; também mencionam ambientes de cliente/Dataprev e limites de valor/operações associados ao empregador/WebTabelas (`00:44:32–00:48:10`).

**Síntese e cuidado:** a fala não autoriza chamada a ambiente real, uso de CPF/dados reais nem alteração de margem. Validar que o mock/stub, massa sintética, limites e ambiente são os aprovados antes de planejar qualquer teste.

## 6. Resultado relatado, não confirmado

**Fala ASR:** na parte final, a conversa relata uma nova averbação/consulta, cancelamento, acompanhamento do levantamento, status “concluído”, consulta de movimentações do contrato e status “desaverbado”; um participante diz que o retorno de sucesso foi registrado após uma alteração cuja palavra é reconhecida pelo ASR como “streaming” (termo e significado não confirmados) (`01:00:58–01:06:33`).

**Limite:** esta é somente a fala reconhecida pelo ASR. Não vimos a tela, a resposta, o banco ou o vídeo; portanto não afirmamos que a operação tenha sido concluída nem que o status/causa estejam corretos.

## 7. Cenários de exclusão citados

Ao final, são mencionados como cenários diferentes a exclusão de operação normal após inclusão confirmada e cancelamento/reprovação, uma situação dita como “recomando de exclusão”, operação liquidada/estornada e operações normal, de refinanciamento e de portabilidade (`01:07:23–01:08:35`). Algumas palavras são reconhecimentos ASR incertos. Confirmar a taxonomia e as condições de cada evento na EF vigente.

## Resumo

O ASR sustenta que a conversa trata de investigar e testar um fluxo de cancelamento/desaverbação, passando por parâmetros de Consignado Privado, stub, esteira e retorno. A causa da falha inicial, a semântica dos tipos `A/P/F`, os valores de configuração, a consulta SQL, a versão e o sucesso final continuam sem confirmação. Use o pacote apenas como lista de perguntas para revisão e validação autorizada; não o use como runbook.

--- Atualização Passo 8 (2026-10-15) — timestamps reais do ASR (não validado visualmente) ---
- 00:00:43 — "exclusão de averbação" (conceito reconhecido pelo ASR; não confirmar como procedimento oficial sem revisão visual).
- 00:01:36 — "modelo de averbação" (rotina mencionada; nome oficial da tela não confirmado).
- 00:03:04 / 00:03:38 / 00:03:44 — "stub", "exclusão", "link do stub" (componentes mencionados; endpoint/configuração não registrados nesta sessão).
- 01:05:36–01:06:33 — "consulta movimentações de contrato" / status "desaverbado" (último trecho instrutivo do ASR; último cue excede áudio em 26,39 s).
Nenhum destes timestamps substitui validação visual, confirção de SQL ou verificação de configuração.
