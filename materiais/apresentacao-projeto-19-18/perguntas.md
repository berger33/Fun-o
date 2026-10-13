> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste** (não há dado real de cliente ou de pessoa). Preservados
> conforme instrução: o nome **Função Sistemas** e os **nomes dos operadores**. Não são
> publicadas **imagens de pessoas** (câmeras/participantes) — as capturas ficam restritas às
> telas do documento.

# Perguntas e respostas — Apresentação projeto 19-18.mp4


1. **O que o banco pediu neste item? (00:00:19)**
   A criação de **três variáveis** para o documento da CCB de refinanciamento quando há múltiplos
   contratos.

2. **Como os números dos contratos aparecem hoje e como devem aparecer? (00:00:34 – 00:00:56)**
   Hoje aparecem **um abaixo do outro** no agrupamento "contratos/operação"; a variável 1 deve
   exibi-los **na mesma linha, lado a lado, separados por ponto e vírgula**.

3. **Qual é a regra da variável de credor? (00:01:00 – 00:01:37)**
   Hoje o nome do credor se **repete** a cada contrato. Com a nova variável, se for o **mesmo
   credor**, aparece **uma única vez**; se houver credores **diferentes**, todos aparecem,
   separados por ponto e vírgula.

4. **E o saldo devedor? (00:01:37 – 00:01:55)**
   Hoje cada operação exibe o **seu próprio** saldo devedor. Passa a ser a **somatória** dos saldos
   devedores de **todos os contratos** relacionados àquele refinanciamento.

5. **Onde esses dados são gerados, segundo o documento? (leitura de tela, 00:05:03)**
   No módulo **SIC Minutas** do **Autorizador**; o limite de escopo do documento diz que as
   implementações serão disponibilizadas para o módulo **Web Autorizador**.

6. **O que muda no item 2 do escopo? (00:02:09 – 00:02:25)**
   A **API de formalização** deve ser atualizada com as novas variáveis, para que a **jornada de
   contratação** consiga emitir a CCB já com as variáveis atualizadas.

7. **Se duas operações de origem tiverem credores diferentes, como fica a saída? (00:02:36 – 00:03:12)**
   Concatenados como nas operações: os dois credores aparecem, **separados por ponto e vírgula**;
   se forem o mesmo, aparece só uma vez.

8. **A variável consegue dizer a qual operação pertence cada credor? (00:04:00 – 00:04:37)**
   **Não.** Segundo a resposta dada na reunião, a variável **não discrimina a operação**: ela indica
   que, para as operações daquele refinanciamento, existem aqueles credores; não determina qual
   operação é a distinta.

9. **Existe parametrização de credor no sistema? (00:06:00 – 00:06:45)**
   **Não respondido no vídeo.** O encaminhamento foi verificar no **fonte/query** (suspeita de estar
   no convênio) e a hipótese levantada foi a de que **não é parametrização**, e sim informação da
   proposta; ficou combinado enviar depois e alinhar com o desenvolvimento.

10. **Qual é o esforço estimado de desenvolvimento? (00:06:54 – 00:07:32)**
    Item 1 (criação das variáveis): **28 h**; item 2 (API de formalização): **6 h**. As horas foram
    confirmadas como "as mesmas que vocês tinham passado".

11. **E o esforço de CQ e de plano de teste? (00:07:04 – 00:07:32)**
    CQ foi citado como "**21**" no início da confirmação e depois como "**ok para o CQ também**" pelo
    participante E; plano de teste foi citado como "**21, 3 e 16**", **sem** explicar a distribuição —
    registrado como ambiguidade em `incertezas.md`.

12. **Qual é o produto/negócio por trás do item? (leitura de tela, item 1.1 – 1.2)**
    Adequar a exibição de **operações originais** e **saldo devedor** no modelo de **CCB do INSS**
    em **refinanciamento com múltiplos contratos**, evitando a repetição desnecessária de
    informações no documento.

13. **Que evidência visual sustenta a regra de exibição? (00:03:18; 00:05:03; 00:06:18)**
    A **Figura 1** do documento — "Cédula de Crédito bancário INSS refinanciamento – Página 1" — com
    o bloco de contratos/operação/credor/saldo devedor e a indicação da página de reprot. Os valores
    de exemplo foram **omitidos** nesta extração (ver `incertezas.md`, item 3).

14. **O que não ficou claro na reunião? (00:04:37 – 00:05:47; 00:07:32)**
    (a) a distinção/parametrização do credor por operação; (b) a divisão "21, 3 e 16" do plano de
    teste; (c) parte do áudio do intervalo 00:04:37–00:05:47 ficou inaudível por ruído.