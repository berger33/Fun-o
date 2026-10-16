# Glossário — Gravando 2026-07-08 182343.mp4

Termos sustentados pela **fala (ASR)** e/ou pela **tela** (verificado quadro a quadro). Onde a única fonte é o ASR, o campo “Fonte” indica isso.

| Termo / sigla | Significado sustentado pela gravação | Categoria | Timestamp | Fonte |
|---|---|---|---|---|
| **WebAutorizador** | Pasta/aplicação Web do pacote de teste; também o nome da aplicação aberta no navegador. Contém `bin`, `Config`, `Estreia`, `Web References`, `Web.Config`, `WSAutorizador.asmx`. | SISTEMAS | 00:00:32–00:02:32 | tela + fala |
| **WS / `WSAutorizador`** | Serviço Web do mesmo pacote, em `...\WS\WSAutorizador`; o interlocutor afirma que acompanha o autorizador (“atualizou um, tem que atualizar o outro”). | SISTEMAS | 00:02:04–00:02:36 | tela + fala |
| **`WsRegChaveLicenca.asmx`** | Arquivo presente no pacote, ao lado de `WSAutorizador.asmx`; finalidade não demonstrada (o nome sugere registro de chave de licença). | SISTEMAS | 00:02:36 | tela |
| **`Config` (pasta de configuração)** | Pasta presente no pacote Web e no pacote do WS; segundo a fala, já contém parâmetros de SIC, GDOK e API e deve ser preservada/copiada como backup. Data observada no pacote do WS: `09/09/2025`. | INFRA_E_ACESSO | 00:00:33; 00:02:34–00:03:24; 00:02:36 | tela + fala |
| **`Estreia`** | Pasta presente nos dois pacotes, ao lado de `Config` (`08/07/2026 11:28` no pacote do serviço Web). Conteúdo não aberto na gravação. | SISTEMAS | 00:00:35; 00:02:36 | tela |
| **`bin` / `Web References`** | Pastas do pacote lidas na lista de arquivos (`bin` com `FI.*`/`FLA*.dll`). | SISTEMAS | 00:00:35–00:00:52; 00:02:36; 00:05:10–00:05:30 | tela |
| **Esteira** | Objeto de teste que se copia/importa; no próprio diálogo do sistema aparece como “nova esteira ‘9999 - teste’”. Corresponde, na prática, a um **modelo de decisão** identificado por número e descrição. | SISTEMAS / PROCESSOS / NEGOCIO | 00:05:48–00:07:20; 00:07:14 | tela + fala |
| **Modelo de Decisão** | Objeto manipulado em `Serviços → Decisão`; possui `Nº Modelo` (ex.: `9999`), uma descrição e um arquivo de importação (`Estaira112233.xml`). | SISTEMAS / NEGOCIO | 00:06:15–00:07:35 | tela |
| **`Estaira112233.xml`** | Nome do arquivo de importação exibido no campo `Arquivo de Importação de Modelo de Decisão` — modelo de arquivo de esteira (`Estaira*`). | SISTEMAS | 00:06:55–00:07:20 | tela |
| **`Serviços → Decisão`** | Caminho de menu que reúne tabelas de modelo/decisão, relacionamento modelo × produto, exportação, importação e visualizador de fluxo. | SISTEMAS / PROCESSOS | 00:05:45–00:06:40 | tela |
| **Tolerância (mínima/máxima)** | Percentual aplicado sobre o valor **solicitado** (mínimo → margem de variação inferior; máximo → margem de variação superior). Campo **opcional**, **2 casas decimais**, faixa prevista pela EF **0–99**. | NEGOCIO | 00:03:00–00:03:22; 00:05:26; 00:07:53–00:08:03 | tela (documento) + fala |
| **`Limites do Valor Solicitado` (tela)** | Caixa da tela do Autorizador que contém `Valor mínimo solicitado`, `Valor máximo solicitado`, `(%) Tolerância mínimo`, `(%) Tolerância máximo`, `Aplicar tolerância em` e os botões `Confirmar`/`Cancelar`/`Voltar`. | SISTEMAS / NEGOCIO | 00:03:00–00:03:22 (evidência anexada) | tela |
| **`Aplicar tolerância em`** | Lista de seleção da mesma tela; aparece como `NaoSelecionado` no exemplo. Valores possíveis não demonstrados. | SISTEMAS | 00:03:00–00:03:22 | tela |
| **Incidente / `Incidente01.pdf`** | Documento usado para relatar a divergência de tolerância, com seções `Evidência` e “De acordo com a EF”, e tabela de encaminhamento por projeto. | PROCESSOS / NEGOCIO | 00:03:00–00:03:22; 00:07:40 | tela |
| **EF** | Documento de especificação dos campos citado no incidente (“De acordo com a EF: Detalhamento dos Campos”). | PROCESSOS / NEGOCIO | 00:03:10–00:03:22 | tela |
| **SIC** | Sistema/parâmetro citado como conteúdo da configuração e como caso em que “é só o autorizador mesmo”. | SISTEMAS / INFRA_E_ACESSO | 00:02:58–00:03:04; 00:04:20–00:04:24 | fala (ASR) |
| **GDOK** | Nome citado junto dos parâmetros da configuração; expansão e finalidade não demonstradas. | SISTEMAS / INFRA_E_ACESSO | 00:02:58–00:03:04 | fala (ASR) |
| **API** | Componente citado na fala sobre o que é atualizado (“você só atualiza API mesmo”). Serviço e versão não especificados. | SISTEMAS | 00:03:02–00:04:27 | fala (ASR) |
| **“AWS” (ASR)** | Palavra reconhecida ao falar de um componente que “não atualiza”; pode ser o próprio WS, outra sigla ou erro de reconhecimento. **Não** usar como identificação confirmada. | DÚVIDA_OU_CONFLITO | 00:04:26 | fala (ASR) |
| **“N”** | Resposta mencionada em “a gente roda sempre com N”; não há diálogo evidente no quadro correspondente. Não tratar como opção padrão. | DÚVIDA_OU_CONFLITO | 00:03:41 | fala (ASR) |
| **`Autorizador Web - BANCO FISCA`** | Título da janela/aplicação aberta no navegador durante a demonstração do menu `Serviços`. | SISTEMAS | 00:03:35–00:07:35 | tela |
| **`Web Site` / família de produtos Web** | Diretório que reúne as aplicações Web do ambiente (`WebCTC`, `WebTabelasCorp`, `WebEmpregador`, `WebTabelas`, `WebSIC`, `WebAutorizador2`, `WidgetsGCTS`, `WebLiberacao`, ...). | SISTEMAS | 00:01:35–00:02:47 | tela |
| **`FI.*` / `FLA*` (dll)** | Padrão de nomes de bibliotecas visto na pasta `bin` do pacote. | SISTEMAS | 00:00:35–00:00:52; 00:05:10–00:05:30 | tela |
| **“Erro genérico”** | Classificação dada pelo interlocutor a mensagens em vermelho surgidas durante a operação, com a afirmação de que “não interfere em nada”. Sem diagnóstico demonstrado. | DÚVIDA_OU_CONFLITO | 00:04:29–00:04:39 | fala (ASR) + tela (mensagens ilegíveis) |
| **C6 (ambiente)** | Referência da fala à raiz do ambiente de teste (“a gente vai vir em C6”); a tela mostra a raiz `...\WK01058CQ\c6`. Caminho completo não é reproduzido. | INFRA_E_ACESSO | 00:00:23–00:00:32 | fala + tela |

Não inferir dependências entre componentes nem transformar termos ambíguos em nomenclatura oficial. Ver [`incertezas.md`](incertezas.md).
