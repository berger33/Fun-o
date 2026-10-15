> **Plano de elaboração/revisão, não procedimento de produção.** Não executar chamadas, alterar convênios/configuração, criar propostas ou publicar evidências com base apenas na transcrição. Nenhum teste foi executado neste lote.

# Procedimentos — Como fazer EPT.mp4

## Fluxo A — Ler e decompor a EF

1. Obter a EF/EPT vigentes por canal autorizado e confirmar projeto, versão, item, responsável e ambiente (**00:02:12–00:02:48; 00:27:25–00:28:21**).
2. Ler objetivo, situação atual, requisito funcional, premissas e dependências; listar o que já precisa estar implementado para o cenário ser executável (**00:27:40–00:31:13**).
3. Delimitar cada item testável. Não derivar nomes de campos, rota, regra ou identificador apenas da fala ASR.
4. Resolver lacunas com o responsável antes de preparar massa ou escrever resultado esperado.

## Fluxo B — Usar o template EPT vigente

1. Obter o template oficial e conferir os cabeçalhos/colunas completos. A gravação cita seis colunas, mas a enumeração ASR é parcial (**00:09:17–00:10:05**).
2. Preencher projeto, referência do caso e item da EF nos campos aprovados. Separar casos distintos conforme o padrão vigente (**00:09:36–00:10:05; 00:11:53–00:12:47**).
3. Registrar pré-condições, premissas e pós-condições conforme o template; reutilizar texto padrão apenas quando for de fato válido para o projeto (**00:09:58–00:10:05; 00:26:47–00:27:16**).
4. Descrever cada ação/navegação em ordem reprodutível e associar a cada etapa o resultado esperado, conferido na EF/documentação aprovada (**00:11:04–00:12:47; 00:13:05–00:15:06; 00:23:14–00:24:24**).
5. Usar exemplos anteriores apenas como referência; não copiar sem revisar cada pressuposto e passo (**00:08:57–00:09:14; 00:25:39–00:27:16**).

## Fluxo C — Planejar cenário de resposta detalhada de proposta (exemplo da gravação)

**Executar somente se este projeto e ambiente forem formalmente aprovados.**

1. Confirmar na EF o endpoint, os parâmetros de entrada e o schema de saída. A gravação relata número de proposta e usuário como entradas, com novos objetos de despesa e reaproveitamento na saída (**00:04:29–00:06:18**).
2. Criar, em sandbox, proposta e dados sintéticos que satisfaçam as pré-condições da despesa; documentar a preparação necessária (**00:06:28–00:06:52; 00:15:09–00:16:03**).
3. Se o caso exigir reaproveitamento, preparar apenas o cenário de refinanciamento que a EF autorizar; o vídeo descreve esse vínculo como condição para o exemplo (**00:06:53–00:07:08; 00:18:35–00:18:53**).
4. Invocar somente endpoint de teste ou mock autorizado; comparar retorno com o schema e a EF e, se pertinente, com a interface autorizada (**00:17:05–00:17:42; 00:21:02–00:21:18**).
5. Registrar resultado, versão, ambiente e dados sintéticos. Não tratar números ou mensagens ditos na aula como valores de aceite.

## Fluxo D — Planejar exercício de recálculo/margem de tolerância

1. Obter a EF completa e identificar fórmula, limites configuráveis, percentual, dependência de projeto e ordem das validações (**00:27:25–00:30:21**).
2. Aguardar a implementação da dependência indicada pela EF e confirmar o estado de implantação antes de escrever/executar o caso (**00:30:01–00:31:13**).
3. Depois de aprovação funcional, especificar cenários sintéticos de valor abaixo, dentro e acima dos limites; confirmar arredondamento, limites inclusivos, precedência entre percentual e valores fixos e resultado esperado com o dono do produto. Esses detalhes não estão resolvidos na gravação.
4. Elaborar a EPT com ambiente, proposta, convênio e configuração exclusivamente de teste, seguindo o template oficial.
5. Submeter a EPT à revisão do responsável; só executar depois de autorização e preparação/rollback aprovados (**00:34:39–00:35:14**).

## Critérios de parada

- EF/template/versão, fórmula, dependência ou schema ausente → não fechar o resultado esperado.
- Ambiente não isolado, massa real ou endpoint de produção → não executar.
- Perfil, convênio, proposta ou configuração necessária sem aprovação → não criar nem modificar.
- Nome/ID lido pelo ASR sem confirmação visual → não usar como chave de busca ou evidência.
- A transcrição não é autorização para executar consultas, chamadas, implantação ou alteração de dados.
