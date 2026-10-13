> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Zé, Priscilla/Pri, Augusto, Gabriel). Não são publicadas **imagens
> de pessoas** (avatares/câmeras da reunião).

# Procedimentos — PROJETO 14-08.mp4

## Fluxo A — Incluir o campo CNPJ do empregador (`CRN`) no envio ao sistema externo (00:00:00 – 00:03:23)

1. **Identificar o plugin alvo (00:00:00 – 00:00:12):** módulo **ServCom**, plugin **Envio da
   Proposta ao Sistema Externo** (envio de informações à instituição para **formalização
   digital**).
2. **Acrescentar o novo campo (00:00:14 – 00:00:46):** incluir o campo de **CNPJ do
   empregador** — na tabela de layout da EF, o campo **`CRN`** (*Company Registration
   Number*) — String
   ([`00:02:00`](capturas/01-tabela-campos-crn-destacado.png)).
3. **Definir a origem do dado (00:00:47 – 00:01:12):** o valor vem da **consulta de margem**,
   com base na **`origem 4` da proposta**, a partir de um campo do bloco **`ETRACPD`**
   (mesma origem dos demais campos da tabela: `ETRACPD.ETDTNASCTO`, `ETRACPD.ETNMEMPR` etc.).
4. **Resolver o ponto em aberto (00:01:27 – 00:02:12):** descobrir **qual campo `ETRACPD.*`**
   corresponde ao CNPJ: "colocar no select", consultar o negócio e, se preciso, alguém do
   empregador; **Zé** devolve o nome do campo.
5. **Registrar na EF (00:02:40 – 00:03:00):** preencher a **última coluna** da tabela de layout
   com `ETRACPD.<nome do campo>` e complementar a EF com essa informação, para ficar
   registrado qual campo está sendo enviado.
6. **Conferir o impacto no cadastro (00:03:05 – 00:03:20):** o cadastro da proposta do cliente
   **não muda** — continua com o **CPF do cliente**; o CNPJ é dado do empregador.

## Fluxo B — Incluir o campo `simulation_id` no envio ao sistema externo (OS 556576) (00:05:28 – 00:08:44)

1. **Identificar o item (00:05:28 – 00:05:40):** **OS 556576** — "Gravação do ID da simulação
   na consulta do pro rata", EF de um item só
   ([`00:06:00`](capturas/02-os-556576-simulation-id.png)).
2. **Contexto (00:05:40 – 00:06:02):** o parceiro passa a enviar o **ID da simulação** do
   reaproveitamento (pro rata); a informação da simulação está disponível na **tabela de
   consultas de reaproveitamento**.
3. **Acrescentar o campo (00:05:56 – 00:06:16):** no plugin **Envio da Proposta ao Sistema
   Externo**, criar o campo **`simulation_id`**: identificador da simulação retornado pelo
   plugin **Integração para Consulta De Reaproveitamento de Seguro**.
4. **Usar o JSON de exemplo com parcimônia (00:06:16 – 00:07:24):** a EF traz o JSON completo
   como o parceiro envia, mas **só o `simulation_id`** é o campo novo a ser tratado.
5. **Aplicar a regra de preenchimento (00:07:43 – 00:08:20):** se houver reaproveitamento e
   o ID vier preenchido, repassar o ID; **se não for reaproveitamento, enviar o campo vazio**
   — repassar exatamente o que veio.
6. **Implementar de forma simples (00:08:33 – 00:08:44):** o campo **já é retornado** hoje;
   basta **levantá-lo no build do plugin e passá-lo para frente** (expressão conforme
   transcrição automática — ver [`incertezas.md`](incertezas.md)).

## Fluxo C — Fechamento do pacote 4 no Gantt (00:08:47 – 00:09:21)

1. **Zé** envia o **Gantt dos dois projetos** na **segunda-feira** (`00:08:47 – 00:08:53`).
2. Criar o Gantt do **pacote 4** separado e ir acrescentando os demais projetos do pacote
   (`00:08:54 – 00:09:02`).
3. Avisar a equipe ao enviar, para registrar "certinho no mapa" (`00:09:04 – 00:09:10`).
4. Lembrar o **Gabriel** de lançar as horas dele no Gantt (`00:09:13 – 00:09:19`).
