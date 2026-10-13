from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parent.parent
records = json.loads((ROOT / 'partes-videos.json').read_text(encoding='utf-8'))
for rec in records:
    target = ROOT / rec['original']
    tmp = target.with_suffix(target.suffix + '.reconstruindo')
    total = 0
    with tmp.open('wb') as out:
        for part in rec['parts']:
            path = ROOT / part['name']
            digest = hashlib.sha256()
            size = 0
            with path.open('rb') as f:
                while True:
                    data = f.read(8 * 1024 * 1024)
                    if not data:
                        break
                    out.write(data)
                    digest.update(data)
                    size += len(data)
            if size != part['bytes'] or digest.hexdigest() != part['sha256']:
                tmp.unlink(missing_ok=True)
                raise SystemExit(f"Parte inválida: {part['name']}")
            total += size
    if total != rec['bytes']:
        tmp.unlink(missing_ok=True)
        raise SystemExit(f"Tamanho final inválido: {rec['original']}")
    tmp.replace(target)
    print(f"Reconstruído e validado: {rec['original']} ({total} bytes)")
