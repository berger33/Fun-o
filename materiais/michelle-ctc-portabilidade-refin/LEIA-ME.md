# MICHELLE CTC PORTABILIDADE REFIN.mp4 — análise concluída

Esta pasta reúne a transcrição e a organização do conhecimento da gravação, agora analisada a partir da **fonte primária** (bytes baixados e conferidos), com revisão visual quadro a quadro do fluxograma compartilhado.

- **Fonte:** `MICHELLE CTC PORTABILIDADE REFIN.mp4` — 473540507 bytes; SHA-256 `621565bd87d2c0240cc9c1802ab8509363095a69dd63d3ebe24fb6181a5b2493` (idêntico ao ponteiro LFS e ao manifesto). Duração `00:16:56.62`; fala até `00:16:50.26`.
- **Transcrição:** `faster-whisper` `large-v3`, `pt`, 388 segmentos. Conferência de cobertura: nenhum trecho audível (limiar `-60 dB`) com mais de 4 s ficou sem segmento de ASR; TXT/SRT/VTT desta coleta são byte a byte idênticos aos da execução anterior.
- **O que a gravação ensina:** o mecanismo de coordenação entre portabilidade e refim desenhado no fluxograma — o losango `Tem Refin Vinculado?`, o acionamento `CTC – Aciona Esteira de Refinanciamento (CTCACIPROPREF)` (regra da “última proposta” + parâmetro `G_AVERERR`) e a espera `CTC – Aguarda Analise do Refin de Portabilidade (CTCAGANREFIN)` — e o desenho verbal de um teste (duas propostas, duas esteiras, parada na análise de crédito).
- **Cautela central:** o fluxograma exibido é, por declaração da autora, desenho feito para **outro cliente** — **não** é a esteira do C6 (`00:00:05–00:00:23`). A regra de dependência entre as propostas **não foi decidida** na reunião, a etapa “unificada” só existe na fala e o teste foi apenas delegado, não executado. Não replique configuração nem “pule” o CTC fora de sandbox aprovado com base nesta gravação.
- **Privacidade:** 4 capturas publicadas, recortadas no fluxograma (sem participantes, sem nomes completos, sem barra de tarefas, sem identificação de cliente). Detalhes e omissões em [`capturas.md`](capturas.md).

## Arquivos de análise

- [`transcricao.md`](transcricao.md) — fala reconhecida com timestamps + **cenas observadas na tela** (tabela verificada quadro a quadro).
- [`guia_de_estudo.md`](guia_de_estudo.md) — síntese com timestamps: as duas faixas do desenho, as nuvens transcritas literalmente, o problema do cliente e o teste combinado.
- [`procedimentos.md`](procedimentos.md) — mecanismo do desenho (observação) e o teste proposto marcado como **não executado**, com bloqueios.
- [`perguntas.md`](perguntas.md) — 18 perguntas com respostas e timestamps.
- [`glossario.md`](glossario.md) — termos e siglas sustentados por fala e/ou tela, com a fonte indicada.
- [`incertezas.md`](incertezas.md) — conflitos, termos só falados, cobertura de áudio e decisões de privacidade.
- [`metadados.md`](metadados.md) — origem, integridade, coleta dos ramos temporários, processamento, auditorias e limitações.
- [`capturas.md`](capturas.md) + [`capturas/`](capturas/) — 4 imagens sanitizadas com legenda, timestamp e finalidade.
- Artefatos brutos preservados: `transcricao_bruta.txt`, `transcricao.srt`, `transcricao.vtt`, `transcricao_meta.json`.
