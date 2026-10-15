# Consultas SQL do acervo — texto completo

Todas as consultas que aparecem **escritas** em alguma fonte do acervo, com o texto como foi
exibido, o que cada uma faz e onde ela roda. Serve de complemento ao
[`INDICE_SQL.md`](INDICE_SQL.md), que registra objetivo, origem, dialeto, tabelas e tipo de cada
consulta — e que também lista as fontes onde o SQL foi apenas **mencionado, sem texto**.

- **Dialeto:** T-SQL (Microsoft SQL Server) — `SELECT TOP`, banco qualificado `FCSMONITOREMPR..`,
  dica `(NOLOCK)`, `USE` para troca de contexto, interface SSMS.
- **Tipo de comando:** somente leitura (`SELECT`) em todas as consultas reproduzidas abaixo.
  Nenhum comando foi executado na produção deste material.
- **Dígitos ilegíveis:** onde a leitura da tela não fechou, o dígito aparece como `?` — mantenha a
  marcação ao reutilizar a consulta e confirme o valor na base.
- **Identificadores:** números de proposta, CPF e demais identificadores diretos são substituídos
  por marcadores (`'número-da-proposta'`).

---

## 1. Identificar o perfil de consulta pelo código do serviço

- **O que faz:** descobre o registro do **perfil de consulta** a partir de um trecho do código do
  perfil. É o primeiro passo do rastreio: `TBPERFCON` é o cadastro de perfis de consulta, e o
  resultado traz o identificador de perfil (`PRIDPFCON`) usado pela consulta principal.
- **Onde roda:** banco `FCSMONITOREMPR` · tabela `TBPERFCON` · coluna `PRCODPFCON`.
- **Como ler:** pesquise pelo trecho do código do perfil; o valor de `PRIDPFCON` liga o perfil às
  execuções registradas em `ECONSULT`.
- **Fonte:** `jonas-ept-explicacao/guia_de_estudo.md` §3 (editor do SSMS, `00:00:00`).

```sql
SELECT * FROM FCSMONITOREMPR..TBPERFCON WHERE PRCODPFCON LIKE ('%chsInOferta%')
```

## 2. Listar as execuções do serviço de envio da proposta ao sistema externo

- **O que faz:** encontra a **execução do serviço** que envia a proposta ao sistema externo
  (`SrvEnvioPropExt`) e devolve a chave do evento. Filtra pela **descrição do serviço** — e não pelo
  número da proposta — para ver todas as chamadas daquele serviço; a mais recente aparece primeiro.
- **Onde roda:** banco `FCSMONITOREMPR` · `ECONSULT` (eventos de execução de serviços e plugins do
  monitor) com `INNER JOIN` em `TBPERFCON` (`CSIDPFCON = PRIDPFCON`) · dica `NOLOCK`.
- **Como ler:** confira descrição do perfil (`PRDESCPFCON`), versão do plugin (`CSVERPLUG`), número
  da proposta (`CSNRPROP`), servidor (`CSSERVER`), retorno (`CSRETTEXT`), erro (`CSERRO`), data/hora
  de agendamento (`CSDTHRAGEN`) e situação (`CSSTATUS`). A chave `CSIDCONS` da linha encontrada é o
  que abre o detalhe do payload na consulta 3.
- **Variante:** trocar o filtro por descrição por `WHERE CSNRPROP = 'número-da-proposta'` (é o
  filtro que aparece comentado no editor) faz a mesma leitura olhando por proposta.
- **Fonte:** `jonas-ept-explicacao/guia_de_estudo.md` §3 e `procedimentos.md` §1
  (`00:02:50`–`00:03:40`).

```sql
USE FCSMONITOREMPR
SELECT TOP 100? PRDESCPFCON, CSVERPLUG, CSNRPROP, CSSERVER, CSRETTEXT, CSERRO, CSDTHRAGEN, CSSTATUS, *
FROM FCSMONITOREMPR..ECONSULT(NOLOCK)
INNER JOIN FCSMONITOREMPR..TBPERFCON ON CSIDPFCON = PRIDPFCON --where CSNRPROP='8??83216?'
WHERE PRDESCPFCON LIKE ('%Servico de Envio da Proposta ao Sistema Externo%')
ORDER BY CSIDCONS DESC
```

## 3. Abrir o detalhe (chave-valor) do evento e ler o payload enviado

- **O que faz:** abre o **detalhe da execução** em formato chave-valor — cada linha traz o nome de
  um campo do corpo enviado e o seu conteúdo. É onde o payload JSON do envio é conferido campo a
  campo.
- **Onde roda:** banco `FCSMONITOREMPR` · tabela `ECONSULTD` · colunas `CDIDCONS` (id da consulta),
  `CDCONTROLE` (sequencial do detalhe) e `CDCAMPO` (nome do campo).
- **Como ler:** use o `CDIDCONS` da linha encontrada na consulta 2. Aparecem campos de consulta do
  trabalhador (por exemplo `DATAPREV_CNPJEMPR`, `DATAPREV_CODCATEG`, `DATAPREV_DESCCBO`,
  `VLRMRGDL…`) e os demais blocos do envio.
- **Outro identificador:** o mesmo comando aparece com `CDIDCONS='915516'` para abrir um segundo
  detalhe no editor.
- **Fonte:** `jonas-ept-explicacao/guia_de_estudo.md` §3, `procedimentos.md` §1 e `transcricao.md`
  (notas de revisão) — `00:03:11`, `00:05:40`.

```sql
SELECT * FROM ECONSULTD WHERE CDIDCONS='84942'
```

## 4. Monitorar esteira e averbação de uma proposta

- **O que faz:** mostra os **eventos de esteira e averbação** de uma proposta específica, no contexto
  de integração de reaproveitamento de seguro: quais etapas rodaram, com que retorno e em que ordem.
- **Onde roda:** banco `FCSMONITOREMPR` · `ECONSULT` (`PRDESCPFCON`, `CSNRPROP`, `CSSERVER`,
  `CSRETTEXT`, `CSDTHRAGEN`, `CSSTATUS`) com `INNER JOIN` em `TBPERFCON`.
- **Como ler:** filtre pelo número da proposta (`CSNRPROP`) e leia a etapa (`PRDESCPFCON`), a
  situação (`CSSTATUS`), o retorno (`CSRETTEXT`) e o agendamento (`CSDTHRAGEN`). O primeiro
  comentário identifica a finalidade do diagnóstico; o segundo (dentro do `WHERE`) é o filtro
  alternativo por descrição do plugin de levantamento para exclusão de averbação.
- **Fonte:** `gravando-2026-10-07-152044/guia_de_estudo.md` §4, `procedimentos.md` Fluxo B e
  `transcricao.md` (`00:00:00`; captura `01`).

```sql
--INTEGRAÇÃO DE REAPROVEITAMENTO DE SEGURO
SELECT TOP 1000 PRDESCPFCON, CSNRPROP, CSSERVER,CSRETTEXT,CSDTHRAGEN,CSSTATUS,* FROM FCSMONITOREMPR..ECONSULT(NOLOCK)
INNER JOIN FCSMONITOREMPR..TBPERFCON ON CSIDPFCON = PRIDPFCON WHERE CSNRPROP = '000033373'
--where PRDESCPFCON LIKE ('%INSS - Plugin de levantamento para exclusão de averbação%')
ORDER BY CSIDCONS DESC

USE FCSMONITOREMPR
```

## 5. Consultar o log de refinanciamento

- **O que faz:** lê o **log de refinanciamento** e o seu detalhe. `CLOGREFIN` guarda o registro do
  processamento; `CLOGREFIND` traz o detalhamento linha a linha do mesmo evento.
- **Onde roda:** banco `FCSPROPEMPR` · tabelas `CLOGREFIN` e `CLOGREFIND`.
- **Como ler:** as duas consultas aparecem juntas no editor — primeiro o registro do log, depois o
  detalhe.
- **Fonte:** `jonas-ept-explicacao/guia_de_estudo.md` §3 (consultas preparadas no editor,
  `00:00:00`), `procedimentos.md` §1 e `glossario.md`.

```sql
USE FCSPROPEMPR
SELECT * FROM CLOGREFIN
SELECT * FROM CLOGREFIND
```

## 6. Consultar reaproveitamento de seguro por proposta

- **O que faz:** mostra o **reaproveitamento de seguro** registrado para uma proposta.
- **Onde roda:** banco `FCSPROPEMPR` · tabela `EREAPSEG` · coluna `EPRNRPROP` (número da proposta,
  usada como filtro; na tela o literal aparece parcialmente ilegível: `'8??8321??'`).
- **Como ler:** filtre pelo número da proposta. É a consulta de apoio que acompanha a investigação
  de reaproveitamento — a mesma frente monitorada na consulta 4.
- **Fonte:** `jonas-ept-explicacao/guia_de_estudo.md` §3, `procedimentos.md` §1 e `glossario.md`.

```sql
USE FCSPROPEMPR
SELECT * FROM EREAPSEG WHERE EPRNRPROP='8??8321??'
```

## 7. Consultar o complemento da proposta

- **O que faz:** lê o **complemento da proposta** pelo número da proposta.
- **Onde roda:** banco `FCSPROPEMPR` · tabela `CCOMP` · coluna `CSNRPROP` (número da proposta, usada
  como filtro; literal parcialmente ilegível na tela: `8??83288?`).
- **Como ler:** filtre pelo número da proposta. Serve para conferir os dados que complementam a
  proposta no banco de propostas.
- **Fonte:** `jonas-ept-explicacao/guia_de_estudo.md` §3, `procedimentos.md` §1 e `glossario.md`.

```sql
USE FCSPROPEMPR
SELECT * FROM CCOMP WHERE CSNRPROP=8??83288?
```

---

## Operações de banco citadas sem o comando escrito

Pontos do acervo em que a operação no banco é descrita em palavras, sem o comando. Entram aqui
porque mostram **onde** essas consultas aparecem na rotina; o texto de cada uma continua em
[`INDICE_SQL.md`](INDICE_SQL.md).

| Operação | Onde aparece | Situação |
|---|---|---|
| Configurar alias em `TPARWFIUTIL.PWALIAS`, criar procedures `.NET` (opções `C` e `W`) e apagar registros do site atual em `TRTHB` | `liberacao-padrao-glauco` (planilha operacional) | passos de planilha, sem comando SQL escrito; altera dados — depende de validação operacional |
| Correção pontual por `INSERT`/`UPDATE` | `mcb-qista` | citado como possibilidade de ajuste em base local, sem script |
| `SELECT` para localizar o número da operação | `primeiro-projeto` | consulta prometida na fala, texto não exibido |
| `select` na tabela referida como `coper` filtrando pelo CPF | `conversa-matheus-refin-api` (fonte textual) | objetivo indicado na conversa, comando não reproduzido |
| Editar um `SELECT` na base e rodar a consulta para conferir convênio/produto | `desaverbacao` | intenção registrada na fala; nomes parciais na transcrição (`Cprop`, `ppcodicomv`, `ppcodprd`), sem esquema ou texto de consulta |
| Incluir no `select` o campo de origem do CNPJ do empregador (`ETRACPD.*`) | `projeto-14-08` | menção à verificação do campo, consulta não escrita |
| `SELECT` ao discutir data de liquidação e despesa de seguro | `gravando-2026-10-06-110907` | menção a tabela/campo, sem comando |

Nenhum comando desta lista foi escrito, reproduzido ou executado na produção deste material.
