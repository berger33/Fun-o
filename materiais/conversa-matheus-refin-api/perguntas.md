> **Fonte textual** fornecida pelo responsável em **2026-10-15**; identificadores diretos mascarados.
> Nomes de operadores da Função preservados conforme autorização registrada em
> [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md).

# Perguntas e respostas — refinanciamento pela API (Matheus)

As respostas citam a âncora `[Mnn]` da mensagem em [`transcricao.md`](transcricao.md). Onde a
conclusão é do analista (e não do interlocutor), está marcado **[inferência]**.

1. **Qual dica de método o tester dá para quem vai testar refinanciamento pela API? ([M05], [M06])**
   Simular a mesma proposta **também pelo Autorizador**: “quando vc for fazer uma proposta refin pela
   api, vai simulando tbm pelo autorizador” — ele completa que “ajuda mt”. A simulação serve de
   referência do resultado esperado. **[inferência]** O operador confirma depois que já fez isso
   ([M09]) e que **simula pelo Autorizador sem dificuldade**, o problema está no Test API ([M10]).

2. **O que estava errado no primeiro envio e isso impediu a proposta de entrar? ([M02], [M03])**
   A **matrícula** (ou pelo menos a matrícula enviada no JSON) estava incorreta — mas o tester diz
   “ajeita isso ai, mas **esta dando certo** tranquilo”. Ou seja: a inclusão funcionou apesar do dado
   errado. A correção é necessária pela qualidade do dado, não porque bloqueia o envio.

3. **Erro desse tipo deve virar incidente? ([M04])**
   Não. A reação do tester é explícita: “kkkk nao é incidente”. Dado incorreto em massa de teste é
   ajuste a fazer e seguir. **[inferência]** Abrir incidente por isso gera ruído para o time e
   desgasta o canal de escalada.

4. **Por que o payload reenviado pelo operador não era o mais recente? ([M07])**
   Porque ele **fechou a tela sem salvar** as últimas alterações da simulação; o JSON que tinha em
   mãos era uma cópia anterior, guardada em bloco de notas. A fonte do payload é a tela de simulação —
   o que não foi salvo não existe no payload.

5. **Qual foi o diagnóstico do tester depois de reproduzir o cenário? ([M11]–[M13])**
   Que havia **uma operação já quitada** dentro de uma proposta de refinanciamento: “vi que vc esta
   com uma operação ja quitada em uma proposta refin”. Contrato liquidado não serve como origem do
   refin.

6. **Qual caminho ele indica para investigar as operações do cliente? ([M14], [M15])**
   Rodar um **`select` na tabela que ele chama de “coper”**, filtrando pelo CPF do cliente. A fonte
   **não** informa ambiente, esquema, colunas nem dialeto — ver [`incertezas.md`](incertezas.md)
   itens 1 e 2. **Nenhuma consulta foi executada nesta análise.**

7. **Como saber, na tela de simulação, quais contratos podem ser usados? ([M16], [M17], [M18])**
   A própria tela diferencia: há contratos **“em vermelhinho”** que **não dão para usar**
   ([M16]) — “ai vc nao usa esses” ([M17]) — e a regra final é “usa somente os que dao para marcar”
   ([M18]). O critério operacional, portanto, é: **só entram no cenário os contratos marcáveis**.

8. **O que o campo `SubTipoRefin` recebeu neste envio que funciona? ([M07])**
   O valor literal `"NaoDefinido"`, dentro do bloco `OperacoesRefin`. **[inferência]** Esse valor
   ganha importância cruzado com a outra conversa do acervo, em que `SubTipoRefin` nulo derruba a
   conversão do modelo na API — ver
   [`../conversa-jonas-testa-api/incertezas.md`](../conversa-jonas-testa-api/incertezas.md).

9. **Quantas operações de origem há neste payload e onde elas ficam? ([M07])**
   Uma operação (`NumeroOperacao` `"800033329-7"`), na coleção `OperacoesRefin.OperacoesRefin[]`. É
   uma coleção, portanto aceita mais de um contrato no mesmo refin.

10. **Como o payload diz que a operação é um refinanciamento? ([M07])**
    Pelo discriminante `TipoOperacao` = `"Refinanciamento"`, combinado com o preenchimento do bloco
    `OperacoesRefin` e com `TipoFormalizacao` = `"DIGITAL"`.

11. **Quais blocos do payload ficaram nulos e o que isso significa? ([M07])**
    `CondicaoRefinanciamentoConjunto`, `LiberacoesAdicionais`, `OperacoesPortabilidade`,
    `ReaproveitamentoSeguro`, `Garantias` e `Despesas` foram enviados como `null`. São blocos
    existentes no contrato, não usados neste cenário; **[inferência]** não devem ser confundidos com
    campos inexistentes — o bloco `ReaproveitamentoSeguro` é funcionalidade monitorada em outras
    fontes do acervo.

12. **Qual é a condição de crédito registrada e o que ela ensina sobre o formato? ([M07])**
    36 parcelas, `ValorParcela` 125,71 com `MetaCalculo` = `"ValorParcela"`, datas de primeiro e
    último vencimento (`07/09/2027` / `07/08/2030`) no formato `dd/MM/aaaa`, `TaxaCETAM` 2,73 e
    `TaxaCLAM` 1,7. **[inferência]** São valores de **uma tentativa de teste**: servem para
    reconhecer o formato do payload, não como regra de negócio.

13. **Que dado do cadastro profissional é crítico neste teste? ([M02], [M07])**
    `DadoCadastral.DadoProfissional.NumeroMatricula` — foi exatamente o campo apontado como
    incorreto. O mesmo sub-bloco traz `EmpresaCNPJ`, `Profissao`, `Cargo` e `DataAdmissao`.

14. **O que se aprende com a menção a um contrato/anexo em `[M01]`? ([M01])**
    Que o tester já tinha em mãos o material do cenário enviado antes do recorte e **reproduziu a
    simulação por conta própria** antes de responder. **[inferência]** Reproduzir o cenário é o que
    transforma “não sei o que está errado” em diagnóstico — é o mesmo padrão de trabalho da conversa
    com Jonas (tester tenta reproduzir antes de classificar como incidente).

15. **A conversa termina com o cenário resolvido? ([M22])**
    Não. Termina com o operador dizendo “vou tentar fazer isso”. Não há confirmação de sucesso no
    recorte — por isso o estado do material é `em revisão` e não `concluído`.
