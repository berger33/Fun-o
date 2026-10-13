# Procedimentos — Gravando 2026-09-22 111258.mp4

- **Categoria:** `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO`
- **Sistema:** Autorizador (*Anexar/Consultar Documentação*), SrvEnvioPropExt / ServCon (plugin *Envio da Proposta ao Sistema Externo*), SIC, web service do Autorizador
- **Assunto:** construção e validação do agrupamento `attachment_document`
- **Fonte:** `Gravando 2026-09-22 111258.mp4` — ver [`guia_de_estudo.md`](guia_de_estudo.md)
- **Confiança da extração:** **média** (ver metadados no guia)

> Fluxos abaixo são o que a gravação **mostra ou diz**. Não há comando de alteração de dados, nem SQL, demonstrado. Passos não demonstrados estão marcados como tal.

## Fluxo A — Entender a alteração e levantar os campos

**Pré-condições (faladas):** existe o plugin *Envio da Proposta ao Sistema Externo* no módulo ServCon; existe a RFP001 e a Especificação Funcional da OS 586780.

1. Abrir a **RFP001 — Novo Campo no Plugin de Envio da Proposta ao Sistema Externo** e ler *Necessidade* e *Solução proposta 001.1* — `[00:02:30]` ([`capturas/01-rfp001-necessidade-solucao.png`](capturas/01-rfp001-necessidade-solucao.png)).
2. Identificar o nome do agrupamento: `attachment_document` — `[00:02:30]`.
3. Levantar os três campos: `document_type`, `document_name`, `user` — `[00:03:05]`; na fala, `[00:02:43]`–`[00:02:58]`.
4. Confirmar, com a base do sistema, se as informações já existem (fala: "a gente já tem os campos na base") — `[00:03:10]`–`[00:03:29]`. **Validação pendente**: não demonstrado na tela.
5. Se a informação não existir, enviar **nulo** — `[00:03:43]`–`[00:03:48]`.

## Fluxo B — Regra de funcionamento do agrupamento

**Entradas:** checklist de documentos previstos da proposta; rotina *Anexar/Consultar Documentação* do módulo Autorizador (referência de comportamento).

1. Para cada proposta, identificar os documentos anexados previstos no checklist — Funcionamento I e II, `[00:03:50]`.
2. Se houver documentos anexados, evidenciá-los no agrupamento `attachment_document` com os três campos.
3. Se não houver documentos anexados, enviar o agrupamento como `null` — `[00:03:50]`.
4. **Resultado esperado:** o sistema externo recebe o agrupamento com a existência dos documentos ou `null`.

**Decisão em aberto:** o campo `document_type` é **código** ou **descrição**? Conclusão falada: **código** (`[00:04:49]`), com ressalva de que a descrição pode ter sido pedida ao cliente (`[00:05:00]`–`[00:05:08]`). **Validar antes de implementar** (ver [`incertezas.md`](incertezas.md)).

## Fluxo C — Integração com SIC e web service

**Pré-condições (faladas):** o código do perfil deve estar configurado no SIC e também no web service, quando a execução for por web service (`[00:05:13]`–`[00:05:34]`).

1. Obter as informações do SIC (fala: "dá pra gente pegar tudo do SIC") — `[00:05:14]`.
2. Verificar se a execução é pelo **web service** — `[00:05:22]`–`[00:05:32]`.
3. Se for pelo web service, confirmar que o código do perfil está configurado nele — `[00:05:26]`–`[00:05:32]`.
4. **Cuidado:** a rotina do time, segundo a fala, costuma ser só pela tela do Autorizador, e o código do perfil pode não estar configurado — `[00:05:38]`–`[00:05:44]`. *Não há tela que mostre essa configuração.*

> Não registrar valores de perfil, usuário ou credencial. Não sugerir contornar controle de acesso.

## Fluxo D — Teste, documentação e review

1. Montar o documento de teste do cliente com um passo que explique como o perfil está configurado (`[00:06:23]`–`[00:06:30]`).
2. Verificar com a importação se é preciso criar um tipo de documento para eles, depois da versão entregue ou apenas na versão entregue (`[00:05:55]`–`[00:06:12]`). **Decisão não tomada na gravação.**
3. Levar o projeto para a **review** quando o pacote for fechado; a apresentação de projetos costuma ocorrer nessa review (`[00:06:09]`–`[00:06:35]`).
4. Responsáveis pelo teste (falados): Jonas e William, em conjunto — `[00:06:52]`–`[00:06:56]`. Anotar a verificação do web service (`[00:07:01]`, expressão incerta).

## Fluxo E — Controle de horas e item de desenvolvimento

1. Registrar as horas no Gantt / nos projetos separados — `[00:07:08]`–`[00:07:15]`.
2. Preencher o mapa de acompanhamento — `[00:07:19]`.
3. Ao abrir o item de desenvolvimento, avisar para marcar o início do desenvolvimento; sem o item, não há como iniciar — `[00:07:30]`–`[00:07:39]`.
4. Item em definição de prazo, marcado em vermelho, foi discutido — `[00:07:52]`–`[00:08:27]`. *Procedimento não demonstrado.*

## Exceções e pontos de atenção

- Sem documento anexado: enviar `null`, não um agrupamento vazio (`[00:03:50]`).
- Campo sem valor cadastrado: enviar `null` (`[00:03:43]`–`[00:03:48]`).
- Execução por web service sem código do perfil configurado: o fluxo falha segundo a fala (`[00:05:22]`–`[00:05:34]`).

## Resultado

- Especificação de agrupamento `attachment_document` com três campos e regra de `null`.
- Documento de teste e apresentação na review.
- Itens pendentes: decisão código × descrição, confirmação da base, configuração do perfil no web service — ver [`incertezas.md`](incertezas.md).
