> **Fonte deste rascunho:** transcrição automática `faster-whisper large-v3`; mídia e telas não foram revisadas neste lote. As afirmações abaixo são hipóteses extraídas do ASR, não configuração aprovada.

# Guia de estudo — MCB - QISTA.mp4

- **Categoria:** `PROCESSOS`, `SISTEMAS`, `NEGOCIO`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO`
- **Sistema:** Autorizador, módulo MCB, API de consulta de pontuação, WebTabelas e ambiente local de teste (nomes/versões precisam de confirmação)
- **Assunto:** validação de agentes certificados durante a esteira de uma proposta, configuração de integração MCB e investigação de cadastro de promotora/produto não encontrado
- **Fonte:** `MCB - QISTA.mp4` (543851523 bytes; SHA-256 `5e9d76d8…`), duração declarada `00:15:46.97`
- **Confiança da extração:** **baixa a média** — organização baseada na transcrição automática `large-v3` com 199 segmentos; sem escuta humana nem inspeção visual neste lote. Siglas, nomes de tela/tabela, códigos e a sequência de configuração permanecem por confirmar.

## 1. Objetivo e contexto

A conversa explica, em termos gerais, como o Autorizador poderia consultar informações de certificação/pontuação de um agente no módulo MCB ao processar uma proposta. Também tenta orientar um teste de promotora interna/externa e discute um erro de cadastro relacionado à disponibilidade de formas de liberação ou à mensagem “produto não encontrado”.

A explicação é verbal e mistura contexto de negócio, configuração do MCB/API e diagnóstico de um ambiente local. Não é uma demonstração completa nem um runbook aprovado.

## 2. Conceitos e fluxo descritos

### 2.1 Consulta de agente durante a esteira

- A pessoa que apresenta descreve a certificação do agente na Núclea e uma pontuação/status, com possíveis suspensões temporárias ou definitivas (**00:00:00–00:00:28**). Limite, critérios e estados oficiais não são verificados.
- Ao informar os dados do agente numa proposta, o Autorizador consultaria o MCB por API para obter um resultado que permita ou impeça a continuidade, incluindo pontuação e situação do agente (**00:00:33–00:01:13**). A transcrição contém a menção a CPF, mas nenhum número foi reproduzido neste guia.
- O acionamento é associado a uma atividade configurada na esteira. A conversa diz que a configuração do MCB deve relacionar a esteira e a atividade correspondentes, para que os dados de configuração coincidam (**00:01:13–00:01:52; 00:02:22–00:02:52**).
- O MCB é descrito como módulo separado e a comunicação como mediada por API (**00:02:04–00:02:19**). Não foram mostrados endpoint, parâmetros, autenticação, payload ou tratamento de falha.

### 2.2 Teste por tipo de promotora

A conversa sugere testar a classificação da promotora como **interna** ou **externa**, pois o comportamento de validação do agente seria diferente (**00:07:27–00:09:01**). A navegação falada aponta para WebTabelas e cadastro de promotora, com a ressalva de que em outro ambiente ela poderia aparecer como uma origem (**00:04:22–00:05:59; 00:06:25–00:07:59**).

Como hipótese de cenários — não como resultado aprovado:

| Cenário a preparar no ambiente autorizado | Comportamento esperado segundo a fala | O que ainda validar |
|---|---|---|
| Promotora classificada como interna | A conversa sugere que a validação do agente pode não ocorrer | Confirmar a regra funcional e o evento/etapa que deve ou não ser acionado |
| Promotora classificada como externa | A conversa sugere validação do agente e consulta de certificação/pontuação na esteira | Confirmar resposta do MCB, status, critério de bloqueio/liberação e evidência |

### 2.3 Configuração de integração (apenas pontos mencionados)

A fala cita configurar no MCB o vínculo de esteira/atividade, publicar uma API de consulta de pontuação e apontar para ela nas configurações do Autorizador (**00:02:22–00:02:52; 00:10:02–00:10:42**). Não informa os valores, a URL, a versão ou os passos completos. Tratar isso somente como mapa de componentes para confirmação com o responsável técnico; não publicar, alterar ou apontar uma URL baseado apenas no ASR.

## 3. Diagnóstico do cadastro e da consulta de promotora

- A apresentadora atribui a ausência de formas de liberação a um erro de cadastro/base (chamado de “T-Lib/Telib” no ASR), não ao código da aplicação (**00:03:54–00:04:20; 00:06:03–00:06:21**). É uma avaliação feita sobre um ambiente local e não prova a causa em outro ambiente.
- A consulta da promotora é direcionada verbalmente ao WebTabelas; a promotora pode ser representada por uma origem, em vez de existir sob o nome de uma tabela “promotora” (**00:04:22–00:05:59; 00:06:25–00:06:46**). Siglas e categorias de origem precisam ser conferidas na documentação/tela vigente.
- Para o erro “produto não encontrado”, a fala pede os dados das origens relevantes (promotora, órgão, empregador) para investigar uma possível inconsistência em três tabelas relacionadas (**00:14:29–00:15:24**). As tabelas e a regra de correlação não são nomeadas de forma verificável.
- A conversa menciona alterações por `INSERT`/`UPDATE` apenas como possibilidade, sem fornecer comandos ou autorização (**00:02:54–00:03:09**). Nenhum SQL foi demonstrado ou executado nesta análise; não alterar a base com base nessa fala.

## 4. Ambiente e dependências citados

A conversa passa por uma versão local do MCB que poderia estar antiga ou sem a configuração necessária; menciona ainda reinstalação do ambiente, publicação de componentes um a um, troca de apontamento UDL e erro ao abrir outra ferramenta (**00:09:09–00:12:08; 00:13:49–00:14:16**). Isso descreve o contexto individual da chamada, não um padrão de implantação. Versões, UDL, origem dos dados, dependências e sequência de publicação não foram confirmados.

## 5. Cuidados e limites

- Não assumir que pontuação máxima, faixas de suspensão, nomes de tela, códigos de sistema ou classificação interna/externa transcritos sejam valores oficiais.
- Não reutilizar os códigos candidatos `190` e `061` sem conferir a especificação/tela autorizada (**00:10:02–00:10:18**).
- Não copiar uma correção feita numa base local nem executar `INSERT`, `UPDATE` ou outra alteração; não há script, backup documentado, autorização ou rollback nesta conversa.
- Não publicar URL, arquivo de configuração, UDL ou segredo de API. Nenhum valor de conexão é necessário para este guia.
- Não considerar “pegar a última versão”, publicar API ou mudar configuração como um procedimento completo: os requisitos e o ambiente-alvo não estão definidos.
- O procedimento de teste ainda depende da regra de negócio, das versões e do resultado esperado aprovados pelo responsável.

## 6. Roteiro para validação humana

1. Conferir a gravação e o material funcional oficial para confirmar termos, nomes e estados de certificação.
2. Identificar qual atividade da esteira aciona a consulta MCB e qual vínculo a configuração exige.
3. Aprovar cenários internos/externos em ambiente isolado, com critérios observáveis para consulta, continuidade/bloqueio e tratamento de falha.
4. Confirmar em documentação autorizada a representação/cadastro da promotora e as origens necessárias ao diagnóstico.
5. Investigar “produto não encontrado” com responsável técnico, sem alterar tabelas até haver instrução aprovada e rollback.

Ver também [`procedimentos.md`](procedimentos.md), [`perguntas.md`](perguntas.md), [`glossario.md`](glossario.md), [`incertezas.md`](incertezas.md) e [`transcricao.md`](transcricao.md).
