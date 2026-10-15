> **Plano de validação, não procedimento aprovado.** Foi preparado a partir de ASR não revisado, e nenhum passo abaixo foi executado. A gravação não autoriza alteração de dados ou ambientes.

# Plano de teste — recálculo e tolerância

## Fluxo A — Confirmar regra e escopo

1. Obter a EF, versão e EPT vigentes; identificar o projeto/caso correto. Os nomes “2.1”, “3.2”, “caso 3” e “caso 2” são inconsistentes no ASR (**00:00:21–00:00:35; 00:03:31–00:03:41**).
2. Confirmar com negócio/desenvolvimento a fórmula exata da tolerância, sua base de cálculo, limites inclusivos, direção de aplicação, arredondamento e comportamento para percentual zero. A conversa alterna exemplos de 1% e 10% (**00:11:46–00:13:15; 00:59:49–01:01:16; 01:06:30–01:07:03**).
3. Definir se a regra altera dados do convênio, da proposta ou de ambos; confirmar se os modos “somente recálculo” e “ambos” são seletores distintos e qual etapa da esteira cada um percorre (**00:14:54–00:15:10; 00:24:50–00:29:00**).
4. Definir quais APIs, telas, plugin, perfil e versão participam. O ASR menciona versões/ambientes divergentes, sem identificá-los de forma verificável (**00:37:37–00:39:28**).
5. Aprovar formalmente o sandbox e usar apenas massa sintética. Não reutilizar valores, propostas, identificadores ou instruções de ambiente da transcrição como dados de teste.

## Fluxo B — Preparar matriz de cenários (somente após aprovação)

1. Registrar a configuração autorizada para limite inferior, limite superior e tolerância, com fonte na EF.
2. Para cada modo que a EF exigir, planejar cenários sintéticos independentes: abaixo do limite inferior; no limite inferior; dentro da faixa; dentro da tolerância; fora da tolerância; no limite superior; e acima do limite superior.
3. Registrar para cada caso: estado inicial, configuração, valor solicitado, rota/atividade, resultado esperado, mensagem/estado de esteira e evidência necessária. Não preencher o esperado por extrapolação da fala.
4. Se a regra diferir por “somente recálculo” e “ambos”, repetir a matriz de forma comparável, controlando versão, dados e demais condições.
5. Submeter a EPT e a matriz para revisão do responsável de CQ, desenvolvimento e negócio antes da execução.

## Fluxo C — Executar em ambiente autorizado

1. Confirmar por canal oficial o ambiente, a versão instalada, a configuração e a ausência de uso concorrente que possa contaminar o resultado.
2. Se houver atualização, seguir somente o runbook vigente, com backup, autorização do responsável e plano de rollback. Não copiar binários/arquivos entre máquinas ou apontar para base compartilhada com base apenas na conversa (**00:37:37–00:39:28**).
3. Criar ou selecionar proposta e convênio sintéticos conforme autorização; não usar dados reais nem mudar o convênio fora do ambiente aprovado.
4. Executar um caso por vez, observar a atividade/estado e registrar resultado real. Parar se o estado divergir da EF ou se a configuração/versão não puder ser confirmada.
5. Não usar ou enviar JSON, CPF, IOF, API, plugin ou chamada mencionados no ASR sem especificação e autorização próprias (**00:05:05–00:06:22; 01:07:48–01:08:44**).

## Fluxo D — Evidência e encerramento

1. Comparar resultado real com o esperado aprovado; registrar versão, ambiente autorizado, caso, parâmetros sintéticos e timestamp.
2. Guardar apenas evidência aprovada e minimizada conforme política vigente; revisar a captura final antes de compartilhá-la.
3. Reportar diferenças como defeito/questão para triagem, sem concluir que são falha de produto até controlar versão, modo, entrada e pré-condições.
4. Remover massa temporária apenas conforme o procedimento autorizado; não limpar dados ou pastas por inferência.

## Critérios de parada

- EF, fórmula, limite, modo, versão, ambiente ou resultado esperado não identificados → não executar.
- Ambiente compartilhado/produção, massa real ou autorização ausente → interromper.
- Instrução baseada apenas em ASR, inclusive nome de campo, código, servidor ou versão → confirmar com fonte oficial.
- Divergência de resultado entre modos/versões sem variáveis controladas → registrar como inconclusiva; não declarar correção.
- Nenhuma consulta SQL é reproduzida na transcrição; não inventar nem executar SQL com base neste pacote.
