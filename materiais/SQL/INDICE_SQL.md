# Índice de SQL

Consultas e comandos SQL identificados nas gravações analisadas:

| Objetivo | Gravação e timestamp | Dialeto | Tabelas e colunas citadas | Tipo | Análise detalhada e captura |
|---|---|---|---|---|---|
| Consultar eventos/etapas de esteira e averbação por proposta (`CSNRPROP`) para diagnóstico de integração de reaproveitamento de seguro | `Gravando 2026-10-07 152044.mp4` — `00:00:00` | T-SQL (SQL Server) | Banco `FCSMONITOREMPR`: `ECONSULT` (`CSNRPROP`, `CSSERVER`, `CSRETTEXT`, `CSDTHRAGEN`, `CSSTATUS`, `CSIDCONS`, `CSIDPFCON`) `INNER JOIN` `TBPERFCON` (`PRIDPFCON`, `PRDESCPFCON`) | **somente leitura (`SELECT`)** (+ `USE FCSMONITOREMPR`) | [`../gravando-2026-10-07-152044/guia_de_estudo.md`](../gravando-2026-10-07-152044/guia_de_estudo.md) §4 · [`../gravando-2026-10-07-152044/procedimentos.md`](../gravando-2026-10-07-152044/procedimentos.md) Fluxo B · [`01`](../gravando-2026-10-07-152044/capturas/01-consulta-sql-monitor-empr.png) |
| Instruções operacionais de banco na planilha `Liberacao_Padrao_V30.xlsx`: configurar alias em `TPARWFIUTIL.PWALIAS`, criar procedures `.NET` (opções `C` e `W`) e deletar registros do site atual em `TRTHB` antes de cadastrar rotinas | `Liberação padrão - Glauco.mp4` — `00:00:50`, `00:01:40`, `00:02:33 – 00:02:43` | não identificado (instrução textual em planilha) | Tabela `TPARWFIUTIL` (campo `PWALIAS`); tabela `TRTHB` (exclusão por site atual); procedures `.NET` (opções `C` e `W`) | **altera dados** (configuração de alias, criação de procedures e exclusão prévia em `TRTHB` — requer validação operacional; nenhum comando SQL literal exibido) | [`../liberacao-padrao-glauco/guia_de_estudo.md`](../liberacao-padrao-glauco/guia_de_estudo.md) §§4–5 · [`01`](../liberacao-padrao-glauco/capturas/01-planilha-liberacao-padrao-website-net.png), [`03`](../liberacao-padrao-glauco/capturas/03-cenarios-plugin-7-registros.png) |

## Gravações sem SQL demonstrado

| Gravação | Situação | Observação |
|---|---|---|
| `Apresentação projeto 19-18.mp4` | **não aplicável** | Houve apenas a menção verbal a verificar "no fonte/query" (`00:06:12`) como encaminhamento — nenhuma consulta foi escrita ou executada. |
| `Gravando 2026-07-07 155307.mp4` | **não aplicável** | Nenhuma consulta SQL exibida ou ditada. |
| `PROJETO 14-08.mp4` | **menção, sem texto** | Apenas a fala "é só a gente colocar lá no select" (`00:01:36`) como encaminhamento para identificar o campo `ETRACPD.*` do CNPJ — nenhuma consulta escrita, exibida ou executada. |
| `Gravando 2026-09-22 111258.mp4` | **não aplicável** | Nenhuma consulta SQL exibida ou ditada. A tela mostra o PDF da especificação (OS 586780) e a fala trata de campos "na base" (`00:03:10`–`00:03:29`) sem consulta. |

Cada entrada traz objetivo, gravação e timestamp (`HH:MM:SS`), dialeto, tabelas/colunas citadas, tipo (`somente leitura` / `altera dados`) e link para a análise detalhada no vídeo. Comandos que alteram dados (`INSERT`, `UPDATE`, `DELETE`, DDL) recebem sinalização explícita de efeito e de validação operacional; nenhum comando é executado.
