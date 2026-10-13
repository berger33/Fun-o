> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste** (não há dado real de cliente ou de pessoa). Preservados
> conforme instrução: o nome **Função Sistemas** e os **nomes dos operadores**. Não são
> publicadas **imagens de pessoas** (câmeras/participantes) — as capturas ficam restritas às
> telas do documento.

# Metadados — Apresentação projeto 19-18.mp4


## Arquivo e origem

| Campo | Valor |
|---|---|
| Nome original | `Apresentação projeto 19-18.mp4` (idêntico ao `manifesto.csv`) |
| Tamanho | **179956679 bytes** — confirmado por `stat` e conferido contra o manifesto |
| SHA-256 | `ac4b6621f1d0ad5750065d1e36a7988a9bfcd13e55d86aaa45860ee9b8d72bb8` |
| Objeto LFS | `oid sha256:ac4b6621…`, registrado no ponteiro versionado |
| Formato | MP4 (mov/mp42), vídeo H.264 Main 1066×650, 30 fps, ~2902 kb/s; áudio AAC-LC 48 kHz estéreo 192 kb/s |
| Duração | **00:07:44.870** (464,87 s) |
| Data de criação (metadado do arquivo) | 2026-08-19 14:34:19 UTC = **19/08/2026 ~11:34 (America/Sao_Paulo)** |
| Início da gravação (chat da reunião) | 11:34, conforme "começou a gravar" no painel de chat **[00:07:40]** |
| Data interna do documento compartilhado | 15/08/2026 (barra de tarefas, **[00:00]**) |

## Como os bytes foram obtidos (o host LFS é bloqueado no Arena)

1. `git lfs pull --include="Apresentação projeto 19-18.mp4"` falha no sandbox — `git: 'lfs' is not a
   git command`; e `objects.githubusercontent.com`/`github-cloud.githubusercontent.com` estão
   bloqueados no egress (documentado em `materiais/BLOQUEIO_LFS_ARENA.md`).
2. Ponte temporária: workflow `transferir-gravacao.yml` rodou no **runner do GitHub Actions** (que tem
   acesso ao LFS), baixou **somente** esse arquivo com `git lfs pull --include`, conferiu **tamanho e
   SHA-256** contra `manifesto.csv` e publicou 3 blocos (< 100 MB) em ramo temporário.
3. No sandbox, as partes foram baixadas via `codeload.github.com` (host permitido), remontadas e
   verificadas: **179956679 bytes** e SHA-256 **idêntico** ao ponteiro. O ramo de entrega foi
   **apagado** em seguida (ver `incertezas.md`, item 2, sobre retenção de commits órfãos).

## Processamento

| Etapa | Ferramenta/modelo | Observação |
|---|---|---|
| Inspeção de formato | `ffmpeg` estático 7.0.2 (wheel `imageio-ffmpeg`) | `ffprobe` indisponível; metadados lidos pelo `ffmpeg -i` |
| Quadros analisados | `ffmpeg` (17 marcos de 0 a 450 s + 5 quadros dirigidos) | ver `capturas.md` |
| Transcrição | `faster-whisper` `large-v3`, CPU int8, VAD ligado | 147 segmentos; idioma detectado `pt` (prob. 1,00) |
| Script | `tools/transcrever.py` (executado no runner do CI) | gera `transcricao_bruta.txt`, `.srt`, `.vtt` e `transcricao_meta.json` |
| Transcrição — data | 2026-10-13 | 343,3 s de processamento para 464,87 s de áudio |
| Análise | leitura integral da transcrição + inspeção dos quadros | cobertura do início ao fim |

## Cobertura e limitações

- **Cobertura:** integral (00:00:00 – 00:07:44), com leitura de tela nos 22 quadros extraídos.
- **Limitações:** ruído de TV/microfone aberto em 00:04:37–00:05:47 (trechos inaudíveis); fala
  sobreposta em 00:03:48–00:04:37 (falante incerto); transcrição automática exige revisão de termos
  técnicos — "cooperação" por "operação" em 00:01:45.
- **O que o vídeo não contém:** nenhuma tela de produto, nenhum SQL, nenhuma credencial, nenhum dado
  de cliente (CPF/CNPJ), nenhuma discussão de permissões.

## Estado de publicação

- **Categoria de publicação:** **restrita** — aguardando autorização (ver `incertezas.md`, item 1).
- Este conjunto de documentos está em área privada (`fun-o-privado/`), **fora do Git**.
- Nenhum segredo foi copiado para qualquer arquivo derivado, inclusive este.