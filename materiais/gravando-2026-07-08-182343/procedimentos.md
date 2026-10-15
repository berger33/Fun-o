> **Status:** observações preliminares; não são autorização para alterar ambiente ou dados.

# Procedimentos — Gravando 2026-07-08 182343.mp4

A gravação **não** contém um procedimento técnico reproduzível. Esta página registra o que foi dito e define verificações de segurança que precisam ser atendidas antes de qualquer runbook ser aprovado. Não faça limpeza, cópia, atualização ou importação com base apenas nesta chamada.

## Fluxo A — Preparação de atualização (menção, não liberada para execução)

- **Objetivo aparente:** preparar para teste componentes chamados de WebAutorizador, WS e/ou API **[00:00:23–00:04:27]**.
- **Pré-condições a confirmar com o responsável técnico:**
  1. sistema, ambiente e host autorizados;
  2. pacote, versão e componentes que realmente devem ser atualizados;
  3. procedimento oficial de backup e restauração da configuração;
  4. janela e coordenação com quem mais usa o ambiente;
  5. smoke tests e critério explícito de rollback.
- **Observações da conversa:**
  - há versões locais e compartilhadas e pode ser necessário alinhar qual será testada **[00:00:54–00:01:30]**;
  - WebAutorizador e WS são mencionados juntos em uma situação **[00:02:25–00:02:32]**;
  - a pasta de configuração é descrita como contendo parâmetros de SIC, GDOK e API, e o interlocutor recomenda copiá-la como backup **[00:02:58–00:03:24]**.
- **Bloqueio:** as falas de `00:00:33` (“apagar tudo, menos a config”) e `00:02:34` (“apaga config”) não concordam. **Não executar Ctrl+A, exclusão ou substituição de configuração.** A gravação também não identifica quais arquivos ou serviços compõem uma atualização válida.
- **Resultado:** nenhum resultado de atualização verificável. As telas não demonstram um ciclo completo de implantação e rollback.

## Fluxo B — Importar esteira/teste de tolerância (insuficiente para reprodução)

- **Objetivo aparente:** experimentar importação de um objeto chamado “esteira” e verificar um teste de tolerância **[00:05:26–00:08:03]**.
- **O que a fala permite registrar:** o interlocutor corrige “copiar” para “importar”, faz uma tentativa e pergunta se a operação funcionou **[00:05:48–00:07:20]**.
- **Dados necessários que faltam:** nome do sistema/tela, arquivo de origem, ambiente de destino, significado dos campos e valores, pré-condições e mensagem de sucesso. As referências a valores numéricos em `00:06:27–00:07:33` não têm contexto suficiente.
- **Resultado:** não confirmado. Não trate a tentativa como teste aprovado nem os valores falados como parâmetros.

## Verificações para futura versão aprovada

- Obter um runbook atualizado do responsável e identificar o ambiente pelo mecanismo corporativo autorizado (sem copiar caminhos internos para esta documentação).
- Fazer backup testável antes de qualquer alteração e confirmar como restaurá-lo.
- Registrar versão atual/pretendida e quais componentes (WebAutorizador, WS, API e eventuais integrações) pertencem ao mesmo pacote.
- Não prosseguir com instruções de exclusão enquanto a contradição de configuração não for resolvida.
- Confirmar por evidência não sensível a importação e o resultado do teste de tolerância.

Nenhum SQL foi demonstrado ou executado nesta gravação.
