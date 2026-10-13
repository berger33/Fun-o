from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parent.parent
CHUNK_SIZE = 1536 * 1024 * 1024
IO_SIZE = 8 * 1024 * 1024
SOURCES = ['AVERBACAO.mp4', 'dESAVERBAÇÃO.mp4', 'Gravando 2026-10-07 132428.mp4', 'recalculo.mp4']
records = []
for name in SOURCES:
    src = ROOT / name
    if not src.exists():
        raise SystemExit(f'Fonte ausente: {name}')
    size = src.stat().st_size
    parts = []
    with src.open('rb') as f:
        index = 1
        while True:
            part_name = f'{name}.part{index:03d}'
            part_path = ROOT / part_name
            digest = hashlib.sha256()
            part_size = 0
            with part_path.open('wb') as out:
                while part_size < CHUNK_SIZE:
                    data = f.read(min(IO_SIZE, CHUNK_SIZE - part_size))
                    if not data:
                        break
                    out.write(data)
                    digest.update(data)
                    part_size += len(data)
            if part_size == 0:
                part_path.unlink(missing_ok=True)
                break
            parts.append({'name': part_name, 'bytes': part_size, 'sha256': digest.hexdigest()})
            print(f'{part_name}: {part_size} bytes', flush=True)
            index += 1
    records.append({'original': name, 'bytes': size, 'parts': parts})
(ROOT / 'partes-videos.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Manifesto de partes criado: {len(records)} vídeos', flush=True)
