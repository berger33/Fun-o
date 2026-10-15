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

- **Ação:** a transcrição automática foi coletada do run do GitHub Actions `38491679930`; o vídeo não foi republicado por essa execução como partes binárias. Tamanho e SHA-256 conferidos: `356602844` bytes; `07a7166a9dd98f7355d90cd0777a1e7b11b2b6ac732eed80227bdcb7ad0c9404`. Foram gerados 127 segmentos em português com `faster-whisper` `large-v3`.
- **Coleta:** os quatro arquivos de transcrição foram copiados para `materiais/gravando-2026-07-08-182343/`. O ramo temporário `entrega/transcricao-gravando-2026-07-08-182343` não consta mais nos heads remotos.
- **Objeto provavelmente retido:** commit `114674378a63cee686b77091365b1007ff2a0510`; a API do GitHub ainda o retorna em 2026-10-14. O commit contém texto de transcrição e diagnósticos, não o MP4.
- **Recomendação:** incluir esse SHA na solicitação ao GitHub Support. Apagar o ramo de entrega não remove o commit órfão; não reutilizar pontes para material que não possa permanecer acessível por SHA.

## 7. Registro — transcrição de `MICHELLE CTC PORTABILIDADE REFIN.mp4` (2026-10-14)

- **Ação:** run do GitHub Actions `38504260909` gerou a transcrição automática; tamanho e SHA-256 constam como conferidos na execução anterior (473540507 bytes; `621565bd87d2c0240cc9c1802ab8509363095a69dd63d3ebe24fb6181a5b2493`). Foram gerados 388 segmentos em português com `faster-whisper` `large-v3`.
- **Coleta:** os arquivos de transcrição foram recuperados para `materiais/michelle-ctc-portabilidade-refin/`. O ramo temporário `entrega/transcricao-michelle-ctc-portabilidade-refin` não consta nos heads remotos.
- **Objeto provavelmente retido:** commit `7b319cc4cb3af8e12971c2be2d96109b7a76bc79`; a API do GitHub ainda o retorna em 2026-10-14. O commit corresponde à ponte temporária de transcrição (texto/diagnósticos; sem confirmação de conteúdo além do registro da execução).
- **Recomendação:** incluir esse SHA na solicitação ao GitHub Support; excluir o ramo temporário não remove o objeto do commit órfão.

## 8. Registro — transcrição de `MCB - QISTA.mp4` (2026-10-14)

- **Coleta:** os quatro arquivos automáticos de transcrição e o `LEIA-ME.md` foram copiados da referência de sessão `origin/arena/17453ccc-fun-o` para `materiais/mcb-qista/`. Os metadados/README dessa execução registram `large-v3`, 199 segmentos e conferência prévia da fonte (`543851523` bytes; SHA-256 `5e9d76d88342fd82a697eaf4f65f52a9e50bd22aa2416b63ac40e889c8fa11a0`). O MP4 não foi baixado nem re-hasheado nesta etapa.
- **Objeto provavelmente retido:** commit `d8d18b64d7800e55591fed2617d28ef52a7b7af8`, mensagem “Salva transcricao preliminar do video MCB QISTA”; a API do GitHub ainda o retorna em 2026-10-14. O tree contém os artefatos de transcrição e o ponteiro LFS do vídeo, não os bytes do MP4. A branch temporária `entrega/transcricao-mcb-qista` não foi encontrada nos heads remotos observados.
- **Recomendação:** incluir o SHA na solicitação ao GitHub Support. O objeto pode continuar acessível mesmo sem branch apontando para ele.

## 9. Registro — transcrição de `Primeiro projeto.mp4` (2026-10-14)

- **Coleta:** quatro artefatos ASR e `LEIA-ME.md` foram copiados de `origin/arena/17453ccc-fun-o` para `materiais/primeiro-projeto/`. O registro da execução informa `large-v3`, 274 segmentos, 616715835 bytes e SHA-256 `3f761d2a7a1dadeae053910a2a3940d081bcd1e0afd90a96cb826c46d8bd1ac0`; os bytes não foram baixados/re-hasheados neste lote.
- **Sanitização do derivado local:** a cópia pública substitui identificador de cliente e nome de base/ambiente por marcadores e omite um trecho não técnico fora do escopo entre `00:16:15.94` e `00:17:48.66`. Nenhum valor omitido é repetido neste registro.
- **Objeto possivelmente retido:** commit `b26af329e7c0524a4f5151aa864c6dce4d82e1ba`, mensagem “Restaura transcrições integrais autorizadas”; a API do GitHub confirmou o commit em 2026-10-14. O commit inclui a transcrição integral de origem, além de outros arquivos e ponteiros LFS. A cópia sanitizada deste lote não remove nem altera o objeto upstream.
- **Recomendação:** incluir o SHA no pedido ao GitHub Support se a política exigir a remoção dos derivados integrais acessíveis por SHA; exclusão de refs não garante remoção do objeto.

## 10. Registro — derivado sanitizado de `Gravando 2026-08-24 124650.mp4` (2026-10-14)

- **Coleta:** quatro artefatos ASR e README foram copiados da referência remota para `materiais/gravando-2026-08-24-124650/`; metadados registram `large-v3`, 352 segmentos, 644238242 bytes e SHA-256 `1b9b6afd8564786180ac96df1582f64fc7be773b16a20a1df52e82c2234f256c`. O MP4 não foi baixado/re-hasheado neste lote; o README da execução anterior informa conferência da fonte e ponteiro/manifesto.
- **Sanitização:** identificadores de teste de promotora e valor exemplificativo foram trocados por marcadores; o trecho `00:06:01.19–00:09:31.31` foi omitido por conter material sensível não necessário ao guia. Nenhum valor pessoal, SQL ou comando foi copiado para o material público. A cópia sanitizada mantém marcador de omissão e anota o escopo em metadados/incertezas.
- **Duplicidade:** `Gravando 2026-08-24 161729.mp4` tem o mesmo OID LFS `1b9b6afd…`; um único pacote sanitizado atende ambos.
- **Objeto upstream possivelmente retido:** o commit `b26af329e7c0524a4f5151aa864c6dce4d82e1ba` (registrado também em §9) contém transcrições integrais de origem, inclusive este conteúdo, além de outros arquivos/ponteiros. A sanitização local não remove nem altera o commit upstream.
- **Ação recomendada:** incluir a referência ao vídeo no pedido existente ao GitHub Support se a política exigir remoção de transcrições integrais acessíveis por SHA. Excluir refs não garante remoção do commit órfão; manter derivados públicos sanitizados e `STATUS.md` em revisão.

## 11. Registro — derivado sanitizado de `Gravando 2026-10-06 110907.mp4` (2026-10-15)

- **Coleta:** transcrição ASR e metadados foram copiados da referência `origin/arena/17453ccc-fun-o`. O README/metadata dessa execução registram `faster-whisper large-v3`, 683 segmentos, `770228772` bytes e SHA-256 `66e36717be17ba97597a75eb1cf057a4b34a33f843d528ea90f1c3a42f90deb3`; o ponteiro LFS e o manifesto conferem. O MP4 não foi baixado nem re-hasheado neste lote.
- **Sanitização do derivado local:** a referência nominal a outro sistema/projeto foi substituída por marcador; a fala de formato de data ininteligível foi marcada, sem completar valores; conversa paralela sobre incidente/validação/liberação entre `00:23:04.06–00:23:47.48` foi omitida. Não há URL, credencial, SQL literal, payload ou identificador de operação nos derivados.
- **Objeto upstream:** commit `0bf2514b357ca6dae6e1927ce9d43d3684c12057`, mensagem “Salva transcricao preliminar Gravando 2026-10-06”, contém os artefatos ASR integrais e ponteiro LFS (não os bytes do MP4). A sanitização desta branch não remove nem altera aquele objeto.
- **Ação recomendada:** se a política exigir remoção do ASR integral acessível por commit, incluir o SHA no pedido ao GitHub Support; exclusão de refs não garante remoção de objeto órfão. Manter publicada apenas a cópia sanitizada e o status **em revisão** até análise visual/humana.


## 12. Registro — transcrição de `Gravando 2026-09-23 164626.mp4` (2026-10-15)

- **Coleta:** os quatro artefatos ASR de `origin/arena/17453ccc-fun-o` foram copiados byte a byte; hashes e procedência estão em [`gravando-2026-09-23-164626/metadados.md`](gravando-2026-09-23-164626/metadados.md). A execução de origem registra `large-v3`, 396 segmentos, `1087239062` bytes e SHA-256 `e533f6e54565688b09519b83ccf32b121494ebf33d211245d261ccb769e9d8b8`. O MP4 não foi baixado/re-hasheado nem revisto visualmente neste lote.
- **Preservação:** TXT/SRT/VTT/metadados originais permanecem sem alteração; a representação Markdown reproduz integralmente o TXT. Não houve corte nem mascaramento, conforme a instrução expressa registrada no §13. A revisão humana permanece pendente; o último cue termina em `00:26:14.39`, antes do fim declarado do áudio (`00:33:59.98`).
- **Procedência e retenção upstream:** a referência identifica o commit de entrega temporária `91c25e6484be239dbbf77615a9eb76d4a7924e48`; a cópia integral está também no commit `b26af329e7c0524a4f5151aa864c6dce4d82e1ba` da branch de referência. Esses commits e seus objetos podem permanecer acessíveis por SHA após exclusão de refs. Eles contêm transcrições/diagnósticos e ponteiros LFS, não os bytes do MP4.
- **Ação de retenção:** a autorização registrada pelo responsável prevê copiar os materiais para uso interno e excluir o repositório ao término da fila. Enquanto o repositório permanecer público, a transcrição integral e os commits upstream podem continuar acessíveis; a exclusão de branches temporárias não é remoção garantida de objetos.

## 13. Instrução do responsável — preservação integral (2026-10-14)

O responsável instruiu expressamente a **não ocultar nenhuma informação** e autorizou a continuidade com transcrições integrais, declarando que copiará o conteúdo para uso interno da empresa ao término e depois excluirá o repositório. Em resposta, os arquivos TXT/SRT/VTT/metadados de `Primeiro projeto.mp4`, `Gravando 2026-08-24 124650.mp4` e `Gravando 2026-09-23 164626.mp4` foram restaurados das entregas originais, sem cortes ou mascaramento. O responsável declarou os dados como fictícios/de teste e autorizou preservar nomes dos operadores; fotos/câmeras de pessoas não devem ser publicadas. A revisão humana continua pendente. Essa diretriz permanece valendo para os vídeos seguintes da fila, até que o responsável a altere.

Enquanto o repositório não for excluído, ele permanece público. Apagar um ramo temporário não apaga commits acessíveis por SHA, conforme §1. O responsável planeja copiar os materiais e excluir o repositório após a conclusão da fila.


## 14. Registro — transcrição de `Como fazer EPT.mp4` (2026-10-15)

- **Coleta:** quatro artefatos ASR copiados de `origin/arena/17453ccc-fun-o`; hashes e procedência em [`como-fazer-ept/metadados.md`](como-fazer-ept/metadados.md). O arquivo de referência registra `large-v3`, 854 segmentos, `1229228708` bytes e SHA-256 `52cbfc76a421a37d639f7e9a2887386687f175f04dfda2cf41c65abb577102b6`. Os arquivos TXT/SRT/VTT/metadados foram comparados byte a byte com a referência; o MP4 não foi baixado/re-hasheado nem revisado visualmente.
- **Preservação:** os quatro originais ASR e a representação Markdown integral foram mantidos sem cortes/mascaramento conforme §13. Revisão humana e visual permanece pendente. O último cue termina em `00:35:43.14`; o áudio declarado termina em `00:35:47.18` e existem intervalos sem segmentos reconhecidos.
- **Referências de retenção:** a branch de referência registra commit `11473fc1377bc25cda027cbdd580591da99f6669` (transcrição preliminar integrada) e documenta que o commit de entrega temporária `ef0e24ee90bdd78007c8a6fb426da2534b7fe7fc` continuava acessível por SHA; o ramo `entrega/transcricao-como-fazer-ept` foi apagado. A nota upstream descreve esses objetos como transcrição/diagnósticos, não bytes do MP4. A cópia desta branch não remove esses objetos.
- **Retenção:** enquanto refs/commits continuarem acessíveis, a transcrição integral poderá permanecer acessível no GitHub. O responsável planeja copiar o material para uso interno e excluir o repositório ao concluir a fila, conforme §13.


## 15. Registro — transcrição de `projeto EPT.mp4` (2026-10-15)

- **Fonte:** o manifesto/ponteiro LFS e a referência registram `1246682448` bytes, SHA-256 `57f4232365d3ef9291aa2773793d812dcade581b71c273da0a61a0bec97c0a52`, áudio de `2176.70 s` (`00:36:16.70`). A fonte não foi baixada/re-hasheada nem revisada visualmente neste lote.
- **ASR:** o passe anterior `large-v3` com VAD (`38583447570`) teria produzido um segmento. O segundo passe foi sem VAD (`filtro_vad: false`, 73 segmentos), run `38584641492`; auditoria de integração `38587056159`. Segundo o README upstream, quatro artefatos do passe sem VAD foram copiados byte a byte do commit `d240427c50ed6f964f4918c448b8eac4f86b4baf`; os quatro arquivos conferiram contra a branch de referência. O TXT contém 69 ocorrências de “Legenda Adriana Zanotto”; isso não foi confirmado como fala, legenda visual nem conteúdo da fonte.
- **Preservação:** TXT/SRT/VTT/metadados e representação Markdown integral foram mantidos sem cortes/mascaramento conforme §13. A revisão humana e visual permanece pendente; a baixa qualidade da saída não permite inferir fala ou silêncio.
- **Discrepâncias:** a duração do áudio é `00:36:16.70`, mas o último cue chega a `00:36:29.98`; o campo `duracao_transcricao_s: 788.8` não tem definição registrada.
- **Retenção upstream:** a referência registra que os ramos `entrega/transcricao-projeto-ept` e `entrega/transcricao-projeto-ept-sem-vad` foram apagados; os commits `ad453ffa703c0229a18f75387867eff672c15f75` (passe VAD) e `d240427c50ed6f964f4918c448b8eac4f86b4baf` (passe sem VAD) continuavam acessíveis pela API por SHA e contêm transcrição/diagnósticos, não o MP4. Esta branch não remove esses objetos.
- **Retenção:** enquanto refs/commits continuarem acessíveis, a transcrição integral poderá permanecer no GitHub. O responsável planeja copiar os materiais para uso interno e excluir o repositório ao concluir a fila, conforme §13.


## 16. Registro — transcrição de `ClientSecret EWEN TREINAMENTO.mp4` (2026-10-15)

- **Fonte:** referência/manifesto/ponteiro registram `1681225396` bytes, SHA-256 `edf619d212cf3bc2868cde0e7548987b51024404b5b641469f902990c1d62022` e áudio de `2936.36 s` (`00:48:56.36`). O MP4 não foi baixado, re-hasheado ou revisado visualmente neste lote.
- **ASR/procedência:** run `38587211559`, `faster-whisper large-v3`, idioma `pt`, sem VAD (`filtro_vad: false`), 649 segmentos; auditoria da configuração `38587211603` e após integração `38592319279` concluídas com sucesso, conforme registro upstream. TXT/SRT/VTT/metadados foram comparados byte a byte com a referência. A transcrição integral foi mantida conforme §13.
- **Credenciais:** a transcrição descreve geração/configuração de Client Secret e licença, mas não contém valor literal reconhecível de segredo/token. A varredura do ASR não encontrou URL, e-mail, padrão de CPF/CNPJ nem sequências longas semelhantes a token. O MP4/telas não foram revisados, portanto não se afirma que a fonte visual não exiba segredo. Orientação oral sobre validade longa e perfil Supervisor não é política aprovada.
- **Dados pessoais:** o ASR preservado inclui conversa incidental (idade/trajetória profissional) e uma autodeclaração de saúde, além de nomes reconhecidos automaticamente. Mantido sem cortes/mascaramento pela instrução expressa do responsável, que declarou os dados fictícios/de teste. A declaração não foi verificada independentemente; o repositório segue público enquanto não for excluído.
- **Retenção upstream:** a branch de referência informa que `entrega/transcricao-clientsecret-ewen-treinamento` foi removido; commit `3704f0c134cc54c8ee3b13643bba0f198b4fa41` continuava acessível por SHA pela API do GitHub e contém transcrição/diagnósticos, não os bytes do MP4. Esta branch não remove esse objeto.
- **Limites:** o último cue termina em `00:48:54.82`, aproximadamente `1.54 s` antes do áudio declarado; `duracao_transcricao_s: 1799.9` não tem definição no JSON. Testes, geração de segredo, mudança de perfil/licença e CTC não foram executados nesta análise.


## 17. Registro — transcrição de `explicacao mesa c6.mp4` (2026-10-15)

- **Fonte:** referência/manifesto/ponteiro registram `1982033592` bytes, SHA-256 `44344aaad2c507992b90790b981678729dac4abe7d20f0015ee533da74b54998` e áudio de `3461.57 s` (`00:57:41.57`). O MP4 não foi baixado, re-hasheado ou revisado visualmente neste lote.
- **ASR/procedência:** run `38592430811`, `faster-whisper large-v3`, idioma `pt`, sem VAD, 1.394 segmentos; auditoria de configuração `38592430977` e após integração `38599760998` concluídas conforme o registro upstream. Os quatro artefatos TXT/SRT/VTT/metadados foram comparados byte a byte com a referência e conferiram; hashes em [`explicacao-mesa-c6/metadados.md`](explicacao-mesa-c6/metadados.md).
- **Preservação:** o TXT/SRT/VTT e a representação Markdown integral foram mantidos sem cortes/mascaramento conforme §13. O ASR contém nomes, rótulos de máquina/pasta e menção genérica a login/senha, sem valor literal reconhecível de credencial ou URL. A fonte visual não foi revisada; não afirmar que o vídeo não exiba informação adicional.
- **Conteúdo e risco:** a transcrição contém instruções de atualização de pastas/ambientes que se contradizem, inclusive sobre preservar/apagar `config`, além de bases/servidores diferentes. Não usar como runbook. Nenhum arquivo, banco, permissão ou ambiente foi alterado; não houve query, teste ou captura.
- **Varredura:** TXT/SRT/VTT não acusaram URL, e-mail, padrão de CPF/CNPJ, telefone ou sequência longa semelhante a token. Isso não é revisão visual nem validação independente dos dados declarados fictícios/de teste.
- **Retenção upstream:** o ramo `entrega/transcricao-explicacao-mesa-c6` foi removido; commit `51d643f786add40768b8e5bed49d9af72534d2f6` continuava acessível por SHA pela API do GitHub e contém transcrição/diagnósticos, não os bytes do MP4. Esta branch não remove esse objeto. O repositório permanece público até exclusão conforme §13.
- **Cobertura:** último cue `00:57:29.58`, áudio `00:57:41.57`; o campo `duracao_transcricao_s: 2802.8` não está definido. “Legenda Adriana Zanotto” aparece em quatro cues e requer revisão auditiva/visual.
