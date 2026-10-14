# Privacidade e retenção — constatações desta análise

Registro técnico, **sem conteúdo sensível**, de fatos descobertos durante a extração e que afetam a
política de publicação deste repositório público.

## 1. Ramo apagado **não** remove os objetos do servidor

Para transferir uma gravação a um ambiente sem acesso ao host de conteúdo do Git LFS, foi usada uma
**ponte temporária** (workflow `.github/workflows/transferir-gravacao.yml`): os bytes foram
publicados em um ramo `entrega/*`, baixados e o ramo foi **apagado** logo depois.

**Verificação (2026-10-13):** o commit do ramo apagado **continua acessível pelo seu SHA**, inclusive
**sem autenticação**:

```
$ git fetch --depth=1 origin <sha-do-commit>        # sem token → sucesso
$ curl -s -o /dev/null -w '%{http_code}\n' https://api.github.com/repos/berger33/Fun-o/commits/<sha>
200
```

**Consequência:** publicar bytes em um ramo temporário **não é reversível** por exclusão do ramo —
o GitHub mantém commits órfãos acessíveis por SHA. O mesmo vale para o **armazenamento de Git LFS**:
remover ponteiros não remove os objetos.

**Ações recomendadas:**

1. Solicitar ao GitHub Support, por escrito, a remoção dos objetos órfãos (informar repositório,
   SHA do commit, data e motivo).
2. Para conteúdo que não pode permanecer acessível, avaliar com o responsável a **exclusão do
   repositório** e a recriação a partir do histórico atual, já que a remoção de LFS/objetos órfãos
   pelo usuário não é garantida.
3. Não usar a ponte temporária para material que não possa ser exposto temporariamente.

## 2. Regra de uso da ponte temporária (a partir de agora)

- Somente **uma gravação por vez**, com `git lfs pull --include="<nome exato>"` — nunca a coleção.
- Conferir **tamanho e SHA-256** contra `manifesto.csv` e o ponteiro antes de publicar as partes.
- Apagar o ramo imediatamente após a conferência **e** registrar o SHA como "objeto provavelmente
  retido" no `STATUS.md` enquanto o GitHub Support não confirmar a remoção.
- A ponte **não** deve ser usada para material cuja exposição temporária seja inaceitável — nesses
  casos, o caminho é transportar o arquivo por canal autorizado (fora do GitHub).

## 3. Princípio aplicado nesta análise

Ao encontrar conteúdo restrito (documentação interna e informação de cliente) em uma gravação:

1. **Não publicar** o derivado nem capturas; manter o material em área privada, fora do Git.
2. **Não revelar** o conteúdo na pendência: descrever apenas o **tipo** de risco e o timestamp.
3. Registrar o estado real (`em revisão`) em `STATUS.md` e pedir decisão ao responsável pela
   divulgação — sem marcar o vídeo como `concluído`.

## 4. Registro — lote `Gravando 2026-09-22 111258.mp4` (2026-10-13)

- **Constatação:** ao iniciar o lote, os ramos `entrega/partes-gravando-2026-09-22-111258` e `entrega/transcricao-gravando-2026-09-22-111258` **não existiam mais** no remoto (`git ls-remote` vazio; codeload 404). Os logs de execução do Actions não puderam ser lidos no sandbox, e o SHA do 1º disparo não ficou registrado.
- **Ação:** novo disparo da ponte pela branch do lote (`transferencia/tarefa.json`). Bytes conferidos (297627736 bytes; SHA-256 `c617494d…`) e ramo de partes apagado logo após a coleta.
- **Objetos que permanecem acessíveis por SHA (provavelmente retidos):**
  - partes, 2º disparo: `d55b80a7bf78886556ac78cc5784e787b689cfeb`;
  - transcrição, 2º disparo: `3a1920d32ad9e278cfefd11e7a6063f8f38ba36a`;
  - 1º disparo: SHA não registrado nesta sessão (ramos criados em 2026-10-13 entre 19:25 e 19:44 UTC).
- **Recomendação:** incluir esses SHAs no pedido de remoção ao GitHub Support (§1, item 1) e não reutilizar a ponte para outros vídeos até decisão do responsável sobre exposição.

## 5. Registro — lote `Jonas EPT explicação.mp4` (2026-10-13)

- **Constatação:** o commit de encerramento do lote anterior (branch `arena/e81830e4-fun-o`) disparou a ponte deste vídeo (runs do Actions ~20:24–20:28 UTC de 2026-10-13), publicando os ramos `entrega/partes-jonas-ept-explicacao` e `entrega/transcricao-jonas-ept-explicacao`. Os ramos foram apagados às ~20:33 UTC **antes da coleta** por esta sessão, e os SHAs do 1º disparo não ficaram registrados.
- **Ação:** novo disparo da ponte pela branch deste lote (`arena/3755a69f-fun-o`). Bytes conferidos (318342582 bytes = manifesto; SHA-256 `f99bd7955fbcb8960a2356d727233b00fe4847ba145baf7d96f938e8005a894e` = oid do ponteiro) e transcrição coletada (91 segmentos, `large-v3`). Ambos os ramos do 2º disparo foram apagados imediatamente após a coleta e verificação (`git ls-remote` vazio).
- **Objetos que permanecem acessíveis por SHA (provavelmente retidos):**
  - partes, 2º disparo: `acb6a44844071309f8320dc9e318492ad561cac6`;
  - transcrição, 2º disparo: `842507e4e7e051220553138ce29fa1230a84afd6`;
  - 1º disparo: SHAs não registrados (ramos publicados ~20:25–20:28 UTC e apagados ~20:33 UTC de 2026-10-13).
- **Recomendação:** somar esses SHAs ao pedido de remoção do §4 (GitHub Support) e manter a diretriz de coletar/apagar o mais rápido possível em cada novo disparo.

### 5.1. Aditivo — atividade de sessão paralela (2026-10-13, ~22:50–23:00 UTC)

Após a fusão do PR #4 (lote `Jonas EPT explicação.mp4`), outra branch de sessão (`arena/e3de2b35-fun-o`) re-disparou a ponte do mesmo vídeo e ramos `entrega/*` foram publicados e apagados novamente — inclusive os do próximo vídeo (`Gravando 2026-07-08 182343.mp4`), criados pelo commit de encerramento deste lote. Commits órfãos adicionais, **confirmados como retidos** (acessíveis via API em 2026-10-13):

- `4299f397f1c54d880e7deaef91d88a0defe0e5c9` — `entrega/partes-gravando-2026-07-08-182343` (**bytes de vídeo** do próximo da fila);
- `bb31e7d7235ecbf2eb4146775a3862333ecdf276` — republicação da transcrição de `Jonas EPT explicação.mp4` (texto, mesmo conteúdo do `842507e4…` já registrado).

O ramo de **partes** do jonas re-publicado pela sessão paralela (run 38480441190) também carrega bytes de vídeo; o SHA dele não pôde ser capturado nesta sessão (ramo apagado antes da observação). **Incluir todos no pedido de remoção ao GitHub Support** e redobrar a coordenação para não disparar a ponte do mesmo vídeo em sessões simultâneas.

## 6. Registro — transcrição de `Gravando 2026-07-08 182343.mp4` (2026-10-14)

- **Ação:** run do GitHub Actions `38491679930` executou somente o workflow de transcrição (o MP4 foi lido no runner pelo LFS; não houve nova publicação de partes binárias do vídeo). Tamanho e SHA-256 conferem com o manifesto/ponteiro: `356602844` bytes, `07a7166a9dd98f7355d90cd0777a1e7b11b2b6ac732eed80227bdcb7ad0c9404`. Foram gerados 127 segmentos em português com `faster-whisper` `large-v3`.
- **Coleta:** os quatro arquivos de transcrição foram copiados para `materiais/gravando-2026-07-08-182343/`. O ramo temporário `entrega/transcricao-gravando-2026-07-08-182343` foi apagado após a coleta.
- **Objeto provavelmente retido:** commit `114674378a63cee686b77091365b1007ff2a0510` (a API ainda o retorna após apagar o ramo). Esse commit contém texto da transcrição e arquivos de diagnóstico; não contém o MP4.
- **Pendência:** incluir esse SHA e o SHA não registrado do run `38484199544` no pedido ao GitHub Support. Esse run anterior terminou com sucesso, mas o ramo de entrega foi apagado antes da coleta; a exclusão do ramo não garante a remoção dos commits órfãos.

## 7. Registro — transcrição de `MICHELLE CTC PORTABILIDADE REFIN.mp4` (2026-10-14)

- **Ação:** run do GitHub Actions `38504260909` executou o workflow de transcrição a partir de `transcricao/tarefa.json`; não disparou a ponte de partes. Tamanho e SHA-256 conferem com o manifesto/ponteiro: `473540507` bytes, `621565bd87d2c0240cc9c1802ab8509363095a69dd63d3ebe24fb6181a5b2493`. Foram gerados 388 segmentos em português com `faster-whisper` `large-v3`.
- **Coleta:** os quatro arquivos de transcrição foram copiados para `materiais/michelle-ctc-portabilidade-refin/`. O ramo temporário `entrega/transcricao-michelle-ctc-portabilidade-refin` foi apagado após a coleta.
- **Objeto provavelmente retido:** commit `7b319cc4cb3af8e12971c2be2d96109b7a76bc79`; após apagar o ramo, a API ainda o retorna. Contém texto da transcrição e diagnósticos, não o MP4.
- **Pendência:** incluir esse SHA no pedido ao GitHub Support; apagar o ramo não garante a remoção do commit órfão.

## 8. Registro — transcrição de `MCB - QISTA.mp4` (2026-10-14)

- **Ação:** run do GitHub Actions `38507869989` executou o workflow isolado de transcrição a partir de `transcricao/tarefa.json`; não disparou a ponte de partes. Tamanho e SHA-256 conferem com o manifesto/ponteiro: `543851523` bytes, `5e9d76d88342fd82a697eaf4f65f52a9e50bd22aa2416b63ac40e889c8fa11a0`. Foram gerados 199 segmentos em português com `faster-whisper` `large-v3`.
- **Coleta:** os quatro arquivos de transcrição foram copiados para `materiais/mcb-qista/`. O ramo temporário `entrega/transcricao-mcb-qista` foi apagado após a coleta.
- **Objeto provavelmente retido:** commit `83f223e8d5ce3a2b561b968772bbd73e6021704a`; após apagar o ramo, a API ainda o retorna. Contém texto da transcrição e diagnósticos, não o MP4.
- **Pendência:** incluir esse SHA no pedido ao GitHub Support; apagar o ramo não garante a remoção do commit órfão.
