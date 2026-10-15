# Metadados — MCB - QISTA.mp4

## Fonte e integridade

| Campo | Valor |
|---|---|
| Arquivo | `MCB - QISTA.mp4` |
| Tamanho no manifesto/ponteiro LFS | 543851523 bytes |
| SHA-256 / OID LFS | `5e9d76d88342fd82a697eaf4f65f52a9e50bd22aa2416b63ac40e889c8fa11a0` |
| Conferência neste lote | Tamanho e OID do ponteiro local coincidem com manifesto e `transcricao_meta.json`; os bytes do MP4 não foram baixados/re-hashados neste lote |
| Registro anterior | A transcrição/`LEIA-ME.md` da execução anterior informa conferência de tamanho e SHA-256 da fonte; ver também `materiais/PRIVACIDADE_E_RETENCAO.md` §8 |
| Duração do áudio declarada | 946,97 s (`00:15:46.97`) |
| Último segmento SRT | `00:15:41.94–00:15:45.12` |

## Transcrição

| Campo | Valor |
|---|---|
| Ferramenta/modelo | `faster-whisper` (`CTranslate2`), `large-v3` |
| Idioma | Português (`pt`); detectado `pt`, probabilidade declarada 1 |
| Segmentos | 199 |
| `duracao_transcricao_s` nos metadados JSON | 556,8 s; sem definição explícita; não corresponde ao timestamp do último segmento |
| Arquivos de entrada | `transcricao_bruta.txt`, `transcricao.srt`, `transcricao.vtt`, `transcricao_meta.json` |

## Análise deste lote

- A transcrição automática foi organizada em `transcricao.md` e usada como insumo para guia, plano de teste, glossário e registro de pendências.
- Não houve download do MP4, re-hash dos bytes, escuta humana integral nem inspeção visual de telas/configurações neste lote.
- Nenhum SQL foi reproduzido ou executado; nenhuma alteração de dados ou teste de sistema foi realizado.
- A transcrição não permite confirmar nomes de tabelas, rótulos, códigos, URL, configuração ou comportamento de negócio; ver [`incertezas.md`](incertezas.md).
- `python3 tools/validar_materiais.py --video mcb-qista` e a varredura geral executados em 2026-10-14: 9 verificações ok, 0 avisos/falhas/achados automatizados para o lote; 112 arquivos examinados pela varredura geral. O resultado é heurístico e não substitui revisão contextual.

## Estado

**Em revisão.** O material resume a conversa, mas não substitui a conferência da gravação nem os critérios oficiais de configuração/teste. Não usar como runbook.
