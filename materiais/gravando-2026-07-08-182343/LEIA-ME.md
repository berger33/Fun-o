# Gravando 2026-07-08 182343.mp4 — análise concluída

Esta pasta reúne a transcrição e a organização do conhecimento da gravação, agora analisada a partir da **fonte primária** (bytes baixados e conferidos), com revisão visual quadro a quadro.

- **Fonte:** `Gravando 2026-07-08 182343.mp4` — 356602844 bytes; SHA-256 `07a7166a9dd98f7355d90cd0777a1e7b11b2b6ac732eed80227bdcb7ad0c9404` (idêntico ao ponteiro LFS e ao manifesto). Duração `00:10:23.63`; áudio útil até `00:08:28` (depois disso, silêncio digital).
- **Transcrição:** `faster-whisper` `large-v3`, `pt`, 127 segmentos. Conferência de cobertura: nenhum trecho audível acima de `-50 dB` ficou sem segmento de ASR.
- **O que a gravação ensina:** composição do pacote WebAutorizador/WS (`bin`, `Config`, `Estreia`, `Web References`), o caminho `Serviços → Decisão` e a **importação de modelo de decisão (“esteira”)**, motivada pelo **incidente de tolerância** (regra 0–99 × comportamento 0–100 na faixa de valor solicitado).
- **O que continua bloqueado:** a rotina de exclusão/atualização de arquivos é **contraditória** (`00:00:33` × `00:02:34` × `00:03:09–00:03:24`) e o “erro genérico” de `00:04:29` não tem diagnóstico. Não execute limpeza, troca de `Config` ou importação em ambiente real com base nesta gravação.
- **Privacidade:** 5 capturas publicadas, recortadas no documento/tela (sem participantes, sem identificação de usuário/servidor, sem valor de OS, sem cliente). Detalhes e omissões em [`capturas.md`](capturas.md).

## Arquivos de análise

- [`transcricao.md`](transcricao.md) — fala reconhecida com timestamps + **cenas observadas na tela** (tabela verificada quadro a quadro).
- [`guia_de_estudo.md`](guia_de_estudo.md) — síntese com timestamps, regra de tolerância, navegação e limites.
- [`procedimentos.md`](procedimentos.md) — fluxos observados (reconhecimento do pacote, modelo de decisão, incidente) e o fluxo de atualização marcado como **bloqueado**.
- [`perguntas.md`](perguntas.md) — 18 perguntas com respostas e timestamps.
- [`glossario.md`](glossario.md) — termos e siglas sustentados por fala e/ou tela.
- [`incertezas.md`](incertezas.md) — conflitos, trechos ilegíveis, cobertura de áudio e decisões de privacidade.
- [`metadados.md`](metadados.md) — origem, integridade, processamento, auditorias e limitações.
- [`capturas.md`](capturas.md) + [`capturas/`](capturas/) — 5 imagens sanitizadas com legenda, timestamp e finalidade.
- Artefatos brutos preservados: `transcricao_bruta.txt`, `transcricao.srt`, `transcricao.vtt`, `transcricao_meta.json`.
