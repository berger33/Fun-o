> **Atenção:** os fluxos abaixo são um plano de validação, não um procedimento operacional aprovado. Não executar em produção, não usar serviço externo real e não inferir consulta SQL. Nenhum passo foi executado nesta análise.

# Procedimentos — Gravando 2026-10-06 110907.mp4

## Fluxo A — Aprovar o plano e preparar sandbox

**Objetivo:** validar a especificação de integração de cancelamento de seguro descrita na reunião sem produzir efeito financeiro.

### Pré-condições obrigatórias

- EF aprovada, responsável funcional do CDC identificado, regras de elegibilidade e critérios de aceite documentados.
- Sandbox isolado; serviço externo substituído por stub/mock; logs e persistência sob teste; rollback conhecido.
- Dados inteiramente sintéticos, contratos de teste e seguro fictício; endpoint e credenciais obtidos exclusivamente de configuração autorizada no cofre.
- Testador autorizado para a rotina e a linha de comando; nenhum job recorrente ligado a ambiente real.

### Passos

1. Conferir na EF a divisão dos itens 1.1 (configuração), 1.2 (remessa/plugin e linha de comando) e 1.3 (consulta/status e relatório) mencionada em `00:01:34–00:03:34`.
2. Resolver com o responsável do CDC quais grupos, produtos, tipos de operação e eventos de histórico financeiro tornam uma operação elegível (`00:10:47–00:12:15`).
3. Confirmar de forma autorizada qual fonte representa a despesa de seguro **na operação**; a reunião não identifica tabela ou campo (`00:14:02–00:15:21`). Não consultar/alterar banco com base no ASR.
4. Revisar campos/configuração, URL, proxy e referência a segredo diretamente na EF e no ambiente aprovado (`00:00:48–00:01:33`). Não copiar URL ou segredo para evidência, texto ou commit.
5. Preparar cenários sintéticos que cubram elegível/não elegível e eventos de negócio distintos, conforme os critérios aprovados. Se não houver regra formal, parar e registrar a lacuna.

## Fluxo B — Validar remessa manual e execução agendada (sandbox/mock)

1. Confirmar na EF o conjunto de parâmetros da tela e da linha de comando. A gravação cita datas inicial/final e nomes ASR incertos; não reutilizar esses literais (`00:05:08–00:07:18`).
2. Executar somente com intervalo sintético pequeno e serviço mock; comparar seleção de operações com a regra funcional aprovada.
3. Testar execução manual e job agendado de forma controlada; validar substituição de cada variável de data, calendário/dias úteis, limites do período e comportamento sem resultados.
4. Verificar logs: início/fim, quantidade selecionada, resposta mock, estado e observação por requisição. Remover identificadores e payloads de qualquer captura.
5. Repetir o mesmo cenário para verificar idempotência e ausência de duplicação. Não chamar endpoint real nem agendar produção.

## Fluxo C — Monitorar e reprocessar erros em sandbox/mock

1. Preparar respostas mock de sucesso, rejeição e falha técnica/timeout.
2. Conferir que a consulta de acompanhamento distingue resultado, erro e observação e mostra somente dados sintéticos (`00:03:23–00:04:17; 00:16:29–00:17:13`).
3. Testar seleção individual e em lote somente com a política de reenvio aprovada. Verificar autorização, trilha de auditoria, contagem e idempotência antes/depois do reprocessamento.
4. Interromper quando o mock não garantir que nenhuma solicitação chegue ao serviço externo real.

## Fluxo D — Relatório

1. Validar com o dono do produto os filtros e colunas esperados; a conversa sugere filtros semelhantes à tela e campos de lote/operação/tipo/valor de seguro/status (`00:04:19–00:04:53; 00:17:27–00:17:53`).
2. Comparar a saída ao conjunto sintético da tela, inclusive período vazio, limites e múltiplos lotes.
3. Confirmar formato, padrão de emissão e permissões com o CDC/SIC; `RPT` e `SIG` não foram resolvidos (`00:07:32–00:07:57; 00:18:57–00:19:11`).

## Bloqueios

- Sem EF/regra aprovada, serviço mock ou fonte de dados definida → não executar.
- Sem confirmação de idempotência e de efeitos do reenvio → não testar lote nem usar dados reais.
- URL/segredo, tabela/campo ou parâmetro ausente → pedir confirmação pelo canal autorizado; não adivinhar.
- Não foi executado SQL, job, plugin, consulta, alteração de configuração, envio ou reenvio nesta etapa.
