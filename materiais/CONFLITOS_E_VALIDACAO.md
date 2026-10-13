# Conflitos e validações pendentes

Atualizado em **2026-10-13**.

## Conflitos entre gravações

Nenhum identificado até o momento (nenhuma gravação analisada).

## Pendências de validação

1. **Acesso ao Git LFS no ambiente Arena** — o piloto `Apresentação projeto 19-18.mp4` (179956679 bytes) não pôde ser baixado: cliente `git-lfs` ausente e host de conteúdo do LFS inacessível no sandbox. Decisão humana necessária (liberar egress, fornecer o arquivo ou fornecer transcrição). Ver [`BLOQUEIO_LFS_ARENA.md`](BLOQUEIO_LFS_ARENA.md).
2. **Pesos de transcrição automática** — hospedados em `huggingface.co`, fora da lista de hosts permitidos no Arena; avaliar liberação ou uso de `SRT/VTT` fornecido.
3. **Possíveis duplicidades de fonte** — `Jonas EPT explicação.mp4` × `jonas2309.mp4` (318342582 bytes cada) e `Gravando 2026-08-24 124650.mp4` × `Gravando 2026-08-24 161729.mp4` (644238242 bytes cada): confirmar se são gravações distintas antes da extração, pois o plano proíbe fundir fontes diferentes.
