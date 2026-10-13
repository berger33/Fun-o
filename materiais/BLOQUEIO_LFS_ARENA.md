# Bloqueio de download Git LFS no ambiente Arena — piloto "Apresentação projeto 19-18.mp4"

- **Data:** 2026-10-13
- **Objetivo da tentativa:** obter **somente** `Apresentação projeto 19-18.mp4` via Git LFS (sem `git lfs pull` geral), confirmar `179956679` bytes e analisar o vídeo integralmente.
- **Resultado:** **bloqueado**. Nenhum byte do vídeo foi baixado neste ambiente. Nenhum material derivado foi produzido, para não inventar conteúdo.
- **Vídeo permanece:** `pendente` (ver [`../STATUS.md`](../STATUS.md)).

## 1. Comando solicitado e erro exato

Comando executado dentro do clone (`/home/user/Fun-o`):

```bash
git lfs pull --include="Apresentação projeto 19-18.mp4"
```

Saída literal (stderr, código de saída 1):

```
git: 'lfs' is not a git command. See 'git --help'.

The most similar command is
	log
```

Ou seja: **o cliente Git LFS não está instalado** na imagem do sandbox Arena.

## 2. Ambiente onde ocorreu

| Item | Valor observado |
|---|---|
| Ambiente | Sandbox Arena sobre E2B (`E2B_SANDBOX=true`), host `e2b.local` |
| Sistema | Debian GNU/Linux 12 (bookworm), x86_64, kernel 6.1.158+ |
| Git | 2.39.5 (sem extensão `lfs`) |
| Cliente `gh` | autenticado como `berger33` (token presente no ambiente; valor não registrado) |
| Python | 3.11.2 (sem `ffmpeg`, `ffprobe` ou `whisper` no PATH) |
| Egress permitido | `github.com`, `api.github.com`, `codeload.github.com`, `pypi.org`, `files.pythonhosted.org` |
| Egress bloqueado (verificado) | `objects.githubusercontent.com`, `github-cloud.githubusercontent.com`, `raw.githubusercontent.com`, `media.githubusercontent.com`, `deb.debian.org`, `huggingface.co`, `openaipublic.azureedge.net` |

## 3. Evidências coletadas

### 3.1 Instalação do cliente não é possível

- `sudo apt-get update` → `W: Failed to fetch http://deb.debian.org/debian/dists/bookworm/InRelease Connection failed [IP: 151.101.194.132 80]` (repositórios Debian inacessíveis; sem `apt install git-lfs`).
- Download do pacote oficial `git-lfs-linux-amd64-v3.8.0.tar.gz` a partir de `github.com/.../releases/download/...`: a URL responde `302` apontando para `objects.githubusercontent.com`, e o download falha com `curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to objects.githubusercontent.com:443`.
- Solução alternativa por PyPI não se aplica: não existe pacote PyPI que forneça o binário `git-lfs`, e mesmo com o cliente instalado o host de conteúdo LFS continuaria inacessível (item 3.3).

### 3.2 O objeto LFS existe e o ponteiro local está correto

Verificações positivas (não bloqueantes):

- Ponteiro local `Apresentação projeto 19-18.mp4` = **134 bytes**, conteúdo:
  ```
  version https://git-lfs.github.com/spec/v1
  oid sha256:ac4b6621f1d0ad5750065d1e36a7988a9bfcd13e55d86aaa45860ee9b8d72bb8
  size 179956679
  ```
- `manifesto.csv` espera `179956679` bytes para esse arquivo — **o ponteiro confere** com o manifesto (o tamanho do *ponteiro* não é o do vídeo).
- `git check-attr filter -- "Apresentação projeto 19-18.mp4"` → `filter: lfs`.
- `git rev-list --objects --all` + `git cat-file --batch-check`: o maior blob do histórico é `10806` bytes (`PLANO_EXTRACAO_ARENA.md`); **não há bytes de vídeo em nenhum commit**. Não existe `.git/lfs/` local (nada em cache).
- Consulta à API LFS do próprio repositório (`POST https://github.com/berger33/Fun-o.git/info/lfs/objects/batch` com o `oid` e `size` acima) → **HTTP 200**, com ação `download` para o objeto. **O objeto existe no armazenamento LFS**; a falha é só de acesso de rede da sandbox.

### 3.3 O host de conteúdo LFS é inacessível (bloqueio de egress)

- A `href` de download retornada pela API aponta para `github-cloud.githubusercontent.com`; um `GET` (mesmo com `Range: bytes=0-200`) falha com `curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to github-cloud.githubusercontent.com:443`.
- Comportamento idêntico em `objects.githubusercontent.com`, `raw.githubusercontent.com` e `media.githubusercontent.com`.
- Diagnóstico: o DNS resolve (ex.: `objects.githubusercontent.com → 185.199.111.133`) e o **TCP na porta 443 conecta**, mas a conexão é derrubada durante o *handshake* TLS (`SSL_connect`). Isso é compatível com filtro de egress por SNI, que libera apenas os hosts da lista do item 2.
- URLs servidas por `github.com` e `api.github.com` funcionam (HTTP 200/302), mas elas só entregam o **ponteiro** de 134 bytes, nunca os bytes do vídeo.

### 3.4 Consequência para a análise

Sem os bytes do vídeo não é possível: extrair áudio, transcrever com timestamps, capturar telas para `capturas/`, medir duração ou verificar qualquer fala. Por isso **não** foram criados `transcricao.md`, `guia_de_estudo.md`, `procedimentos.md`, `perguntas.md`, `glossario.md`, `incertezas.md`, `metadados.md` nem `capturas/` — produzi-los sem a fonte violaria o roteiro ("não invente conteúdo ausente").

## 4. Privacidade e confidencialidade

- Nenhum segredo, dado pessoal, dado de cliente ou documentação interna foi copiado para este documento ou para o repositório.
- A URL assinada de download retornada pela API contém token temporário e **foi deliberadamente omitida**; registra-se apenas o host.
- Nenhuma captura de tela foi produzida (não há imagem disponível).
- O `oid` acima já é público: consta no ponteiro versionado no repositório.

## 4.1 Ferramenta pronta para o momento em que o acesso abrir

`tools/baixar_objeto_lfs.py` (novo, validado neste ambiente) baixa **um único** objeto pela API LFS do repositório, sem `git lfs pull` geral:

```bash
python3 tools/baixar_objeto_lfs.py "Apresentação projeto 19-18.mp4"             # baixa e confere
python3 tools/baixar_objeto_lfs.py --verificar "Apresentação projeto 19-18.mp4" # só confere
```

Comportamento verificado: recusa nome fora do `manifesto.csv`; lê `oid`/tamanho do ponteiro e confere com o manifesto; consulta a API LFS (funciona **sem token** neste repositório público); baixa retomando de `<arquivo>.parcial`; só renomeia após conferir tamanho e SHA-256; em falha de rede reporta o host e o erro, sem baixar nada. Testado localmente com objeto servido por `file://`, com retomada de download parcial e com hash propositalmente errado.

## 4.2 Transcrição automática: pré-requisito pendente

Mesmo com o vídeo em mãos, a transcrição automática continua dependendo de pesos de modelo hospedados fora dos hosts permitidos (`huggingface.co` e `openaipublic.azureedge.net` estão bloqueados). Verificado nos pacotes do PyPI (host permitido): trazem apenas o **código**, não os modelos — `pywhispercpp` (wheel de 4,7 MB, sem `.bin`), `whisper-cpp-python` (sdist de 3,8 MB), `openai-whisper`/`faster-whisper` (sem pesos); `pocketsphinx` embute apenas modelo de inglês. Alternativas: liberar os hosts de pesos **ou** receber do responsável um `SRT/VTT` da gravação para amarrar a transcrição aos timestamps.

## 4.3 Esteira de decodificação validada a seco

Para reduzir o risco na hora do desbloqueio, a esteira foi testada com um vídeo sintético (fora do repositório, em `/tmp`):

- `ffmpeg` estático 7.0.2 obtido do wheel `imageio-ffmpeg` (29,5 MB, host PyPI permitido) — decodifica, mede duração e extrai quadros para PNG;
- captura de quadro em timestamp exato gera imagem legível pronta para `materiais/<slug>/capturas/`.

Pendente apenas o insumo (o MP4) para produzir `transcricao.md`, capturas e demais derivados.

## 5. Caminhos para desbloquear (em ordem de preferência)

1. **Permitir egress no Arena** para `objects.githubusercontent.com` e `github-cloud.githubusercontent.com` (e, para outros vídeos, `media.githubusercontent.com`). Com isso, basta repetir:
   ```bash
   git lfs pull --include="Apresentação projeto 19-18.mp4"
   ```
   e conferir `stat -c %s` = `179956679` e `sha256sum` = `ac4b6621f1d0ad5750065d1e36a7988a9bfcd13e55d86aaa45860ee9b8d72bb8`.
2. **Disponibilizar o arquivo na área de trabalho do Arena** (anexo na conversa). O vídeo fica **fora do Git** (não deve ser commitado: `*.mp4` é rastreado por LFS e o arquivo é grande). Nesse caso a decodificação de quadros/áudio é viável via PyPI (`imageio-ffmpeg` 7.0.2 já validado neste ambiente); a **transcrição automática** ainda depende de pesos de modelo hospedados fora da lista permitida (`huggingface.co` bloqueado), então seria necessário também um `SRT/VTT` fornecido pelo usuário ou liberação desse host.
3. **Dividir o piloto em partes ≤ 90 MB gravadas como blobs comuns (não LFS)** em um branch temporário — por exemplo por workflow do GitHub Actions, que tem acesso ao LFS —, depois buscar as partes no Arena via `codeload.github.com` (host permitido) e validar a concatenação contra o `oid` acima. Contrapartida: coloca ~180 MB de binário no repositório até o branch ser apagado; usar apenas como medida temporária.

## 6. Pendência humana

- Decisão necessária: escolher um dos caminhos do item 5 (ação de plataforma/infraestrutura ou fornecimento do arquivo/transcrição). Sem isso, o piloto "Apresentação projeto 19-18.mp4" **não pode** ser analisado e **não deve** ser marcado como concluído.
- **2026-10-13 — encaminhamento escolhido pelo responsável: liberar o egress na plataforma** (opção 1). Aguardando a liberação dos hosts mínimos `objects.githubusercontent.com` e `github-cloud.githubusercontent.com` para repetir o comando do item 1 e retomar a análise. Nova verificação de conectividade em 2026-10-13 (2ª rodada, após a decisão): `objects.githubusercontent.com`, `github-cloud.githubusercontent.com`, `raw.githubusercontent.com`, `media.githubusercontent.com` e `huggingface.co` continuam inacessíveis (`SSL_ERROR_SYSCALL`), enquanto `github.com`/`api.github.com` respondem 200 e a API LFS segue devolvendo o objeto de 179956679 bytes. Nada foi baixado; piloto continua `pendente`.
