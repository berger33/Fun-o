# Glossário — Como fazer EPT.mp4

| Termo / sigla | Significado sustentado pela fala | Categoria | Fonte / timestamp |
|---|---|---|---|
| **EPT** | Artefato de teste que descreve cenários, pré-condições, etapas e resultados esperados; a aula enfatiza que deve ser reproduzível por outra pessoa. | PROCESSOS | Transcrição — `00:07:08–00:08:05`, `00:09:17–00:12:47`, `00:31:16–00:32:06` |
| **“IPT”** | Forma reconhecida pelo ASR em algumas falas para o artefato de teste; provavelmente “EPT”, mas a grafia não foi conferida na tela. | DÚVIDA_OU_CONFLITO | `00:02:19–00:02:21`, `00:07:08`, `00:31:16–00:31:50` |
| **EF** | Especificação funcional usada para entender objetivo, comportamento atual, requisitos, premissas e dependências antes de escrever testes. | PROCESSOS | `00:02:19–00:02:48`, `00:27:25–00:30:21` |
| **Pré-condição / premissa / pós-condição** | Informação sobre o estado/configuração necessários antes do caso e o estado esperado depois; nomes exatos das colunas dependem do template. | PROCESSOS | `00:09:17–00:10:05`, `00:26:47–00:27:16` |
| **Caso / cenário / etapa** | Estrutura da EPT descrita como casos com várias etapas; ao começar caso novo, o modelo mostrado separa a seção e preenche nova linha. | PROCESSOS | `00:09:36–00:12:47` |
| **Web Autorizador / Autorizador** | Aplicação citada no contexto de API de consulta e configuração de despesa/proposta; telas/caminhos não conferidos visualmente. | SISTEMAS | `00:03:00–00:04:19`, `00:18:12–00:18:35`, `00:23:18–00:24:21` |
| **Web API Consulta de Propostas (detalhada)** | Serviço/endpoint verbalmente descrito como consulta com parâmetros de entrada e retorno detalhado, incluindo novos objetos; rota/schema precisam de confirmação. | SISTEMAS | `00:02:48–00:06:18` |
| **Objeto `Despesa`** | Novo objeto citado na saída da API; campos exatos foram apontados para EF/anexo, mas não são enumerados com clareza no ASR. | SISTEMAS / NEGOCIO | `00:03:11–00:03:21`, `00:06:28–00:06:52`, `00:13:05–00:15:06` |
| **Objeto `Reaproveitamento`** | Objeto citado na saída e no exemplo de refinanciamento com reaproveitamento de seguro; contrato e campos não validados. | SISTEMAS / NEGOCIO | `00:03:24–00:03:42`, `00:06:53–00:07:08`, `00:18:35–00:21:18` |
| **Parâmetro de entrada / saída** | A aula diferencia valores enviados à API dos dados apresentados como retorno; o exemplo cita número de proposta e usuário como entradas. | SISTEMAS | `00:04:47–00:06:18` |
| **Documentação da API** | Documento/página usado para comparar a estrutura de campos com a EF; a fala descreve visualmente uma “telinha azul”, sem confirmar ferramenta específica. | SISTEMAS / PROCESSOS | `00:14:30–00:15:06`, `00:17:05–00:18:08` |
| **Reaproveitamento de seguro** | Exemplo de negócio em que, no refinanciamento, uma parte do prêmio anterior é descontada do novo seguro; valores ouvidos são apenas ilustrativos, não critérios de teste. | NEGOCIO | `00:18:35–00:20:33` |
| **Refinanciamento / proposta refim** | Tipo de proposta que a fala associa ao cenário de reaproveitamento; regra oficial e estados do produto dependem da EF. | NEGOCIO | `00:18:35–00:18:53`, `00:19:31–00:20:33` |
| **Despesa / política de despesa** | Configuração citada como preparação para registrar uma proposta com a despesa necessária ao exemplo; sequência e tela não verificadas. | SISTEMAS / NEGOCIO | `00:15:09–00:16:10`, `00:18:12–00:18:35` |
| **Recálculo** | Processo que, segundo a leitura verbal da EF do exercício, aplicaria validações de valor solicitado e tolerância. | PROCESSOS / NEGOCIO | `00:28:03–00:29:36` |
| **Margem de tolerância** | Parâmetro do exercício de recálculo: limites de valor solicitado no convênio e tolerância percentual; fórmula/limites não foram validados. | NEGOCIO | `00:28:03–00:29:36` |
| **`Mesa C6`** | Local/pasta mencionado ao orientar busca de documentos de referência; não há endereço de rede completo validado. | INFRA_E_ACESSO | `00:00:23–00:00:33` |
| **“Nexo”, “UTE”, “UTPT”** | Grafias reconhecidas pelo ASR em contexto de documentos/projetos de referência; função, expansão e grafia não confirmadas. | DÚVIDA_OU_CONFLITO | `00:04:23`, `00:33:52–00:34:02` |

Ver [`incertezas.md`](incertezas.md). A transcrição foi preservada integralmente por orientação do responsável; termos ASR não são schema nem runbook.
