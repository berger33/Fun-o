# Metadados e proveniência — explicacao mesa c6.mp4

## Fonte

- **Nome:** `explicacao mesa c6.mp4`
- **Tamanho declarado:** `1982033592` bytes
- **SHA-256/OID LFS declarado:** `44344aaad2c507992b90790b981678729dac4abe7d20f0015ee533da74b54998` (README/nota upstream registram conferência; o MP4 não foi baixado/re-hasheado neste lote)
- **Duração declarada:** `3461.57 s` (`00:57:41.57`)
- **Revisão audiovisual neste lote:** não realizada.

## ASR original preservado

- **Ferramenta/modelo:** `faster-whisper (CTranslate2)`, `large-v3`
- **Idioma:** declarado/detectado `pt`; probabilidade registrada `1`
- **Filtro VAD:** `false`
- **Segmentos:** `1394`
- **`duracao_transcricao_s`:** `2802.8`; definição não informada
- **Execução:** workflow run `38592430811`; auditoria de configuração run `38592430977`; auditoria após integração run `38599760998`
- **Retenção de origem:** referência informa que o ramo `entrega/transcricao-explicacao-mesa-c6` foi removido; commit `51d643f786add40768b8e5bed49d9af72534d2f6` continuava acessível por SHA pela API do GitHub e contém transcrição/diagnósticos, não o MP4.

## Comparação dos artefatos copiados

Os quatro arquivos foram comparados byte a byte com `origin/arena/17453ccc-fun-o:materiais/explicacao-mesa-c6/`:

| Arquivo | SHA-256 local | Resultado |
|---|---|---|
| `transcricao_bruta.txt` | `a458de4e2218bb9cc127ce96e86bae5190d5c7f7767767015c42294bbcad41fd` | idêntico |
| `transcricao.srt` | `186d1078ba1dc04f60b599432900bb91f665dc99a598179ba46fea9d4104806e` | idêntico |
| `transcricao.vtt` | `f046f19d1a387d7f447122f1dd4adcefd019f27b300c8a004593cd7dd3978b0b` | idêntico |
| `transcricao_meta.json` | `a70c8a3759f3d3351b667c2a1ab558209a63602e5893d871dac8435f35a14c37` | idêntico |

- TXT/SRT/VTT têm 1.394 segmentos/cues segundo os metadados/README de origem.
- Último cue SRT: `00:57:29.220–00:57:29.580`; áudio termina em `00:57:41.57` (cerca de `11.99 s` sem cue ao final).
- “Legenda Adriana Zanotto” ocorre em quatro cues: `00:13:10`, `00:13:40`, `00:14:10`, `00:14:40`.
- `transcricao.md` reproduz integralmente o TXT original após um cabeçalho editorial, sem cortes/mascaramento.

## Limites

A igualdade dos artefatos comprova apenas cópia fiel. Não houve escuta, inspeção de tela, correção de termos, medição local do MP4, teste de API/ambiente ou validação de regra de negócio. Ver [`incertezas.md`](incertezas.md).
