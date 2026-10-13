> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Gabriel, William, Santana). Não são publicadas **imagens de pessoas**
> (avatares/fotos de perfil), URLs de sessão nem campos de CPF/telefone/e-mail de teste.

# Glossário — Gravando 2026-10-07 152044.mp4

- **Autorizador Web (`WebAutorizador`)** — sistema web (`C6/WebSite/WebAutorizador`, versão
  `26.0929.124.7113` no vídeo) usado para cadastro de propostas, parametrização de tabelas,
  convênios, produtos e políticas de despesas (**[00:00:06 – 00:04:10]**).
- **Cód. Política de Despesa/Tarifa (`98`)** — campo exibido no modal **Despesas** do cadastro do
  **Convênio** (`UI.ConfigConvenio.aspx`) que identifica qual política de despesas e tarifas está
  associada ao convênio; no exemplo `989898 - CONV MS`, o código vinculado é `98` (`teste`,
  **[00:03:07 – 00:03:21]**).
- **Condição Escolhida** — grade da tela **Proposta Sintetizada** (`UI.PropostaSintetizada.aspx`)
  que lista as tabelas/convênios disponíveis para a simulação (`000012`, `000013`, `000200`, `000222`,
  `101010`, `989898`), com taxa de juros a.m., valor da parcela, valor solicitado e valor cliente
  (**[00:00:51 – 00:01:20]**).
- **Convênio (`989898 - CONV MS`)** — cadastro do módulo `998` no menu `Tabelas -> Convênios` que
  agrupa tipos de operação (`Nova`, `Refinanciamento`, `Renegociação`, `Portabilidade`), produto
  (`009898 - PRODUTO MS`), origens, despesas, taxas/prazos, formalização e políticas de reneg/refin
  (**[00:02:00 – 00:04:00]**).
- **Despesas / Tarifas** — quadro da tela **Proposta Sintetizada** onde são exibidos o `Vlr. IOF` e
  as despesas configuradas para o convênio, incluindo despesas do tipo **seguro** (`Seguro A`,
  `SEGUROS`), com opção `Incluir` e valor calculado/informado (**[00:00:11 – 00:01:26]**).
- **`ECONSULT` (`FCSMONITOREMPR..ECONSULT`)** — tabela do banco `FCSMONITOREMPR` consultada via
  SSMS para inspecionar eventos/consultas de esteira e averbação por proposta (`CSNRPROP`), status
  (`CSSTATUS`), servidor (`CSSERVER`), retorno (`CSRETTEXT`) e agendamento (`CSDTHRAGEN`) (**[00:00:00]**).
- **`FCSMONITOREMPR`** — banco de dados SQL Server que armazena as tabelas de monitoramento de
  consultas/integrações de empréstimo (`ECONSULT` e `TBPERFCON`) (**[00:00:00]**).
- **Reaproveitamento de seguro** — funcionalidade de refinanciamento citada na conversa inicial do
  Teams e no comentário SQL (`--INTEGRAÇÃO DE REAPROVEITAMENTO DE SEGURO`) pela qual o seguro de uma
  operação anterior é reaproveitado no refinanciamento (**[00:00:00]**).
- **`TBPERFCON` (`FCSMONITOREMPR..TBPERFCON`)** — tabela de perfis de consulta do banco
  `FCSMONITOREMPR`, relacionada a `ECONSULT` por `CSIDPFCON = PRIDPFCON`, que fornece a descrição
  da etapa/plugin (`PRDESCPFCON`, como `Esteira Autorizador` e `Averbação Proposta`) (**[00:00:00]**).
- **Valores de TC por Convênio** — seção do modal **Despesas** dentro do cadastro do convênio que
  permite parametrizar faixas de `Valor Solicitado` (`Até:`), `Tipo:` e `Valor TC:` (**[00:03:07 – 00:03:35]**).
