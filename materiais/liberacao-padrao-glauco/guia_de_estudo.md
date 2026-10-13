> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Glauco, William e equipe CQ 1). Não são publicadas **imagens de
> pessoas** (avatares/câmeras da reunião).

# Guia de estudo — Liberação padrão - Glauco.mp4

- **Categoria:** `PROCESSOS`, `SISTEMAS`, `NEGOCIO`, `SQL`, `DÚVIDA_OU_CONFLITO`
- **Sistema:** Planilha **`Liberacao_Padrao_V30.xlsx`** (artefatos **`Web Site .Net`**, **`Plugin`**, **`WFIUTIL`**, **`FI.SQLResutil`**, **`WebAcesso`** e tabelas **`TPARWFIUTIL`** / **`TRTHB`**)
- **Assunto:** execução e evidenciação de testes de **disponibilização / liberação padrão** pela aba `Cenários` da planilha `Liberacao_Padrao_V30.xlsx`, com exemplo prático para **Portobank** (`Plugin` em `Entrega inicial - Completo`) e ressalva sobre procedures `.NET` com opção `C` e conferência da opção `W`
- **Fonte:** `Liberação padrão - Glauco.mp4` (181378373 bytes), gravação de 2026-05-06 ~10:03 (BRT), duração 00:05:16.50 — SHA-256 `067265c5…`
- **Confiança da extração:** **alta** — áudio de Glauco e William claro e planilha `Liberacao_Padrao_V30.xlsx` legível em 1366×768.

## 1. Objetivo e público

- **Objetivo do vídeo:** instruir a equipe `CQ 1` (e especificamente **William**) sobre como utilizar
  a planilha **`Liberacao_Padrao_V30.xlsx`** para conduzir testes de **disponibilização padrão**
  (demanda que antes ficava com a frente citada como "Galo" e passou a ser atendida pela equipe),
  filtrando o **Artefato** e a **modalidade de entrega** para saber exatamente o que testar e
  evidenciar.
- **Público/pré-requisitos:** testadores de CQ da **Função Sistemas** encarregados de validar pacotes
  de disponibilização padrão de módulos/plugins para clientes (como **Portobank**).

## 2. Estrutura e regras de uso da planilha `Liberacao_Padrao_V30.xlsx` (00:00:29 – 00:01:27)

1. **Usar exclusivamente a aba `Cenários` (00:00:41 – 00:00:49):**
   - As demais abas da pasta de trabalho (`Planilha1`, `Planilha2`, `Esforço Padrão`, `Esforço Liberações`,
     `Liberações`) são abas auxiliares de cálculo e devem ser ignoradas pelo testador.
2. **Orientações gerais registradas no cabeçalho da aba `Cenários` (linhas 1–6):**
   - A planilha contempla todos os processos que devem ser realizados durante testes de
     disponibilização padrão.
   - As colunas **`G`** e **`H`** são preenchidas pelo analista; o testador deve validar somente o que
     estiver marcado como **`"Sim"`** (ou filtrar a coluna correspondente à modalidade da entrega).
   - A coluna **`Status`** (`Não se aplica`, `Pendente`, `And`, `NOK`, `OK`, `Evidenciado`, `OK + Evidenciado (Geral)`)
     serve para controle próprio do testador e **não precisa ser enviada ao analista nem publicada**,
     a menos que o analista peça.
   - Caso um módulo não possua processo na planilha, deve-se avisar o analista.
3. **Filtro por `Artefato` (coluna `A`, 00:00:50 – 00:01:14):**
   - Seleciona-se na coluna `A` o tipo de artefato que está sendo liberado (`Web Site .Net`, `Plugin`,
     `Linha de comando .Net`, `Linha de comando Delphi`, `Relatório`, `Todos - Tema / Reg / FiMenu`,
     `Web Aut SubSite CP`, `Web Aut SubSite Empr`, `Web Aut SubSite FGTS`, `Web Aut SubSite Veic`,
     `Web Autorizador de Acordos` — ver [`capturas/02-filtro-artefatos-planilha.png`](capturas/02-filtro-artefatos-planilha.png)).

## 3. Evidência obrigatória × conferência sem evidência (00:01:28 – 00:01:59)

- **[00:01:28 – 00:01:40]** Para artefatos simples como **`Plugin`**, o teste principal consiste em
  demonstrar o plugin **instalado e rodando** (`Instalação / Evidências`).
- **[00:01:42 – 00:01:59]** Nem todas as linhas da planilha geram documento de evidência: itens como
  `Lista de plugins conforme planilha disponível nas ocorrências da OS de projeto (ou subprojeto, checar nos dois)`
  (linha `87`) são apenas uma **conferência** para verificar se a lista está correta, sem necessidade de
  anexar evidência formal.

## 4. Seleção da modalidade de entrega e caso prático Portobank (00:02:00 – 00:02:47)

Nas colunas `G` a `J` da aba `Cenários`, cada processo indica (`Sim` / `Não`) em quais modalidades ele
deve ser executado (ver [`capturas/04-colunas-entrega-inicial-completo-sim.png`](capturas/04-colunas-entrega-inicial-completo-sim.png)):

- **Coluna `G`:** `Entrega inicial - Completo` (quando o cliente **ainda não possui** o módulo).
- **Coluna `H`:** `Testar se o cliente já tiver o módulo?`
- **Coluna `I`:** `Fluxo Limpo Versão Padrão`
- **Coluna `J`:** `Entrega inicial - Reduzido`

No caso atribuído a **William** (**Portobank — liberação do módulo padrão**, **[00:02:10 – 00:02:34]**):
- Como o cliente **não tem o módulo**, aplica-se a coluna **`G` (`Entrega inicial - Completo` = `Sim`)**.
- Filtrando `Artefato = Plugin` e `Entrega inicial - Completo = Sim`, restam apenas **2 processos** (de
  162 registros da planilha):
  1. **Linha 84 (`Instalação / Evidências`, esforço `0:06:00`):** mostrar o plugin aberto/instalado e rodando.
  2. **Linha 86 (`Criação de procedures: .NET - com a opção C, sem erros.`, esforço `0:08:00`):** executar
     a criação de procedures `.NET` com a opção **`C`** sem erros.

### Ressalva crítica sobre a linha 86 (opção `C` e opção `W`, 00:02:35 – 00:02:43)

- Glauco alerta que o texto da linha 86 na planilha (`Criação de procedures: .NET - com a opção C, sem erros.`)
  **está desatualizado**: além da criação com **`C`**, é necessário **conferir se o `W` existe lá** (criação/conferência
  com **`W`**) para garantir que está tudo certo (**[00:02:35 – 00:02:43]**).

## 5. Tabelas e utilitários de banco/sistema documentados na planilha (00:00:50 – 00:01:40)

Embora nenhum comando SQL seja digitado em um console durante o vídeo, a planilha exibe instruções
diretas sobre tabelas e utilitários de banco de dados (ver
[`capturas/01-planilha-liberacao-padrao-website-net.png`](capturas/01-planilha-liberacao-padrao-website-net.png)
e [`capturas/03-cenarios-plugin-7-registros.png`](capturas/03-cenarios-plugin-7-registros.png)):

- **Tabela `TPARWFIUTIL`, campo `PWALIAS` + utilitário `WFIUTIL` (linhas 18 e 85):**
  *"Configurar alias específico do cliente na tabela `TPARWFIUTIL`, campo `PWALIAS`, e regularizar a estrutura via `WFIUTIL`."*
- **Tabela `TRTHB` + utilitário `FI.SQLResutil` / menu `Serviços` + `WebAcesso` (linhas 20 e 21):**
  *"Cadastro de rotinas no acesso (.NET - Via `FI.SQLResutil` [ou Via rotina da Aplicação, geralmente no menu `Serviços`] - Deletar da tabela `TRTHB` os registros referentes ao site atual antes) - após o cadastro, checar se as rotinas aparecem no `WebAcesso`, rotina de cadastro de direitos."*
  - **Atenção:** trata-se de instrução operacional que **altera dados** (exclusão prévia de registros do site atual na tabela `TRTHB` antes de recadastrar rotinas de acesso).

## 6. Resumo em uma frase

Em **00:05:16**, **Glauco** ensina à equipe `CQ 1` como usar a aba **`Cenários`** da planilha
**`Liberacao_Padrao_V30.xlsx`** para filtrar o **Artefato** (ex.: `Plugin`) e a modalidade da entrega
(ex.: `Entrega inicial - Completo = Sim` no caso **Portobank** de **William**), diferenciando itens de
evidência e itens de simples conferência e alertando que na etapa de procedures `.NET` deve-se validar
tanto a opção **`C`** quanto a existência da opção **`W`**.
