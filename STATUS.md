# Status da extração

Atualizado em **2026-10-13** (Arena). Estados: `pendente`, `em análise`, `em revisão`, `concluído`.

**Fila de extração:** piloto `Apresentação projeto 19-18.mp4` **concluído**; demais vídeos processados do **menor para o maior** tamanho conforme `manifesto.csv`. Como o sandbox Arena não alcança o host de conteúdo do Git LFS diretamente (ver [`materiais/BLOQUEIO_LFS_ARENA.md`](materiais/BLOQUEIO_LFS_ARENA.md)), cada vídeo é obtido sob demanda por ponte temporária no CI (`git lfs pull --include="<arquivo>"`), validado por tamanho e SHA-256 contra o manifesto/ponteiro e analisado integralmente.

| Vídeo | Slug previsto | Bytes (manifesto) | Estado | Responsável/data | Último timestamp processado | Categorias | Observações / commit |
|---|---|---|---|---|---|---|---|
| Apresentação projeto 19-18.mp4 | apresentacao-projeto-19-18 | 179956679 | **concluído** | Arena / 2026-10-13 | 00:07:44 (fim) | SISTEMAS, NEGOCIO, PROCESSOS, DÚVIDA_OU_CONFLITO | Fonte obtida e verificada (179956679 bytes; SHA-256 `ac4b6621…`). 8 documentos + 3 capturas publicados em [`materiais/apresentacao-projeto-19-18/`](materiais/apresentacao-projeto-19-18/LEIA-ME.md). Auditoria do roteiro: 0 falhas. |
| AVERBACAO.mp4 | averbacao | 5033624752 | pendente | — | — | — | Dividido em 4 partes; exige reconstrução seletiva. |
| ClientSecret EWEN TREINAMENTO.mp4 | clientsecret-ewen-treinamento | 1681225396 | pendente | — | — | — | — |
| Como fazer EPT.mp4 | como-fazer-ept | 1229228708 | pendente | — | — | — | — |
| dESAVERBAÇÃO.mp4 | desaverbacao | 2531378142 | pendente | — | — | — | Dividido em 2 partes; exige reconstrução seletiva. |
| explicacao mesa c6.mp4 | explicacao-mesa-c6 | 1982033592 | pendente | — | — | — | — |
| Gravando 2026-07-07 155307.mp4 | gravando-2026-07-07-155307 | 56195092 | **concluído** | Arena / 2026-10-13 | 00:01:39 (fim) | PROCESSOS, SISTEMAS, INFRA_E_ACESSO, DÚVIDA_OU_CONFLITO | Menor vídeo da fila (56195092 bytes; SHA-256 `e2a73df2…`). 8 documentos + 1 captura sanitizada publicados em [`materiais/gravando-2026-07-07-155307/`](materiais/gravando-2026-07-07-155307/LEIA-ME.md). Auditoria do roteiro: 0 falhas. |
| Gravando 2026-07-08 182343.mp4 | gravando-2026-07-08-182343 | 356602844 | pendente | — | — | — | — |
| Gravando 2026-08-24 124650.mp4 | gravando-2026-08-24-124650 | 644238242 | pendente | — | — | — | **Duplicado exato** de `Gravando 2026-08-24 161729.mp4` (mesmo objeto LFS `1b9b6afd…`): analisar uma vez e remeter a outra. |
| Gravando 2026-08-24 161729.mp4 | gravando-2026-08-24-161729 | 644238242 | pendente | — | — | — | **Duplicado exato** de `Gravando 2026-08-24 124650.mp4` (mesmo objeto LFS `1b9b6afd…`). |
| Gravando 2026-09-22 111258.mp4 | gravando-2026-09-22-111258 | 297627736 | pendente | — | — | — | — |
| Gravando 2026-09-23 164626.mp4 | gravando-2026-09-23-164626 | 1087239062 | pendente | — | — | — | — |
| Gravando 2026-10-06 110907.mp4 | gravando-2026-10-06-110907 | 770228772 | pendente | — | — | — | — |
| Gravando 2026-10-07 132428.mp4 | gravando-2026-10-07-132428 | 3151497131 | pendente | — | — | — | Dividido em 2 partes; exige reconstrução seletiva. |
| Gravando 2026-10-07 152044.mp4 | gravando-2026-10-07-152044 | 134290125 | **concluído** | Arena / 2026-10-13 | 00:04:10 (fim) | SISTEMAS, PROCESSOS, NEGOCIO, SQL, DÚVIDA_OU_CONFLITO | Fonte obtida e verificada (134290125 bytes; SHA-256 `07fc2d87…`). 8 documentos + 5 capturas sanitizadas publicados em [`materiais/gravando-2026-10-07-152044/`](materiais/gravando-2026-10-07-152044/LEIA-ME.md). Auditoria do roteiro: 0 falhas. |
| Jonas EPT explicação.mp4 | jonas-ept-explicacao | 318342582 | pendente | — | — | — | **Duplicado exato** de `jonas2309.mp4` (mesmo objeto LFS `f99bd795…`): analisar uma vez. |
| jonas2309.mp4 | jonas2309 | 318342582 | pendente | — | — | — | **Duplicado exato** de `Jonas EPT explicação.mp4` (mesmo objeto LFS `f99bd795…`). |
| Liberação padrão - Glauco.mp4 | liberacao-padrao-glauco | 181378373 | em análise | Arena / 2026-10-13 | — | — | Próximo menor vídeo da fila (181,4 MB); iniciando transferência/transcrição sob demanda. |
| MCB - QISTA.mp4 | mcb-qista | 543851523 | pendente | — | — | — | — |
| MICHELLE CTC PORTABILIDADE REFIN.mp4 | michelle-ctc-portabilidade-refin | 473540507 | pendente | — | — | — | — |
| Primeiro projeto.mp4 | primeiro-projeto | 616715835 | pendente | — | — | — | — |
| PROJETO 14-08.mp4 | projeto-14-08 | 231977005 | pendente | — | — | — | — |
| projeto EPT.mp4 | projeto-ept | 1246682448 | pendente | — | — | — | — |
| recalculo.mp4 | recalculo | 2434086989 | pendente | — | — | — | Dividido em 2 partes; exige reconstrução seletiva. |

## Resumo da coleção

- Vídeos no manifesto: **24** (conferidos linha a linha contra os arquivos/ponteiros presentes no repositório pelo `tools/checar_manifesto.py`).
- Conteúdos distintos: **22** — dois pares são cópias exatas (mesmo objeto LFS), confirmado por oid: `Gravando 2026-08-24 124650/161729.mp4` e `Jonas EPT explicação.mp4`/`jonas2309.mp4`.
- Concluídos: **3** — `Apresentação projeto 19-18.mp4`, `Gravando 2026-07-07 155307.mp4` e `Gravando 2026-10-07 152044.mp4`.
- Em análise: **1** — `Liberação padrão - Glauco.mp4`.
- Em revisão: **0**.
- Pendentes: **20** — aguardando a vez na fila (ordem: menor → maior).
- Último lote/commit publicado: `Gravando 2026-10-07 152044.mp4` **concluído** e publicado (2026-10-13).
- Ordem da fila adotada: **do menor para o maior** (por `bytes` do manifesto), pulando duplicatas exatas por oid.
- Pendências e diretrizes humanas registradas:
  1. **Autorização de divulgação** — concedida em 2026-10-13 (dados declarados fictícios/de teste; preservar o nome **Função Sistemas** e os nomes dos operadores como Jonas, William, Gabriel, etc.; não publicar fotos/câmeras de pessoas).
  2. **Retenção de objetos no GitHub** — os ramos temporários usados na transferência são apagados imediatamente após a coleta, mas os commits órfãos permanecem acessíveis por SHA até coleta de lixo do GitHub. Ver [`materiais/PRIVACIDADE_E_RETENCAO.md`](materiais/PRIVACIDADE_E_RETENCAO.md).
  3. **Duplicidades confirmadas por oid** (cópias exatas): `Gravando 2026-08-24 124650.mp4` = `Gravando 2026-08-24 161729.mp4`; `Jonas EPT explicação.mp4` = `jonas2309.mp4`. Analisar uma vez e referenciar a partir da outra entrada.
