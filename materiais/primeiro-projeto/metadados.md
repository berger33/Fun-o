# Metadados — Primeiro projeto.mp4

## Fonte e integridade

| Campo | Valor |
|---|---|
| Arquivo | `Primeiro projeto.mp4` |
| Tamanho no manifesto/ponteiro LFS | 616715835 bytes |
| SHA-256 / OID LFS | `3f761d2a7a1dadeae053910a2a3940d081bcd1e0afd90a96cb826c46d8bd1ac0` |
| Conferência neste lote | Ponteiro local e `manifesto.csv` concordam em tamanho/OID; os bytes do MP4 não foram baixados ou re-hasheados nesta etapa |
| Registro anterior | README da execução anterior informa conferência da fonte; transcrição Actions run `38510583430`, auditoria run `38510583443` (conforme registro upstream) |
| Duração do áudio declarada | 1073,66 s (`00:17:53.66`) |

## Transcrição automática de origem

| Campo | Valor |
|---|---|
| Ferramenta/modelo | `faster-whisper` (`CTranslate2`), `large-v3` |
| Idioma | Português (`pt`); detectado `pt`, probabilidade declarada 1 |
| Segmentos de origem | 274 |
| Último segmento original | `00:17:47.42–00:17:48.66` |
| `duracao_transcricao_s` no JSON de origem | 896,4 s; definição não informada e não corresponde ao último timestamp |

## Derivado público desta etapa

- `transcricao.md`, `.srt`, `.vtt` e cópia de texto ASR foram sanitizados: identificador de cliente e nome de base/ambiente foram substituídos; conteúdo não técnico fora do escopo entre `00:16:15.94–00:17:48.66` foi substituído por um marcador. A origem declara 274 segmentos; nesta cópia permanecem 255 segmentos de fala e um marcador de omissão.
- A gravação, a especificação, as telas e chamadas de API não foram conferidas visualmente nem por escuta humana integral nesta etapa.
- Não houve teste, consulta SQL, download de documentos ou alteração de sistema.
- Nenhuma captura foi produzida.
- `python3 tools/validar_materiais.py --video primeiro-projeto` executado em 2026-10-14: 9 verificações ok, sem avisos/falhas/achados automatizados para o lote; a varredura geral examinou 122 arquivos. Auditoria completa (`python3 tools/validar_materiais.py`) na mesma data: 59 verificações ok, 0 avisos, 0 falhas e 0 achados de privacidade. Resultado heurístico, não substitui revisão contextual.

## Estado

**Em revisão.** Os documentos organizam o ASR e as hipóteses de teste, mas o contrato do endpoint, a resolução GED/back-office, os nomes das propriedades e a sequência de ambiente ainda dependem da fonte e da documentação aprovada.
