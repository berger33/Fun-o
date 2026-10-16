# Metadados — Gravando 2026-07-08 182343.mp4

## Fonte e integridade

| Campo | Valor |
|---|---|
| Arquivo | `Gravando 2026-07-08 182343.mp4` |
| Tamanho | 356602844 bytes (confere com `manifesto.csv`) |
| SHA-256 | `07a7166a9dd98f7355d90cd0777a1e7b11b2b6ac732eed80227bdcb7ad0c9404` (idêntico ao ponteiro LFS) |
| Obtenção | Ponte seletiva no CI (`git lfs pull --include`) publicada em 6 blocos de 64 MB no ramo `entrega/partes-gravando-2026-07-08-182343`, baixada por `codeload.github.com`, remontada com `cat parte*.bin` e conferida (tamanho + SHA-256) antes da análise |
| Criação do contêiner | `2026-07-08T15:32:33Z` (UTC) |
| Duração | `00:10:23.63` |
| Vídeo | H.264 (Main), 1364×766, 30 fps, ~4380 kb/s |
| Áudio | AAC (LC), 48 kHz, estéreo, 192 kb/s |
| Áudio útil | `00:00:00`–`00:08:28` (silêncio digital de `00:08:28.08` a `00:10:23.63`, leitura `-91,0 dB`) |

O arquivo de vídeo **não** foi adicionado a esta pasta (é rastreado por Git LFS no repositório). A conferência de hash garante que os materiais abaixo descrevem exatamente o objeto do manifesto.

## Transcrição

| Campo | Valor |
|---|---|
| Ferramenta/modelo | `faster-whisper`, `large-v3` (execução anterior, preservada) |
| Idioma declarado/detectado | Português (`pt`), probabilidade 1,0 |
| Segmentos | 127 |
| Primeiro/último segmento | `00:00:01` / `00:08:19.57–00:08:20.29` |
| VAD | Não confirmado pelos metadados preservados — não inferir configuração |
| Formatos | `transcricao_bruta.txt`, `transcricao.md`, `transcricao.srt`, `transcricao.vtt`, `transcricao_meta.json` |

## Análise realizada neste lote (fonte primária)

1. **Integridade:** tamanho e SHA-256 conferidos contra `manifesto.csv`, o ponteiro LFS e o `COMO_REMONTAR.md` da ponte.
2. **Mídia:** inspeção de contêiner com `ffmpeg 7.0.2` (wheel `imageio-ffmpeg` do PyPI).
3. **Áudio:** `silencedetect` em `-50 dB`/1 s (63 regiões) e em `-40 dB`/2 s; `volumedetect` global (`média -45,0 dB`, `máximo -19,7 dB`) e por trecho. Confirmado **silêncio digital** no fim da gravação.
4. **Cobertura de fala:** comparação automática entre os trechos audíveis (> `-50 dB`) e os 127 segmentos do ASR — **nenhum trecho audível acima de 4 s ficou sem cobertura**.
5. **Visual:** amostragem de 1 quadro a cada 5 s em toda a gravação (125 quadros) + 40 quadros dirigidos em pontos de interesse, com leitura em resolução nativa e ampliação de recortes para conferir rótulos. A ordem de exibição foi conferida contra o timestamp impresso no nome do quadro.
6. **Capturas:** 5 imagens sanitizadas produzidas a partir de `00:02:36`, `00:03:12`, `00:06:10`, `00:07:35` — recortadas no documento/tela, sem participantes, sem identificação de usuário/servidor, sem valor de OS.
7. **Auditoria:** `tools/validar_materiais.py --video gravando-2026-07-08-182343` e `tools/checar_manifesto.py` (resultados registrados em `STATUS.md`).

## Limitações conhecidas

- A transcrição é automática e informal: há trechos ambíguos e pelo menos um caso em que o ASR não acompanha o rótulo da tela (`00:07:31`).
- Não houve escuta humana integral; a validação de cobertura é **técnica** (níveis de áudio × segmentos).
- Trechos de tela ilegíveis na amostragem foram registrados como não lidos em [`incertezas.md`](incertezas.md) §5, em vez de interpretados.
- Permissões/perfis necessários para as telas demonstradas não foram demonstrados.

## Estado

**Concluído** para os critérios do roteiro: fonte conferida byte a byte, conteúdo instrutivo coberto com timestamps, telas relevantes capturadas e sanitizadas, incertezas e conflitos registrados, índices atualizados. A conclusão **não** valida a rotina de atualização descrita na fala nem a regra de negócio do incidente — ambas continuam pendentes de confirmação humana (`incertezas.md` §9).
