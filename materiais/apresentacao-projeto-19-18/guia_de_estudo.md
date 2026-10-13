> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste** (não há dado real de cliente ou de pessoa). Preservados
> conforme instrução: o nome **Função Sistemas** e os **nomes dos operadores**. Não são
> publicadas **imagens de pessoas** (câmeras/participantes) — as capturas ficam restritas às
> telas do documento.

# Guia de estudo — Apresentação projeto 19-18.mp4


**Categoria:** `SISTEMAS`, `NEGOCIO`, `PROCESSOS`, `DÚVIDA_OU_CONFLITO`
**Sistema:** módulos **SIC Minutas** e **Web Autorizador** (CCB do INSS — consignado)
**Assunto:** especificação funcional de novo modelo de CCB em refinanciamento com múltiplos
contratos: exibição de contratos de origem, credor e somatória de saldo devedor; atualização da API
de formalização; estimativa de esforço (desenvolvimento, CQ e plano de teste)
**Fonte:** `Apresentação projeto 19-18.mp4` (179956679 bytes), reunião de 2026-08-19 ~11:34 (BRT),
duração 00:07:44.870 — SHA-256 `ac4b6621…`
**Confiança da extração:** **média-alta** — áudio inteligível na maior parte (ruído de 00:04:37 a
00:05:47 e fala sobreposta em 00:03:48–00:04:37), documento lido com boa legibilidade; sem SQL
executado no vídeo.

## 1. Objetivo e público

- **Objetivo do vídeo:** apresentar o item de trabalho da ordem de serviço interna (OS 552267) que
  adequa a exibição de informações de operações originais, credor e saldo devedor na CCB do INSS em
  casos de refinanciamento com múltiplos contratos, alinhar a dúvida sobre identificação do credor e
  confirmar o esforço estimado.
- **Público/pré-requisitos:** pessoas de desenvolvimento, CQ (controle de qualidade) e produto do
  time; exige conhecer o fluxo de **refinanciamento com múltiplos contratos** e a geração de CCB nos
  módulos **SIC Minutas**/**Web Autorizador**.

## 2. O problema hoje (00:00:19 – 00:00:40)

- **[00:00:19]** O banco (cliente) pediu a criação de **três variáveis** para o documento da CCB de
  refinanciamento quando existem múltiplos contratos.
- **[00:00:34 – 00:00:40]** No agrupamento atual da CCB, em "contratos"/"operação", os números dos
  contratos aparecem **um abaixo do outro**.
- **[00:00:00 — leitura do documento, item 1.2]** "No modelo atual de CCB do INSS, quando ocorre
  refinanciamento envolvendo mais de um contrato, as informações das operações originais, credor e
  saldo devedor são exibidas uma abaixo da outra no documento."

## 3. Especificação técnica do documento (leitura de tela; ver `transcricao.md`)

Título: **ESPECIFICAÇÃO FUNCIONAL — Ordem de Serviço: 552267 — (ÁGIL) (I) Atualização Novo Modelo CCB**.

1. **[1.1 OBJETIVO]** "Adequar a forma de exibição das informações de operações originais e saldo
   devedor no modelo de CCB do INSS em casos de refinanciamento com múltiplos contratos."
2. **[1.3 LIMITES DO ESCOPO]** "As implementações descritas neste escopo serão disponibilizadas para
   o módulo **Web Autorizador**."
3. **[Funcionamento, itens I a III — 00:05:03]**
   - **I.** "Esta implementação prevê a criação de novas variáveis no módulo **SIC Minutas** do
     Autorizador, com o objetivo de adequar a apresentação das informações referentes às operações
     originais em cenários de refinanciamento que envolvam múltiplos contratos na CCB do INSS."
   - **II. (variável 1 — contratos):** "permitirá que os números dos contratos de origem sejam
     exibidos na mesma linha do documento, apresentados de forma sequencial, lado a lado e separados
     por ponto e vírgula, conforme demonstrado na Figura 1."
   - **III. (variável 2 — credor):** "variável específica para apresentação da informação do credor,
     de forma que o dado seja exibido apenas uma única vez no documento, mesmo quando houver mais de
     uma operação original vinculada ao refinanciamento, evitando repetição desnecessária da
     informação. Nos casos em que houver credores distintos entre as operações de origem, estes
     deverão ser apresentados de forma sequencial, lado a lado, separados por ponto e vírgula."
   - **IV. (variável 3 — saldo devedor):** o item IV não aparece completo nos quadros capturados;
     pela fala **[00:01:37 – 00:01:55]**, a terceira variável é a **somatória dos saldos devedores**
     de todos os contratos relacionados àquele refinanciamento (hoje cada operação mostra o seu).

## 4. Fala do apresentador que consolida as três variáveis (00:00:49 – 00:01:55)

| # | Variável | Regra falada | Timestamp |
|---|---|---|---|
| 1 | Contratos de origem | exibir os números dos contratos **lado a lado, separados por ponto e vírgula** (hoje: um abaixo do outro) | 00:00:49 – 00:00:56 |
| 2 | Credor | **mesmo credor → aparece uma única vez**; credores **diferentes → todos aparecem**, separados por ponto e vírgula | 00:01:00 – 00:01:37, reforçado em 00:02:36–00:03:12 |
| 3 | Saldo devedor | **somatória** dos saldos devedores de todos os contratos relacionados ao refinanciamento | 00:01:37 – 00:01:55 |

## 5. Segundo item: API de formalização (00:02:09 – 00:02:28)

- Atualizar a **API de formalização** com as novas variáveis, para que na **jornada de contratação**
  seja possível **emitir a CCB já com as variáveis atualizadas**.
- Observação de escopo: a leitura de tela do documento restringe as implementações ao módulo **Web
  Autorizador** (item 1.3); a fala, porém, fala em "SIC Minutas do Autorizador" e na "jornada de
  contratação" — **conciliação pendente** (ver `incertezas.md`, item 4).

## 6. Alinhamento do credor (00:02:36 – 00:03:14)

- Cenário do participante B: contrato original para o **credor X**, outro contrato para o **credor
  Y** → "aí eu vou concatenar igual estou fazendo com a operação?"
- Resposta: **sim** — mesma lógica da concatenação de operações: se for o mesmo credor, aparece uma
  vez; se diferente, aparecem ambos, **separados por ponto e vírgula**, "igual ao contrato".

## 7. A dúvida em aberto: parametrização/identificação do credor (00:03:34 – 00:06:45)

- **[00:03:34 – 00:03:56]** Dúvida (participante D): como distinguir a informação do credor para a
  operação X e a operação Y — **como distinguir ou como parametrizar**?
- **[00:04:00 – 00:04:37]** Resposta no sentido de que a variável **não discrimina a operação**: se
  houver mais de um credor, os dois aparecem; o documento indicará que para todas as operações
  daquele refinanciamento existe cada credor, **sem determinar qual operação é distinta**.
- **[00:04:37 – 00:05:47]** Ruído de áudio (televisão/microfone aberto); repetição pedida; a dúvida
  é encaminhada para o **chat** pelo participante remoto (E).
- **[00:06:00 – 00:06:45]** Encaminhamento: verificar no **fonte/query** se há (ou não)
  parametrização de credor ("Não sei se é no convênio. Vou ver certinho aqui"); hipótese levantada:
  **não é parametrização**, e sim informação da proposta; combinaram **alinhar com desenvolvimento**
  e enviar a resposta depois.
- **Status:** **não concluído no vídeo** — é a principal pendência técnica registrada.

## 8. Estimativas de horas (00:06:49 – 00:07:42)

| Item de trabalho | Esforço falado | Timestamp |
|---|---|---|
| Item 1 — criação das variáveis (desenvolvimento) | **28 h** | 00:07:02, 00:07:21 |
| Item 2 — API de formalização (atualização) | **6 h** | 00:07:13, 00:07:24 |
| CQ (controle de qualidade) | "21" (citado como CQ no início), depois "ok para o CQ também" pelo participante E | 00:07:04, 00:07:29 |
| Plano de teste | "**21, 3 e 16**" (valores falados em sequência, sem explicar a que correspondem) | 00:07:32 |

- Confirmado ao final: "as horas vão ficar as mesmas que vocês tinham passado" **[00:06:54]**.
- **Ambiguidade:** a distribuição "21, 3 e 16" para o plano de teste não é explicada no vídeo (ver
  `incertezas.md`, item 5).

## 9. Erros, cuidados e ressalvas

- **Não publicar** este conteúdo fora dos canais autorizados: é especificação interna de cliente
  (ver `incertezas.md`, item 1).
- Não confundir a **numeração da OS interna** (552267) com número de contrato/operação de cliente: a
  figura do documento contém números de contrato usados como exemplo (omitidos aqui).
- A dúvida de parametrização **não** foi resolvida na reunião: não tratar a hipótese "não é
  parametrização" como regra.
- Áudio com ruído (00:04:37–00:05:47) e sobreposição de falas (00:03:48–00:04:37): não inferir o que
  não ficou claro.

## 10. Resumo em uma frase

Em **00:07:44**, a reunião detalha três novas variáveis da CCB de refinanciamento (contratos lado a
lado separados por ponto e vírgula; credor exibido uma única vez quando o mesmo e concatenado quando
diferente; somatória dos saldos devedores), atualiza a API de formalização com elas e confirma o
esforço (28 h desenvolvimento no item 1, 6 h no item 2, plano de teste citado como "21, 3 e 16"),
deixando **aberta** a questão de como distinguir/parametrizar o credor por operação.