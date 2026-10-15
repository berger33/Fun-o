# Metadados e proveniência — projeto EPT.mp4

## Fonte

- **Nome:** `projeto EPT.mp4`
- **Tamanho declarado:** `1246682448` bytes
- **SHA-256 da fonte / OID LFS declarado:** `57f4232365d3ef9291aa2773793d812dcade581b71c273da0a61a0bec97c0a52` (a nota de origem registra conferência com manifesto e ponteiro; o MP4 não foi baixado/re-hasheado neste lote)
- **Duração declarada:** `2176.70 s` (`00:36:16.70`)
- **Revisão audiovisual neste lote:** não realizada.

## ASR original preservado

- **Ferramenta/modelo:** `faster-whisper (CTranslate2)`, `large-v3`
- **Idioma:** declarado/detectado `pt`; probabilidade registrada `1`
- **Filtro VAD:** `false`
- **Segmentos:** `73`
- **`duracao_transcricao_s`:** `788.8`; definição não informada
- **Execução:** workflow run `38584641492`; auditoria após integração run `38587056159`; auditoria/configuração run `38584641428`
- **Artefato da primeira execução:** o README da referência registra `large-v3` com VAD, somente 1 segmento; run `38583447570`. Esse resultado não acompanha esta pasta.
- **Commit de origem do passe sem VAD:** `d240427c50ed6f964f4918c448b8eac4f86b4baf`; os ramos temporários das execuções foram removidos segundo a nota de retenção upstream.

## Comparação dos arquivos copiados

TXT/SRT/VTT/metadados conferidos byte a byte contra `origin/arena/17453ccc-fun-o:materiais/projeto-ept/`:

| Arquivo | SHA-256 local | Resultado |
|---|---|---|
| `transcricao_bruta.txt` | `a7e190e27b462541af96069e7fc1ac12ba5830e956939550206329a1d892e340` | idêntico |
| `transcricao.srt` | `e693599db583e56767beb3e1ffc2495ffc43434c81a4c78831cf40bd22815ac` | idêntico |
| `transcricao.vtt` | `70c0b43562112d647c3b1d2e1b36daf30d8a04f65286ab9a3437433bd27384cc` | idêntico |
| `transcricao_meta.json` | `2fb200056b26efbc9131dc5be0ec82dff93d6629cac0d5c9cedd0fb44cfd16ba` | idêntico |

- O TXT contém `73` segmentos; `69` repetem “Legenda Adriana Zanotto”.
- O último cue SRT/VTT vai de `00:36:00.000` a `00:36:29.980`; excede a duração declarada do áudio em `13.28 s`.
- O campo `duracao_transcricao_s` (`788.8`) não está definido e não deve ser interpretado como duração de fala confirmada.
- `transcricao.md` preserva integralmente o TXT ASR original após um cabeçalho editorial; a atribuição do conteúdo à fala permanece sem validação.

## Limites

A equivalência dos quatro artefatos ASR com a branch de referência comprova apenas cópia fiel, não acurácia. Não houve escuta, inspeção de quadros/capturas, correção de nomes, medição local do MP4 nem validação do assunto.
