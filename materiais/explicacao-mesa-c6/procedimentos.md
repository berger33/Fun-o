> **Plano de trabalho a validar; não é runbook aprovado.** Nenhum procedimento foi executado nem conferido contra o vídeo, a EF ou o ambiente. Em especial, **não executar as instruções conflitantes de exclusão/cópia de pastas**.

# Procedimentos candidatos — explicacao mesa c6.mp4

## Fluxo A — Preparar um item de CQ a partir da EF (relato em 00:05:21–00:07:25, 00:20:36–00:22:47)

1. Confirmar escopo, versão, itens atribuídos, responsáveis e ambiente de teste em fontes oficiais.
2. Ler a EF antes do planejamento e registrar objetivo, comportamento atual, regras, dependências, estados e dúvidas.
3. Alinhar ambiguidades com negócios/desenvolvimento pelo canal institucional; registrar decisão aprovada na especificação. Não abrir/fechar incidente baseado somente em conversa oral.
4. Planejar cenários, critérios e estimativa segundo o processo de CQ vigente; Planner/Gantt/sprint são ferramentas citadas, não configuração confirmada.

## Fluxo B — Elaborar e revisar a EPT (relato em 00:22:51–00:33:10)

1. Usar a EF vigente para decompor cada requisito em preparação, dados fictícios, pré-condições, ações, resultado esperado e critérios verificáveis.
2. Para um parâmetro de recálculo, validar em sandbox os estados e limites especificados (por exemplo, recalculado menor/igual/maior), sem inferir fórmula, nome de parâmetro ou resultado pelo exemplo transcrito.
3. Preparar a planilha/documento usando o template oficial. Se reutilizar um modelo anterior, retirar dados de outro projeto e conferir cabeçalhos/versão antes de salvar como novo.
4. Atualizar EPT e evidências durante a execução; revisão de CQ antes de envio ao banco/cliente conforme o fluxo aprovado.
5. Capturar apenas evidência necessária, com data/hora e conteúdo suficiente para reproduzir o cenário, aplicando política de segurança/privacidade vigente. Nenhuma captura foi gerada nesta análise.

## Fluxo C — Qualquer atualização de ambiente (relato em 00:33:11–00:45:04; bloqueado)

1. **Parar antes de alterar/copiar/excluir.** A gravação alterna entre excluir tudo exceto `config`, copiar arquivos sobre a pasta e nunca excluir `config`; também descreve máquinas/bases distintas.
2. Obter runbook atual aprovado por Infra/desenvolvimento, com host/ambiente exato, versão, arquivos, backup, autorização, janela e rollback.
3. Identificar UDL/base e servidor por inventário oficial, não por rótulo de transcrição. Conferir que ninguém está usando ambiente compartilhado.
4. Executar somente após revisão por segundo responsável; verificar configuração, logs e smoke tests autorizados; documentar resultado e rollback.
5. **Nenhum passo deste fluxo foi executado**; não utilizar a transcrição para modificar `config`, procedures, login, banco ou pasta de servidor.

## Fluxo D — Exercício de treinamento no Autorizador/Test API (relato em 00:46:20–00:57:29)

1. Solicitar usuário de teste e privilégios mínimos com aprovação; não usar `Supervisor` compartilhado se isso conflitar ou exceder o necessário.
2. Em sandbox próprio e com massa sintética, configurar produto/convênio/esteira conforme procedimento vigente e confirmar a associação antes de criar proposta.
3. Seguir a ordem oficial para simulação/inclusão; a fala corrige a própria ordem. Validar o payload e o estado de integração contra EF e ambiente de teste, sem usar valores ou credenciais reais.
4. Se houver outro teste ativo, não copiar/atualizar componentes compartilhados sem coordenação formal; manter ambientes isolados.
5. Registrar evidência sanitizada e revogar acessos temporários. Nenhum teste/chamada/alteração foi realizado neste lote.

## Bloqueios e limites

- Contradição sobre `config`, pastas, versões ou bases → exigir runbook; não improvisar.
- Sem fonte audiovisual, EF e tela não revisadas → termos, nomes de ferramentas e configuração permanecem hipóteses.
- A transcrição não contém consulta SQL literal; nenhuma query deve ser criada a partir da fala sobre tabela/base.
