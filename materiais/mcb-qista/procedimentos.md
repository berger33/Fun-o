> **Classificação:** rascunho de planejamento/validação, não runbook. A mídia original não foi revisada nesta etapa; confirme cada rótulo no procedimento oficial antes de executar qualquer ação.

# Procedimentos — MCB - QISTA.mp4

## Fluxo A — Desenhar teste de validação de agente (sandbox)

**Objetivo declarado:** observar se uma proposta aciona a consulta de certificação/pontuação do agente pelo MCB e se o resultado altera o andamento na esteira (**00:00:33–00:01:13; 00:02:22–00:02:52; 00:08:48–00:09:01**).

### Pré-condições obrigatórias

- Aprovação de negócio para os resultados esperados e de engenharia para integração e ambiente.
- Sandbox isolado, versão conhecida de Autorizador, MCB e API, com mecanismo de retorno/rollback documentado.
- Mapeamento oficial da atividade da esteira e do processo do MCB; documentação da API, autenticação e tratamento de indisponibilidade.
- Dados sintéticos autorizados para os estados de certificação necessários; nenhum CPF ou registro real neste roteiro.
- Confirmação da classificação interna/externa e dos efeitos funcionais de cada cenário.

### Plano de cenários — não executado

1. **Registrar o estado inicial:** versão/ambiente, configuração aprovada da esteira e atividade vinculada ao MCB, sem publicar endpoints, segredos ou dados pessoais.
2. **Cenário interno:** preparar uma promotora de teste cuja classificação interna esteja validada. Observar se a consulta do agente é omitida ou segue a regra oficial. A fala sugere que talvez não haja validação, mas não é critério confirmado (**00:08:24–00:08:48**).
3. **Cenário externo:** preparar uma promotora de teste classificada como externa. Observar a tentativa de consulta e registrar resposta/status de agente e resultado de transição, conforme critérios aprovados (**00:08:40–00:09:01**).
4. **Conferir dados e evento:** verificar somente em ferramenta autorizada que o Autorizador envia o contexto previsto, a atividade correta aciona o MCB e a resposta corresponde ao cenário. A conversa não define payload, códigos ou evidência técnica.
5. **Avaliar desvios:** interromper em caso de falha de comunicação, configuração incompatível, resposta inesperada ou dado não sintético; não contornar validação nem forçar avanço.
6. **Registrar e restaurar:** guardar evidência sanitizada e resultado esperado/obtido; limpar/restaurar apenas pelo procedimento de sandbox aprovado.

**Resultado desta análise:** teste não executado; este roteiro registra somente um desenho de cenário derivado da conversa.

## Fluxo B — Verificar componentes/configuração antes do teste (checklist, não publicação)

A gravação menciona MCB separado, uma API de consulta de pontuação e configuração de vínculo entre esteira/atividade; também menciona referência da API nas configurações do Autorizador (**00:02:04–00:02:52; 00:10:02–00:10:42**). Antes de qualquer teste, solicitar ao responsável que confirme, em documentação vigente:

- nomes e versões de cada componente;
- atividade/processo de esteira e sua correspondência no MCB;
- contrato, URL e autenticação da API (manter segredos fora deste material);
- ambiente e origem dos dados;
- tratamento de indisponibilidade, pontuação/status e bloqueio/liberação;
- passos aprovados de publicação, validação e rollback.

Não baixar/publicar API, editar app settings, alterar UDL ou promover versão com base apenas na transcrição automática.

## Fluxo C — Investigar classificação/cadastro da promotora (sem alteração)

1. Confirmar o ambiente e consultar a documentação funcional/técnica de **WebTabelas** e do cadastro aplicável (**00:04:22–00:05:59; 00:06:25–00:07:59**).
2. Confirmar se, naquela versão, a promotora aparece como cadastro de promotora ou sob uma categoria de origem; não presumir o rótulo “Origem 3”.
3. Confirmar a regra interna/externa com negócio e o cenário autorizado, registrando apenas o resultado esperado.
4. Se o problema for ausência de formas de liberação ou “produto não encontrado”, coletar apenas dados sintéticos e encaminhar ao responsável técnico para diagnóstico. A afirmação de que o erro estava numa tabela de liberações refere-se ao ambiente local apresentado (**00:03:54–00:04:20; 00:06:03–00:06:21**).
5. Não executar SQL nem alterar tabela/base. A menção genérica a `INSERT`/`UPDATE` não inclui comando, objeto, validação ou permissão (**00:02:54–00:03:09**).

## Exceções e bloqueios

- Código, esteira, atividade, tabela, regra de elegibilidade ou forma de liberação não confirmados → **parar e confirmar**, não adivinhar.
- Sem sandbox/dados sintéticos/rollback → **não executar**.
- Não contornar CTC/MCB, a verificação de agente ou a governança de publicação.
- Nenhum comando de banco, endpoint ou alteração de configuração foi executado nesta análise.
