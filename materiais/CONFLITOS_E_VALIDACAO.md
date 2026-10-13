# Conflitos e validações pendentes

Atualizado em **2026-10-13**.

## Conflitos entre gravações

Nenhum conflito **de conteúdo** identificado até o momento (nenhuma gravação analisada). Há, porém, duplicidade de **arquivo**:

### Duplicidades confirmadas por objeto LFS (2026-10-13)

| Arquivos | Objeto LFS (oid, prefixo) | Evidência | Ação proposta |
|---|---|---|---|
| `Gravando 2026-08-24 124650.mp4` = `Gravando 2026-08-24 161729.mp4` | `1b9b6afd8564…` | Mesmo `oid` nos dois ponteiros versionados (`tools/checar_manifesto.py`) | Analisar uma única vez e apontar a segunda entrada para o mesmo material; o plano proíbe fundir gravações **diferentes**, não proíbe tratar cópias idênticas como uma. |
| `Jonas EPT explicação.mp4` = `jonas2309.mp4` | `f99bd7955fbc…` | Mesmo `oid` nos dois ponteiros versionados | Idem. |

Consequência para a contagem: 24 arquivos no manifesto correspondem a **22 conteúdos distintos**. Confirmar com o responsável se as duas cópias devem continuar listadas — nenhum valor sensível está envolvido nesta conclusão (apenas hashes já públicos nos ponteiros).

## Pendências de validação

1. **Acesso ao Git LFS no ambiente Arena** — o piloto `Apresentação projeto 19-18.mp4` (179956679 bytes) não pôde ser baixado: cliente `git-lfs` ausente e host de conteúdo do LFS inacessível no sandbox. Decisão humana necessária (liberar egress, fornecer o arquivo ou fornecer transcrição). Ver [`BLOQUEIO_LFS_ARENA.md`](BLOQUEIO_LFS_ARENA.md).
2. **Pesos de transcrição automática** — hospedados em `huggingface.co`, fora da lista de hosts permitidos no Arena; avaliar liberação ou uso de `SRT/VTT` fornecido.
3. **Possíveis duplicidades de fonte** — `Jonas EPT explicação.mp4` × `jonas2309.mp4` (318342582 bytes cada) e `Gravando 2026-08-24 124650.mp4` × `Gravando 2026-08-24 161729.mp4` (644238242 bytes cada): confirmar se são gravações distintas antes da extração, pois o plano proíbe fundir fontes diferentes.
