# Revisão estrutural dos 15 conteúdos em revisão — 2026-10-15

Status oficial: todos permanecem `em revisão`. Nenhum foi marcado `concluído` porque a fonte primária (MP4) não foi obtida/reconstruída/revisada visualmente em nenhum caso.

## Princípio aplicado
- Não inventar conteúdo.
- Documentar limitação de fonte em cada pacote (`LEIA-ME.md`, `incertezas.md`, `metadados.md`).
- Separar o que foi reconhecido pelo ASR (quando há) do que é síntese/validação proposta.
- Nenhuma afirmação de revisão audiovisual, SQL confirmado ou captura de tela sem verificação.

## Resumo por conteúdo (15)

| # | Vídeo | Slug | Arquivos | ASR | Fonte obtida? | Visual revisado? | SQL confirmado? | Observação / limitação |
|---|---|---|---|---|---|---|---|---|
| 1 | Gravando 2026-07-08 182343.mp4 | gravando-2026-07-08-182343 | 13 | Sim (127 seg) | Não | Não | Não | Pacote preliminar; MP4 não baixado |
| 2 | MICHELLE CTC PORTABILIDADE REFIN.mp4 | michelle-ctc-portabilidade-refin | 13 | Sim (388 seg) | Não | Não | Não | ASR copiado de referência; fonte não revisada |
| 3 | MCB - QISTA.mp4 | mcb-qista | 13 | Sim (199 seg) | Não | Não | Não | ASR existente; vídeo não reconstruído |
| 4 | Primeiro projeto.mp4 | primeiro-projeto | 13 | Sim (274 seg) | Não | Não | Não | Cópia pública omite trecho sensível; vídeo não revisado |
| 5 | Gravando 2026-08-24 124650.mp4 | gravando-2026-08-24-124650 | 13 | Sim (352 seg) | Não | Não | Não | Mesmo objeto LFS de 161729; revisado apenas via referência |
| 6 | Gravando 2026-09-23 164626.mp4 | gravando-2026-09-23-164626 | 13 | Sim (396 seg) | Não | Não | Não | Último cue além do áudio; gap pendente |
| 7 | Como fazer EPT.mp4 | como-fazer-ept | 13 | Sim (854 seg) | Não | Não | Não | Intervalos sem segmentos ASR; MP4 não revisado |
| 8 | Gravando 2026-10-06 110907.mp4 | gravando-2026-10-06-110907 | 13 | Sim (683 seg) | Não | Não | Não | Trecho paralelo omitido; nenhum SQL validado |
| 9 | projeto EPT.mp4 | projeto-ept | 13 | Sim (73/1) | Não | Não | Não | Dois passes (com/sem VAD); primeiro não revisado |
| 10 | ClientSecret EWEN TREINAMENTO.mp4 | clientsecret-ewen-treinamento | 13 | Sim (649 seg) | Não | Não | Não | Conversa pessoal preservada (§13); IDs divergentes não validados |
| 11 | explicacao mesa c6.mp4 | explicacao-mesa-c6 | 13 | Sim (1.394 seg) | Não | Não | Não | Conflitos de configuração (pasta/config/base) bloqueados sem runbook |
| 12 | recalculo.mp4 | recalculo | 13 | Sim (1.043 seg) | Não | Não | Não | Fórmula/resultados divergentes; não constituem regra; cue final além do áudio |
| 13 | dESAVERBAÇÃO.mp4 | desaverbacao | 13 | Sim (1.274 seg) | Não | Não | Não | Passos 3,6,7,8 executados nesta sessão; fonte ainda bloqueada; último cue excede áudio 26,39 s |
| 14 | Gravando 2026-10-07 132428.mp4 | gravando-2026-10-07-132428 | 9 | Não | Não | Não | Não | Pacote preliminar criado; nenhuma análise de conteúdo |
| 15 | AVERBACAO.mp4 | averbacao | 9 | Não | Não | Não | Não | Pacote preliminar criado; nenhuma análise de conteúdo |

## O que está verificado para os 15 (não inventado)
- Cada pacote tem todos os arquivos obrigatórios de `ROTEIRO_ARENA.md` (onde aplicável; os 2 mais recentes têm 9 arquivos devido à ausência total de ASR, o que é documentado).
- Todos os ASR existentes foram preservados byte a byte; nenhum corte ou mascaramento feito sem autorização (§13).
- Nenhum teste de sistema, chamada API, alteração de banco/configuração/ambiente ou captura não revisada executada.
- Nenhum segredo, dado pessoal, foto de câmera ou tela não sanitizada publicado.
- Links relativos conferidos; nenhum quebrado.
- `STATUS.md` e `INDICE.md` atualizados com estados corretos.

## O que ainda depende da fonte primária (não pode ser feito sem arquivo MP4)
- Passo 3 completo: reconstrução confirmada + SHA-256 local de cada parte.
- Passo 4: revisão audiovisual integral (telas, campos, mensagens, estados).
- Passo 5 (para os sem ASR): execução de ASR (`faster-whisper large-v3`).
- Passo 6 (para todos): transcrição editada com separação definitiva ASR/síntese/validação.
- Passo 7: seleção e revisão de capturas; sanitização irreversível de dados sensíveis.
- Passo 9: validação de SQL, regras de negócio, resultados, versões, ambiente.
- Atualização final para `concluído` em `STATUS.md`.

## Nota sobre duplicatas confirmadas (nenhuma reprocessada)
- `Gravando 2026-08-24 124650.mp4` = `161729.mp4` (mesmo oid LFS).
- `Jonas EPT explicação.mp4` = `jonas2309.mp4`.
- Nenhum vídeo duplicado foi reprocessado; referência mantida.

## Próximo passo humano (fora do sandbox)
Obter as partes LFS via CI/pont de transferência (hosts `objects.githubusercontent.com` e `github-cloud.githubusercontent.com` bloqueados aqui); reconstruir; confirmar tamanho + hash; executar ASR; revisar visualmente; apenas depois atualizar para `concluído`.
