# Incertezas e limitações — ClientSecret EWEN TREINAMENTO.mp4

1. **Fonte primária:** o MP4 não foi baixado nem revisto auditiva/visualmente neste lote. Não confirmar nomes de telas, valores, resultado, segredo visível ou configuração a partir do ASR.
2. **Qualidade/cobertura:** saída `large-v3` sem VAD, 649 segmentos. Há pausas, conversa paralela e trechos de baixa inteligibilidade; o JSON registra `duracao_transcricao_s: 1799.9` sem definir o que mede. Não inferir que intervalos sem cue sejam silêncio.
3. **Termo do segredo:** o ASR alterna `Client Secret`, `CloudSecret` e `Cloud Secret`; o significado, escopo e relação entre esses nomes não foram confirmados.
4. **Credencial:** o texto descreve geração de um segredo que seria exibido uma única vez, mas não apresenta valor literal reconhecível de token/segredo, URL ou payload completo. Isso não prova o que aparece nas telas do vídeo, que não foi revisado. Não inserir nenhum segredo em derivado público, evidência, chat ou Git.
5. **Expiração e privilégio:** a fala sugere prazo “bem longo” e perfil `Supervisor`; não há política de segurança, justificativa ou autorização demonstrada. Não são recomendações aprovadas. Usar menor privilégio, vida útil mínima e rotação conforme padrão vigente.
6. **Client ID:** aparecem dois números reconhecidos de forma diferente em `00:15:09` e `00:21:12`; não selecionar nem publicar como configuração correta. O valor não foi verificado na tela.
7. **Aplicação/ambiente:** `Test API`, `WPWebService`, `Simula proposta`, `Sensei`, `ORECA` e nomes afins podem conter erro de ASR ou ser específicos de uma versão; URL/ambiente não foram identificados.
8. **Licença:** versões e números são corrigidos pelo próprio interlocutor durante a fala; instalação, assinatura, origem, método/API liberados, código de ativação e “contrassenha” não foram verificados.
9. **Permissões:** sequência para manter/remover licença e atribuir direitos por rotina foi explicada verbalmente, inclusive correção de um erro anterior; matriz, aprovação e opções `A`/`M` não foram confirmadas.
10. **CTC/CIP:** apenas fluxo em alto nível; o instrutor diz que testou pouco e que tentaria demonstrar depois. Não é descrição suficiente de integração.
11. **Conteúdo pessoal:** a transcrição integral contém conversa incidental sobre idade, trajetória de trabalho e autodeclaração de saúde. Mantida sem corte/mascaramento por instrução expressa do responsável, que declarou os dados fictícios/de teste. Isso permanece uma declaração de origem, não uma verificação independente; o repositório continua público até sua exclusão.
12. **Privacidade técnica do ASR:** varredura automatizada do TXT/SRT/VTT não encontrou URL, e-mail, padrão de CPF/CNPJ ou sequências alfanuméricas longas semelhantes a token. A varredura não valida imagens/áudio e não substitui revisão de segurança.
13. **SQL:** “SQL Result” é mencionado, mas nenhuma consulta/comando é reproduzido. Nenhum SQL foi executado neste lote.
14. **Validação:** nenhum teste de API/CTC, geração de credencial, instalação de licença, chamada externa, alteração de perfil ou captura foi realizado/confirmado nesta análise.

**Ação necessária:** confrontar com a fonte audiovisual e confirmar os procedimentos com Segurança/Infra e documentação oficial antes de qualquer uso. Ver [`perguntas.md`](perguntas.md) e [`procedimentos.md`](procedimentos.md).
