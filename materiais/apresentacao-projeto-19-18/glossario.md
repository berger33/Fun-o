> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste** (não há dado real de cliente ou de pessoa). Preservados
> conforme instrução: o nome **Função Sistemas** e os **nomes dos operadores**. Não são
> publicadas **imagens de pessoas** (câmeras/participantes) — as capturas ficam restritas às
> telas do documento.

# Glossário — Apresentação projeto 19-18.mp4


| Termo / sigla | Significado sustentado pelo vídeo | Categoria | Timestamp |
|---|---|---|---|
| **CCB (INSS)** | Cédula de Crédito Bancário do INSS; o documento cujo modelo está sendo alterado. No vídeo aparece também como "CCB do refim" (refinanciamento) e "CCB do INSS". | NEGOCIO | 00:00:25, 00:01:41, item 1.1 (tela) |
| **Refim / refinanciamento** | Operação que agrupa **múltiplos contratos** (operações originais) e cujas informações aparecem no documento; "refinanciamento com múltiplos contratos" é o cenário do item. | NEGOCIO | 00:00:25, 00:01:41, item 1.1 (tela) |
| **Operações originais / contratos de origem** | Contratos anteriores que compõem o refinanciamento; seus números são exibidos no documento. | NEGOCIO | 00:00:49, item II (tela) |
| **Credor** | Titular/beneficiário das operações de origem; a variável 2 controla sua exibição (única quando o mesmo, concatenada quando distinta). | NEGOCIO | 00:01:00 – 00:01:37 |
| **Saldo devedor** | Valor devido em cada contrato; a variável 3 passa a exibir a **somatória** de todos os contratos do refinanciamento. | NEGOCIO | 00:01:37 – 00:01:55 |
| **Variável (de documento)** | Campo/etiqueta do modelo de documento que será incluída/alterada para controlar a exibição das informações na CCB. | SISTEMAS | 00:00:19, item I (tela) |
| **SIC Minutas** | Módulo onde serão criadas as novas variáveis, segundo o documento ("módulo SIC Minutas do Autorizador"). | SISTEMAS | item I (tela, 00:05:03) |
| **Web Autorizador** | Módulo indicado no **limite de escopo** do documento como destino das implementações. | SISTEMAS | item 1.3 (tela, 00:00) |
| **API de formalização** | Interface que precisa ser atualizada com as novas variáveis para que a jornada de contratação emita a CCB atualizada. | SISTEMAS | 00:02:09 – 00:02:25 |
| **Jornada de contratação** | Fluxo do sistema em que o usuário contrata e **emite/extrai a CCB** ("tirar a CCB"). | PROCESSOS | 00:02:13 – 00:02:25 |
| **Agrupamento (contratos/operação)** | Agrupamento do documento onde hoje os números dos contratos aparecem um abaixo do outro. | SISTEMAS | 00:00:34 – 00:00:40 |
| **Ponto e vírgula (`;`)** | Separador definido para exibir os valores **lado a lado** (contratos e credores distintos). | NEGOCIO | 00:00:49, 00:03:08 |
| **CQ** | Controle de qualidade; etapa de qualidade cujas horas são confirmadas na reunião. | PROCESSOS | 00:07:04, 00:07:29 |
| **Plano de teste** | Artefato de teste cujo esforço é citado ("21, 3 e 16"). | PROCESSOS | 00:07:32 |
| **Reprot** | Referência de página do documento de teste exibido ("Página 3 REPROT - CÉDULA"). | SISTEMAS | 00:06:18 (tela) |
| **Convênio** | Local citado como possível origem da parametrização de credor ("não sei se é no convênio"). | DÚVIDA_OU_CONFLITO | 00:06:19 |
| **Fonte / query** | Verificação técnica proposta para descobrir se existe parametrização do credor; **não** foi executada no vídeo. | DÚVIDA_OU_CONFLITO | 00:06:12 – 00:06:22 |
| **Proposta** | Origem presumida da informação de credor, alternativa à parametrização (hipótese). | DÚVIDA_OU_CONFLITO | 00:06:34 – 00:06:38 |
| **OS 552267** | Número da ordem de serviço interna que titula o documento e a reunião; **não é** dado de cliente. | PROCESSOS | título (tela, 00:00) |