# Como baixar um vídeo sob demanda

O repositório usa Git LFS. Evite `git lfs pull` sem filtro: isso pode baixar toda a coleção. Para cada piloto, baixe somente o vídeo requerido.

## Vídeo não dividido

Na cópia local do repositório, execute:

```powershell
git lfs pull --include="Apresentação projeto 19-18.mp4"
```

Substitua o argumento pelo nome idêntico listado no `manifesto.csv`. Confirme que o arquivo local tem tamanho igual à coluna `bytes` e que `git lfs ls-files --size` mostra o tamanho esperado. A visualização no GitHub/API pode retornar o ponteiro LFS, que é pequeno; isso não significa que o objeto LFS esteja ausente. Baixe via Git LFS no clone.

> Limitação conhecida do ambiente Arena (verificado em 2026-10-13): o sandbox não traz o cliente `git-lfs` (`git: 'lfs' is not a git command`) e o egress libera apenas `github.com`, `api.github.com`, `codeload.github.com`, `pypi.org` e `files.pythonhosted.org`; portanto `objects.githubusercontent.com` e `github-cloud.githubusercontent.com`, que entregam os bytes do LFS, ficam inacessíveis e o download falha com `OpenSSL SSL_connect: SSL_ERROR_SYSCALL`. Registro completo, comandos e erro exato em [`materiais/BLOQUEIO_LFS_ARENA.md`](materiais/BLOQUEIO_LFS_ARENA.md). Execute este procedimento em uma máquina com Git LFS funcional (ou peça a liberação desses hosts).

## Vídeo dividido em partes

Os nomes e tamanhos estão em `partes-videos.json`. Baixe somente as partes do vídeo escolhido, por exemplo:

```powershell
git lfs pull --include="AVERBACAO.mp4.part*"
```

O script existente `tools/reconstruir_videos.py` processa todos os vídeos divididos e exige que todas as partes estejam presentes. Para um piloto único, use um procedimento seletivo que valide bytes e SHA-256 das partes daquele registro em `partes-videos.json`, concatene na ordem listada para `<original>.reconstruindo` e só então renomeie para o original. Não execute a reconstrução se algum tamanho/hash falhar. Não faça cópias redundantes do vídeo: arquivos divididos podem ocupar vários GB, e a montagem precisa de espaço temporário semelhante ao tamanho final.

Nunca baixe toda a coleção de uma vez quando o ambiente ou armazenamento tiver limite. Processar um vídeo por lote permite liberar os arquivos temporários entre etapas.
