> **Publicação autorizada pelo responsável em 2026-10-13** (dados declarados fictícios/de teste; nome Função Sistemas e nomes dos operadores preservados; sem imagens de pessoas).

# Guia de estudo — Gravando 2026-09-22 111258.mp4

- **Categoria:** `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO` (SQL: não demonstrado — ver [`../SQL/INDICE_SQL.md`](../SQL/INDICE_SQL.md))
- **Sistema:** **Autorizador** (módulo *Anexar/Consultar Documentação*, citado na especificação), serviço **SrvEnvioPropExt** / plugin **Envio da Proposta ao Sistema Externo** no módulo **ServCon**, integração com **SIC** e **web service** do Autorizador
- **Assunto:** novo agrupamento `attachment_document` no envio de proposta ao sistema externo para informar a existência e os dados básicos de documentos anexados (**OS 586780**, `[ÁGIL] (I) Nova Flag informativa de Docs anexados no SrvEnvioPropExt`)
- **Fonte:** `Gravando 2026-09-22 111258.mp4` (297627736 bytes; SHA-256 `c617494d…`), duração `00:08:42.93`, reunião com compartilhamento de tela de um PDF da especificação (`DS586780 (3).PDF`, 41 páginas)
- **Confiança da extração:** **média** — a especificação foi lida em tamanho real nos pontos listados em [`capturas.md`](capturas.md) e amostrada a cada 10 s; a fala é ruidosa (conversa paralela, cortes e nomes), e vários trechos da discussão não têm tela correspondente. Itens incertos estão em [`incertezas.md`](incertezas.md).

## 1. Objetivo e público

- **Objetivo da gravação:** apresentar a alteração de **Nova Flag informativa de Docs anexados** e discutir como o envio de proposta ao sistema externo deve informar documentos anexados ao cliente — com o agrupamento `attachment_document`, os campos `document_type`, `document_name` e `user`, e o valor `null` quando não houver documento (`[00:02:08]`–`[00:04:48]`).
- **Público/pré-requisitos:** equipe de desenvolvimento, análise e teste da **Função Sistemas** que trabalha no plugin de envio de proposta, na integração com o cliente C6 e na documentação funcional (OS 586780).

## 2. Contexto e origem da alteração (00:02:08 – 00:02:58)

- **[00:02:08 – 00:02:19]** A fala apresenta o item como "uma alteração" no plugin de envio externo, para incluir um novo agrupamento. Confere com a RFP001 (`[00:02:30]`, [`capturas/01-rfp001-necessidade-solucao.png`](capturas/01-rfp001-necessidade-solucao.png)).
- **[00:02:22 – 00:02:40]** A justificativa falada é que o cliente precisa de informações na **jornada de formalização** dele; por isso o plugin receberá mais conteúdo. A fala também diz que o motivo do agrupamento é o cliente usar esse plugin. *Síntese da fala; não há tela que confirme a razão de negócio.*
- **[00:02:43 – 00:02:58]** O novo agrupamento segue o padrão em inglês usado pelo C6 e terá três campos: **tipo do documento**, **nome do documento** e **usuário que anexou**.

## 3. Requisito e campos do agrupamento (00:02:30 – 00:03:50)

- **[00:02:30] RFP001 — *Novo Campo no Plugin de Envio da Proposta ao Sistema Externo*** (página 2 do PDF):
  - *Necessidade:* implementar um novo agrupamento destinado à identificação de documentação anexa que compõe as informações do cliente.
  - *Solução proposta 001.1:* implementar no módulo **ServCon**, no serviço (plugin) **Envio da Proposta ao Sistema Externo**, novo agrupamento responsável por identificar documentação anexa para compor as informações do cliente.
  - *Detalhamento do novo agrupamento:* `attachment_document`.
- **[00:03:05] Especificação funcional — OS 586780** (página 3): dentro do objeto `Client`, os campos do agrupamento são:
  - `document_type` — identificação do tipo de documento;
  - `document_name` — indicador do nome do documento anexado;
  - `user` — usuário responsável pela anexação do documento.
- **[00:03:29 – 00:03:48]** Discussão: os campos já existem na base (segundo a fala), e a implementação só precisa **resgatar** a informação, sem criar nova gravação; quando a informação não existir, deve-se **enviar nulo**.

## 4. Funcionamento do agrupamento (00:03:50 – 00:04:10)

- **[00:03:50]** *Funcionamento I:* para identificar a existência de documentos anexos à proposta, será implementado um novo agrupamento `attachment_document` no serviço (plugin) *Envio da Proposta ao Sistema Externo*, dentro do objeto `Client`, responsável pelo armazenamento das informações do cliente.
- **[00:03:50]** *Funcionamento II:* o agrupamento `attachment_document` indicará a existência de documentos anexados previstos no **checklist da proposta**, de forma análoga ao funcionamento atual da rotina **Anexar/Consultar Documentação** do módulo **Autorizador**. Os documentos anexados serão evidenciados no agrupamento e, **quando não houver documentos anexados, o agrupamento será enviado como `null`**.
- **[00:04:10] Considerações** (início da seção na página 3; texto completo não legível em tamanho real — ver [`incertezas.md`](incertezas.md)).

## 5. Decisões e dúvidas discutidas (00:03:49 – 00:05:11)

- **Tipo do documento: código ou descrição?** (`[00:04:02]`–`[00:04:49]`) A conversa oscila: uma fala diz que o tipo deve ser o **código**, outra lembra que a **descrição** é o nome cadastrado; exemplos citados são tipos de documento (CPF, RG, comprovante de interesse), sem valores. A conclusão falada é **código** (`[00:04:49]` "o tipo de documento é o código"), porque a equipe do cliente vai plugar isso do lado deles e não seria bom integrar por texto (`[00:04:52]`–`[00:04:57]`). Há ressalva em `[00:05:00]`–`[00:05:08]`: a descrição foi pedida ao cliente, e a implementação deve colocar o código. **Não confirmado por tela** — ver [`incertezas.md`](incertezas.md) item 1.
- **Nome do documento:** a fala explica que o nome é o que a pessoa cadastra para o tipo de documento (`[00:04:29]`–`[00:04:39]`). *Síntese; a regra de cadastro não foi demonstrada.*

## 6. Integração e acesso técnico (00:05:11 – 00:05:46)

- **[00:05:13] SIC:** a informação deve ser obtida do **SIC**, que precisa ter o **código do perfil** configurado.
- **[00:05:22] Receio:** se a execução for pelo **web service**, o código do perfil também precisa estar configurado lá. A fala diz que a rotina falada até então é apenas pela tela do Autorizador, e que às vezes o código do perfil não é configurado (`[00:05:38]`–`[00:05:44]`).
- **Cuidado:** esta seção trata de configuração, não de credencial. Nenhum valor de perfil, usuário ou senha foi demonstrado na tela; não há material de acesso neste guia.

## 7. Teste, review e acompanhamento (00:05:55 – 00:08:41)

- **[00:05:55] Documento de tipo para a importação:** pergunta sobre montar um tipo de documento para a equipe de importação depois da versão entregue ou só na versão entregue; a fala indica que isso costuma ser visto no **review**, que é feito ao fechar o pacote (`[00:06:09]`–`[00:06:12]`).
- **[00:06:12] Documento de teste:** recomenda-se detalhar no documento de teste do cliente, com um passo que informa a configuração do perfil (`[00:06:23]`–`[00:06:30]`).
- **[00:06:33] Apresentação de projetos:** a fala diz que a apresentação costuma ser feita na review.
- **[00:06:52] Responsáveis pelo teste:** Jonas e William farão o teste em conjunto; a anotação falada é **"mostrar as procurações lá do web service"** (`[00:07:01]`; expressão incerta — ver [`incertezas.md`](incertezas.md)). Se precisar, a fala indica chamar o Zé.
- **[00:07:08] Horas e planejamento:** pede-se que as horas sejam registradas no Gantt / nos projetos separados (`[00:07:13]`–`[00:07:15]`) e que o mapa seja preenchido.
- **[00:07:30] Item de desenvolvimento:** o documento está em status **IP** (sigla não definida na gravação); ao abrir o item, avisar para marcar o início do desenvolvimento, porque "sem o item eu não consigo iniciar" (`[00:07:33]`–`[00:07:39]`).
- **[00:07:52] Item que "explodiu":** conversa sobre um item que estourou/atingiu o prazo e a marcação que deveria ser feita, com menção a item em definição de prazo e cor vermelha (`[00:07:52]`–`[00:08:27]`). *Trecho pouco claro; não há tela de planejamento para confirmar.*
- **[00:08:30] Encerramento:** pergunta geral de dúvidas (`[00:08:30]`); o restante é conversa de fechamento e a parada da gravação e da transcrição (aviso visível por volta de `00:08:15`, leitura aproximada).

## 8. Resumo

1. O plugin **Envio da Proposta ao Sistema Externo** (módulo **ServCon**) ganha o agrupamento `attachment_document` com `document_type`, `document_name` e `user` (`[00:02:30]`–`[00:03:05]`).
2. O agrupamento sinaliza documentos anexados previstos no checklist da proposta, no padrão de *Anexar/Consultar Documentação* do Autorizador, e vai como `null` sem documentos (`[00:03:50]`).
3. Os valores devem ser resgatados das informações já existentes, sem nova gravação (falado, `[00:03:10]`–`[00:03:29]`).
4. Decisão falada: `document_type` como **código**, com ressalva (`[00:04:49]`, `[00:05:00]`).
5. Integração com SIC e web service depende do código do perfil configurado (`[00:05:13]`–`[00:05:46]`).
6. Teste em conjunto (Jonas e William), documento de teste e apresentação na review (`[00:06:12]`–`[00:07:01]`).

## Erros e cuidados

- Não tratar a decisão de código × descrição como regra fechada: ela não foi validada com a tela nem com a especificação em tamanho real (`[00:04:49]`).
- A especificação é um documento de trabalho (`DS586780 (3).PDF`, 41 páginas); só as páginas 2 e 3 foram lidas. Restante do documento não foi analisado nesta gravação.
- Quando a fala citar "Zé", "Léo", "Gleison" e outros, são participantes/responsáveis citados; a gravação não confirma o papel de cada um.

Ver também: [`procedimentos.md`](procedimentos.md), [`perguntas.md`](perguntas.md), [`glossario.md`](glossario.md), [`incertezas.md`](incertezas.md), [`transcricao.md`](transcricao.md), [`metadados.md`](metadados.md).
