# Guia de estudo — Gravando 2026-07-08 182343.mp4

- **Categoria:** `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO` (sem SQL demonstrado)
- **Sistema:** WebAutorizador (aplicação Web e serviço Web `WS\WSAutorizador`) no ambiente de teste; aplicação aberta como **`Autorizador Web - BANCO FISCA`**, com menus `Cadastro · Esteira · Consulta · Relatórios · Tabelas · Plugins · INSS Online · Auxílio Brasil · CPD Online · Serviços`.
- **Assunto:** atualização do pacote (WebAutorizador + WS) em ambiente de teste, navegação `Serviços → Decisão`, exportação/importação de **modelo de decisão** (“esteira”) e o **incidente de tolerância** (0–99 × 0–100).
- **Fonte:** `Gravando 2026-07-08 182343.mp4` — 356602844 bytes; SHA-256 `07a7166a…`; duração `00:10:23.63` (áudio útil até `00:08:28`).
- **Confiança da extração:** **média** no visual (telas lidas diretamente dos quadros, com timestamp); **média/baixa** na fala (ASR automático e informal); **baixa** na rotina de atualização de componentes (contraditória; sem pacote, versão ou ordem definidos).

> **Publicação autorizada pelo responsável em 2026-10-13** (dados declarados fictícios/de teste). Este lote foi analisado a partir da **fonte primária**, com bytes conferidos. As capturas publicadas foram recortadas no documento/tela: sem imagens de participantes, sem a faixa de identificação de usuário/servidor, sem valor de OS e sem dados de cliente.

## 1. Objetivo e público

A gravação é uma **passagem de orientação entre dois operadores** (o interlocutor explica a outro como trabalhar com o pacote e com a esteira de teste) e serve a quem precisa:

1. entender **o que existe dentro do pacote** `WebAutorizador` / `WS\WSAutorizador` (pastas `bin`, `Config`, `Estreia`, `Web References`);
2. saber **onde ficam** as telas de configuração de esteira/processo no Autorizador Web;
3. reconhecer o **incidente de tolerância** da faixa de valor solicitado e o procedimento informal usado para registrar/importar um caso de teste;
4. saber o que **não** deve ser feito sem procedimento aprovado (exclusão de arquivos, troca de configuração, alteração de ambiente compartilhado).

Não é um runbook: não define pacote oficial, versão, ambiente autorizado, plano de rollback nem critério de sucesso.

## 2. Conhecimento sustentado pela gravação

### 2.1 Pacote do WebAutorizador e do WS (`00:00:20–00:02:47`)

- A navegação começa na raiz do pacote em ambiente de teste (`...\WK01058CQ\c6`) e entra em `Web Site` → **`WebAutorizador`** (`00:00:20–00:00:35`). A pasta aparece com data de modificação `08/07/2026 12:34` (`00:02:25–00:02:32`).
- Conteúdo de `WebAutorizador` (`00:00:35–00:00:52`; captura 04 mostra o pacote irmão do WS): `bin`, `Config`, `Estreia`, `Web References`, `Dados.dat`, `Global.asax`, `inst.dat`, `Web.Config`, `WSAutorizador.asmx`, `WSAutorizador.XmlSerializers.dll`, `WsRegChaveLicenca.asmx`.
- A seleção visível na lata é de **10 itens / 1,46 MB** (`00:00:35`) — coerente com a fala “a gente vai dar um CTRL A, apagar tudo, menos a config” (`00:00:33`).
- A lista de `Web Site` mostra a família de aplicações do ambiente (`WebCTC`, `WebTabelasCorp`, `WebEmpregador`, `WebTabelas`, `WebSIC`, `WebAutorizador2`, `WidgetsGCTS`, `WebLiberacao`, ...) (`00:02:36`; captura 04).
- O interlocutor passa a `...\WS\WSAutorizador` e afirma que **o WS “sempre vem junto”**: “atualizou um, tem que atualizar o outro” (`00:02:25–00:02:32`). A pasta `Config` do WS aparece com data `09/09/2025 11:35`, mais antiga que os binários de `08/07/2026` — indício (não prova) de que a configuração é preservada entre versões.

### 2.2 Preservação da configuração e backup (`00:02:34–00:03:24`)

- A configuração é descrita como já preenchida com parâmetros de **SIC**, **GDOK** e **API** (`00:02:58–00:03:04`).
- Recomendação explícita: **copiar a pasta `config` para a máquina local como backup**, porque “vai que dá uma travadinha na máquina... deleta tudo” (`00:03:09–00:03:24`), com relato de quase-acidente na própria máquina do interlocutor (`00:03:24–00:03:39`).
- ⚠️ Conflito registrado: há duas falas de exclusão (`00:00:33` “apagar tudo, menos a config” e `00:02:34` “apaga config”, esta dita no contexto do WS). Ver [`incertezas.md`](incertezas.md) §1. **Nenhuma exclusão deve ser executada com base nesta gravação.**

### 2.3 O que muda em cada tipo de alteração (`00:04:03–00:04:27`)

- “O autorizador é sempre esses dois [...] só não é esses dois quando é caso do SIC, tipo uma variável, aí é só o autorizador mesmo” (`00:04:03–00:04:24`).
- Em seguida: “o **AWS** não atualiza... depende das vezes também” (`00:04:26–00:04:27`).
- A leitura operacional é: **de componente para tipo de alteração** — mas a matriz não fecha com o texto do ASR (“AWS” pode ser o próprio WS, sigla diferente ou erro de reconhecimento). Não transformar em matriz de implantação.

### 2.4 Erro durante a operação (`00:03:40–00:04:39`)

- Durante a cópia de itens para a pasta do serviço Web, aparecem mensagens em vermelho em uma janela escura (`00:03:40–00:05:05`).
- O interlocutor avalia: “correu um erro aqui... mas isso aqui não interfere em nada... é um erro genérico” (`00:04:29–00:04:39`) e volta a trabalhar.
- Os textos não são legíveis nos quadros amostrados. **Não usar essa avaliação como diagnóstico**: o efeito não é demonstrado.

### 2.5 Incidente de tolerância (`00:03:00–00:03:22`; `00:07:40–00:07:55`)

Documento `Incidente01.pdf` (aberto fora do compartilhamento; lido diretamente do quadro em `00:03:12`):

- **Regra declarada:** “Os valores de Tolerância mínimo e Tolerância máximo deveriam permitir o preenchimento com valores **entre 0 e 99**. Porém, o sistema está permitindo o preenchimento com valores **entre 0 e 100**.”
- **Evidência anexada:** caixa **Limites do Valor Solicitado** com `Valor mínimo solicitado 0,00`, `Valor máximo solicitado 0,00`, `(%) Tolerância mínimo 100,00`, `(%) Tolerância máximo 100,00`, `Aplicar tolerância em: NaoSelecionado`, botões `Confirmar` / `Cancelar` / `Voltar`; os dois campos de tolerância estão destacados em vermelho.
- **De acordo com a EF — Detalhamento dos Campos** (transcrito do quadro): “**(%) Tolerância Mínimo**: campo numérico de preenchimento **opcional**, destinado ao cadastro do percentual de tolerância aplicado sobre o valor mínimo solicitado. Permite definir uma **margem de variação inferior**. O campo deve aceitar apenas valores **entre 0 e 99**, com até **2 casas decimais**.” / “**(%) Tolerância Máximo**: campo numérico de preenchimento opcional destinado ao cadastro do percentual de tolerância aplicado sobre o valor máximo solicitado. Permite definir uma margem de variação superior. O campo deve aceitar apenas valores entre 0 e 99, com até 2 casas decimais.”
- **Cabeçalho** com campos `Projeto / OS / Analista / Data entrega / Cliente / Módulo / Descrição OS` — **todos em branco** nos quadros.
- **Tabela de encaminhamento** (exemplos do próprio documento, **fictícios de teste**): `Projeto FIDC – Base de cálculo`, `Projeto FIDC Baixa Renda` e `Projeto FIDC Não Elegível`, com responsáveis e datas. Não são dados de cliente reais; o conteúdo não é reproduzido como instrução.
- O chat da reunião confirma que o caso foi discutido com **“Michelle de negócios”**, que orientou o encaminhamento, e que a evidência já foi anexada (`00:07:40`).

> O valor de OS usado no teste aparece desfocado no quadro e **não** é registrado neste material.

### 2.6 Navegação e importação da esteira/modelo (`00:05:30–00:07:35`)

Sequência observada na aplicação `Autorizador Web - BANCO FISCA` (`localhost/WebAutorizador/...`):

1. Menu **`Serviços`** → agrupamentos visíveis (`00:05:45–00:06:15`; captura 05): `Configuração de Parâmetros do Sistema`, `Alteração de senha`, `Monitor de Ambiente`, `Parâmetros`, `Gerenciamento de Bloqueios`, `Campos Editáveis`, `Campos Obrigatórios`, `Configuração de Processo`, **`Decisão`**, `Aprovação/Consulta`, `Perfil de Consulta Externa`, `Configuração da Grade de Execução da Provisão de Recálculo`, `Configuração do Comportamento da Provisão de Recálculo`, `Fila de Provisão de Recálculo`, `Desbloquear Minhas Propostas`.
2. **`Decisão`** → `Tabela de Modelos`, `Tabela de Decisão`, `Relacionamento Modelo X Produto`, **`Exportar Modelo Decisão`**, **`Importar Modelo Decisão`**, `Visualizador de Fluxo Decisão` (`00:06:15–00:06:40`).
3. **Exportar Modelo de Decisão** (`00:06:20–00:06:50`): diálogo com `Nº Modelo` e botões `Confirmar` / `Cancelar` / `Voltar`.
4. **Importar Modelo de Decisão** (`00:06:55–00:07:35`, captura 03): `Arquivo de Importação de Modelo de Decisão: Estaira112233.xml`, `Nº Modelo: 9999` e descrição `teste_tolerancia`; a confirmação pergunta “**Confirma a importação da nova esteira ‘9999 - teste’?**”; o sistema responde “**As informações foram salvas**”.
5. Em `00:05:26` o interlocutor anuncia “**a parte de tolerância**”; ao final confirma “Teste de tolerância. Parece que eu criei mesmo, não foi? ... Então é isso” (`00:07:53–00:08:03`).

> O termo **“esteira”** aparece nas duas pontas: na fala (“copiar/importar a esteira”) e no próprio diálogo do sistema (“nova esteira ‘9999 - teste’”). No vocabulário do produto, a esteira é representada por um **modelo de decisão** identificado por número e descrição, materializado em um arquivo `Estaira*.xml`.

### 2.7 Encerramento (`00:08:03–00:08:20`)

- O interlocutor encerra oferecendo suporte e pedindo que o colega confira a esteira: “bate o olho na F mesmo assim... se tiver faltando alguma coisa, você também coloca... se tiver dúvida, pergunta” (`00:05:09–00:05:23`); despedida em `00:08:11–00:08:19`.

## 3. Leitura operacional segura

- **Controle de mudança antes de técnica:** identificar o tipo de alteração (variável/SIC × pacote), confirmar o que compõe o pacote (aplicação Web **e** serviço Web) e **preservar a configuração**.
- **Evidência de defeito:** o caso de tolerância mostra o padrão aceito pela empresa — regra escrita na EF, evidência visual da tela e encaminhamento ao responsável de negócio **antes** de tratar como bug.
- **Modelo de decisão:** `Serviços → Decisão` é o caminho para exportar/importar a esteira; importar cria/atualiza o modelo por número, com confirmação e mensagem de sucesso.
- **O que continua bloqueado:** exclusão em massa de arquivos (`Ctrl+A`), troca/substituição de `Config`, e qualquer conclusão de que “o erro não interfere”.

## 4. O que não foi demonstrado

- Matriz oficial de componentes/versões e o significado de “AWS” (`00:04:26`).
- O que é a opção “N” citada em `00:03:41` (nenhum diálogo correspondente aparece claramente).
- Conteúdo do terminal (`00:01:55–00:02:15`), das mensagens em vermelho (`00:03:45–00:05:05`) e da lista de anotações sobre a área de trabalho (`00:10:20`) — ilegíveis na amostragem.
- Permissões/perfis necessários para `Serviços`/`Decisão`; a faixa de identificação de usuário foi desfocada e não é registrada.
- Nenhuma consulta SQL e nenhum comando de banco foram ditados ou demonstrados.

## 5. Resumo

A gravação documenta uma **rotina informada de atualização** do pacote WebAutorizador/WS em ambiente de teste (com backup da configuração e a ressalva de que a fala de exclusão é contraditória), e uma **demonstração real de importação de modelo de decisão** (“esteira”) pelo caminho `Serviços → Decisão`, motivada pelo **incidente de tolerância** cuja regra (0–99) e evidência (0–100) foram registradas em documento. O valor prático imediato está em: saber onde ficam as telas, reconhecer o vocabulário (esteira = modelo de decisão, tolerância mínima/máxima sobre valor solicitado) e **não** executar limpeza/alteração sem runbook aprovado.

Ver também: [`procedimentos.md`](procedimentos.md), [`perguntas.md`](perguntas.md), [`glossario.md`](glossario.md), [`incertezas.md`](incertezas.md), [`transcricao.md`](transcricao.md), [`capturas.md`](capturas.md) e [`metadados.md`](metadados.md).
