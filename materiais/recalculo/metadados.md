# Metadados editoriais — `recalculo.mp4`

## Fonte e execução ASR

- **Arquivo no manifesto:** `recalculo.mp4`.
- **Tamanho do original reconstruído (declarado):** `2434086989` bytes.
- **SHA-256 do original / OID LFS (declarado):** `d8f2ed3de2a8b79512df333327a3d03c5c88c6ab4f2a626156561be75fb27bda`.
- **Divisão:** 2 partes LFS; README da execução anterior informa que cada parte foi comparada em bytes e SHA-256 com `partes-videos.json`, e que o total foi reconstruído no runner. A fonte não foi baixada/reconstruída/re-hasheada localmente neste lote.
- **Fonte desta análise:** artefatos em `origin/arena/17453ccc-fun-o:materiais/recalculo/`; README indica execução GitHub Actions run `38600117592`, concluída, e auditorias `38600117590` (configuração) e `38607455403` (pós-integração), também concluídas.
- **Ferramenta/modelo:** `faster-whisper` (CTranslate2), `large-v3`.
- **Idioma declarado/detectado:** `pt`; probabilidade informada `1`.
- **VAD:** desativado (`filtro_vad: false`).
- **Segmentos:** 1.043.
- **Duração de áudio informada:** `4250.82 s` (`01:10:50.82`).
- **Campo `duracao_transcricao_s`:** `2527.5 s`; definição não informada.
- **Último cue:** `01:10:48.560–01:11:18.540`; o fim excede a duração declarada em `27.72 s`. Revisar contra a fonte.
- **Estado:** em revisão; revisão humana/visual pendente.

## Integridade dos artefatos ASR locais

Os arquivos foram comparados byte a byte com a referência acima. SHA-256 local:

| Arquivo | SHA-256 |
|---|---|
| `transcricao_bruta.txt` | `04274a962fdb69baab13d9be2ae4a08bb1d7bee3a566b1e465faf54929a8ac01` |
| `transcricao.srt` | `7fa6912d6f072e029bc2ca58922c283c71774a69df5baa92b5f664100f7a6329` |
| `transcricao.vtt` | `cd1df0a4fbd65f34cc915e51e3a3488675b78e78af63dd69449609d1c14883ff` |
| `transcricao_meta.json` | `f6b48762f49bddf5f2824a8c2c61f36389a24c51bf90f3da86ac88e02b8e451c` |

`transcricao.md` acrescenta cabeçalho editorial ao conteúdo completo do TXT, sem alterar o arquivo ASR original. Os hashes listados são dos quatro artefatos locais, não do MP4.

## Escopo e privacidade

- Transcrição ASR preservada sem cortes ou mascaramento, conforme instrução do responsável registrada em [`../PRIVACIDADE_E_RETENCAO.md`](../PRIVACIDADE_E_RETENCAO.md) §13.
- O conteúdo tem diálogo não técnico/aparente mídia de fundo. A análise trata somente dos tópicos relacionados ao recálculo; não remove o restante do ASR.
- O MP4/telas não foram vistos; nenhuma captura, teste, chamada de API, consulta SQL ou alteração de ambiente/dados foi feita.
- Nenhum endpoint, JSON, fórmula, sistema/tela ou resultado de teste foi verificado contra a EF.
- **Limitação:** a cópia upstream de transcrição não substitui análise da fonte primária e não permite afirmar o que aparece na tela.
