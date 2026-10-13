# Índice de processos

| Rotina / fluxo | Pré-requisitos | Resultado | Exceções | Gravação e timestamps | Detalhe |
|---|---|---|---|---|---|
| **Geração da CCB de refinanciamento** com as novas variáveis | refinanciamento com múltiplos contratos vinculados à mesma operação | CCB com contratos e credores lado a lado (separador `;`) e saldo devedor **somado** | credor diferente → todos aparecem; credor igual → aparece uma vez | `Apresentação projeto 19-18.mp4` — 00:00:49 – 00:01:55; 00:02:36 – 00:03:12 | [`guia_de_estudo.md`](../apresentacao-projeto-19-18/guia_de_estudo.md) §4 |
| **Atualização da API de formalização** | definir as novas variáveis | jornada de contratação emite a CCB atualizada | — | `…` — 00:02:09 – 00:02:25 | [`procedimentos.md`](../apresentacao-projeto-19-18/procedimentos.md) Fluxo B |
| **Tratamento da dúvida técnica do credor** | dúvida levantada na reunião | **pendente** (verificar fonte/query; alinhar com desenvolvimento) | áudio ruim → dúvida enviada pelo chat | `…` — 00:03:34 – 00:06:45 | Fluxo C |
| **Estimativa e fechamento de esforço** | horas já propostas | confirmado: 28 h (item 1), 6 h (item 2); CQ "21"; plano de teste "21, 3 e 16" (ambíguo) | — | `…` — 00:06:54 – 00:07:42 | Fluxo D + [`incertezas.md`](../apresentacao-projeto-19-18/incertezas.md) §5 |
| **Início de execução de testes no Autorizador a partir da EPT** | EPT escrita (`570023`) e item principal (`558139`) identificados | Operador executa os testes da própria EPT alinhado com o responsável pela API (Santana) e sem conflito na base compartilhada | Se Santana já tiver alterado a pasta/base compartilhada, não sobrescrever sem alinhar | `Gravando 2026-07-07 155307.mp4` — 00:00:01 – 00:01:32 | [`procedimentos.md`](../gravando-2026-07-07-155307/procedimentos.md) Fluxo A |

Quando houver entradas, cada rotina deve trazer: ordem de execução, pré-requisitos, responsáveis citados, decisões e exceções, resultado esperado, conferência final e gravações/timestamps de origem.
