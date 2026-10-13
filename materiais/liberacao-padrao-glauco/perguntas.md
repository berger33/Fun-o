> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Glauco, William e equipe CQ 1). Não são publicadas **imagens de
> pessoas** (avatares/câmeras da reunião).

# Perguntas e respostas — Liberação padrão - Glauco.mp4

1. **Qual é a finalidade da planilha `Liberacao_Padrao_V30.xlsx` apresentada por Glauco? (00:00:29 – 00:01:26)**
   Orientar os testes de **disponibilização / liberação padrão**, listando na aba **`Cenários`** todos
   os processos que devem ser testados e evidenciados conforme o artefato e a modalidade de entrega
   (**[00:00:36 – 00:01:26]**).

2. **Por que o testador deve ignorar as abas `Planilha1`, `Planilha2`, `Esforço Padrão`, `Esforço Liberações` e `Liberações`? (00:00:41 – 00:00:49)**
   Porque são abas auxiliares de cálculo; o trabalho operacional de filtro e execução dos cenários é
   feito somente na aba **`Cenários`** (**[00:00:41 – 00:00:49]**).

3. **Como o testador filtra os processos correspondentes ao componente que está validando? (00:00:50 – 00:01:14)**
   Filtrando a coluna **`A` (`Artefato`)** da aba `Cenários` pelo tipo de componente em teste, como
   `Web Site .Net` ou `Plugin` (**[00:00:53 – 00:01:13]**).

4. **Qual é a diferença explicada por Glauco entre itens que exigem evidência e itens de simples conferência? (00:01:28 – 00:01:59)**
   Em itens como a instalação de um `Plugin`, é preciso registrar evidência mostrando-o instalado e
   rodando; já em itens como `Lista de plugins conforme planilha disponível`, trata-se apenas de uma
   conferência para verificar se está tudo ok, sem necessidade de anexar evidência (**[00:01:32 – 00:01:59]**).

5. **Quais são as quatro colunas de modalidade/contexto de entrega existentes à direita da planilha (colunas `G` a `J`)? (00:02:00 – 00:02:28)**
   `Entrega inicial - Completo` (coluna `G`), `Testar se o cliente já tiver o módulo?` (coluna `H`),
   `Fluxo Limpo Versão Padrão` (coluna `I`) e `Entrega inicial - Reduzido` (coluna `J`)
   (**[00:02:00 – 00:02:28]**, [`capturas/04-colunas-entrega-inicial-completo-sim.png`](capturas/04-colunas-entrega-inicial-completo-sim.png)).

6. **Qual era o cliente e o cenário específico da tarefa atribuída a William? (00:02:10 – 00:02:28)**
   Cliente **Portobank**, **liberação do módulo padrão**; como o cliente ainda não tinha o módulo, o
   cenário aplicável era **`Entrega inicial - Completo` = `Sim`** (**[00:02:10 – 00:02:28]**).

7. **Quais processos restaram na planilha ao filtrar `Artefato = Plugin` e `Entrega inicial - Completo = Sim`? (00:02:25 – 00:02:35)**
   Apenas 2 de 162 registros: linha **`84`** (`Instalação / Evidências`, `0:06:00`) e linha **`86`**
   (`Criação de procedures: .NET - com a opção C, sem erros.`, `0:08:00`) (**[00:02:29 – 00:02:35]**).

8. **Qual alerta de desatualização da planilha Glauco faz sobre a linha 86 (`Criação de procedures: .NET - com a opção C, sem erros.`)? (00:02:35 – 00:02:43)**
   Ele avisa que esse item está **desatualizado** na planilha: além da criação com a opção **`C`**, é
   necessário também fazer/conferir se a opção **`W`** existe lá para garantir que está tudo certo
   (**[00:02:35 – 00:02:43]**).

9. **A planilha preenchida com a coluna `Status` precisa ser enviada ao analista ou publicada? (00:00:50)**
   Não; conforme as **Orientações gerais** (linha 5 da planilha), a coluna `Status` serve apenas para
   facilitar o uso pelo testador e não precisa ser enviada ao analista nem publicada, a menos que o
   analista peça (**[00:00:50]**).

10. **Quais tabelas e utilitários são mencionados nos processos de `Web Site .Net` e `Plugin` visíveis na planilha? (00:00:50 – 00:01:40)**
    A tabela **`TPARWFIUTIL`** (campo **`PWALIAS`**) com regularização de estrutura via **`WFIUTIL`**,
    e a tabela **`TRTHB`** (exclusão dos registros referentes ao site atual antes do cadastro de
    rotinas via **`FI.SQLResutil`** ou menu `Serviços`, conferindo depois no **`WebAcesso`**)
    (**[00:00:50 – 00:01:40]**).
