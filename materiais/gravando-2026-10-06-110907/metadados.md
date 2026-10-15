# Metadados — Gravando 2026-10-06 110907.mp4

- **Data desta análise:** 2026-10-15.

## Fonte e integridade

| Campo | Valor |
|---|---|
| Arquivo | `Gravando 2026-10-06 110907.mp4` |
| Tamanho conforme manifesto/ponteiro LFS | 770228772 bytes |
| SHA-256 / OID do ponteiro | `66e36717be17ba97597a75eb1cf057a4b34a33f843d528ea90f1c3a42f90deb3` |
| Conferência neste lote | O ponteiro local/remoto e a linha de `manifesto.csv` concordam em tamanho/OID; os bytes do MP4 não foram baixados nem re-hasheados nesta etapa. |
| Origem dos artefatos ASR | `origin/arena/17453ccc-fun-o`, commit `0bf2514b357ca6dae6e1927ce9d43d3684c12057` (`Salva transcricao preliminar Gravando 2026-10-06`) |
| Execução registrada | GitHub Actions run `38513838946`; auditoria da execução `38513838921` |

## Áudio e ASR de origem

| Campo | Valor |
|---|---|
| Ferramenta/modelo | `faster-whisper` (`CTranslate2`), `large-v3` |
| Idioma | Português (`pt`); detectado `pt`, probabilidade declarada 1 |
| Segmentos ASR de origem | 683 |
| Duração do áudio declarada | 1432,43 s (`00:23:52.43`) |
| Último cue de fala original | `00:23:46.70–00:23:47.48` |
| `duracao_transcricao_s` no JSON de origem | 1442,9 s; excede o áudio declarado em 10,47 s; significado não documentado, não usar como duração da gravação |

## Derivado público deste lote

- `transcricao.md`, `.srt`, `.vtt` e `transcricao_bruta.txt` foram sanitizados; SRT/VTT têm 662 cues: 661 falas e um marcador da conversa não técnica omitida.
- Duas ocorrências de um sistema/projeto de referência foram substituídas; uma fala de exemplo de data foi marcada como ininteligível; conversa paralela sobre incidente e sua validação foi omitida de `00:23:04.06` até `00:23:47.48`.
- A conversa menciona `SELECT` e candidatos de nomes de tabela/campo, mas nenhum SQL literal aparece no ASR público, guia ou índices; nenhuma consulta foi executada.
- MP4/telas não foram baixados ou revisados neste lote; não houve chamada externa, job, reenvio ou teste. Nenhuma captura foi gerada.

## Estado

**Em revisão.** A gravação e o ASR descrevem uma discussão preliminar de especificação; regras de elegibilidade, fonte de dados, contrato, parâmetros e fluxo de reenvio dependem de validação humana/técnica.
