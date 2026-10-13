# Dependências de estudo

Os arquivos terminados em `.mp4.partNNN` são partes binárias exatas de quatro vídeos que excedem o limite de tamanho por arquivo do Git LFS. Não são vídeos independentes. Para recuperar os originais sem perda, depois de clonar e baixar o LFS, execute:

```powershell
python tools/reconstruir_videos.py
```

O script junta as partes na ordem, confere o SHA-256 e o tamanho de cada uma, e só então recria o MP4 original. O Arena deve reconstruir esses quatro arquivos antes da análise e seguir o roteiro em `ROTEIRO_ARENA.md`.
