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

1. **Autorização de divulgação — piloto `Apresentação projeto 19-18.mp4`** *(bloqueia a conclusão)*.
   A extração está **completa** (fonte verificada: 179956679 bytes, SHA-256 `ac4b6621…`), mas a
   revisão de privacidade e confidencialidade identificou **documentação interna restrita e
   informação de cliente**, além de **nomes e imagens de pessoas**. Por isso os derivados ficaram em
   área privada, fora do Git, e o vídeo está `em revisão` — **sem revelar o conteúdo nesta
   pendência**. Decisão necessária do responsável pela divulgação: autorizar versão descritiva
   sanitizada ou manter privado. Ver [`apresentacao-projeto-19-18/LEIA-ME.md`](apresentacao-projeto-19-18/LEIA-ME.md).
2. **Retenção de objetos no GitHub** — o ramo temporário da transferência foi apagado, mas o commit
   **continua acessível por SHA** (verificado, inclusive sem autenticação). Avaliar pedido de
   remoção ao GitHub Support. Ver [`PRIVACIDADE_E_RETENCAO.md`](PRIVACIDADE_E_RETENCAO.md).
3. **Acesso ao Git LFS no ambiente Arena** — o download direto segue bloqueado; o contorno por ponte
   temporária funcionou para um vídeo e pode ser reutilizado com os cuidados do item 2. Ver
   [`BLOQUEIO_LFS_ARENA.md`](BLOQUEIO_LFS_ARENA.md).
2. **Pesos de transcrição automática** — hospedados em `huggingface.co`, fora da lista de hosts permitidos no Arena; avaliar liberação ou uso de `SRT/VTT` fornecido.
3. **Possíveis duplicidades de fonte** — `Jonas EPT explicação.mp4` × `jonas2309.mp4` (318342582 bytes cada) e `Gravando 2026-08-24 124650.mp4` × `Gravando 2026-08-24 161729.mp4` (644238242 bytes cada): confirmar se são gravações distintas antes da extração, pois o plano proíbe fundir fontes diferentes.
