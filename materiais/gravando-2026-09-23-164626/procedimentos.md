> **Este documento é um plano de validação, não um procedimento operacional aprovado.** Não executar em produção nem alterar perfil/chaves a partir do ASR. A gravação original e suas telas não foram verificadas neste lote; nenhum passo abaixo foi executado.

# Procedimentos — Gravando 2026-09-23 164626.mp4

## Fluxo A — Aprovar escopo e preparar ambiente

**Objetivo:** verificar, sem efeito real, a anexação de documentos e sua representação no JSON do plugin, assunto descrito em `00:00:43–00:02:12` e `00:04:19–00:05:01`.

### Pré-condições obrigatórias

- EF/schema vigentes e aprovados; esclarecer a grafia do objeto e os três campos mencionados.
- Sandbox isolado, build/versão autorizados, dados sintéticos e documentos de teste sem dados pessoais reais.
- GED/Autorizador e serviço receptor em modo de teste; integração externa real desabilitada ou substituída por stub/mock.
- Perfil GED previamente aprovado pelo responsável, com privilégio mínimo. Não conceder/remover chaves nem copiar a configuração relatada na gravação.
- Procedimento de auditoria, rollback e captura de evidência previamente definido.

### Passos

1. Confirmar com o responsável o objetivo do item, a EF/EPT, versão, base, rotina/tela do Autorizador e fronteira do plugin.
2. No schema aprovado, confirmar objeto pai (`attach_document` é apenas uma grafia ouvida), nome oficial (`attachment_document`/`attached_document` aparece em outras gravações), cardinalidade e campos. Não escolher uma grafia com base no ASR.
3. Identificar o perfil mínimo autorizado e a chave/escopo que permite consultar e anexar documentos; validar em sandbox com o dono do GED. Não usar números de perfil/chave da transcrição como configuração padrão.
4. Criar proposta e arquivos sintéticos, registrar os identificadores somente na evidência interna aprovada e proteger logs/payloads.

## Fluxo B — Cobrir ausência, um e vários documentos

1. **Nenhum documento:** enviar o cenário sem anexos e comparar o JSON ao contrato aprovado. A transcrição relata `null`, mas isso ainda precisa ser confirmado como resultado esperado, em contraste com lista vazia ou objeto ausente.
2. **Um documento:** anexar um arquivo sintético pela rotina aprovada e conferir que tipo, nome e usuário (ou os campos definidos pela EF) chegam com valores e tipos corretos no payload.
3. **Mais de um documento:** anexar dois documentos sintéticos e verificar cardinalidade, ordem, persistência, metadados e ausência de duplicação.
4. Em cada cenário, conferir o resultado no Autorizador/GED e no ponto autorizado de observação do plugin; não supor que o registro visual, o GED e o payload sejam equivalentes.
5. Comparar somente com o schema aprovado. Redigir/mascarar payload e logs antes de exportar evidência, conforme a política aplicável.

## Fluxo C — Verificar permissão sem elevar privilégio

1. Usar perfis de teste previamente aprovados: um com permissão necessária e outro sem ela, se a política de segurança permitir.
2. Para o perfil sem permissão, confirmar negação controlada e mensagem esperada, sem expor dados do documento.
3. Para o perfil autorizado, validar consulta/anexação somente no escopo permitido.
4. Se aparecer erro de chave/perfil ou for necessária alteração de acesso, interromper e obter autorização formal do responsável por GED/segurança. Não alterar permissões durante o teste sem mudança aprovada, trilha de auditoria e rollback.

## Fluxo D — Confirmar reenvio/retorno e ciclo do documento

1. Com um cenário sintético, determinar na EF se a proposta volta a uma etapa anterior, repete a esteira ou usa outro mecanismo.
2. Se o reenvio for aprovado, verificar se o primeiro documento permanece, se o segundo é adicionado uma única vez e se o JSON reflete o conjunto esperado.
3. Executar repetição somente no mock/sandbox e medir idempotência; conferir que falha/timeout não cria duplicatas nem aciona o serviço externo real.
4. Não tratar “retornar e enviar de novo” nem “seguir a esteira normal” da conversa como decisão formal de fluxo.

## Resultado e evidências

- Matriz mínima: sem documento / um documento / dois documentos; perfil sem permissão / perfil permitido; primeira execução / retorno ou reenvio aprovado.
- Para cada caso: pré-condição, resultado esperado aprovado, resultado observado, versão e referência à EF; armazenar só o mínimo necessário.
- `null`, campos, objeto pai, ordem de anexos, persistência e retry são critérios pendentes até validação da especificação.

## Bloqueios

- EF ou schema ausente/ambíguo → não testar integração.
- Ambiente externo não isolado ou dados reais → interromper.
- Necessidade de editar perfil/chaves sem aprovação → não alterar; escalar ao responsável.
- Divergência `attachment_document` × `attached_document`, ou fluxo retorno × loop sem decisão → registrar conflito e aguardar.
- Nenhum teste, alteração de perfil, chamada do plugin, consulta GED ou envio foi executado nesta análise.
