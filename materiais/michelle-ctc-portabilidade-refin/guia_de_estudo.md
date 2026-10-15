> **Publicação autorizada pelo responsável em 2026-10-13.** A documentação do projeto declara que os dados são fictícios/de teste. Este resumo não reproduz nomes pessoais, detalhes de cliente não necessários, IDs de proposta ou configuração de esteira.

# Guia de estudo — MICHELLE CTC PORTABILIDADE REFIN.mp4

- **Categoria:** `PROCESSOS`, `SISTEMAS`, `NEGOCIO`, `DÚVIDA_OU_CONFLITO`
- **Sistema:** esteiras de portabilidade e refinanciamento (`refim`), integração/retorno de CTC e tela unificada (nomes de produto e telas não demonstrados)
- **Assunto:** sincronização de duas propostas relacionadas e proposta de teste para o processo “CTC aciona refim” e a etapa de espera da tela unificada
- **Fonte:** `MICHELLE CTC PORTABILIDADE REFIN.mp4` (473540507 bytes; SHA-256 `621565bd…`), duração declarada `00:16:56.62`
- **Confiança da extração:** **baixa a média** — síntese baseada em ASR `large-v3` com 388 segmentos; a mídia e o desenho não foram inspecionados visualmente neste lote. Vários nomes de etapas foram reconhecidos de forma instável.

## 1. Objetivo e contexto

A conversa discute como uma proposta de **portabilidade** ligada a um **refinanciamento** deveria avançar em esteiras relacionadas. A preocupação de negócio é que os dados do refinanciamento — mencionam especialmente saldo/valores usados para gerar a CCB — estejam consistentes antes de avançar a portabilidade e concluir etapas posteriores (**00:03:36–00:04:59**).

**Limite importante:** a pessoa que apresenta o desenho diz explicitamente que ele foi feito para **outro cliente**, não exatamente para o C6, e que é apenas um exemplo de funcionamento (**00:00:05–00:00:23; 00:15:34–00:16:07**). Não copiar a configuração desse desenho para a esteira do C6.

## 2. Conceitos sustentados pela fala

### 2.1 Portabilidade e refim são fluxos relacionados

- A explicação descreve duas propostas/esteiras — portabilidade e refim — que podem avançar em paralelo, mas precisam coordenar estados e resultados (**00:00:24–00:01:22**).
- A fala diz que uma portabilidade pode ter um refim vinculado e que, no retorno associado ao CTC, um processo pode acionar o avanço do refim (**00:01:00–00:01:22**).
- Se houver várias portabilidades ligadas ao mesmo refim, a explicação afirma que todas precisam passar por determinada etapa antes do avanço do refim (**00:02:00–00:02:30**). A regra e a etapa exata não foram confirmadas visualmente.

### 2.2 Etapa de espera e tela unificada

- A conversa distingue uma etapa descrita como **“aguarda análise de refim de portabilidade”** e outra como **“aguarda alteração unificada”** (**00:03:02–00:03:15; 00:07:25–00:07:47**).
- O cenário falado é que a tela unificada trata as propostas de portabilidade e refim juntas; uma etapa de espera permitiria manter ambas no ponto de coordenação até que a alteração fosse feita (**00:02:40–00:03:36; 00:05:31–00:06:00**).
- A relação entre bloqueio, integração do refim e liberação da portabilidade não fica consistente ao longo da conversa. Ver [`incertezas.md`](incertezas.md); não inferir a regra de transição.

### 2.3 Motivo de negócio

A justificativa apresentada é evitar que a portabilidade avance antes de os dados do refim estarem conferidos e, com isso, produzir uma CCB com valores divergentes (**00:03:36–00:04:59**). O vídeo não comprova a regra em tela nem especifica quais campos ou status determinam a liberação.

## 3. Cenário de teste discutido (ainda não aprovado)

A conversa sugere criar uma portabilidade com refim associado, que gera dois registros/números de proposta, e levar ambos a um ponto controlado de teste (**00:06:22–00:07:47; 00:09:28–00:10:33; 00:12:50–00:13:18**). Em seguida, os participantes discutem testar configurações de esteira separadas por tipo de proposta/convênio/produto, mantendo o processo de acionamento e a etapa de espera pertinente (**00:10:34–00:12:14; 00:14:21–00:16:39**).

Isso é **uma proposta exploratória**, não um teste executado nem um passo a passo validado. A fala também sugere, para aquele ambiente de teste, pular etapas de CTC por falta de configuração/acesso (**00:06:39–00:06:49; 00:09:23–00:09:46**). Não transportar essa simulação para produção nem contornar a integração real.

## 4. Observações com timestamps

- **00:00:05–00:00:23:** o desenho é apresentado como exemplo de outro cliente, não como diagrama C6.
- **00:00:24–00:02:30:** explicação de duas esteiras, vínculo portabilidade/refim, acionamento e múltiplas portabilidades.
- **00:02:40–00:03:36:** diferença entre fluxo normal e tela unificada; etapa de espera e status esperado.
- **00:03:36–00:04:59:** dependência entre avanço do refim, consistência de valores/CCB e continuação da portabilidade.
- **00:05:09–00:06:00:** hipótese de encaminhar o acionamento para “aguarda alteração unificada”; a fala diz que o processo acionaria, mas não validaria.
- **00:06:22–00:08:36:** desenho do teste pretendido e discussão sobre quais etapas deveriam segurar ou liberar as propostas.
- **00:09:23–00:12:14:** teste sem CTC configurado, necessidade sugerida de fluxos separados e discussão de produtos/convênios.
- **00:12:50–00:16:39:** modo verbal de criar portabilidade e refim e lista de processos mencionados; sem demonstração visual verificável.

## 5. O que não concluir

- Não assumir que o desenho/fluxo de outro cliente corresponde ao C6.
- Não afirmar que uma esteira deve liberar ou bloquear a outra sem confirmação da regra de negócio e dos status efetivos.
- Não usar “CTC aciona refim”, “aguarda alteração unificada”, “guarda” ou “MEI” como nomes oficiais sem validar grafia e semântica.
- Não pular CTC, remessa, liberação ou outras integrações fora de um ambiente de teste autorizado.
- Nenhum SQL, tela de produto, configuração real ou resultado de teste foi conferido neste lote.

Ver também: [`procedimentos.md`](procedimentos.md), [`perguntas.md`](perguntas.md), [`glossario.md`](glossario.md), [`incertezas.md`](incertezas.md), [`transcricao.md`](transcricao.md) e [`metadados.md`](metadados.md).
