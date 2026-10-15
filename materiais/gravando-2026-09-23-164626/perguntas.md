# Perguntas de validação — Gravando 2026-09-23 164626.mp4

As perguntas abaixo vêm da transcrição ASR e não têm resposta validada pela EF, pelo vídeo ou por teste independente. Resolver com os responsáveis funcionais/técnicos antes de converter qualquer fala em requisito.

## Especificação e JSON

1. Qual EF/EPT e item de demanda definem a alteração descrita? A gravação usa um exemplo anterior de envio de atributo e não identifica claramente a demanda atual.
2. Qual é a grafia oficial do objeto: `attachment_document`, `attached_document` ou outra? Outras gravações da mesma funcionalidade divergem; qual documento vigente prevalece?
3. O nome “Attach documento” refere-se ao objeto pai, a uma propriedade, à rotina de tela ou a outra coisa?
4. Quais são os campos obrigatórios e tipos? A conversa cita tipo do documento, nome do documento e usuário, mas não confirma nomes de propriedade, nulabilidade ou origem.
5. `document_type` representa código, sigla ou descrição? Como tratar tipos não cadastrados, nomes repetidos ou alterações de cadastro?
6. O usuário transmitido é quem anexou, quem iniciou o processo ou outro ator? Qual identificador/descrição o contrato exige?
7. Quando não há documento, o contrato exige `null`, lista vazia, propriedade omitida ou objeto vazio? O relato de que “retornou nulo” precisa ser conferido na EF e no payload.
8. Como representar múltiplos documentos: ordem, cardinalidade, duplicatas, metadados e limite de tamanho/quantidade?
9. O JSON é apenas enviado ao plugin ou também precisa ser persistido/mostrar nova linha em alguma tela? Qual ponto é fonte de verdade para o aceite?

## GED, Autorizador e permissões

10. Qual é a rotina/tela oficial do Autorizador para anexar e consultar o arquivo? Quais tipos e formatos são aceitos?
11. Qual serviço/versão do GED é chamado, e quais são as regras aprovadas para perfil/chaves? A gravação relata mensagens de permissão e ajuste em ambiente de teste, mas não autoriza replicar a configuração.
12. Qual matriz de autorização deve ser testada para consulta e anexação? Quem aprova mudança de perfil, e como ficam trilha de auditoria e rollback?
13. Qual é o resultado esperado quando arquivo ou cadastro do tipo não existe, quando o GED está indisponível ou quando o usuário não tem acesso?

## Fluxo, reenvio e cobertura

14. Ao reprocessar, a proposta deve voltar a uma etapa anterior, repetir a esteira ou seguir uma rotina de loop? A transcrição registra alternativas e não prova uma decisão formal.
15. Um documento já anexado precisa permanecer quando um segundo é acrescentado? Como garantir que o retry não duplique arquivos ou não perca anexos existentes?
16. Qual endpoint/serviço recebe o JSON e como isolar completamente a execução do sistema externo real durante o teste?
17. A duração ASR acumulada é `891,9 s`; o último cue termina em `00:26:14.39`, mas o áudio declarado tem `00:33:59.98`. O trecho restante e os intervalos sem fala reconhecida contêm silêncio, fala não detectada ou interrupção? Quem fará a revisão integral?
18. A saída automática foi copiada sem cortes/mascaramento conforme diretriz expressa do responsável; qual classificação, acesso e retenção se aplicam ao repositório público e aos objetos upstream de transcrição?
