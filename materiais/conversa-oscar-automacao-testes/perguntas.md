> **Fonte textual** fornecida pelo responsável em **2026-10-15**; sem identificadores diretos.

# Perguntas e respostas — automação de testes e trilha de estudo (Oscar)

Respostas ancoradas em [`transcricao.md`](transcricao.md); conclusões do analista estão marcadas
**[inferência]**. **A autoria das falas não é confiável** no recorte — as respostas tratam as falas
como posições do diálogo, não de pessoas (ver [`incertezas.md`](incertezas.md) item 1).

1. **Qual autocrítica sobre estudo abre a conversa? ([M01], [M02])**
   “acabo estudando muito pouco código e mais automação, aplicações, coisas de ia” — e a menção a
   “pessoas que usem essas ferramentas”. **[inferência]** O interlocutor percebe um desequilíbrio entre
   estudar **código** e estudar **automação/IA/aplicações**.

2. **Qual é o contraponto apresentado em seguida? ([M05], [M08])**
   “mas ao mesmo tempo gente que entende regra de negócio”, com a confirmação de que “isso vai ser cada
   vez mais necessário”. O valor está em quem **entende o negócio**, não só em quem opera ferramenta.

3. **Qual proposta concreta de melhoria para a Função aparece? ([M09], [M10])**
   Trazer o **Cypress** para a Função e ver “se funciona pra agilizar alguns testes padrão — tipo api e
   etc”. É uma **proposta de PoC**, não uma prática existente.

4. **Qual stack foi informada para essa proposta? ([M12])**
   **JavaScript**.

5. **Qual é o nível de experiência do interlocutor com a ferramenta? ([M11])**
   Nenhum: “bacana, ainda não tive contato com o Cypress”. **[inferência]** Isso define o esforço da
   PoC — inclui aprendizagem, não apenas instalação.

6. **Por que “testes padrão de API” é um bom primeiro alvo? ([M09], [M10] + acervo)**
   Porque o acervo já tem **cenários de API documentados** (inclusão de proposta de refin, mensagens de
   erro de modelo, massa de teste) — material pronto para virar caso automatizado. **[inferência]** É o
   tipo de teste com resultado esperado claro e pouco dependente de tela.

7. **O que a conversa diz sobre PSA? ([M20], [M21], [M23]–[M26])**
   Que há dificuldade em achar **uma configuração** no PSA (“ta um porre”), com demanda **urgente**, e
   que o interlocutor pergunta se o outro “já pegou psa” — a resposta é “nunca”. PSA e PEGEUT aparecem
   juntos, e o problema é descrito como “chato pra algumas config”.

8. **O que sabemos sobre PSA/PEGEUT depois desta conversa? ([M25], [M26])**
   Apenas que: (a) existem; (b) envolvem **configuração**; (c) dão trabalho. **Não** há definição,
   módulo, tela, parâmetro ou procedimento. A fonte é insuficiente para qualquer uso operacional.

9. **Como a configuração de PSA chegou a esse interlocutor? ([M21])**
   Por **assunção da pauta de um colega** (“assumi a pauta de colega”). **[inferência]** Isso explica a
   urgência e a falta de familiaridade: assumir pauta não garante transferência de conhecimento.

10. **O que fazer quando ninguém do diálogo tem a experiência necessária? ([M22], [M24])**
    A resposta registrada é “vou dar um salve por aqui” — **procurar quem sabe** em outro canal.
    **[inferência]** É o mesmo padrão da conversa com Cler: escalar a pergunta a quem conhece o sistema,
    em vez de adivinhar configuração.

11. **Que princípio de ordem de aprendizado a conversa sustenta? ([M05], [M08] + [M09])**
    Primeiro **regra de negócio** e **processo**; depois ferramenta. Automatizar sem entender o processo
    produz teste que passa com o sistema errado. Este mesmo princípio aparece na conversa com Gabriel
    (automatizar/gerar EPTs com IA exige compreender bem os processos).

12. **Qual é a única menção a ferramenta de assistente? ([M18])**
    “As conexões que o arena oferece se vc ficar atualizando kkkk” — uso de assistente **com conectores**
    já presente na rotina. **[inferência]** Registro de método (inventário de ferramentas), sem
    conteúdo técnico sobre a Função.

13. **Como tratar a menção à faculdade? ([M06], [M07])**
    Como **contexto pessoal de formação** (“amanha tem prova da faculdade”, “desenvolvimento de
    sistemas”), sem qualquer relação com processo da empresa. Mantido na transcrição para preservar a
    ordem da conversa; não gera procedimento.

14. **A PoC com Cypress pode ser considerada aprovada? ([M09]–[M12])**
    Não. A fala é “quero passar um Cypress aqui na função **pra ver se funciona**” — intenção de
    experimentar. Não há aprovação, escopo, ambiente, prazo ou responsável na fonte. O material
    registra como **proposta** e o estado do pacote é `em revisão`.
