# Glossário — Gravando 2026-09-22 111258.mp4

Termos com definição sustentada pela gravação ou pela especificação exibida. Quando a definição não está na gravação, isso é dito. Tempos são do arquivo `HH:MM:SS`.

| Termo | Categoria | Definição sustentada | Fonte e timestamp |
|---|---|---|---|
| **Autorizador** | `SISTEMAS` | Sistema onde a proposta é trabalhada; tem a rotina *Anexar/Consultar Documentação*, usada como referência de comportamento. | `00:03:50` (Funcionamento II); `00:05:40` |
| **ServCon** | `SISTEMAS` | Módulo que contém o serviço (plugin) de envio da proposta ao sistema externo. | RFP001 `001.1`, `00:02:30` ([capturas/01](capturas/01-rfp001-necessidade-solucao.png)) |
| **SrvEnvioPropExt** | `SISTEMAS` | Serviço de envio externo da proposta, citado no título da OS 586780. | Título da janela, `00:00:00`–`00:08:43` |
| **Envio da Proposta ao Sistema Externo** | `SISTEMAS` | Nome do serviço (plugin) em que o agrupamento `attachment_document` é implementado. | RFP001 `001.1`, `00:02:30`; `00:03:50` |
| **Plugin de envio externo** | `SISTEMAS` | Forma falada de se referir ao serviço *Envio da Proposta ao Sistema Externo*. | `00:02:13` |
| **OS 586780** | `PROCESSOS` | Ordem de Serviço da especificação, de título `[ÁGIL] (I) Nova Flag informativa de Docs anexados no SrvEnvioPropExt`. | Cabeçalho da especificação (quadro `00:03:05`; o recorte da captura 02 não inclui o cabeçalho) |
| **Nova Flag informativa de Docs anexados** | `NEGOCIO` | Nome da alteração: informar, no envio, que há documentos anexados à proposta. | Título da OS, `00:03:05` |
| **Agrupamento** | `SISTEMAS` | Bloco de informações do envio externo. A gravação não define o termo além do uso (`attachment_document`). | RFP001, `00:02:30`; fala `00:02:17` |
| **attachment_document** | `SISTEMAS` | Nome em inglês do novo agrupamento que informa documentos anexados. | RFP001 `001.1`, `00:02:30`; `00:03:50` |
| **Client** | `SISTEMAS` | Objeto onde o agrupamento fica, responsável pelo armazenamento das informações do cliente. | `00:03:05`; `00:03:50` |
| **document_type** | `SISTEMAS` | Campo que identifica o tipo do documento anexado. Código ou descrição: **em aberto** (ver [`incertezas.md`](incertezas.md)). | `00:03:05`; `00:04:02`–`00:05:08` |
| **document_name** | `SISTEMAS` | Campo que indica o nome do documento anexado. | `00:03:05`; `00:04:29`–`00:04:39` |
| **user** | `SISTEMAS` | Campo com o usuário responsável pela anexação do documento. | `00:03:05`; `00:02:58` |
| **null** | `SISTEMAS` | Valor enviado quando não há documento anexado ou a informação não existe na base. | `00:03:43`–`00:03:48`; `00:03:50` |
| **Checklist da proposta** | `PROCESSOS` | Lista de documentos previstos para a proposta; o agrupamento indica quais estão anexados. | `00:03:50` (Funcionamento II) |
| **SIC** | `INFRA_E_ACESSO` | Sistema de onde as informações devem ser obtidas, segundo a fala; precisa ter o código do perfil configurado. | `00:05:13`–`00:05:20` |
| **Código do perfil** | `INFRA_E_ACESSO` | Configuração necessária no SIC e no web service para a execução do envio. Valor não demonstrado; não registrar. | `00:05:13`–`00:05:34` |
| **Web service** | `INFRA_E_ACESSO` | Forma de execução do Autorizador; exige o código do perfil configurado. | `00:05:22`–`00:05:46` |
| **C6 / C6 Consig** | `NEGOCIO` | Cliente e projeto da janela da reunião (*C6 Consig — PLANNING*). Padrão de nomes em inglês do C6. | Título da janela; `00:02:43` |
| **Função Sistemas** | `NEGOCIO` | Empresa responsável pelo sistema; aparece na especificação. | Logo da especificação, `00:03:05` |
| **Review** | `PROCESSOS` | Revisão feita ao fechar o pacote de uma versão; local onde costuma haver apresentação de projetos. | `00:06:09`–`00:06:35` |
| **Documento de teste** | `PROCESSOS` | Documento do cliente que descreve o passo a passo do teste; deve incluir a configuração do perfil. | `00:06:12`–`00:06:30` |
| **Gantt / mapa** | `PROCESSOS` | Ferramentas de acompanhamento de horas e de projetos citadas para registro. | `00:07:08`–`00:07:19` |
| **IP** | `PROCESSOS` | Situação do item no acompanhamento. **Sigla não definida na gravação.** | `00:07:30` |
| **Anexo I (métodos de integração de importação de proposta)** | `SISTEMAS` | Título de anexo da especificação visível em miniatura. Conteúdo não lido em tamanho real. | Miniatura, aprox. `00:04:00`–`00:05:00` |
| **Procurações do web service** | `INFRA_E_ACESSO` | Expressão falada, não confirmada. Pode ser transcrição errada. | `00:07:01`; ver `incertezas.md` |
