# Perguntas e respostas — MICHELLE CTC PORTABILIDADE REFIN.mp4

1. **Qual é o assunto geral da gravação? (00:00:05–00:01:22)**
   Uma explicação, sobre um fluxograma compartilhado, de como as esteiras de **portabilidade** e de **refim** se coordenam — seguida do desenho de um teste para verificar se a portabilidade pode avançar sem depender do refim.

2. **O fluxograma exibido é a esteira do C6? (00:00:05–00:00:23; 00:15:34–00:16:07)**
   Não. A apresentadora diz duas vezes que o desenho foi feito para **outro cliente**, “não é exatamente do C6”, e serve só como exemplo do mecanismo. Não copie a configuração dele para o cliente-alvo.

3. **Que processos antecedem a pergunta “Tem Refin Vinculado?” no desenho? (00:00:36–00:01:00)**
   Na faixa da portabilidade: `Envio/Aguarda Retorno da Núclea` → `CTC – Atualizar Proposta com NU da Portabilidade` → `CTC - Verificação de Alteração de Saldo e Prazo` (que, havendo divergência, direciona a `Pendente` e ao `Recálculo de PMT e Prazo da Portabilidade`) → losango `Tem Refin Vinculado?`.

4. **O que acontece se não houver refim vinculado? (00:01:00)**
   Segundo a nuvem do próprio desenho, “a proposta seguirá o fluxo de uma portabilidade "pura"” (captura 01).

5. **Qual é o nome exato do processo de acionamento lido na tela — e o que ele faz? (00:01:11–00:02:30)**
   `CTC – Aciona Esteira de Refinanciamento`, mnemônico `CTCACIPROPREF`. É um processo **sem tela** que verifica a **última** proposta de portabilidade vinculada: só quando ela passa é que o acionamento da proposta de refinanciamento é realizado.

6. **Que cuidado a anotação do desenho registra para esse acionamento? (00:02:00–00:02:30)**
   O parâmetro de rotina `G_AVERERR` “deve estar desligado, a fim de não validar a averbação no momento de andar a esteira de refim”. A fala reforça que o refim não pode estar averbado nesse momento.

7. **E se houver várias portabilidades para o mesmo refinanciamento? (00:02:00–00:02:30)**
   Todas precisam ter passado pelo processo de acionamento para o refim andar — é a regra da “última proposta” descrita na nuvem e na fala.

8. **Qual é o nome exato do processo de espera da portabilidade no desenho — e o que ele faz? (00:03:02–00:03:36)**
   `CTC – Aguarda Analise do Refin de Portabilidade`, mnemônico `CTCAGANREFIN`. Processo sem tela que “permite o bloqueio da proposta de portabilidade de acordo com a situação da proposta de refinanciamento vinculada a ela”.

9. **Por que, no mecanismo descrito, a portabilidade espera o refim? (00:03:36–00:04:59)**
   Para garantir a consistência dos valores antes de gerar/avançar a **CCB**: se a portabilidade andasse antes da validação do refim (saldo retornado da CIP/Núclea), “a CCB saiu com valores diferentes”.

10. **O que é a “tela unificada” e onde ela entra na conversa? (00:02:40–00:03:15)**
    É a tela do C6 que, segundo a fala, faz **refim e portabilidade juntos**. O problema discutido é que, nesse caminho, as duas propostas teriam de parar num processo de espera (“aguarda alteração unificada”, na fala) para entrarem juntas na atividade seguinte. Nenhuma caixa com esse nome aparece legível no desenho exibido.

11. **O processo de acionamento também “segura” a proposta? (00:05:31–00:06:00)**
    Não, segundo o esclarecimento atribuído ao Zé: ele **só aciona, não valida**; quem segura é a **próxima etapa configurada** na esteira. Daí a hipótese de que bastaria configurar a etapa seguinte (“verdadeira”) como o processo de aguardo desejado.

12. **O que o banco/cliente quer, afinal? (00:05:09–00:08:19)**
    Que as propostas da tela unificada e da tela de cadastro caiam no **mesmo** processo de espera e que, depois do acionamento, a portabilidade **continue andando sem dependência** do refim. O cliente relatou não conseguir; a hipótese da reunião é erro de configuração — nada disso é demonstrado.

13. **Como nasce o cenário de duas propostas usado no teste? (00:12:48–00:13:18)**
    Na tela de cadastro normal: grava-se a portabilidade, um **pop-up** pergunta se quer fazer o refinanciamento da proposta, grava-se o refim e, ao final, o sistema mostra **dois números de proposta** (portabilidade e refim).

14. **Por que o teste precisa de duas esteiras (e dois convênios/produtos)? (00:10:34–00:11:57)**
    Para isolar o comportamento de cada tipo de proposta; a equipe declara não ter esteiras separadas por tipo (“a gente costuma usar uma pra todos os tipos de propostas”), então o isolamento seria obtido com convênio/produto diferentes para portabilidade e refim.

15. **Onde as propostas devem parar no teste — e o que é pulado? (00:06:39–00:07:47; 00:09:23–00:09:50)**
    As duas andam até a **análise de crédito**; o refim fica parado nela. Na portabilidade, pulam-se os processos de CTC (atualização/envio) — porque a equipe não consegue exercitar o CTC naquele ambiente — e coloca-se o processo de acionamento seguido da etapa de aguardo em discussão. Isso é limitação do ambiente de teste, não autorização para contornar o CTC fora de sandbox.

16. **O teste foi executado ou alguma tela de sistema foi demonstrada? (00:00:00–00:16:50)**
    Não. A tela compartilhada é o fluxograma o tempo todo; o teste é apenas combinado (Santana executa depois, com William acompanhando) e nenhum resultado é mostrado.

17. **Há SQL nesta gravação? (00:00:00–00:16:56)**
    Não — nenhum comando, consulta, tabela ou dialeto é demonstrado ou ditado.

18. **A regra “portabilidade espera o refim integrado” ficou confirmada? (00:03:15–00:04:59; 00:07:50–00:08:29)**
    Não. A mesma conversa apresenta a espera (status “integrada”, apenas falado) e o desejo oposto de avançar sem dependência. É uma decisão de negócio pendente — ver [`incertezas.md`](incertezas.md) §2.
