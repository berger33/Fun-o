# Metadados editoriais — `dESAVERBAÇÃO.mp4`

## Fonte primária e manifesto

- **Nome no manifesto:** `dESAVERBAÇÃO.mp4`.
- **Tamanho declarado do original:** `2531378142` bytes.
- **Divisão:** 2 partes LFS, na ordem `part001`, `part002`.
- **Parte 1:** `dESAVERBAÇÃO.mp4.part001`; esperado `1610612736` bytes; SHA-256/OID `40d90b320472059c25d78678030bae1ec361c7de5ebb48bbe053a70f33052f90`.
- **Parte 2:** `dESAVERBAÇÃO.mp4.part002`; esperado `920765406` bytes; SHA-256/OID `55e2fb9ea7328f9bf79f1094a0857f7460be4ac930191f1886bb43fbeff68263`.
- **Integridade histórica do original:** `7d40df158d1aa66ae718ef4e2a45fd24332d923a44441dfee277d862ec0a9ce2` (informado pelo `transcricao_meta.json` e pelo README da execução upstream; não calculado novamente nesta sessão).
- **Estado dos arquivos locais das partes:** `part001` e `part002` são ponteiros LFS de 135 e 134 bytes, respectivamente. Não são os bytes de vídeo.
- **Tentativa atual de acesso:** `git lfs version` falhou porque o cliente não está instalado. A API batch LFS retornou HTTP 200 com ações para os dois OIDs; as sondagens `Range: bytes=0-0` falharam em `github-cloud.githubusercontent.com` com `SSLZeroReturnError`/EOF. Nenhum byte de parte foi recebido, nenhum arquivo foi reconstruído e nenhum hash de parte foi recalculado nesta sessão.
- **Relato upstream:** `materiais/desaverbacao/LEIA-ME.md` da referência diz que o runner reconstruiu as partes, conferiu tamanho/SHA-256 com `partes-videos.json` e validou o total. Trata-se de registro da execução anterior, não de verificação independente neste lote.

## Origem e integridade dos artefatos ASR

- **Referência:** branch `arena/17453ccc-fun-o`, commit `a2d53d4b25b7b01105621cc9dc2e0ac4edf0acb2`, pasta `materiais/desaverbacao/`.
- **Coleta nesta sessão:** conteúdo lido pela API de conteúdo do GitHub e decodificado localmente; para cada arquivo, o Git blob SHA-1 calculado sobre os bytes conferiu com o `sha` remoto.
- **Execução ASR upstream:** run `38607546249`; auditoria de configuração `38607546082`; auditoria após integração `38614902771` (registradas como concluídas na referência).
- **Ferramenta/modelo:** `faster-whisper` (CTranslate2), `large-v3`.
- **Idioma informado:** `pt`; probabilidade de idioma `1`.
- **VAD:** desativado (`filtro_vad: false`).
- **Segmentos:** 1.274.
- **Duração de áudio informada:** `4420.67 s` (`01:13:40.67`).
- **`duracao_transcricao_s`:** `2678.2`; definição desconhecida.
- **Último cue SRT/VTT:** `01:13:37.080–01:14:07.060`; término 26,39 s depois da duração de áudio informada.
- **Data da análise desta branch:** 2026-10-15.

| Artefato | Bytes | Git blob SHA-1 da referência | SHA-256 local |
|---|---:|---|---|
| `transcricao_bruta.txt` | 46901 | `239a00ff66156d085a402b06a0c9398f52543686` | `fb4e7e82f319f25a9669b1718c426a147b985275c003e6b144347a65dfe1b3d2` |
| `transcricao.srt` | 77386 | `720c19cf37b7151e81f0303b35b7d1e625b89818` | `60ec97b59cd9c0575248f38d423449371189179adcbb0edaa09f54e7d795e0f5` |
| `transcricao.vtt` | 72131 | `88dfc5c114dbe55a4e2bbb0e59f5be4d1696f529` | `4b8b28d8742846949b35b162075f83dcb9bcf8eaf267c2b2b2ad5e0b7d8faf3c` |
| `transcricao_meta.json` | 406 | `6a2337f8becc479db0fe486684a179f99094de15` | `504d71273ef73320ed86ea1fe218a393e507e4a38d57586a72969357e7a0ee11` |

Os quatro artefatos acima foram mantidos sem cortes ou mascaramento, conforme a instrução do responsável em [`../PRIVACIDADE_E_RETENCAO.md`](../PRIVACIDADE_E_RETENCAO.md) §13. `transcricao.md` acrescenta somente cabeçalho editorial antes do TXT ASR.

## Escopo e limitações

- Estado: **em revisão**; a transcrição automática não substitui análise integral da fonte primária nem validação humana.
- O MP4 e suas telas não foram obtidos/revistos visualmente nesta sessão; nenhuma imagem foi incluída.
- Nenhuma chamada a API de produto, consulta SQL, teste de sistema ou mudança de ambiente/dados/configuração foi feita.
- O último cue excede a duração declarada e o campo `duracao_transcricao_s` não está definido; não afirmar cobertura ou sincronização completas.
