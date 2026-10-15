# Glossário — Gravando 2026-09-23 164626.mp4

| Termo / sigla | Significado sustentado pela fala | Categoria | Fonte / timestamp |
|---|---|---|---|
| **Autorizador** | Aplicação em que os participantes procuram a rotina para consultar/anexar documentos a uma proposta; tela e caminho exatos não confirmados. | SISTEMAS | Transcrição — `00:05:01–00:05:26`, `00:10:24–00:11:37` |
| **CQ** | Área/base em que a conversa propõe executar o teste; expansão e arquitetura do ambiente não verificadas. | SISTEMAS / INFRA_E_ACESSO | `00:00:11–00:00:39` |
| **GED / GEDOC / G-Doc / GDock** | Nomes ou grafias ASR relacionados ao repositório/serviço de documentos e a uma consulta por perfil. Não afirmar que todas as grafias correspondem ao mesmo componente. | SISTEMAS | `00:11:25–00:12:50`, `00:14:11–00:14:40`, `00:21:14–00:21:22` |
| **Perfil GEDOC** | Perfil citado durante a análise de mensagens de permissão para consultar/anexar; o perfil e as chaves mencionados são observações de um teste, não configuração recomendada. | INFRA_E_ACESSO | `00:12:20–00:14:40`, `00:15:58–00:16:12` |
| **Chave 2 / chave 4** | Referências a chaves em mensagens de permissão no teste descrito; escopo, nome técnico e privilégio efetivo precisam ser confirmados com o responsável pelo GED. | INFRA_E_ACESSO | `00:12:20–00:12:50`, `00:14:23–00:14:40`, `00:15:58–00:16:12` |
| **Plugin de envio ao sistema externo** | Componente que, segundo a conversa, recebe o JSON com informações dos documentos anexados e o envia ao sistema externo. Nome técnico/contrato não confirmados. | SISTEMAS | `00:00:43–00:01:23`, `00:21:45–00:21:55`, `00:23:56–00:25:23` |
| **JSON** | Formato discutido para transportar dados do documento ao plugin; o payload integral e o schema vigente não estão disponíveis nesta pasta. | SISTEMAS | `00:03:55`, `00:04:19–00:04:51`, `00:19:46–00:20:53`, `00:21:45–00:25:23` |
| **Objeto pai “Attach documento”** | Rótulo ouvido enquanto os participantes discutem o agrupador JSON; grafia/capitalização e posição na hierarquia são incertas. | SISTEMAS | `00:20:22–00:20:39` |
| **`document_type`** | Campo indicado verbalmente como tipo/sigla do documento; código versus descrição não resolvido. | SISTEMAS / NEGOCIO | `00:19:46–00:20:18`, `00:20:42–00:20:53` |
| **`document_name`** | Campo indicado verbalmente como nome do documento anexado. Tipo, regra de preenchimento e origem precisam de confirmação. | SISTEMAS | `00:19:46–00:20:18`, `00:20:42–00:20:53` |
| **`user`** | Campo associado ao usuário responsável pela anexação, conforme a explicação verbal; formato/identificador esperado não confirmado. | SISTEMAS / INFRA_E_ACESSO | `00:19:46–00:20:18`, `00:20:42–00:20:53` |
| **`null`** | Valor que a conversa diz ter sido devolvido no cenário sem documento. Deve ser conferido contra o contrato, que pode exigir `null`, lista vazia ou propriedade omitida. | SISTEMAS | `00:04:43–00:04:51`, `00:25:14–00:25:19` |
| **Esteira** | Fluxo de processamento da proposta; o retorno/reenvio ou a permanência em loop são discutidos sem decisão formal comprovada. | PROCESSOS | `00:02:28–00:02:37`, `00:23:07–00:26:06` |
| **Reenvio / retorno / loop** | Alternativas de fluxo ao acrescentar documento e enviar de novo; a fala relata retorno, mas não estabelece regra de idempotência nem desenho oficial. | PROCESSOS | `00:23:07–00:25:34`, `00:25:47–00:26:06` |
| **CNPJ** | Atributo citado como exemplo de uma implementação anterior, distinto do documento anexado desta conversa; nenhum valor é necessário à análise. | NEGOCIO / SISTEMAS | `00:01:44–00:02:12` |
| **CPF cliente** | Rótulo mencionado ao consultar informações de proposta; a transcrição não apresenta número completo. | NEGOCIO | `00:21:58–00:22:07`, `00:23:46–00:25:09` |
| **“CPS” / “CCD”** | Siglas reconhecidas pelo ASR em referência ao tipo de documento; grafia e significado precisam ser conferidos. | DÚVIDA_OU_CONFLITO | `00:10:28–00:10:32`, `00:19:46–00:20:09` |

Ver também [`incertezas.md`](incertezas.md) e as divergências de nomenclatura registradas em [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md). Não usar nenhuma grafia ASR como contrato técnico sem confirmação na EF vigente.
