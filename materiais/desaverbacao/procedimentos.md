> **Plano de validação, não procedimento aprovado.** Foi elaborado a partir de ASR não revisado. Nenhuma etapa abaixo foi executada nesta sessão. Não altere dados, configuração, versão, permissões, esteira ou ambiente com base somente nesta gravação.

# Plano de validação — cancelamento e desaverbação

## Evidência ASR que orienta as perguntas

- Proposta deve estar averbada antes da exclusão, segundo a fala (`00:00:34–00:00:45`).
- Parâmetros do Consignado Privado, link de stub, vínculo do empregador e seleção manual/automática são discutidos (`00:01:36–00:05:10`).
- O primeiro erro reconhecido é “Proposta não se encontra na situação para ser escolhida”; depois são descritos plugin de levantamento e serviço de exclusão (`00:15:05–00:16:11`).
- A investigação passa por convênio/produto, menção a query e árvore/esteira (`00:24:47–00:31:17`), seguida por alterações faladas na tabela de decisão (`00:32:33–00:44:01`).
- A parte final relata retorno concluído e status “desaverbado”, sem evidência visual disponível para esta análise (`01:03:19–01:06:33`).

## Fluxo A — confirmar escopo e condições antes de testar

1. Obter a EF/EPT, o runbook de cancelamento/desaverbação, versão do sistema e matriz de cenários vigentes. Identificar responsável de negócio, CQ e proprietário do ambiente.
2. Confirmar se cancelamento da proposta, exclusão de averbação e desaverbação são eventos/estados diferentes; definir pré-condições e estados elegíveis por fonte oficial. A fala inicial e a lista de estados são indícios ASR, não especificação (`00:00:34–00:00:45`; `00:15:42–00:17:18`).
3. Aprovar sandbox isolado, mock/stub e massa sintética. Não chamar Dataprev, cliente ou produção e não usar CPF, margem ou dados reais; a conversa diferencia cenário “mocado” e ambiente real (`00:44:32–00:46:47`).
4. Registrar a versão do plugin, configuração e empregador de teste aprovados. O ASR demonstra dúvida sobre versão e parâmetros, não aponta uma configuração correta (`00:18:06–00:23:39`).

## Fluxo B — revisar configuração sem alterá-la

1. Com responsável técnico, mapear a rotina que o ASR chama “modelo de averbação” para o nome e caminho oficiais do cadastro de parâmetros do Consignado Privado (`00:01:36–00:03:44`).
2. Conferir, por documentação aprovada, configuração do stub, associação do empregador e modo de exclusão. A fala alterna entre manual e automático; não copiar link, valor ou modo (`00:03:00–00:05:10`; `00:13:33–00:13:47`).
3. Confirmar separadamente os retornos de levantamento e de envio da exclusão. Registrar request/response e códigos apenas conforme o contrato aprovado; “BF”, “competência” e a versão falada ficam pendentes (`00:15:42–00:16:11`; `00:18:06–00:23:39`).
4. Documentar a árvore/esteira e as regras de transição atuais. Confirmar a semântica de `A`, `P` e `F`, elegibilidade, grupos, alçada/fase e próxima decisão em documentação oficial (`00:32:33–00:40:44`). Não adicionar processo `99`, mudar decisões nem desvincular produto com base na gravação (`00:30:32–00:31:17`; `00:40:46–00:44:01`).
5. Tratar a menção à consulta em `Cprop` e aos nomes ASR `ppcodicomv`/`ppcodprd` como indício para localizar documentação; não reconstruir nem executar SQL (`00:24:47–00:25:44`).

## Fluxo C — planejar um cenário controlado (somente após aprovação)

1. Preparar uma proposta sintética cuja inclusão/averbação e estado inicial sejam comprováveis conforme EPT. Definir o critério oficial de cancelamento e o motivo admitido; a fala sugere um motivo e um fluxo, mas não estabelece política (`01:03:19–01:03:41`).
2. Planejar um caso por combinação de tipo de operação e evento elegível (normal, refinanciamento, portabilidade; cancelamento/reprovação, liquidação ou estorno), somente se a EF exigir essas dimensões (`01:07:23–01:08:35`).
3. No sandbox aprovado, observar se o plugin de levantamento encontra o caso e se a chamada seguinte é roteada ao serviço de exclusão. Capturar entradas/estados/retorno de forma autorizada; não presumir que um componente substitua o outro (`00:15:42–00:16:11`).
4. Comparar status e resposta com os critérios da EF. A gravação relata “concluído”, “desaverbado” e retorno de sucesso, mas isso não foi confirmado (`01:05:15–01:06:33`).
5. Se houver falha, preservar o estado e parar; revisar logs e contrato com responsáveis. Não alterar versão/configuração nem repetir chamadas sem autorização e política de idempotência.

## Fluxo D — evidência, restauração e encerramento

1. Registrar ambiente, versão, massa sintética, configuração antes/depois, transições da esteira, request/response autorizados e critério esperado/observado.
2. Conferir a rotina oficial de movimentações do contrato e o estado terminal definido pela EF. O nome “Consulta movimentações de contrato” e o rótulo “desaverbado” aparecem no ASR (`01:05:36–01:06:33`), mas caminho e resultado visual não foram verificados.
3. Restaurar configurações e vínculos somente pelo runbook aprovado, com autorização, backup e rollback; verificar que o ambiente não ficou alterado. A sessão ASR descreve desvincular e depois revincular produto/esteira (`00:30:32–00:31:17`; `00:43:21–00:44:01`), sem estabelecer procedimento seguro.
4. Submeter evidências e divergências à revisão de CQ/negócio/desenvolvimento. Não marcar o cenário aprovado até resolver os itens de [`incertezas.md`](incertezas.md).

## Limites desta análise

Este plano não contém SQL reproduzido, payload, endpoint, credenciais, configuração ou comando executável. Nenhum SQL, API de produto ou teste de sistema foi executado; nenhum banco, dado, configuração ou ambiente foi alterado. A gravação e suas telas não foram revisadas nesta sessão.
