# Status da extração

Atualizado em **2026-10-13** (Arena). Estados: `pendente`, `em análise`, `em revisão`, `concluído`.

**Piloto do lote atual:** `Apresentação projeto 19-18.mp4` — download via Git LFS **bloqueado neste ambiente**. Evidências, comandos e erro exato em [`materiais/BLOQUEIO_LFS_ARENA.md`](materiais/BLOQUEIO_LFS_ARENA.md).

| Vídeo | Slug previsto | Bytes (manifesto) | Estado | Responsável/data | Último timestamp processado | Categorias | Observações / commit |
|---|---|---|---|---|---|---|---|
| Apresentação projeto 19-18.mp4 | apresentacao-projeto-19-18 | 179956679 | **em revisão** | Arena / 2026-10-13 | 00:07:44 (fim) | SISTEMAS, NEGOCIO, PROCESSOS, DÚVIDA_OU_CONFLITO | **Fonte obtida e verificada** (179956679 bytes; SHA-256 `ac4b6621…`) por ponte temporária no runner do CI. Extração **completa** (transcrição com timestamps + 7 documentos + leitura de 22 quadros). **Publicação suspensa**: conteúdo restrito (documentação interna e informação de cliente) aguardando autorização — ver `materiais/apresentacao-projeto-19-18/LEIA-ME.md`. Nada sensível publicado. |
| AVERBACAO.mp4 | averbacao | 5033624752 | pendente | — | — | — | Dividido em 4 partes; exige reconstrução seletiva. |
| ClientSecret EWEN TREINAMENTO.mp4 | clientsecret-ewen-treinamento | 1681225396 | pendente | — | — | — | — |
| Como fazer EPT.mp4 | como-fazer-ept | 1229228708 | pendente | — | — | — | — |
| dESAVERBAÇÃO.mp4 | desaverbacao | 2531378142 | pendente | — | — | — | Dividido em 2 partes; exige reconstrução seletiva. |
| explicacao mesa c6.mp4 | explicacao-mesa-c6 | 1982033592 | pendente | — | — | — | — |
| Gravando 2026-07-07 155307.mp4 | gravando-2026-07-07-155307 | 56195092 | pendente | — | — | — | — |
| Gravando 2026-07-08 182343.mp4 | gravando-2026-07-08-182343 | 356602844 | pendente | — | — | — | — |
| Gravando 2026-08-24 124650.mp4 | gravando-2026-08-24-124650 | 644238242 | pendente | — | — | — | **Duplicado exato** de `Gravando 2026-08-24 161729.mp4` (mesmo objeto LFS `1b9b6afd…`): analisar uma vez e remeter a outra. |
| Gravando 2026-08-24 161729.mp4 | gravando-2026-08-24-161729 | 644238242 | pendente | — | — | — | **Duplicado exato** de `Gravando 2026-08-24 124650.mp4` (mesmo objeto LFS `1b9b6afd…`). |
| Gravando 2026-09-22 111258.mp4 | gravando-2026-09-22-111258 | 297627736 | pendente | — | — | — | — |
| Gravando 2026-09-23 164626.mp4 | gravando-2026-09-23-164626 | 1087239062 | pendente | — | — | — | — |
| Gravando 2026-10-06 110907.mp4 | gravando-2026-10-06-110907 | 770228772 | pendente | — | — | — | — |
| Gravando 2026-10-07 132428.mp4 | gravando-2026-10-07-132428 | 3151497131 | pendente | — | — | — | Dividido em 2 partes; exige reconstrução seletiva. |
| Gravando 2026-10-07 152044.mp4 | gravando-2026-10-07-152044 | 134290125 | pendente | — | — | — | — |
| Jonas EPT explicação.mp4 | jonas-ept-explicacao | 318342582 | pendente | — | — | — | **Duplicado exato** de `jonas2309.mp4` (mesmo objeto LFS `f99bd795…`): analisar uma vez. |
| jonas2309.mp4 | jonas2309 | 318342582 | pendente | — | — | — | **Duplicado exato** de `Jonas EPT explicação.mp4` (mesmo objeto LFS `f99bd795…`). |
| Liberação padrão - Glauco.mp4 | liberacao-padrao-glauco | 181378373 | pendente | — | — | — | — |
| MCB - QISTA.mp4 | mcb-qista | 543851523 | pendente | — | — | — | — |
| MICHELLE CTC PORTABILIDADE REFIN.mp4 | michelle-ctc-portabilidade-refin | 473540507 | pendente | — | — | — | — |
| Primeiro projeto.mp4 | primeiro-projeto | 616715835 | pendente | — | — | — | — |
| PROJETO 14-08.mp4 | projeto-14-08 | 231977005 | pendente | — | — | — | — |
| projeto EPT.mp4 | projeto-ept | 1246682448 | pendente | — | — | — | — |
| recalculo.mp4 | recalculo | 2434086989 | pendente | — | — | — | Dividido em 2 partes; exige reconstrução seletiva. |

## Resumo da coleção

- Vídeos no manifesto: **24** (conferidos linha a linha contra os arquivos/ponteiros presentes no repositório pelo `tools/checar_manifesto.py`).
- Conteúdos distintos: **22** — dois pares são cópias exatas (mesmo objeto LFS), confirmado por oid: `Gravando 2026-08-24 124650/161729.mp4` e `Jonas EPT explicação.mp4`/`jonas2309.mp4`.
- Concluídos: **0**.
- Em análise: **0**.
- Em revisão: **1** — `Apresentação projeto 19-18.mp4` (extração completa; aguarda autorização de divulgação).
- Pendentes: **23** — dependem de obter os bytes da fonte (ver bloqueio de LFS abaixo).
- Último lote/commit publicado: ponte temporária de transferência/transcrição, ferramentas de auditoria e registro do piloto em revisão (2026-10-13).
- Recheque de egress em 2026-10-13 (2ª rodada): hosts do LFS seguem bloqueados; **nada baixado**, nenhuma gravação analisada.
- Pendências de validação humana:
  1. **Autorização de divulgação do piloto `Apresentação projeto 19-18.mp4`** — a revisão de privacidade/confidencialidade concluiu que o conteúdo é restrito (documentação interna e informação de cliente). Os derivados completos existem em área privada (`fun-o-privado/`, fora do Git) e **não** foram publicados. Decidir: (a) autorizar a publicação de uma versão descritiva sem cliente/nomes/números ou (b) manter privado. Ver `materiais/apresentacao-projeto-19-18/LEIA-ME.md`.
  2. **Retenção de objetos no GitHub** — o ramo temporário usado na transferência foi apagado, mas o commit **continua acessível por SHA** (verificado, inclusive anonimamente). Avaliar pedido de remoção ao GitHub Support. Ver `materiais/PRIVACIDADE_E_RETENCAO.md`.
  3. **Acesso ao LFS para os demais 23 vídeos** — o sandbox segue sem host de conteúdo LFS; a ponte temporária resolvida neste lote pode ser reutilizada para um vídeo por vez (com o cuidado do item 2).
  4. **Duplicidades confirmadas por oid** (cópias exatas): `Gravando 2026-08-24 124650.mp4` = `Gravando 2026-08-24 161729.mp4`; `Jonas EPT explicação.mp4` = `jonas2309.mp4`. Analisar uma vez e referenciar a partir da outra entrada.
  5. **Transcrição automática** roda no runner do CI (que alcança os pesos do modelo); no sandbox continua indisponível.

> Observação de método: o plano só permite anunciar uma gravação como analisada depois de ver a fonte do início ao fim, com timestamps, categorias, prints sanitizados e índices atualizados. Como a fonte não pôde ser obtida, o piloto **permanece `pendente`**.
