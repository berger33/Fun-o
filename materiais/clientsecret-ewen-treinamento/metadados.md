# Metadados e proveniência — ClientSecret EWEN TREINAMENTO.mp4

## Fonte

- **Nome:** `ClientSecret EWEN TREINAMENTO.mp4`
- **Tamanho declarado:** `1681225396` bytes
- **SHA-256/OID LFS declarado:** `edf619d212cf3bc2868cde0e7548987b51024404b5b641469f902990c1d62022` (README de origem registra conferência com manifesto/ponteiro; o MP4 não foi baixado/re-hasheado neste lote)
- **Duração declarada:** `2936.36 s` (`00:48:56.36`)
- **Revisão audiovisual neste lote:** não realizada.

## ASR original preservado

- **Ferramenta/modelo:** `faster-whisper (CTranslate2)`, `large-v3`
- **Idioma:** declarado/detectado `pt`; probabilidade registrada `1`
- **Filtro VAD:** `false`
- **Segmentos:** `649`
- **`duracao_transcricao_s`:** `1799.9`; definição não informada
- **Execução:** workflow run `38587211559`; auditoria de configuração run `38587211603`; auditoria após integração run `38592319279`
- **Retenção de origem:** README da referência informa que o ramo temporário foi apagado; commit `3704f0c134cc54c8ee3b13643bba0f198b4fa41` continua acessível por SHA segundo a nota upstream e contém transcrição/diagnósticos, não os bytes do MP4.

## Comparação dos artefatos copiados

Os quatro arquivos foram comparados byte a byte com `origin/arena/17453ccc-fun-o:materiais/clientsecret-ewen-treinamento/`:

| Arquivo | SHA-256 local | Resultado |
|---|---|---|
| `transcricao_bruta.txt` | `317232802d6751f6f463ef852989aae2d3217db088ddc756cdf87b8f59a46e22` | idêntico |
| `transcricao.srt` | `ad8f54b40cf7c820b7bc2dc9aac7f75060a452b581521d6db6e24e6fd3bf4e89` | idêntico |
| `transcricao.vtt` | `3da6363212cb5348b7395e13029a732cdc1c876fc59e3366c07253d1987591c0` | idêntico |
| `transcricao_meta.json` | `d84662e9e97b10590f616b582c5a8edf17e425e6f6c063f61dea1e86a5695cb1` | idêntico |

- O SRT/VTT contém 649 cues. O último cue vai de `00:48:53.820` a `00:48:54.820`, cerca de `1.54 s` antes do fim declarado do áudio.
- O TXT/SRT/VTT discutem geração/uso de Client Secret, mas não transcrevem um valor literal reconhecível de segredo/token; isso não comprova o que aparece nas telas, não revisadas.
- O Client ID é reconhecido de modo diferente em `00:15:09` e `00:21:12`; não tratar o número como configuração confirmada.
- `transcricao.md` reproduz integralmente o TXT original após um cabeçalho editorial, sem cortes/mascaramento.

## Limites

A igualdade dos arquivos prova apenas cópia fiel, não acurácia. Não houve escuta, inspeção de quadros/capturas, correção de nomes, teste de API/CTC, validação de versão/licença ou verificação local do MP4.
