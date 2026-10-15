# Metadados — Gravando 2026-07-08 182343.mp4

## Fonte e integridade

| Campo | Valor |
|---|---|
| Arquivo | `Gravando 2026-07-08 182343.mp4` |
| Tamanho | 356602844 bytes |
| SHA-256 | `07a7166a9dd98f7355d90cd0777a1e7b11b2b6ac732eed80227bdcb7ad0c9404` |
| Conferência | Tamanho e SHA-256 conferidos contra `manifesto.csv` e a fonte disponibilizada para análise |
| Duração do contêiner/áudio | 623,64 s (`00:10:23.64`) |
| Vídeo | H.264, 1364×766, 30 fps |
| Áudio | AAC, 48 kHz, estéreo |

O arquivo de vídeo não foi adicionado a esta pasta. A confirmação de integridade não equivale à validação de todos os conteúdos falados ou exibidos.

## Transcrição

| Campo | Valor |
|---|---|
| Ferramenta/modelo | `faster-whisper`, `large-v3` |
| Idioma declarado/detectado | Português (`pt`) |
| Segmentos | 127 |
| Primeiro/último segmento | `00:00:01` / `00:08:19.57–00:08:20.29` |
| VAD | Não confirmado pelos metadados preservados; não inferir configuração |
| Formatos | `transcricao_bruta.txt`, `transcricao.md`, `.srt`, `.vtt`, `transcricao_meta.json` |

## Análise realizada neste lote

- Leitura integral do TXT/SRT/VTT disponíveis e organização temática com timestamps.
- Conferência do tamanho e SHA-256 do arquivo-fonte.
- Inspeção técnica do contêiner e amostragem visual pontual em `00:00:35`; não houve revisão quadro a quadro nem escuta humana do áudio completo.
- Detector técnico de silêncio: `ffmpeg silencedetect` com limiar `-42 dB` e duração mínima de 2 s. Indicou intervalo contínuo de aproximadamente `00:08:28.36–00:10:23.63`; não é prova suficiente de ausência de fala baixa.
- Capturas não publicadas porque a tela amostrada mostra interface de reunião/participantes e referências internas de ambiente.
- `tools/validar_materiais.py --video gravando-2026-07-08-182343`: 9 verificações aprovadas, 0 avisos/falhas/achados nos arquivos suportados (92 arquivos na varredura geral). `.srt` e `.vtt` foram verificados separadamente para padrões comuns de CPF/CNPJ, e-mail, telefone e tokens; 0 padrões encontrados. Essas varreduras heurísticas não substituem revisão humana ou contextual.

## Estado

**Em revisão.** A organização do conhecimento foi iniciada, mas ainda é necessária a conferência da transcrição contra a fonte, a resolução das instruções contraditórias e a validação do procedimento por responsável técnico. Não classificar como `concluído` até cumprir o roteiro de qualidade e privacidade.
