> **Não há procedimento técnico de produto extraível desta transcrição.** O roteiro abaixo é somente um plano de triagem editorial da fonte. Nenhum passo foi executado; o MP4 não foi baixado/revisado.

# Procedimento de triagem — projeto EPT.mp4

## Fluxo A — Confirmar arquivo e metadados

1. Conferir manifesto, ponteiro LFS, tamanho e SHA-256 com a fonte obtida por canal autorizado; o registro da execução anterior declara essa conferência.
2. Verificar a associação entre nome `projeto EPT.mp4`, gravação e pasta de transcrição antes de produzir material técnico.
3. Registrar que a execução atual usou `large-v3` sem VAD (`filtro_vad: false`) e que a execução anterior com VAD gerou apenas um segmento; o artefato da primeira passagem não está nesta pasta, portanto não presumir timestamp ou conteúdo.

## Fluxo B — Revisar a fonte integralmente

1. Baixar/reproduzir o MP4 de forma autorizada e escutar do início ao fim, com revisão visual se necessária para identificar contexto/legendas.
2. Marcar quais trechos contêm fala inteligível, silêncio, ruído, áudio sobreposto ou crédito/legenda; não classificar a repetição como fala ou como alucinação sem escuta.
3. Comparar os trechos com TXT/SRT/VTT; verificar os `69` segmentos repetidos e a extensão do último cue `00:36:00–00:36:29.98` contra o áudio de `00:36:16.70`.
4. Se o arquivo estiver errado, indisponível ou sem áudio inteligível, registrar a causa e manter o item em revisão. Não inventar uma transcrição para preencher o intervalo.

## Fluxo C — Recuperar conteúdo útil, se houver

1. Se a revisão confirmar fala, solicitar novo ASR com configuração apropriada e corrigir apenas após confronto com a fonte, mantendo os originais automáticos como registro.
2. Só elaborar guia, perguntas e procedimentos de produto quando tema, termos e passos forem sustentados por áudio/telas/EF.
3. Revisar privacidade e evidências antes de publicar; manter o texto original integral conforme autorização expressa, sem expor credenciais/dados pessoais reais.

## Bloqueios

- Sem fonte confirmada ou sem revisão humana → não concluir, não declarar “sem conteúdo” e não inferir tópico a partir do título.
- Repetição de legenda/crédito pelo ASR não é requisito, operação ou instrução.
- Nenhum teste de sistema, consulta, alteração de dado ou procedimento de negócio foi identificado ou executado neste lote.
