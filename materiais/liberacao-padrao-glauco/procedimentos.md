> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Glauco, William e equipe CQ 1). Não são publicadas **imagens de
> pessoas** (avatares/câmeras da reunião).

# Procedimentos — Liberação padrão - Glauco.mp4

## Fluxo A — Selecionar e executar cenários de Disponibilização Padrão na planilha `Liberacao_Padrao_V30.xlsx` (00:00:29 – 00:02:47)

- **Artefato de controle:** Planilha **`Liberacao_Padrao_V30.xlsx`**, aba **`Cenários`** (162 registros totais).
- **Objetivo:** determinar exatamente quais processos devem ser testados e evidenciados em uma OS de
  disponibilização/liberação padrão de módulo ou artefato.
- **Pré-condições:**
  - Ter a planilha `Liberacao_Padrao_V30.xlsx` aberta no Excel **[00:00:29 – 00:00:36]**.
  - Conhecer o **artefato** em liberação (ex.: `Web Site .Net`, `Plugin`) e a **situação do módulo no
    cliente** (ex.: cliente ainda não possui o módulo → `Entrega inicial - Completo`, como no caso
    **Portobank** de **William**) **[00:00:50 – 00:02:24]**.
- **Sequência numerada:**
  1. Abrir **`Liberacao_Padrao_V30.xlsx`** e posicionar-se exclusivamente na aba **`Cenários`**,
     ignorando as abas inferiores de cálculo (`Planilha1`, `Planilha2`, `Esforço Padrão`,
     `Esforço Liberações`, `Liberações`) **[00:00:36 – 00:00:49]** (ver
     [`capturas/01-planilha-liberacao-padrao-website-net.png`](capturas/01-planilha-liberacao-padrao-website-net.png)).
  2. Na linha de cabeçalho da tabela (linha `16`), abrir o filtro da coluna **`A` (`Artefato`)** e
     marcar o artefato que está sendo testado (por exemplo, `Web Site .Net` ou `Plugin`)
     **[00:00:50 – 00:01:14]** (ver [`capturas/02-filtro-artefatos-planilha.png`](capturas/02-filtro-artefatos-planilha.png)
     e [`capturas/03-cenarios-plugin-7-registros.png`](capturas/03-cenarios-plugin-7-registros.png)).
  3. Rolar horizontalmente até as colunas **`G` a `J`** (`Entrega inicial - Completo`,
     `Testar se o cliente já tiver o módulo?`, `Fluxo Limpo Versão Padrão`, `Entrega inicial - Reduzido`)
     e filtrar como **`Sim`** a coluna correspondente ao cenário da OS:
     - Se o cliente **não possui o módulo** (ex.: **Portobank — liberação do módulo padrão**), filtrar
       a coluna **`G` (`Entrega inicial - Completo`) = `Sim`** **[00:02:00 – 00:02:28]** (ver
       [`capturas/04-colunas-entrega-inicial-completo-sim.png`](capturas/04-colunas-entrega-inicial-completo-sim.png)).
  4. Executar os processos listados nas linhas resultantes e registrar as evidências cabíveis:
     - No exemplo `Artefato = Plugin` + `Entrega inicial - Completo = Sim` (2 linhas resultantes):
       - **Linha 84 (`Instalação / Evidências`):** demonstrar o plugin aberto/instalado e rodando
         **[00:01:32 – 00:01:40; 00:02:31 – 00:02:33]**.
       - **Linha 86 (`Criação de procedures: .NET - com a opção C, sem erros.`):** executar a criação
         com a opção **`C`** sem erros **e também conferir se a opção `W` existe lá** (pois o texto da
         planilha está desatualizado e cita apenas `C`) **[00:02:33 – 00:02:43]**.
  5. Atualizar a coluna **`C` (`Status`)** (`Pendente`, `And`, `NOK`, `OK`, `Evidenciado`,
     `OK + Evidenciado (Geral)`) para acompanhamento próprio durante o teste (não é necessário enviar a
     planilha ao analista nem publicá-la, salvo solicitação expressa) **[00:00:50 — linha 5 das Orientações gerais]**.
- **Resultado esperado:** todos os processos aplicáveis ao artefato e à modalidade de entrega são
  validados e evidenciados sem executar testes desnecessários (`Não se aplica` / `Não`).
- **Exceções e cuidados:**
  - Diferenciar itens que exigem **evidência** (ex.: plugin instalado e rodando) de itens que são
    apenas **conferência** (ex.: `Lista de plugins conforme planilha disponível nas ocorrências da OS de projeto`)
    **[00:01:42 – 00:01:59]**.
  - Não esquecer de conferir a opção **`W`** além da opção **`C`** na criação de procedures `.NET`
    **[00:02:35 – 00:02:43]**.
  - Caso se depare com um módulo que não tenha processo na planilha, avisar o analista
    **[00:00:50 — linha 6 das Orientações gerais]**.
