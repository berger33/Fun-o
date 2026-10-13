# Status da extração

Inventário conferido em 2026-10-13. Nenhum vídeo foi analisado ainda: os arquivos disponíveis são apenas ponteiros Git LFS, sem os bytes de mídia. A extração está bloqueada antes do piloto; não há timestamp de conteúdo processado.

| Vídeo | Estado | Responsável/data | Último timestamp processado | Categorias | Observações / commit |
|---|---|---|---|---|---|
| `Apresentação projeto 19-18.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; piloto ainda não iniciado |
| `AVERBACAO.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | 4 partes listadas; não reconstruído nem validado por SHA-256 |
| `ClientSecret EWEN TREINAMENTO.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `Como fazer EPT.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `dESAVERBAÇÃO.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | 2 partes listadas; não reconstruído nem validado por SHA-256 |
| `explicacao mesa c6.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `Gravando 2026-07-07 155307.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `Gravando 2026-07-08 182343.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `Gravando 2026-08-24 124650.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `Gravando 2026-08-24 161729.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `Gravando 2026-09-22 111258.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `Gravando 2026-09-23 164626.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `Gravando 2026-10-06 110907.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `Gravando 2026-10-07 132428.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | 2 partes listadas; não reconstruído nem validado por SHA-256 |
| `Gravando 2026-10-07 152044.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `Jonas EPT explicação.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `jonas2309.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `Liberação padrão - Glauco.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `MCB - QISTA.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `MICHELLE CTC PORTABILIDADE REFIN.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `Primeiro projeto.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `PROJETO 14-08.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `projeto EPT.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | LFS não baixado; conteúdo não inspecionado |
| `recalculo.mp4` | pendente | Arena · 2026-10-13 (inventário) | — (mídia indisponível) | — | 2 partes listadas; não reconstruído nem validado por SHA-256 |

Estados: `pendente`, `em análise`, `em revisão`, `concluído`.

## Resumo da coleção

- Vídeos no manifesto: 24.
- Concluídos: 0.
- Em análise: 0.
- Em revisão: 0.
- Pendentes: 24.
- Último lote/commit publicado: nenhum lote de extração; piloto bloqueado antes de começar.
- Pendências de validação humana: nenhuma sobre conteúdo (ainda não analisado).

## Bloqueio e próximo passo

- Conferência local: 24/24 entradas do manifesto têm ponteiros Git LFS com tamanhos declarados compatíveis; os quatro conjuntos divididos somam os tamanhos registrados em `manifesto.csv`. Essa conferência valida apenas metadados dos ponteiros. Os bytes dos objetos não foram baixados; portanto, hashes dos fragmentos, reconstrução, duração, legibilidade e integridade dos vídeos permanecem sem verificação.
- O cliente `git-lfs` não está instalado. O endpoint de lote LFS do GitHub respondeu, mas forneceu a ação de download num host fora dos destinos de rede permitidos neste ambiente. Não foi possível obter a mídia nem iniciar a análise. Nenhum fragmento foi tratado como vídeo independente.
- Próximo passo para retomada: executar em um ambiente com Git LFS e acesso de rede ao host de download LFS; baixar a fonte piloto `Apresentação projeto 19-18.mp4`, conferir tamanho/hash e decodificação, analisar do início ao fim e só então criar/revisar seus documentos e atualizar este status. Repetir em lotes pequenos, reconstruindo os quatro vídeos divididos com `python tools/reconstruir_videos.py` após baixar todas as partes de cada original.
- Não foram criados documentos de conteúdo nem capturas: sem acesso à mídia, qualquer extração seria inventada. A coleção não está concluída.
