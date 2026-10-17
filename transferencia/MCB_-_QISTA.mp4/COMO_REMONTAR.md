# Como remontar (temporário)

- Arquivo original: `MCB - QISTA.mp4`
- Tamanho: 543851523 bytes (conferido contra manifesto.csv)
- SHA-256 do original: 5e9d76d88342fd82a697eaf4f65f52a9e50bd22aa2416b63ac40e889c8fa11a0
- Partes: 9 blocos de 64 MB (o último menor)

```bash
cat MCB_-_QISTA.mp4/parte*.bin > "MCB - QISTA.mp4"
sha256sum "MCB - QISTA.mp4"   # deve ser 5e9d76d88342fd82a697eaf4f65f52a9e50bd22aa2416b63ac40e889c8fa11a0
```

Apague este ramo (`entrega/partes-mcb-qista`) depois de conferir.
