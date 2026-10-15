> **Status:** plano de teste derivado de ASR; não é sequência aprovada nem execução realizada. Confirme a EF vigente, a rota e os critérios com o responsável técnico antes de usar.

# Procedimentos — Primeiro projeto.mp4

## Fluxo A — Validar contrato de consulta por proposta/operação (sandbox)

**Objetivo:** verificar o endpoint simplificado mencionado para listar documentos GED por número da proposta ou da operação (**00:01:37–00:02:25**).

### Pré-condições

- EF e Anexo I aprovados, com nome/rota HTTP, tipos/campos exatos, obrigatoriedade dos parâmetros, status de erro e formato de resposta.
- Web API/Autorizador/GED em sandbox isolado, versões liberadas e procedimento de rollback.
- Dados inteiramente sintéticos: uma proposta de teste, uma operação de teste, vínculo conhecido entre elas e documentos GED preparados.
- Perfil GED e resolução operação→proposta confirmados pela equipe técnica. Não copiar cliente, base, UDL, caminho nem identificadores da gravação.
- Critérios de privacidade e armazenamento de evidências aprovados.

### Sequência de cenários (não executada)

1. **Regressão por proposta:** chamar o comportamento conhecido por número de proposta e comparar com o contrato vigente (**00:00:52–00:01:02**).
2. **Novo endpoint — só proposta:** solicitar a listagem no endpoint simplificado com proposta de teste; conferir a lista de arquivos GED e os campos definidos na EF.
3. **Novo endpoint — só operação:** chamar com operação de teste, sem proposta na requisição; confirmar que a busca interna encontra a proposta pertinente quando a regra do GED exigir esse vínculo (**00:07:54–00:08:29**).
4. **Ambos informados:** testar somente após confirmar a regra formal. A interpretação oral sugere que um identificador não deve ser exigido quando o outro está presente, mas não define precedência nem conflito entre identificadores (**00:03:00–00:03:42**).
5. **Nenhum informado:** confirmar que a requisição é rejeitada conforme o contrato. A fala considera incorreto o sucesso sem proposta e sem operação (**00:03:33–00:03:42**); status/corpo exatos não são informados.
6. **Conferência de conteúdo:** validar que o retorno contém os campos de arquivo especificados e não inclui itens/dados do checklist (**00:03:52–00:04:23; 00:04:41–00:05:09**).
7. **Download:** caso esteja dentro do escopo, exercitar o caminho de download e o parâmetro de operação somente após confirmar se é outro endpoint ou continuação do fluxo (**00:08:42–00:09:16**).
8. **Registrar o resultado:** comparar esperado/obtido por cenário, guardar evidência sanitizada e interromper se houver divergência de contrato, associação, perfil ou exposição de dados.

**Não inferir:** nome de rota, payload, propriedades exatas, códigos HTTP ou comportamento para identificadores inconsistentes. Esses detalhes não foram demonstrados.

## Fluxo B — Preparar ambiente de teste (checklist de aprovação, não instrução de instalação)

A fala cita Autorizador, subsite, Gdoc e Web API e diz que a Web API seria o componente modificado (**00:09:18–00:10:22**). Antes de montar ou alterar ambiente, obter aprovação técnica para:

- identificar versões/artefatos exatos e componente que recebe a alteração;
- confirmar que as versões estão aprovadas para teste — a sugestão oral de usar versão recente não autoriza versão não aprovada (**00:10:29–00:10:42**);
- validar origem dos dados e o perfil GED sem expor chave/valor da configuração;
- definir produto/esteira/checklist somente se forem pré-requisitos documentados para os dados sintéticos;
- fixar ordem de implantação, validação de saúde e rollback.

A conversa não fornece caminho de instalação nem configuração reproduzível. Não publicar endpoint/appsettings, não apontar base real e não alterar checklists sem requisito formal.

## Fluxo C — Diagnóstico de identificador de operação (sem SQL fornecido)

A pessoa sugere que, se faltar o número da operação no contexto da proposta, seja buscado na base para montar a requisição (**00:02:35–00:02:57**). Nenhuma consulta é lida ou mostrada. O teste deve usar a fonte de dados sintéticos aprovada e uma consulta documentada pelo responsável, se necessária. Não inventar nem executar SQL a partir da fala; não usar valores ou bases citados no áudio.

## Evidência e encerramento

A orientação verbal cita versão, percurso até o caso e correlação entre objeto/teste e retorno da API (**00:14:16–00:15:18**). Em sandbox, registrar apenas informação sintética, sem IDs de cliente, dados pessoais, URL/segredo, host ou caminho interno. O lote não contém evidências nem resultado de execução.
