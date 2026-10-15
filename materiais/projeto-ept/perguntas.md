# Perguntas de validação — projeto EPT.mp4

> As perguntas abaixo tratam da fonte e da falha/limitação de extração, não de regras do produto. Timestamps se referem ao SRT/VTT atual, não a fala confirmada.

1. `projeto EPT.mp4` é realmente o arquivo pretendido para este item do manifesto, e o nome corresponde à gravação? (metadados)
2. O áudio contém fala inteligível ao longo dos 36 minutos? Revisar a fonte integral; o ASR não permite concluir ausência de fala.
3. O que explica a repetição de “Legenda Adriana Zanotto” em 69 segmentos, desde `00:00:00` até `00:35:30`: conteúdo audível, crédito/legenda visível, falha de segmentação ou alucinação? (00:00:00–00:35:59)
4. Por que o texto é segmentado em intervalos regulares de aproximadamente 30 segundos? A segmentação representa fala real? (00:00:00–00:36:29)
5. Qual frase foi reconhecida no único segmento do passe com VAD, e qual era seu timestamp? O artefato dessa passagem deve ser recuperado para comparação.
6. O campo `duracao_transcricao_s: 788.8` significa tempo acumulado de fala reconhecida, soma de segmentos ou outra medida? Não coincide de forma evidente com a duração da fonte.
7. Por que o último cue vai de `00:36:00` a `00:36:29.98` se o áudio termina em `00:36:16.70`? Qual saída/temporização deve prevalecer?
8. O vídeo contém de fato orientação de EPT/projeto ou o título é insuficiente/incorreto? Nenhum conteúdo técnico foi extraído para confirmar isso.
9. Depois da revisão auditiva, qual configuração de ASR/segmentação deve ser usada para capturar fala sem repetir conteúdo de silêncio/legenda?
10. A fonte revisada deve substituir a saída atual, ou ambos os passes devem permanecer como artefatos de diagnóstico? Registrar decisão, hashes, método e revisão humana.
