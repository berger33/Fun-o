# Pacote preliminar — `dESAVERBAÇÃO.mp4`

**Estado: em revisão.** Este pacote foi preparado com artefatos ASR já existentes. Não é um runbook aprovado nem uma validação da regra de negócio. O MP4, o áudio e as telas não foram obtidos nem revistos visualmente nesta sessão.

## Fonte primária e disponibilidade

- **Arquivo:** `dESAVERBAÇÃO.mp4`; manifesto: **2.531.378.142 bytes**; 2 partes LFS.
- **Partes esperadas:** `part001` — 1.610.612.736 bytes, SHA-256 `40d90b320472059c25d78678030bae1ec361c7de5ebb48bbe053a70f33052f90`; `part002` — 920.765.406 bytes, SHA-256 `55e2fb9ea7328f9bf79f1094a0857f7460be4ac930191f1886bb43fbeff68263`.
- O endpoint LFS aceitou os dois OIDs (HTTP 200), mas a tentativa de leitura mínima (`Range: bytes=0-0`) falhou para ambos no host de conteúdo `github-cloud.githubusercontent.com` com `SSLZeroReturnError`/EOF. O cliente `git-lfs` não está instalado. Os arquivos locais de 135 e 134 bytes continuam sendo **ponteiros LFS**, não as partes de vídeo; nada foi baixado nem reconstruído nesta sessão.
- **Histórico, não conferido novamente aqui:** o README da execução anterior declara que o runner reconstruiu as duas partes, conferiu tamanho e SHA-256 de cada uma contra `partes-videos.json` e obteve 2.531.378.142 bytes. O SHA-256 do original informado pelo ASR/execução é `7d40df158d1aa66ae718ef4e2a45fd24332d923a44441dfee277d862ec0a9ce2`. Esses dados não equivalem a uma revalidação local da fonte nesta sessão.

## Procedência do ASR

Os quatro artefatos automáticos foram recuperados da referência `arena/17453ccc-fun-o`, commit `a2d53d4b25b7b01105621cc9dc2e0ac4edf0acb2`. Os IDs Git blob retornados pela referência foram conferidos contra os bytes copiados. A execução de origem informa `faster-whisper large-v3`, idioma `pt`, VAD desativado e 1.274 segmentos; detalhes e hashes em [`metadados.md`](metadados.md). O README de origem registra run `38607546249`, auditoria de configuração `38607546082` e auditoria após integração `38614902771`.

## Conteúdo do pacote

- [`transcricao_bruta.txt`](transcricao_bruta.txt), [`transcricao.srt`](transcricao.srt), [`transcricao.vtt`](transcricao.vtt) e [`transcricao_meta.json`](transcricao_meta.json): ASR integral preservado sem cortes ou mascaramento.
- [`transcricao.md`](transcricao.md): apresentação editorial do TXT ASR, sem reescrever sua saída.
- [`guia_de_estudo.md`](guia_de_estudo.md), [`procedimentos.md`](procedimentos.md), [`perguntas.md`](perguntas.md), [`glossario.md`](glossario.md) e [`incertezas.md`](incertezas.md): síntese e plano de validação limitados ao que o ASR permite sustentar.
- [`metadados.md`](metadados.md): origem, integridade e limitações.
- [`capturas.md`](capturas.md): registro de que nenhuma imagem foi produzida ou revisada nesta sessão.

## Limites de uso

O último cue SRT/VTT vai de `01:13:37.080` a `01:14:07.060`, ultrapassando em 26,39 s a duração de áudio declarada (`01:13:40.67`). A métrica `duracao_transcricao_s: 2678.2` não tem definição registrada. ASR não revisado não confirma fala, tela, configuração, status ou resultado; todos os procedimentos permanecem sujeitos à EF/runbook vigentes e à validação humana. Nenhum SQL, API de produto, teste de sistema, alteração de banco/configuração/ambiente ou captura foi executado/feito nesta sessão.

A transcrição integral segue a diretriz de preservação do responsável registrada em [`../PRIVACIDADE_E_RETENCAO.md`](../PRIVACIDADE_E_RETENCAO.md) §13. Isso não autoriza publicar fotos ou imagens de câmeras de pessoas; nenhuma foi incluída.
