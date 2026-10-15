> **Fonte deste rascunho:** transcrição automática `faster-whisper large-v3`; MP4, especificação e telas não foram inspecionados neste lote. Trate nomes e requisitos abaixo como preliminares até comparar com a EF e a gravação.

# Guia de estudo — Primeiro projeto.mp4

- **Categoria:** `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `INFRA_E_ACESSO`, `SQL` (menção sem consulta), `DÚVIDA_OU_CONFLITO`
- **Sistema:** Autorizador, Web API de documentos anexados, GED/Gdoc e ambiente de teste (nomes exatos dos componentes e configurações pendentes de confirmação)
- **Assunto:** consulta e download de documentos GED vinculados a uma proposta **ou** a uma operação, com proposta de cenários de teste para um novo endpoint simplificado
- **Fonte:** `Primeiro projeto.mp4` (616715835 bytes; SHA-256 `3f761d2a…`), duração declarada `00:17:53.66`
- **Confiança da extração:** **baixa a média** — síntese baseada em ASR `large-v3` com 274 segmentos; sem escuta humana integral nem inspeção visual da especificação/API. Uma parte não técnica e possíveis identificadores de teste/ambiente foram omitidos da cópia pública.

## 1. Objetivo da mudança descrita

A conversa lê o objetivo de uma alteração à Web API de documentos anexados: permitir consultar e baixar documentos do GED vinculados a uma operação mesmo quando não há proposta vinculada, mantendo o caso atual de consulta por número da proposta (**00:00:33–00:01:02; 00:01:17–00:01:44**). O endpoint existente é descrito como dependente somente do número da proposta; o novo endpoint é chamado verbalmente de **“Documentos anexados simplificado”** (**00:00:52–00:01:02; 00:02:00–00:02:14**).

**Importante:** a EF não foi aberta neste lote e o método/contrato não foi exercitado. Confirmar nome, rota, campos e regras no documento aprovado antes de implementar ou testar.

## 2. Parâmetros de consulta

A explicação indica dois identificadores de entrada — **número da proposta** e **número da operação** — e lê a regra como “obrigatórios condicionais”: se um for informado, o outro pode ser opcional (**00:02:25–00:03:18**). Ela recomenda verificar cada caminho separadamente e tratar como suspeito um sucesso sem nenhum dos dois (**00:03:18–00:03:42; 00:08:29–00:08:36**).

| Entrada para validar | Interpretação preliminar da fala | Confirmação necessária |
|---|---|---|
| Somente proposta | Deve permitir a consulta conforme o comportamento já conhecido | Verificar regressão do endpoint existente e regra do novo endpoint |
| Somente operação | Deve permitir consulta/download sem exigir proposta na requisição | Conferir no back-office o vínculo exigido pelo GED e a regra de busca interna |
| Proposta e operação | A fala sugere que um parâmetro não deve ser exigido se o outro já foi enviado | Confirmar se ambos podem ser fornecidos simultaneamente e como conflitos entre eles são tratados |
| Nenhum identificador | A fala considera incorreto que a API responda com sucesso | Confirmar resposta de validação prevista pela EF; status/corpo não foram ditos |

Não há exemplos de payload, URL, status HTTP ou execução real. A extração do número da operação por consulta SQL é mencionada sem a consulta; não reutilizar query ou fazer alteração de dados com base nesta conversa (**00:02:35–00:02:57**).

## 3. Resultado e diferença em relação ao checklist

- O retorno é descrito como uma lista com identificadores de armazenamento/arquivo, um ID único e nome/extensão do arquivo (**00:03:52–00:04:23**). Nomes exatos das propriedades e estrutura do objeto precisam ser lidos na EF/Anexo I.
- O novo endpoint simplificado deve apresentar somente informações de arquivos anexados ao GED pela proposta ou operação; a fala diz que **não** deve trazer dados de checklist da proposta (**00:04:41–00:05:09; 00:06:56–00:07:37**).
- O checklist de cadastro/análise/formalização é descrito como um conceito separado da lista de arquivos GED (**00:05:28–00:06:38; 00:07:01–00:07:37**). Não confundir um item ou categoria do checklist com um documento retornado pelo endpoint simplificado.
- A conversa menciona um parâmetro de número de operação para possibilitar download e sugere outra etapa/método da API (**00:08:42–00:09:16**). Se consulta/listagem e download são endpoints distintos, confirmar assinatura e sequência na especificação.

## 4. Relação com perfil GED/back-office

Segundo a explicação, o perfil GED seria o mesmo configurado para o Autorizador por uma chave de configuração identificada verbalmente como `perfil gdoc` (**00:07:37–00:07:54**). Para consulta com número da operação, o sistema buscaria internamente o número de proposta correspondente no back-office; o interlocutor diz que o perfil GED usa o número da proposta como identificador (**00:07:54–00:08:29**).

**Leitura a confirmar:** não é preciso enviar a proposta junto com a operação, mas a relação/identificador necessário ainda pode precisar existir nos dados de back-office. A gravação não explica a regra para operação sem esse vínculo nem como resolver inconsistência entre proposta e operação.

## 5. Planejamento de teste

A conversa recomenda testar com a proposta já conhecida e também com o caminho por operação, para verificar a mudança e evitar regressão (**00:00:06–00:00:27; 00:08:29–00:08:36**). Como preparação menciona Autorizador, um subsite, Gdoc e a Web API como componente de alteração (**00:09:18–00:10:22**), mas não demonstra o ambiente, versão, instalação, rota ou dados.

Antes de qualquer execução, obter aprovação do responsável e confirmar em ambiente isolado:

1. versão e componentes autorizados para o teste; a conversa sugere versões aprovadas/mais recentes, mas essa fala não substitui a política de release (**00:10:29–00:10:42**);
2. dados sintéticos com proposta, operação e documentos GED conhecidos;
3. regra formal para cada combinação dos dois parâmetros e associação operação→proposta;
4. corpo de resposta esperado, itens de checklist a excluir e método de download;
5. critérios de parada, limpeza e rollback.

Não usar identificadores de cliente/base citados na gravação, não apontar para produção e não baixar/publicar aplicações até confirmação técnica. Os nomes da base e do cliente foram substituídos na transcrição sanitizada.

## 6. Evidências sugeridas (a validar)

A pessoa que orienta menciona registrar versão, caminho do cenário, associação entre o objeto de teste e a requisição, e retorno/método da API (**00:13:12–00:15:18**). Se o responsável aprovar a coleta, usar evidências sanitizadas que mostrem apenas:

- versão aprovada e ambiente de teste sem host/caminho interno desnecessário;
- qual dos dois identificadores foi fornecido (valores sintéticos mascarados);
- resultado da listagem e ausência de dados de checklist;
- resultado do download, se estiver no escopo.

O áudio fala também em opções de execução “N” e “W” para evidenciar aplicações (**00:13:12–00:14:08; 00:14:16–00:16:02**). O significado/efeito dessas opções não é explicado; não as tratar como etapa obrigatória sem documentação vigente.

## 7. Limitações e síntese

O ponto central é validar um novo caminho de busca de documentos GED pela operação, sem exigir que o consumidor envie número de proposta, preservando a consulta existente por proposta e excluindo o checklist do retorno simplificado. A regra depende do vínculo interno entre operação, proposta e perfil GED.

Não há SQL literal, chamada executada, payload, código-fonte, tela ou evidência de resultado. O material é um guia de leitura do ASR e de planejamento de perguntas/testes, não um runbook aprovado. Ver [`procedimentos.md`](procedimentos.md), [`perguntas.md`](perguntas.md), [`glossario.md`](glossario.md), [`incertezas.md`](incertezas.md) e [`transcricao.md`](transcricao.md).
