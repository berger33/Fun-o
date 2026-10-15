# Perguntas e respostas — Gravando 2026-10-06 110907.mp4

1. **Qual é o objetivo geral descrito? (`00:00:22–00:00:45`)**
   Uma integração com serviço externo para encaminhar solicitações de cancelamento de seguro associadas a operações elegíveis. A regra de negócio e o contrato externo não estão validados.

2. **Quais entregas são separadas na conversa? (`00:01:34–00:03:34`)**
   Configuração de regras (item 1.1), remessa/plugin e linha de comando (1.2), consulta de situação/relatório (1.3), segundo a fala. Confirmar a estrutura na EF.

3. **Que dimensões aparecem na configuração de regras? (`00:10:47–00:11:24`)**
   Grupo, produto, tipo de operação, histórico financeiro e motivo da chamada. Nomes de campos, obrigatoriedade e combinações não foram confirmados.

4. **Qual é o papel do motivo/`reason`? (`00:11:00–00:11:10`)**
   Texto que seguiria com a solicitação para explicar a razão do cancelamento; domínio e valores aceitos dependem da especificação do serviço externo.

5. **Como a remessa seria iniciada? (`00:01:41–00:02:25`)**
   A fala descreve uma tela com período que aciona um plugin e apresenta logs. Não há execução real demonstrada.

6. **O que se diz sobre a linha de comando e o SIC? (`00:02:47–00:03:23; 00:05:26–00:06:29`)**
   A linha de comando teria função equivalente à remessa, com possibilidade de agendamento como job no SIC e parâmetros variáveis. Sintaxe e implementação precisam ser confirmadas.

7. **Quais datas deveriam ser consideradas no teste? (`00:06:35–00:07:18`)**
   A fala cita data do sistema e dias úteis anterior/próximo, mas não fornece um catálogo confiável. Testar somente parâmetros e calendário especificados na EF.

8. **Quais operações seriam candidatas ao envio? (`00:10:22–00:11:24`)**
   A explicação menciona operações liquidadas com despesa de seguro e regra associada a histórico financeiro; eventos exatos e elegibilidade estão pendentes.

9. **A conversa define quais eventos cancelam o seguro? (`00:11:38–00:12:15; 00:15:37–00:15:55`)**
   Não. Liquidação, estorno e cancelamento são citados, mas a própria pessoa hesita e afirma não ter lido o projeto.

10. **A tabela/campo da despesa de seguro foi identificado? (`00:14:02–00:15:21`)**
    Não. A fala descarta nomes candidatos e pede confirmação com o CDC. Não há tabela nem consulta aprovada.

11. **O que deve aparecer na tela de acompanhamento? (`00:03:23–00:04:17; 00:16:29–00:17:13`)**
    Conforme a descrição verbal, operações/solicitações, estado, observação/erro e possibilidade de reenvio individual ou em lote. Campos e permissões são desconhecidos.

12. **O reenvio em lote pode ser tratado como operação segura? (`00:04:06–00:04:17`)**
    Não sem controle. É apenas comportamento citado; validar autorização, idempotência, trilha e duplicação em sandbox com serviço mock antes de qualquer uso real.

13. **O relatório tem formato definido? (`00:07:32–00:07:57; 00:18:57–00:19:11`)**
    Não. `RPT` e `SIG` aparecem de forma contraditória/incompleta. O padrão deve ser confirmado na EF e com a equipe do CDC.

14. **Há SQL reproduzido? (`00:12:34–00:12:58; 00:14:02–00:15:21`)**
    Não. Há uma menção a `SELECT` e nomes de tabela/campo incertos; nenhuma query literal foi transcrita ou executada.

15. **O trabalho estava iniciado e aprovado na data da reunião? (`00:09:15–00:09:47; 00:19:51–00:20:09`)**
    A fala diz que havia decisões/comitê e alinhamento pendentes. É um registro histórico, não estado atual do projeto.

16. **O fluxo é do Autorizador? (`00:09:57–00:10:16; 00:22:27–00:22:44`)**
    A conversa o caracteriza como separado e ligado ao CDC; confirmar siglas, arquitetura e fronteira de sistemas na especificação vigente.

17. **A gravação mostra uma tela funcional ou teste? (`00:00:27–00:00:45; 00:19:42–00:20:09`)**
    O ASR descreve uma apresentação de especificação/tela compartilhada, mas nenhuma tela foi revisada neste lote e nenhum teste foi comprovado.

18. **Como a análise tratou a referência a outro sistema e o final? (`00:18:23–00:18:27; 00:23:04.06–00:23:47.48`)**
    O nome de referência foi substituído por marcador e a conversa paralela sobre incidente foi omitida para não publicar informação alheia ao escopo.
