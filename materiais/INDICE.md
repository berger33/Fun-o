# Índice da biblioteca de materiais

Atualizado em **2026-10-13**. Conecta as gravações extraídas aos respectivos guias, procedimentos, glossários, capturas e índices temáticos.

## Situação

| Item | Estado |
|---|---|
| Vídeos no manifesto | 24 (22 conteúdos distintos) |
| Gravações concluídas e publicadas | **2** (`Apresentação projeto 19-18.mp4`, `Gravando 2026-07-07 155307.mp4`) |
| Em análise no lote atual | **1** (`Gravando 2026-10-07 152044.mp4`) |
| Método de obtenção no Arena | Ponte seletiva por vídeo via CI (`git lfs pull --include`) + validação de bytes e SHA-256 — ver [`BLOQUEIO_LFS_ARENA.md`](BLOQUEIO_LFS_ARENA.md) e [`PRIVACIDADE_E_RETENCAO.md`](PRIVACIDADE_E_RETENCAO.md) |

## Por categoria

- **`SISTEMAS`** — ver [`SISTEMAS/INDICE_SISTEMAS.md`](SISTEMAS/INDICE_SISTEMAS.md):
  - **SIC Minutas (do Autorizador)** / **Web Autorizador** / **API de formalização**: criação de variáveis para modelo de CCB de refinanciamento INSS (`Apresentação projeto 19-18.mp4`).
  - **Autorizador**: ambientação prática de testes a partir da EPT e coordenação com frente de API (`Gravando 2026-07-07 155307.mp4`).
- **`PROCESSOS`** — ver [`PROCESSOS/INDICE_PROCESSOS.md`](PROCESSOS/INDICE_PROCESSOS.md):
  - Geração da CCB de refinanciamento com novas variáveis, atualização da API de formalização e fechamento de estimativa de horas (`Apresentação projeto 19-18.mp4`).
  - Início de execução de testes a partir da EPT (`570023`), alinhamento com operador de API (Santana) e conferência prévia antes de subir base/mudar pasta compartilhada (`Gravando 2026-07-07 155307.mp4`).
- **`NEGOCIO`** — ver [`GLOSSARIO_GERAL.md`](GLOSSARIO_GERAL.md):
  - CCB (INSS), refinanciamento com múltiplos contratos, operações originais, deduplicação/concatenação de credor e somatória de saldo devedor (`Apresentação projeto 19-18.mp4`).
  - Parâmetro para margem de tolerância em operações C6 Consig (`Gravando 2026-07-07 155307.mp4`).
- **`INFRA_E_ACESSO`**:
  - Uso de base compartilhada (`UDL Base`) e diretórios de rede (`Mesa_C6 Arquivos`), com verificação prévia para evitar sobrescrita de ambiente entre operadores (`Gravando 2026-07-07 155307.mp4` — [`guia_de_estudo.md`](gravando-2026-07-07-155307/guia_de_estudo.md) §3).
- **`DÚVIDA_OU_CONFLITO`** — ver [`CONFLITOS_E_VALIDACAO.md`](CONFLITOS_E_VALIDACAO.md):
  - Parametrização/identificação do credor por operação e distribuição das horas "21, 3 e 16" do plano de teste (`Apresentação projeto 19-18.mp4`).
  - Grafia falada "IPT" × tag escrita `[EPT]` e etapas técnicas detalhadas de "subir na base / mudar a pastinha" (`Gravando 2026-07-07 155307.mp4`).
- **`SQL`** — ver [`SQL/INDICE_SQL.md`](SQL/INDICE_SQL.md):
  - Nenhuma consulta SQL demonstrada nos 2 vídeos concluídos até o momento.

## Por gravação

Fila completa e estados oficiais em [`../STATUS.md`](../STATUS.md) (24 vídeos).

| Gravação | Estado | Pasta | Categorias | Resumo do conteúdo |
|---|---|---|---|---|
| `Apresentação projeto 19-18.mp4` | **concluído** | [`apresentacao-projeto-19-18/`](apresentacao-projeto-19-18/LEIA-ME.md) | `SISTEMAS`, `NEGOCIO`, `PROCESSOS`, `DÚVIDA_OU_CONFLITO` | Especificação funcional OS 552267 — atualização do modelo de CCB do INSS em refinanciamento com múltiplos contratos (3 variáveis no SIC Minutas/Web Autorizador + API de formalização + estimativa de horas). |
| `Gravando 2026-07-07 155307.mp4` | **concluído** | [`gravando-2026-07-07-155307/`](gravando-2026-07-07-155307/LEIA-ME.md) | `PROCESSOS`, `SISTEMAS`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO` | Orientação para iniciar testes no Autorizador usando a EPT (`570023` / `558139` — margem de tolerância), alinhar com Santana (API) e conferir antes de subir base/mudar pasta compartilhada. |

## Índices temáticos

- [`SQL/INDICE_SQL.md`](SQL/INDICE_SQL.md)
- [`SISTEMAS/INDICE_SISTEMAS.md`](SISTEMAS/INDICE_SISTEMAS.md)
- [`PROCESSOS/INDICE_PROCESSOS.md`](PROCESSOS/INDICE_PROCESSOS.md)
- [`GLOSSARIO_GERAL.md`](GLOSSARIO_GERAL.md)
- [`CONFLITOS_E_VALIDACAO.md`](CONFLITOS_E_VALIDACAO.md)
- [`PRIVACIDADE_E_RETENCAO.md`](PRIVACIDADE_E_RETENCAO.md)
