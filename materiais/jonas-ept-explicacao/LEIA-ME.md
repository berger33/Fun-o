# LEIA-ME — materiais de `Jonas EPT explicação.mp4`

> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste** (proposta, cliente, promotora e documentos de exemplo). Em
> respeito às regras acordadas, os derivados preservam o nome **Função Sistemas** e os **nomes
> dos operadores** (Jonas, William), e **omitiram** dados pessoais de teste (CPF/CNPJ/telefone/
> e-mail/endereço, tokens de serviço, caminhos de rede/usuário). Veja
> [`../PRIVACIDADE_E_RETENCAO.md`](../PRIVACIDADE_E_RETENCAO.md).

Esta pasta contém a análise da gravação `Jonas EPT explicação.mp4` (10:25, Teams, 2026-09-23) —
demonstração de tela em que **Jonas** mostra ao colega (pelo chat, **William**) como: rastrear a
execução do plugin **"Serviço de Envio da Proposta ao Sistema Externo"** (`SrvEnvioPropExt`, item
**OS 586780** — "[ÁGIL] (I) Nova Flag informativa de Docs anexados no SrvEnvioPropExt") no banco
`FCSMONITOREMPR` (`ECONSULT` → `ECONSULTD`), ler o **payload JSON** enviado ao sistema externo,
posicionar o novo agrupamento de documentos anexados dentro do objeto `client`, e preencher a
**EPT** (planilha de casos de teste) aproveitando os cenários do **Relatório de Testes** da pasta
compartilhada da equipe.

A gravação `jonas2309.mp4` do manifesto é uma **duplicata exata** deste arquivo (mesmo objeto
LFS `f99bd795…`) e está coberta por esta mesma análise (ver [`../../STATUS.md`](../../STATUS.md)).

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| [`metadados.md`](metadados.md) | Ficha técnica do vídeo, participantes, método de análise, origem dos bytes e SHAs da coleta |
| [`transcricao.md`](transcricao.md) | Fala com timestamps, revisada contra a tela, com indicações visuais e notas de correção |
| [`transcricao_bruta.txt`](transcricao_bruta.txt) / [`transcricao.srt`](transcricao.srt) / [`transcricao.vtt`](transcricao.vtt) / [`transcricao_meta.json`](transcricao_meta.json) | Transcrição automática original (faster-whisper large-v3, pt) e metadados do modelo |
| [`guia_de_estudo.md`](guia_de_estudo.md) | Guia de estudo completo: contexto, linha do tempo, SQL, payload, EPT e cenários de teste |
| [`procedimentos.md`](procedimentos.md) | Roteiros reaproveitáveis (rastreio no banco, conferência no Autorizador, EPT, cenários) |
| [`perguntas.md`](perguntas.md) | 18 perguntas de fixação com respostas e timestamps |
| [`glossario.md`](glossario.md) | Termos e tabelas identificados (ECONSULTD, corban_data, EPT, endpoints, etc.) |
| [`incertezas.md`](incertezas.md) | 15 itens não confirmados (literais SQL, conflito `attached_document`, falas truncadas) |
| [`capturas.md`](capturas.md) | Índice das 7 capturas de tela com verificação de conteúdo |

## Comece por

1. [`guia_de_estudo.md`](guia_de_estudo.md) §1 (contexto) e §3 (a consulta SQL de rastreio);
2. [`capturas.md`](capturas.md) (imagens verificadas do fluxo);
3. [`incertezas.md`](incertezas.md) antes de **usar qualquer literal** (números de proposta,
   nome do objeto do payload) desta gravação.

## Relação com os outros vídeos do acervo

- **`Gravando 2026-09-22 111258.mp4`** — mesma OS 586780: detalhamento da EF e da rotina
  Anexar/Consultar Documentação do Autorizador.
- **`Gravando 2026-10-07 152044.mp4`** — mesma tabela `ECONSULT`, filtrada por número de
  proposta (diagnóstico de reaproveitamento de seguro).
- **`Gravando 2026-07-07 155307.mp4`** — compartilhamentos de rede da equipe (`Mesa_C6`, UDL Base).
