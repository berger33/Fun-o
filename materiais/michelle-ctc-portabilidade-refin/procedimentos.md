> **Status:** hipótese de teste extraída de conversa; não é configuração aprovada nem instrução de produção.

# Procedimentos — MICHELLE CTC PORTABILIDADE REFIN.mp4

A gravação descreve um processo conceitual e uma possível configuração de esteiras. O desenho mencionado é de outro cliente. Não há capturas, tela de produto, status técnico verificado ou execução de teste nesta análise. Antes de alterar qualquer configuração, validar o fluxo C6 vigente com o responsável técnico e de negócio.

## Fluxo A — Modelo conceitual falado (não executar como runbook)

1. **Vínculo de propostas:** a conversa descreve uma proposta de portabilidade associada a um refim e sugere que a jornada possa gerar dois registros/propostas (**00:01:00–00:01:22; 00:12:50–00:13:18**).
2. **Coordenação das esteiras:** portabilidade e refim são descritos como fluxos distintos que precisam coordenar seus estados (**00:00:24–00:00:36**). A quantidade de esteiras e a divisão por produto/convênio variam na própria conversa (**00:10:34–00:12:14**).
3. **Acionamento:** é mencionado um processo com nome aproximado “CTC aciona refim” que acionaria o avanço da esteira de refim (**00:01:07–00:01:22; 00:05:31–00:06:00**). O nome e o comportamento não foram confirmados na tela.
4. **Ponto de espera:** a conversa contrapõe “aguarda análise de refim de portabilidade” a “aguarda alteração unificada” (**00:07:25–00:07:47**). A etapa correta para o cenário C6 está pendente de confirmação.
5. **Validação de consistência:** a justificativa falada é evitar avançar a portabilidade/gerar a CCB antes de validar os valores do refim (**00:03:36–00:04:59**). Quais valores, estados e eventos são necessários não é especificado.

## Fluxo B — Proposta de teste a confirmar em sandbox

A transcrição permite registrar somente uma hipótese para desenho de teste:

- criar, em ambiente de teste autorizado, um caso de portabilidade com refim associado e confirmar se surgem dois registros de proposta;
- definir com o responsável se os fluxos precisam de esteiras distintas para isolar os comportamentos;
- confirmar a etapa de acionamento e a etapa de espera que devem ser exercitadas;
- verificar o status de cada proposta e a consistência dos dados da CCB antes de permitir qualquer avanço posterior.

**Bloqueios antes de executar:** o responsável deve confirmar o diagrama específico do C6, as etapas e nomes oficiais, os status permitidos, o isolamento dos dados e como restaurar a configuração. O teste não foi executado nesta análise e não há resultado esperado aprovado.

### Limite sobre CTC

Os interlocutores dizem que não conseguiriam exercitar o CTC naquele momento e sugerem pular etapas de CTC no teste (**00:06:39–00:06:49; 00:09:23–00:09:46**). Isso é uma limitação/contexto daquele ambiente, não autorização para contornar CTC em produção. Qualquer simulação deve ocorrer somente em sandbox e ser aprovada.

## O que falta para aprovar o procedimento

- obter o fluxo e a configuração atuais do cliente-alvo; não usar o desenho de outro cliente;
- confirmar a nomenclatura e a função de “CTC aciona refim”, “aguarda alteração unificada”, “aguarda análise” e demais processos;
- resolver se a regra exige dependência entre as duas propostas ou se a portabilidade pode avançar independentemente;
- definir pré-condições, statuses, entradas, resultados esperados, critérios de parada e rollback;
- executar e registrar evidências sanitizadas em ambiente autorizado.

Nenhum SQL, comando de implantação ou alteração de dados foi demonstrado ou executado.
