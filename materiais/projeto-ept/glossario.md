# Glossário observado — projeto EPT.mp4

> Termos limitados ao nome do arquivo e aos metadados/artefatos ASR. A frase repetida é transcrição não verificada, não identificação confirmada de pessoa ou legenda vista no vídeo.

| Termo | Sentido neste pacote | Timestamp / cautela |
|---|---|---|
| **ASR** | Reconhecimento automático de fala (`faster-whisper`, `large-v3`); saída ainda não conferida contra a fonte. | 73 segmentos; revisão humana pendente. |
| **VAD** | Detecção de atividade de voz usada no passe anterior; o README de origem relata um segmento somente. | O passe copiado está sem VAD (`filtro_vad: false`). |
| **Segmento** | Unidade registrada pelo transcritor; não implica por si só que haja fala correta. | A saída sem VAD repete a cada ~30 s uma frase igual. |
| **Cue** | Bloco temporizado em SRT/VTT; sua extensão deve ser comparada com o áudio. | O último termina em `00:36:29.98`, depois da duração declarada (`00:36:16.70`). |
| **“Legenda Adriana Zanotto”** | Texto retornado pelo ASR, 69 vezes; significado e origem não confirmados. | `00:00:00`–`00:35:59`; pode ser erro de reconhecimento ou conteúdo da fonte. |
| **EPT** | Sigla no nome do arquivo; não definida com segurança pela saída disponível. | Não inferir processo, sistema ou escopo pelo título. |
