# Incertezas e pendências — Gravando 2026-09-23 164626.mp4

Status geral: **em revisão**. Os pontos abaixo vêm de ASR `large-v3` e não foram conferidos contra o áudio, as imagens ou a EF. A transcrição foi preservada integralmente conforme instrução expressa do responsável; isso não valida os termos nem os resultados.

1. **Cobertura temporal:** áudio declarado com `2039,98 s` (`00:33:59.98`); 396 segmentos ASR e `duracao_transcricao_s: 891,9`. O último cue do SRT termina em `00:26:14.39`, deixando `00:07:45.59` até o fim do áudio sem transcrição. Além disso, há intervalos sem segmentos ao longo da gravação. Não presumir silêncio nem inventar conteúdo; pedir revisão integral do áudio.
2. **Objeto JSON:** a fala ouve “Attach documento”, enquanto gravações relacionadas registram `attachment_document` e `attached_document`. Pode ser objeto pai, diferença de nomenclatura na EF ou erro de reconhecimento. Confirmar no schema vigente.
3. **Campos e tipos:** três campos são citados (`document_type`, `document_name`, `user`), mas nomes exatos, tipos, obrigatoriedade, origem e nulabilidade não estão confirmados. A conversa menciona código/sigla versus descrição para tipo de documento sem resolver.
4. **Resultado sem documento:** os participantes afirmam que o JSON retornou `null`. Não foi possível verificar o payload, se a propriedade foi omitida ou se a forma correta do contrato é `null`, lista vazia ou objeto vazio.
5. **Múltiplos documentos:** a conversa relata que o JSON passou a conter dois documentos após voltar/reexecutar o fluxo. Não há evidência examinada, lista de critérios nem confirmação de ordem, retenção, cardinalidade ou deduplicação.
6. **Fluxo de retorno:** uma fala diz “retornei e enviei de novo”; ao final, discutem “retornar o fluxo” versus “deixar o loop” e dizem seguir a esteira normal. Etapa, regra de reentrada, idempotência e política de retry continuam sem decisão técnica comprovada.
7. **Perfil e chaves GED:** o ASR relata mensagens associadas às chaves 2 e 4 e ao perfil GEDOC 6, seguidas de ajuste e mensagem de sucesso. Não sabemos o nome técnico das chaves, quais mudanças foram feitas, se a configuração era isolada ou aprovada, nem qual privilégio deveria ser concedido. Não reutilizar como instrução.
8. **Identidade dos componentes:** `GED`, `GEDOC`, `G-Doc`, `GDock`, `CPS` e outras siglas podem representar componentes diferentes ou erros ASR. Confirmar arquitetura, serviço, rotina e versão com a equipe responsável.
9. **Persistência/observabilidade:** não está claro se o resultado autoritativo é o registro no Autorizador, a resposta do GED, o JSON do plugin ou a persistência do sistema externo. Também não se confirma se deve existir nova linha visível no registro.
10. **Privacidade e fonte:** a orientação expressa do responsável em 2026-10-14 autoriza preservar integralmente a transcrição, sem cortes/mascaramento; ele declarou que fará cópia para uso interno e excluirá o repositório ao final. Isso não dispensa a proteção contra credenciais ou dados pessoais reais. O MP4 não foi baixado/revisto visualmente neste lote; conferir o escopo e a retenção em [`../PRIVACIDADE_E_RETENCAO.md`](../PRIVACIDADE_E_RETENCAO.md) §§12–13.
11. **Evidência e teste:** embora a fala relate execução e sucesso, este lote não confirma build, ambiente, versão, documento anexado, permissões, conteúdo JSON, destino nem efeitos externos. Nenhum teste foi executado aqui.

## Critérios para sair de revisão

- Escutar/rever o MP4 integralmente, incluindo `00:26:14.39–00:33:59.98` e intervalos sem segmentos.
- Comparar campos e fluxo com a EF/EPT aprovada; resolver a nomenclatura em conflito.
- Obter confirmação formal de perfil/permissões e da regra de retorno/reenvio.
- Reexecutar, se autorizado, os casos sem anexo, um anexo e múltiplos anexos em sandbox isolado com dados sintéticos e receptor mock.
- Conferir e guardar evidência mínima sanitizada conforme a política de retenção aplicável.
