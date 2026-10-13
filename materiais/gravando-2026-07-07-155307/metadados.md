> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Gabriel, William, Santana). Não são publicadas **imagens de pessoas**
> (avatares/fotos de perfil) nem identificadores de máquina na captura derivada.

# Metadados — Gravando 2026-07-07 155307.mp4

## Arquivo e origem

| Campo | Valor |
|---|---|
| Nome original | `Gravando 2026-07-07 155307.mp4` (idêntico ao `manifesto.csv`) |
| Tamanho | **56195092 bytes** — confirmado por `stat` e conferido contra o manifesto |
| SHA-256 | `e2a73df2bf6a9b12aa3833850509f8ab3720d4eae3f0cc1327ac51b8331c52d6` |
| Objeto LFS | `oid sha256:e2a73df2…`, registrado no ponteiro versionado |
| Formato | MP4 (mp42/mp41isom), vídeo H.264 Main 1364×766, 30 fps, ~4342 kb/s; áudio AAC-LC 48 kHz estéreo 192 kb/s |
| Duração | **00:01:39.14** (99,14 s) |
| Data de criação (metadado do arquivo) | 2026-07-07 18:49:19 UTC = **07/07/2026 ~15:49 (America/Sao_Paulo)** |
| Horário visível no relógio do sistema | 15:49 a 15:50 de 07/07/2026 (**[00:00:00 – 00:01:39]**) |

## Como os bytes foram obtidos

1. No runner do GitHub Actions (`transferir-gravacao.yml`), foi executado exclusivamente
   `git lfs pull --include="Gravando 2026-07-07 155307.mp4"`, verificando tamanho (**56195092 bytes**)
   e SHA-256 (`e2a73df2…`) contra `manifesto.csv` e o ponteiro LFS.
2. O arquivo foi transferido ao sandbox via `codeload.github.com`, remontado e revalidado byte a
   byte; os ramos temporários de entrega e transcrição foram removidos imediatamente após a coleta.

## Processamento

| Etapa | Ferramenta/modelo | Observação |
|---|---|---|
| Inspeção de formato | `ffmpeg` estático (wheel `imageio-ffmpeg`) | Metadados de container e streams extraídos via `ffmpeg -i` |
| Quadros analisados | `ffmpeg` (quadros em 00:00:00, 00:00:01–00:00:45 e 00:01:38) | Verificou a entrada da segunda mensagem em **00:00:07** |
| Transcrição | `faster-whisper` `large-v3`, CPU int8, VAD ligado | 41 segmentos; idioma detectado `pt` (prob. 1,00) |
| Script | `tools/transcrever.py` | Gera `transcricao_bruta.txt`, `.srt`, `.vtt` e `transcricao_meta.json` |
| Análise | Leitura integral da transcrição + inspeção visual completa | Cobertura do início ao fim (00:00:00 – 00:01:39) |

## Cobertura e limitações

- **Cobertura:** integral (00:00:00 – 00:01:39).
- **Limitações:** áudio captura apenas uma das pontas da chamada telefônica (pausa em 00:01:02–00:01:13);
  a tela permanece no chat do Teams durante toda a gravação, sem demonstrar telas do Autorizador.
- **Estado de publicação:** `concluído` em `STATUS.md`, com auditoria do roteiro (`tools/validar_materiais.py`) aprovada sem falhas.
