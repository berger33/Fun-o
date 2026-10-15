# Perguntas e respostas — MCB - QISTA.mp4

1. **Qual é o assunto principal da conversa? (00:00:28–00:01:24)**

   Como o Autorizador poderia consultar, pelo MCB, a certificação/situação de um agente durante o fluxo de uma proposta, além de dúvidas de cadastro e teste.

2. **Como a gravação descreve a certificação e a pontuação dos agentes? (00:00:00–00:00:28)**

   Diz que há certificação na Núclea e uma pontuação comparada a uma carteira de motorista, com um limite máximo citado como 20 e possíveis suspensões temporárias ou definitivas. Esses critérios não foram verificados e não devem ser tratados como regra oficial.

3. **O que o Autorizador faria ao processar uma proposta com agente? (00:00:33–00:01:13)**

   A fala descreve consultar o MCB via API e receber uma situação/pontuação para decidir se a proposta pode continuar. Não são mostrados payload, status técnicos nem tratamento de falha.

4. **O que aciona a consulta na esteira, segundo a conversa? (00:01:13–00:01:24)**

   Uma atividade configurada no fluxo. O nome e o identificador dessa atividade não foram registrados.

5. **Que vínculo de configuração é mencionado no MCB? (00:02:22–00:02:52)**

   A fala diz que o módulo precisa associar a esteira e a atividade correspondentes para que a configuração que chega do Autorizador coincida. O desenho real da configuração não foi conferido.

6. **Que componentes são citados para integrar o MCB? (00:02:04–00:02:19; 00:10:02–00:10:42)**

   MCB, uma API de consulta de pontuação e configurações no Autorizador. A gravação não fornece uma sequência completa, endpoint ou parâmetros aprovados.

7. **Qual distinção de promotora é usada como hipótese de teste? (00:07:27–00:09:01)**

   Interna versus externa. A conversa sugere que o comportamento de validação do agente pode variar conforme a classificação; a regra precisa de confirmação.

8. **Onde a consulta de promotora é indicada verbalmente? (00:04:22–00:05:59; 00:06:25–00:07:59)**

   No WebTabelas, em cadastro de promotora; a pessoa diz que em alguns ambientes ela pode aparecer como uma origem. A navegação e os rótulos não foram inspecionados visualmente.

9. **A gravação afirma que existe sempre uma tabela chamada “promotora”? (00:05:37–00:05:59)**

   Não. A fala diz que promotoras são representadas por origens, mas os termos reconhecidos como “TEORGS” e os códigos de origem precisam de conferência.

10. **A falta de formas de liberação é atribuída a quê na conversa? (00:03:54–00:04:20; 00:06:03–00:06:21)**

    A apresentadora atribui a um erro na base/tabela chamada aproximadamente “T-Lib/Telib”, não à aplicação, a partir de sua base local. Isso não comprova a causa em outros ambientes nem constitui orientação para corrigir a base.

11. **O que a conversa diz sobre `INSERT`/`UPDATE`? (00:02:54–00:03:09)**

    Apenas pergunta se a pessoa teria permissão para alterações de base. Não há SQL, alvo, autorização ou validação; nenhum comando foi executado.

12. **O que foi dito sobre os códigos associados a QISTA/MCB? (00:09:09–00:10:18)**

    O ASR registra os valores candidatos `190` e `061` como códigos de módulo/sistema. Eles precisam de confirmação na fonte/documentação e não são orientação de configuração.

13. **Como a conversa aborda o erro “produto não encontrado”? (00:14:29–00:15:24)**

    Pede dados das origens (promotora, órgão, empregador) para investigar e menciona três tabelas correlacionadas, sem nomeá-las ou explicar sua regra.

14. **Qual é a proposta de teste para promotora externa? (00:08:40–00:09:01)**

    A hipótese falada é que a validação consulte o agente e apresente pontuação/situação durante a esteira. Falta definir status esperados, transições e evidências.

15. **A conversa demonstra um procedimento completo de publicação/implantação? (00:09:09–00:12:08; 00:13:49–00:14:37)**

    Não. Descreve problemas e contexto de versão local, UDL e publicação de componentes sem valores, dependências aprovadas, rollback ou confirmação de sucesso.

16. **O que é seguro concluir sobre o teste e o banco? (00:02:54–00:03:09; 00:14:29–00:15:24)**

    Apenas que há cenários de validação e uma investigação de cadastro a planejar. Não executar alteração de dados; primeiro confirmar regra, ambiente, especificação e procedimento aprovado.
