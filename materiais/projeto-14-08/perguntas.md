> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Zé, Priscilla/Pri, Augusto, Gabriel). Não são publicadas **imagens
> de pessoas** (avatares/câmeras da reunião).

# Perguntas e respostas — PROJETO 14-08.mp4

1. **Qual é o novo campo do item 1 e o que ele carrega?** — O campo **`CRN`** (*Company
   Registration Number*), com o **CNPJ — Cadastro Nacional da Pessoa Jurídica — do empregador**,
   incluído no plugin de envio da proposta ao sistema externo para a formalização digital
   (00:00:00–00:00:46; captura em 00:02:00).
2. **Em qual plugin/módulo o campo do item 1 entra?** — No módulo **ServCom**, plugin **Envio
   da Proposta ao Sistema Externo** (00:00:03–00:00:12).
3. **De onde vem o CNPJ do empregador?** — Da **consulta de margem**, com base na **`origem 4`
   da proposta**, a partir de um campo do bloco **`ETRACPD`** (00:00:47–00:01:12).
4. **Qual ponto do item 1 ficou em aberto?** — Qual é o **campo exato `ETRACPD.*`** que guarda
   o CNPJ: precisa ser identificado (inclusive "colocando no select") e registrado na última
   coluna da EF (00:01:27–00:02:12).
5. **Quem resolve o ponto em aberto e como a EF é atualizada?** — **Zé** verifica (com o negócio
   e, se preciso, com alguém do empregador) e devolve o nome; a equipe preenche
   `ETRACPD.<nome do campo>` na EF (00:02:40–00:03:00).
6. **O cadastro da proposta passa a usar o CNPJ em vez do CPF do cliente?** — Não: a proposta
   **continua cadastrada com o CPF normal do cliente**; o CNPJ incluído é o **do empregador**
   (00:03:05–00:03:20).
7. **Qual é o item 2 e qual o seu objetivo?** — A **OS 556576** ("Gravação do ID da simulação
   na consulta do pro rata"): compor, no envio ao sistema externo, a informação da **simulação
   do reaproveitamento** disponível na tabela de consultas de reaproveitamento
   (00:05:28–00:06:02; captura em 00:06:00).
8. **O que é o campo `simulation_id`?** — O **identificador da simulação retornado pelo plugin
   `Integração para Consulta De Reaproveitamento de Seguro`** (tela em 00:06:00; fala em
   00:05:56–00:06:16).
9. **Para que serve o JSON completo que está na EF?** — É o **exemplo** do que o parceiro
   envia; o campo novo a ser tratado é **só o `simulation_id`** (00:06:16–00:07:24).
10. **O que acontece quando não é reaproveitamento?** — O `simulation_id` **vem vazio e é
    enviado vazio**: repassa-se exatamente o que veio (00:07:53–00:08:20).
11. **Por que a implementação do item 2 é considerada simples?** — Porque o campo **já é
    retornado** hoje; basta **levantá-lo no build do plugin e passá-lo para frente**
    (00:08:33–00:08:44).
12. **Quais foram os combinados finais da reunião?** — **Zé** envia o **Gantt dos dois
    projetos** na segunda-feira, em Gantt separado do **pacote 4**, avisa a equipe para
    registrar no mapa e lembra o **Gabriel** de lançar as horas dele (00:08:47–00:09:21).
