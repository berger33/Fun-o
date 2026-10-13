# Índice de SQL

Consultas e comandos SQL identificados nas gravações analisadas:

| Objetivo | Gravação e timestamp | Dialeto | Tabelas e colunas citadas | Tipo | Análise detalhada e captura |
|---|---|---|---|---|---|
| Consultar eventos/etapas de esteira e averbação por proposta (`CSNRPROP`) para diagnóstico de integração de reaproveitamento de seguro | `Gravando 2026-10-07 152044.mp4` — `00:00:00` | T-SQL (SQL Server) | Banco `FCSMONITOREMPR`: `ECONSULT` (`CSNRPROP`, `CSSERVER`, `CSRETTEXT`, `CSDTHRAGEN`, `CSSTATUS`, `CSIDCONS`, `CSIDPFCON`) `INNER JOIN` `TBPERFCON` (`PRIDPFCON`, `PRDESCPFCON`) | **somente leitura (`SELECT`)** (+ `USE FCSMONITOREMPR`) | [`../gravando-2026-10-07-152044/guia_de_estudo.md`](../gravando-2026-10-07-152044/guia_de_estudo.md) §4 · [`../gravando-2026-10-07-152044/procedimentos.md`](../gravando-2026-10-07-152044/procedimentos.md) Fluxo B · [`01`](../gravando-2026-10-07-152044/capturas/01-consulta-sql-monitor-empr.png) |

## Gravações sem SQL demonstrado

| Gravação | Situação | Observação |
|---|---|---|
| `Apresentação projeto 19-18.mp4` | **não aplicável** | Houve apenas a menção verbal a verificar "no fonte/query" (`00:06:12`) como encaminhamento — nenhuma consulta foi escrita ou executada. |
| `Gravando 2026-07-07 155307.mp4` | **não aplicável** | Nenhuma consulta SQL exibida ou ditada. |

Cada entrada traz objetivo, gravação e timestamp (`HH:MM:SS`), dialeto, tabelas/colunas citadas, tipo (`somente leitura` / `altera dados`) e link para a análise detalhada no vídeo. Comandos que alteram dados (`INSERT`, `UPDATE`, `DELETE`, DDL) recebem sinalização explícita de efeito e de validação operacional; nenhum comando é executado.
