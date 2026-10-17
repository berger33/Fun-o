# Metadados — MICHELLE CTC PORTABILIDADE REFIN.mp4

## Fonte e integridade

| Campo | Valor |
|---|---|
| Arquivo | `MICHELLE CTC PORTABILIDADE REFIN.mp4` |
| Tamanho | 473540507 bytes (confere com `manifesto.csv`) |
| SHA-256 | `621565bd87d2c0240cc9c1802ab8509363095a69dd63d3ebe24fb6181a5b2493` (idêntico ao ponteiro LFS) |
| Obtenção | Ponte seletiva no CI (`git lfs pull --include`) publicada em 8 blocos de 64 MB (7×67108864 + 3778459) no ramo temporário `entrega/partes-michelle-ctc-portabilidade-refin` (commit `b75a56b6504dedf0e14d641bda1191c134167269`, disparado pela sessão anterior `arena/792a3d47-fun-o` e **coletado nesta retomada**), baixada por `codeload.github.com`, remontada com `cat parte*.bin` e conferida (tamanho + SHA-256) antes da análise. O ramo e o ramo irmão de transcrição (commit `2ca069da23624d0b394049143e8b67e91541a93b`) foram **apagados** após a coleta — ver retenção em [`../PRIVACIDADE_E_RETENCAO.md`](../PRIVACIDADE_E_RETENCAO.md) §21 |
| Criação do contêiner | `2026-08-20T15:15:20Z` (UTC); a barra de tarefas visível nos quadros indica `20/08/2026 12:15` (horário local) |
| Duração | `00:16:56.62` |
| Vídeo | H.264 (Main), 1186×710, 30 fps, ~3531 kb/s |
| Áudio | AAC (LC), 48 kHz, estéreo, 192 kb/s |
| Áudio útil | fala até `00:16:50.26`; silêncio (limiar `-60 dB`) a partir de `00:16:50.28`, com ruído breve não verbal em ~`00:16:55.7` |

O arquivo de vídeo **não** foi adicionado a esta pasta (é rastreado por Git LFS no repositório). A conferência de hash garante que os materiais abaixo descrevem exatamente o objeto do manifesto.

## Transcrição

| Campo | Valor |
|---|---|
| Ferramenta/modelo | `faster-whisper` 1.2.1 (CTranslate2 4.8.3), `large-v3`, no runner do CI (ver `ambiente.txt`/`execucao.log` da entrega temporária, não versionados) |
| Idioma declarado/detectado | Português (`pt`), probabilidade 1 |
| Segmentos | 388 |
| Primeiro/último segmento | `00:00:00–00:00:00.82` / `00:16:48.56–00:16:50.26` |
| VAD | Não registrado nos metadados preservados — não inferir configuração |
| Procedência | TXT/SRT/VTT da entrega desta retomada são **byte a byte idênticos** aos da execução anterior já versionados; o `transcricao_meta.json` foi atualizado para o da nova entrega (difere apenas em `duracao_transcricao_s`: 951.3 × 958.0) |
| Formatos | `transcricao_bruta.txt`, `transcricao.md`, `transcricao.srt`, `transcricao.vtt`, `transcricao_meta.json` |

## Análise realizada neste lote (fonte primária)

1. **Integridade:** tamanho e SHA-256 conferidos contra `manifesto.csv`, o ponteiro LFS e o `COMO_REMONTAR.md` da ponte (473540507 bytes; `621565bd…`).
2. **Coleta da pendência de infra:** os ramos vivos `entrega/partes-michelle-ctc-portabilidade-refin` e `entrega/transcricao-michelle-ctc-portabilidade-refin` foram baixados por `codeload`, conferidos e **apagados** (`gh api -X DELETE`); os SHAs ficaram registrados como objetos provavelmente retidos ([`../PRIVACIDADE_E_RETENCAO.md`](../PRIVACIDADE_E_RETENCAO.md) §21).
3. **Mídia:** inspeção de contêiner com `ffmpeg 7.0.2` (wheel `imageio-ffmpeg` do PyPI) — ver tabela acima.
4. **Áudio:** `volumedetect` global (média `-51,8 dB`, pico `-31,0 dB`) e `silencedetect` com `noise=-60dB:d=1` (41 regiões). Como a gravação é baixa (pico de apenas `-31,0 dB`), o limiar usado foi `-60 dB`.
5. **Cobertura de fala:** comparação automática entre as regiões audíveis (> `-60 dB`) e os 388 segmentos do SRT — **nenhum trecho audível com mais de 4 s ficou sem segmento**; maior pausa entre segmentos: 3,0 s.
6. **Visual:** amostragem de 1 quadro a cada 5 s em toda a gravação (203 quadros) + 15 quadros dirigidos (1 a cada 3 s) entre `00:02:55–00:03:40`, montados em folhas de contato com Pillow e lidos em resolução nativa, com recortes ampliados (2×) para conferir rótulos e nuvens do fluxograma. A ordem de exibição foi conferida contra o timestamp impresso no nome do quadro.
7. **Capturas:** 4 imagens sanitizadas produzidas de `00:02:25`, `00:03:10`, `00:03:50` e `00:15:45` — recortadas no fluxograma, sem participantes, sem nomes completos, sem barra de tarefas.
8. **Auditoria:** `tools/validar_materiais.py --video michelle-ctc-portabilidade-refin`, auditoria geral e `tools/checar_manifesto.py` (resultados registrados em [`../../STATUS.md`](../../STATUS.md)).

## Limitações conhecidas

- A única imagem exibida é um fluxograma de **outro cliente** (declaração da própria apresentadora); nenhuma tela de sistema é demonstrada, e os rótulos lidos pertencem a esse exemplo.
- A transcrição é automática: há erros de reconhecimento registrados em [`incertezas.md`](incertezas.md) §3 (inclusive leituras prováveis como “MEI” = “do meio”/“e-mail”), mantidos sem correção no texto bruto.
- Não houve escuta humana integral; a validação de cobertura é **técnica** (níveis de áudio × segmentos).
- Regiões do fluxograma nunca ampliadas ou cobertas pela coluna de participantes foram registradas como não lidas, em vez de interpretadas.

## Estado

**Concluído** para os critérios do roteiro: fonte conferida byte a byte, fala coberta com timestamps, tela (o fluxograma) revisada quadro a quadro, capturas sanitizadas, incertezas e o conflito de dependência registrados, índices atualizados. A conclusão **não** valida a regra de sincronização entre portabilidade e refim nem transplantam o desenho de exemplo para o C6 — ambas as questões continuam pendentes de decisão humana (`incertezas.md` §8).
