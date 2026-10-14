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

## 9. Registro — transcrição de `Primeiro projeto.mp4` (2026-10-14)

- **Ação:** run `38510583430` transcreveu o áudio com `faster-whisper` `large-v3` (274 segmentos); auditoria `38510583443` concluiu com sucesso. Fonte conferida pelo manifesto: `616715835` bytes, SHA-256 `3f761d2a7a1dadeae053910a2a3940d081bcd1e0afd90a96cb826c46d8bd1ac0`.
- **Versão integrada:** após a instrução expressa do responsável (registrada no §13), os quatro arquivos de saída originais foram restaurados de `687bd0dbdd4309881da958330f68b247f45ff22e`; a transcrição integrada agora contém os 274 segmentos originais, sem cortes ou mascaramento.
- **Retenção da entrega temporária:** o ramo `entrega/transcricao-primeiro-projeto` foi apagado, mas o commit `687bd0dbdd4309881da958330f68b247f45ff22e` continua acessível pela API do GitHub por SHA. Ele contém a mesma transcrição integral e diagnósticos; não contém o MP4.

## 10. Registro — transcrição de `Gravando 2026-08-24 124650.mp4` (2026-10-14)

- **Ação:** run `38512446731` transcreveu 352 segmentos com `faster-whisper` `large-v3`; auditoria `38512446609` concluiu com sucesso. Tamanho e SHA-256 conferem com manifesto/ponteiro: `644238242` bytes, `1b9b6afd8564786180ac96df1582f64fc7be773b16a20a1df52e82c2234f256c`. É o mesmo objeto LFS de `Gravando 2026-08-24 161729.mp4`.
- **Versão integrada:** após a instrução expressa do responsável (registrada no §13), os quatro arquivos de saída originais foram restaurados de `7421c127d9bdd81cc1767119e4ac81babf7a741f`; a transcrição integrada agora contém os 352 segmentos originais, sem cortes ou mascaramento. Não há um número de CPF completo nos artefatos gerados.
- **Retenção da entrega temporária:** o ramo `entrega/transcricao-gravando-2026-08-24-124650` foi apagado, mas o commit `7421c127d9bdd81cc1767119e4ac81babf7a741f` continua acessível pela API do GitHub por SHA e contém a mesma transcrição integral e diagnósticos; não contém o MP4. A gravação duplicada fica coberta por referência à fonte única em análise.

## 11. Registro — transcrição de `Gravando 2026-10-06 110907.mp4` (2026-10-14)

- **Ação:** run `38513838946` transcreveu 683 segmentos com `faster-whisper` `large-v3`; auditoria `38513838921` concluiu com sucesso. Tamanho e SHA-256 conferem com manifesto/ponteiro: `770228772` bytes, `66e36717be17ba97597a75eb1cf057a4b34a33f843d528ea90f1c3a42f90deb3`.
- **Varredura:** não foram encontrados padrões comuns de CPF/CNPJ, e-mail, telefone ou credencial no texto coletado. Isso não substitui a revisão de contexto nem a conferência das imagens.
- **Retenção da entrega temporária:** o ramo `entrega/transcricao-gravando-2026-10-06-110907` foi apagado após a coleta. O commit `abe0f542cb2c13581fdac5b318bd709e4cc1ca26` continua acessível pela API do GitHub por SHA; contém a transcrição e diagnósticos, não o MP4.
- **Pendência:** incluir esse SHA na solicitação ao GitHub Support para remoção dos objetos órfãos. A transcrição permanece preliminar e em análise.

## 12. Registro — transcrição de `Gravando 2026-09-23 164626.mp4` (2026-10-14)

- **Ação:** run `38516262063` transcreveu 396 segmentos com `faster-whisper` `large-v3`; auditoria `38516261919` concluiu com sucesso. Tamanho e SHA-256 conferem com manifesto/ponteiro: `1087239062` bytes, `e533f6e54565688b09519b83ccf32b121494ebf33d211245d261ccb769e9d8b8`.
- **Versão integrada:** após a instrução expressa do responsável (registrada no §13), os quatro arquivos de saída originais foram restaurados de `91c25e6484be239dbbf77615a9eb76d4a7924e48`; a transcrição integrada agora contém os 396 segmentos originais, sem cortes ou mascaramento.
- **Retenção da entrega temporária:** o ramo `entrega/transcricao-gravando-2026-09-23-164626` foi apagado, mas o commit `91c25e6484be239dbbf77615a9eb76d4a7924e48` continua acessível pela API do GitHub por SHA; contém a mesma transcrição integral e diagnósticos, não o MP4.

## 13. Instrução do responsável — preservação integral (2026-10-14)

O responsável instruiu expressamente a **não ocultar nenhuma informação** e autorizou a continuidade com transcrições integrais, declarando que copiará o conteúdo para uso interno da empresa ao término e depois excluirá o repositório. Em resposta, os arquivos TXT/SRT/VTT/metadados de `Primeiro projeto.mp4`, `Gravando 2026-08-24 124650.mp4` e `Gravando 2026-09-23 164626.mp4` foram restaurados dos commits originais de entrega temporária, sem cortes ou mascaramento. Os artefatos integrados preservam agora a transcrição automática completa; a revisão humana continua pendente. Essa diretriz permanece valendo para os vídeos seguintes da fila, até que o responsável a altere.

Enquanto o repositório não for excluído, ele permanece público. Apagar um ramo temporário não apaga os commits acessíveis por SHA, conforme §1. O responsável planeja copiar os materiais e excluir o repositório após a conclusão da fila.

## 14. Registro — transcrição de `Como fazer EPT.mp4` (2026-10-14)

- **Ação:** run `38578382172` executou somente o workflow de transcrição via `transcricao/tarefa.json`, com `faster-whisper` `large-v3`, idioma `pt`, gerando 854 segmentos; a auditoria após integração, run `38583354198`, concluiu com sucesso. Tamanho e SHA-256 conferem com manifesto/ponteiro: `1229228708` bytes, `52cbfc76a421a37d639f7e9a2887386687f175f04dfda2cf41c65abb577102b6`. Duração do áudio: 2147,18 s (`00:35:47.18`); último segmento reconhecido em `00:35:41`.
- **Versão integrada:** os quatro artefatos TXT/SRT/VTT/metadados foram copiados sem alteração, byte a byte, da saída do workflow. Os três arquivos de transcrição têm 854 entradas; a saída automática foi preservada integralmente, sem cortes ou mascaramento posterior, conforme §13. A revisão humana continua pendente.
- **Retenção da entrega temporária:** após a coleta, o ramo `entrega/transcricao-como-fazer-ept` foi apagado. O commit `ef0e24ee90bdd78007c8a6fb426da2534b7fe7fc` continua acessível pela API do GitHub por SHA; contém transcrição e diagnósticos, não o MP4.
## 15. Registro — transcrição de `projeto EPT.mp4` (2026-10-14)

- **Fonte:** 1246682448 bytes, SHA-256 `57f4232365d3ef9291aa2773793d812dcade581b71c273da0a61a0bec97c0a52`, conferidos com manifesto/ponteiro LFS. Duração do áudio: 2176,70 s (`00:36:16.70`). Auditoria após integração, run `38587056159`, concluída com sucesso.
- **Primeiro passe:** run `38583447570`, `faster-whisper` `large-v3` com filtro VAD, reconheceu somente 1 segmento em mais de 36 minutos. O resultado não foi integrado como transcrição principal por ser anormalmente esparso.
- **Reprocessamento integral:** a opção `--sem-vad` foi acrescentada ao transcritor e configurada para esta execução. Run `38584641492` processou o áudio sem filtro VAD, registrou `filtro_vad: false` nos metadados e gerou 73 segmentos. TXT/SRT/VTT/metadados foram copiados sem alteração, byte a byte, do commit `d240427c50ed6f964f4918c448b8eac4f86b4baf`; fonte conferida. Saída preservada sem cortes ou mascaramento posterior, conforme §13; a revisão humana permanece pendente.
- **Retenção das entregas temporárias:** os ramos `entrega/transcricao-projeto-ept` e `entrega/transcricao-projeto-ept-sem-vad` foram apagados após a coleta. Os commits `ad453ffa703c0229a18f75387867eff672c15f75` (passe VAD) e `d240427c50ed6f964f4918c448b8eac4f86b4baf` (reprocessamento sem VAD) continuam acessíveis pela API do GitHub por SHA. Contêm transcrição e diagnósticos, não o MP4.

## 16. Registro — transcrição de `ClientSecret EWEN TREINAMENTO.mp4` (2026-10-14)

- **Ação:** run `38587211559` executou o workflow de transcrição a partir de `transcricao/tarefa.json`, com `faster-whisper` `large-v3`, idioma `pt` e filtro VAD desativado (`filtro_vad: false`); gerou 649 segmentos. A auditoria da configuração, run `38587211603`, e a auditoria após integração, run `38592319279`, concluíram com sucesso. Tamanho e SHA-256 conferem com manifesto/ponteiro: `1681225396` bytes, `edf619d212cf3bc2868cde0e7548987b51024404b5b641469f902990c1d62022`. Duração do áudio: 2936,36 s (`00:48:56.36`); último segmento reconhecido em `00:48:53`.
- **Versão integrada:** os quatro artefatos TXT/SRT/VTT/metadados foram copiados sem alteração, byte a byte, da saída do workflow. Cada formato contém 649 segmentos. A saída automática foi preservada integralmente, sem cortes ou mascaramento posterior, conforme §13; a revisão humana continua pendente.
- **Retenção da entrega temporária:** após a coleta, o ramo `entrega/transcricao-clientsecret-ewen-treinamento` foi apagado. O commit `3704f0c134cc54c8ee3b13643bba0f198b4fa41b` continua acessível pela API do GitHub por SHA; contém transcrição e diagnósticos, não o MP4.

## 17. Registro — transcrição de `explicacao mesa c6.mp4` (2026-10-14)

- **Ação:** run `38592430811` executou o workflow a partir de `transcricao/tarefa.json`, com `faster-whisper` `large-v3`, idioma `pt` e filtro VAD desativado (`filtro_vad: false`); gerou 1394 segmentos. Auditoria da configuração, run `38592430977`, e auditoria após integração, run `38599760998`, concluíram com sucesso. Tamanho e SHA-256 conferem com manifesto/ponteiro: `1982033592` bytes, `44344aaad2c507992b90790b981678729dac4abe7d20f0015ee533da74b54998`. Duração do áudio: 3461,57 s (`00:57:41.57`); último segmento reconhecido em `00:57:29`.
- **Versão integrada:** TXT/SRT/VTT/metadados foram copiados sem alteração, byte a byte, da saída do workflow; cada formato contém 1394 segmentos. A saída automática foi preservada integralmente, sem cortes ou mascaramento posterior, conforme §13; a revisão humana continua pendente.
- **Retenção da entrega temporária:** após a coleta, o ramo `entrega/transcricao-explicacao-mesa-c6` foi apagado. O commit `51d643f786add40768b8e5bed49d9af72534d2f6` continua acessível pela API do GitHub por SHA; contém transcrição e diagnósticos, não o MP4.

## 18. Registro — transcrição de `recalculo.mp4` (2026-10-14)

- **Ação:** run `38600117592` executou o workflow com `faster-whisper` `large-v3`, idioma `pt` e filtro VAD desativado (`filtro_vad: false`); gerou 1043 segmentos. A fonte foi reconstruída no runner a partir das 2 partes LFS de `recalculo.mp4`; cada parte teve bytes e SHA-256 conferidos com `partes-videos.json`, e o tamanho total corresponde ao manifesto: `2434086989` bytes. SHA-256 do original reconstruído, registrado pelos metadados: `d8f2ed3de2a8b79512df333327a3d03c5c88c6ab4f2a626156561be75fb27bda`. Auditoria da configuração, run `38600117590`, e auditoria após integração, run `38607455403`, concluíram com sucesso. Duração de áudio informada: 4250,82 s (`01:10:50.82`). O último segmento SRT/VTT foi emitido de `01:10:48.560` a `01:11:18.540`, ultrapassando essa duração informada em 27,72 s; a discrepância foi preservada e requer revisão humana.
- **Versão integrada:** os quatro artefatos TXT/SRT/VTT/metadados foram copiados sem alteração, byte a byte, da saída do workflow. Cada formato de transcrição contém 1043 segmentos. O texto automático foi preservado integralmente, sem cortes ou mascaramento, conforme §13. A revisão humana e a análise visual continuam pendentes.
- **Retenção da entrega temporária:** o ramo `entrega/transcricao-recalculo` foi apagado após a coleta. O commit `fb0bb6a70eb8c5809757cab7f1dfd0147e975927` permanece acessível por SHA e contém a transcrição e diagnósticos, não o MP4.
