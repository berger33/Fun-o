# Guia de estudo — depuração no Test API (Jonas)

- **Categoria:** `SISTEMAS`, `PROCESSOS`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO` (sem `SQL`: nenhuma
  consulta é citada nesta conversa)
- **Sistema:** Função Sistemas — **API de inclusão de proposta** (`FIApiAutIncluirProposta`) chamada
  pelo **Test API**; **Autorizador** como origem do payload; dois caminhos de publicação do endpoint
  (`…/Mesa C6/Regressivo <n>/FIApiAutIncluirProposta/` e `…/C6/Api/FIApiAutIncluirProposta/`)
- **Assunto:** como depurar um envio de refin recusado pela API — ler a mensagem de erro do modelo,
  **isolar campo por campo** no Test API e decidir entre ajustar o payload, escalar para o grupo ou
  tratar como incidente.
- **Fonte:** recorte textual de conversa de trabalho com **Jonas**, fornecido pelo responsável em
  **2026-10-15**; âncoras `[Mnn]` conforme [`../CONVENCOES_FONTES_TEXTUAIS.md`](../CONVENCOES_FONTES_TEXTUAIS.md)
- **Confiança da extração:** **alta** para o **texto do erro** (colado literalmente na conversa) e
  para a **postura de escalada** (explícita); **baixa** para reconstruir a sequência exata de
  tentativas (a requisição não aparece) e para o desfecho do caso (não há confirmação de resolução).

## 1. Contexto

O operador **William** não consegue incluir uma proposta de **refinanciamento** pela API
`FIApiAutIncluirProposta`. Ele relata que **simular pelo Autorizador funciona**, mas o envio pelo
**Test API** “ainda dá trabalho” (o relato está na conversa irmã, `[M10]` de
[`../conversa-matheus-refin-api/transcricao.md`](../conversa-matheus-refin-api/transcricao.md)).
**Jonas** conduz o diagnóstico: pede o **endpoint** usado, pergunta se os **campos** foram preenchidos
no Test API, sugere **remover o campo** para observar a crítica e, por fim, encaminha o caso para o
**grupo** e para o responsável pela API (**Santana**).

## 2. Linha de raciocínio da conversa

| Âncora | O que acontece | O que se aprende |
|---|---|---|
| `[M01]`, `[M02]` | O interlocutor mostra o CPF de uma **proposta nova criada** e depois recua (“esquece”) | Existe risco de **descompasso entre a proposta criada e o payload** em teste; o dado é mascarado aqui |
| `[M03]`–`[M05]` | Jonas pede a **URL da API**; o operador mostra **dois caminhos diferentes** para o mesmo endpoint | Antes de discutir payload, **confirme em qual caminho/ambiente** está testando: há mais de uma publicação do mesmo serviço |
| `[M06]` | O operador reproduz: **retirando o número da operação** do payload, vem uma crítica | O erro depende do **que foi removido**: a crítica é a pista, não o obstáculo |
| `[M07]`, `[M08]` | Jonas pergunta se os campos foram preenchidos no Test API; resposta: “Sim” | Primeiro se confirma **o que foi preenchido na ferramenta** (o Test API tem campos próprios; preencher lá ≠ preencher o JSON) |
| `[M09]`–`[M12]` | Instrução: **não preencher esse campo** para ver; “só a operação” | Técnica de **isolamento**: reduzir o payload ao mínimo e reintroduzir campo a campo |
| `[M13]`, `[M14]` | Erro de modelo colado: `Error converting value {null} to type '…Models.SubTipoRefin'`, em `OperacoesRefin.SubTipoRefin`, `CODIGO 100000002` | O campo é **obrigatório no modelo** e **não aceita nulo**: o JSON não consegue virar objeto no servidor |
| `[M15]`, `[M16]` | Jonas: “ai parece incidente”. Operador: tirando o **número da operação**, a API **pede o número da operação** | Ficar removendo campos chega a um limite: um deles é **indispensável**; aí a decisão deixa de ser “ajustar payload” |
| `[M17]`, `[M18]`, `[M22]`–`[M24]` | Encaminhamento: **mandar no grupo**, Jonas continua tentando, **Santana** (frente de API) chama | Escalada saudável: **canal coletivo + par que reproduz** + dono técnico do componente |
| `[M19]`, `[M20]` | Operador conclui “o que dá a entender que seria o próximo passo” e manda no grupo | Leitura de comportamento da API como **evidência de evolução de modelo** — hipótese a confirmar |

## 3. Anatomia do erro de modelo (`[M13]`)

```
"MENSAGEM": "Modelo de entrada de dados inválido:  Error converting value {null} to type
'FIApiAutIncluirProposta.Models.SubTipoRefin'. Path 'OperacoesRefin.SubTipoRefin', line 1,
position 1117. [Objeto: 'OperacoesRefin.SubTipoRefin']",
"CODIGO": 100000002
```

| Elemento | Leitura |
|---|---|
| `Modelo de entrada de dados inválido` | Prefixo de negócio da API: o corpo recebido não atende ao modelo esperado |
| `Error converting value {null} to type '…Models.SubTipoRefin'` | Erro de **desserialização**: chegou `null` onde o modelo tem um **enum** que não aceita nulo |
| `Path 'OperacoesRefin.SubTipoRefin'` | Localização exata do campo: dentro do bloco `OperacoesRefin` — o mesmo bloco do payload de refin da conversa irmã |
| `line 1, position 1117` | Posição no JSON **minificado** (linha 1, caractere ~1117). Serve para achar o campo no corpo enviado |
| `[Objeto: 'OperacoesRefin.SubTipoRefin']` | Repetição do objeto afetado |
| `CODIGO: 100000002` | Código do erro de modelo. **Não há catálogo de códigos na fonte** — não inferir significado além do texto |

**Consequência prática (a regra que sobra):** em refinanciamento, `SubTipoRefin` **precisa ir
preenchido com um valor válido do enum** — não basta omitir. Na conversa irmã, o envio que funcionou
usou o valor literal `"NaoDefinido"` ([`../conversa-matheus-refin-api/transcricao.md`](../conversa-matheus-refin-api/transcricao.md),
`[M07]`).

> **Hipótese a validar (não é fato):** usar `"SubTipoRefin": "NaoDefinido"` é o que destrava o envio
> de um refin sem subtipo específico. A ligação vem de **duas fontes independentes** do acervo (um
> payload que passou e uma crítica que recusou o nulo), mas **nenhuma das duas confirma o enum
> completo** nem que o valor seja aceito pelo modelo na versão em uso. Confirmar com o responsável
> pela API — ver [`incertezas.md`](incertezas.md) item 2.

## 4. Método de isolamento no Test API (o que a conversa ensina)

1. **Reduza ao mínimo.** Jonas manda preencher **somente a operação** (`[M11]`) e **não preencher** o
   campo suspeito (`[M09]`). Payload mínimo → erro mais legível.
2. **Leia a crítica como resposta do modelo**, não como “erro genérico”: o texto diz *qual* campo, em
   *que* caminho e em *que* posição (`[M13]`).
3. **Reintroduza um campo por vez.** A pergunta “se eu tiro ele, critica esse campo” (`[M14]`) mostra
   o ciclo: remove → observa → volta.
4. **Pare quando chegar a um campo indispensável.** Tirando `NumeroOperacao`, a API **pede** o número
   da operação (`[M16]`) — não há como prosseguir removendo; nesse ponto o problema não é mais de
   payload mal montado.
5. **Confirme a ferramenta.** Antes de tudo, confirmar se os campos foram preenchidos **no Test API**
   (`[M07]`) — a ferramenta e o JSON podem divergir.

## 5. Classificação e escalada

- Jonas é explícito: **“ai parece incidente”** (`[M15]`) — a leitura dele é de que o comportamento
  tem cara de falha de sistema, **não** de dado de teste. (Compare com a conversa do Matheus, em que
  dado errado de teste **não** é incidente — `[M04]` daquele pacote.)
- A conduta imediata recomendada antes de registrar incidente:
  1. **levar ao grupo** (“manda lá no grupo tbm para ver se o pessoal consegue ajudar”, `[M17]`);
  2. **alguém tentar reproduzir em paralelo** (“eu to tentando fazer aqui”, `[M18]`, retomado em `[M24]`);
  3. **envolver o dono da frente de API** — Santana chama para ver junto (`[M22]`).
- Isso é o oposto de escalar sozinho e no escuro: **coletar segunda opinião e reprodução** antes de
  classificar.

## 6. Dois caminhos para o mesmo endpoint (`[M04]`, `[M05]`)

- `http://<servidor>/Mesa C6/Regressivo 540791/FIApiAutIncluirProposta/` — caminho dentro de uma área
  de **“Mesa C6”**, com uma pasta de **regressivo** numerada (540791).
- `http://<servidor>/C6/Api/FIApiAutIncluirProposta/` — caminho em **`C6/Api`**.
- O operador diz que **começou pelo primeiro** (“devo ter copiado no grupo”) e **passou ao segundo**
  por não estar conseguindo.
- **Aprendizado operacional:** o mesmo serviço tem **publicações distintas** por área/ambiente. Antes
  de investigar payload, confirme **em qual** endpoint se está testando — e, ao reportar problema,
  **informe o caminho completo** (é a primeira coisa que Jonas pediu: `[M03]`).
- Nomes de servidor mascarados por higiene de infraestrutura; a **estrutura do caminho** foi
  preservada porque é ela que identifica as publicações.

## 7. Erros, riscos e cuidados

- **Não usar estas URLs como referência de ambiente.** São caminhos internos citados em conversa; a
  fonte não confirma qual está atual nem qual é o ambiente oficial de teste.
- **Não registrar incidente por reflexo.** “Parece incidente” é hipótese; o encaminhamento correto
  passa pelo grupo e pela reprodução.
- **Não concluir o significado do código `100000002`** além do que o texto diz.
- **Não reproduzir o CPF** mostrado em `[M01]`: ele foi mascarado aqui porque o material é público.
- **A sequência de tentativas não é reconstruível** (ver [`incertezas.md`](incertezas.md) item 1) —
  não descrever “a ordem correta” como se a fonte a tivesse estabelecido.

## 8. Resumo de uma linha

Ao receber uma crítica de modelo da API, **confirme o endpoint em uso**, **reduza o payload** até
isolar o campo (a mensagem diz qual é), **leia a crítica como contrato de entrada** — e, quando o
campo indispensável aparece, **escale em grupo com quem reproduz**, não sozinho.
