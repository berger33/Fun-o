> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Zé, Priscilla/Pri, Augusto, Gabriel). Não são publicadas **imagens
> de pessoas** (avatares/câmeras da reunião).

# Guia de estudo — PROJETO 14-08.mp4

- **Categoria:** `SISTEMAS`, `NEGOCIO`, `PROCESSOS`, `DÚVIDA_OU_CONFLITO`
- **Sistema:** módulo **ServCom** — serviço/plugin **Envio da Proposta ao Sistema Externo** e plugin **Integração para Consulta De Reaproveitamento de Seguro**
- **Assunto:** apresentação de **duas especificações funcionais (EFs)** do pacote 4 na reunião de planning: (1) novo campo **CNPJ do empregador (`CRN`)** no envio da proposta ao sistema externo para formalização digital; (2) **OS 556576** — novo campo **`simulation_id`** com o ID da simulação de reaproveitamento (pro rata) retornado pelo plugin de consulta de reaproveitamento de seguro
- **Fonte:** `PROJETO 14-08.mp4` (231977005 bytes), gravação de 2026-08-14 ~15:33 (BRT), duração 00:09:25.29 — SHA-256 `5d5e9a2c…`
- **Confiança da extração:** **alta** — áudio inteligível na maior parte (trecho abafado em `00:02:18–00:02:40`) e documentos legíveis em 1110×664 (tabelas de layout das duas EFs).

## 1. Objetivo e público

- **Objetivo do vídeo:** alinhar duas demandas pequenas e bem delimitadas no **plugin de envio de
  proposta ao sistema externo**: a inclusão do **CNPJ do empregador** (item 1) e a inclusão do
  **`simulation_id`** da simulação de reaproveitamento (item 2, **OS 556576**), deixando
  registrados os pontos em aberto de cada uma.
- **Público/pré-requisitos:** desenvolvedores e testadores CQ da **Função Sistemas** que atuam no
  **ServCom** e na jornada de formalização digital, familiares com o layout JSON do plugin e com a
  consulta de margem.

## 2. Item 1 — novo campo CNPJ do empregador (`CRN`) no envio ao sistema externo (00:00:00 – 00:03:23)

1. **O que muda (00:00:00 – 00:00:46):** implementar no módulo **ServCom**, no plugin de **envio
   da proposta ao sistema externo**, um novo campo com o **CNPJ — Cadastro Nacional da Pessoa
   Jurídica do empregador**, para compor as informações enviadas à instituição na **formalização
   digital**. Na tabela de layout da EF, o campo aparece como **`CRN`** — *Company Registration
   Number* — **CNPJ do empregador** ([`00:02:00`](capturas/01-tabela-campos-crn-destacado.png)).
2. **Vizinhança no layout (00:02:00):** o `CRN` (String) entra na mesma tabela de campos pessoais
   e de margem do empregado — `birth_date`, `employee_category_code`, `worker_eligible`,
   `total_pay_amount`, `base_margin_value`, `available_margin_value`, `hire_date`,
   `termination_date`, `termination_code`, `politically_exposed_person`, `code`, `description` —
   todos com coluna de origem no bloco **`ETRACPD`**, seguido de `employer_name`
   (`ETRACPD.ETNMEMPR`).
3. **De onde vem o dado (00:00:47 – 00:01:12):** a informação vem da **consulta de margem**,
   com base na **`origem 4` da proposta**; o campo fica "no meio do bloco" **`ETRACPD`** da
   consulta de margem.
4. **Ponto em aberto registrado (00:01:27 – 00:02:12):** ainda **não se sabe qual é o campo
   exato** de origem: é preciso "colocar no select", identificar o campo `ETRACPD.<campo>` e
   **registrar o nome do campo na última coluna da EF** (a própria EF será complementada).
   Encaminhamento: **Zé** verifica — inclusive com alguém do empregador / do negócio — e devolve
   o nome do campo para constar na EF.
5. **Esclarecimento de cadastro (00:03:05 – 00:03:20):** a proposta do cliente **continua sendo
   cadastrada com o CPF normal do cliente**; o novo campo é o CNPJ **do empregador** — não há
   troca do documento do cliente.

## 3. Transição entre os itens (00:03:34 – 00:05:26)

- **Pri (Priscilla)** apresentaria a próxima EF, mas a tela dela **travou** (`00:04:19 – 00:04:46`);
  **Augusto** compartilha a tela e abre a EF.
- Houve confusão falada com o número do item ("556776…" / "556576" em `00:04:53 – 00:04:58`);
  na tela, o documento é a **Ordem de Serviço 556576**
  ([`00:06:00`](capturas/02-os-556576-simulation-id.png)).

## 4. Item 2 — OS 556576: campo `simulation_id` do reaproveitamento (00:05:28 – 00:08:44)

1. **Objetivo (00:05:28 – 00:06:02):** viabilizar a integração das informações da **simulação
   do reaproveitamento (pro rata)** no plugin de **Envio da Proposta ao Sistema Externo**:
   a partir de agora, o parceiro **passa a enviar o ID da simulação** para nós.
2. **Detalhamento do novo campo (tela, [`00:06:00`](capturas/02-os-556576-simulation-id.png)):**
   implementar no módulo **ServCom**, no plugin **Envio da Proposta ao Sistema Externo**, novo
   campo responsável por compor a **informação da simulação do reaproveitamento** disponível na
   **tabela de consultas de reaproveitamento**. O campo **`simulation_id`** é o **identificador
   da simulação retornado pelo plugin `Integração para Consulta De Reaproveitamento de Seguro`**.
3. **Regra de preenchimento (00:07:43 – 00:08:20):** se for reaproveitamento e o ID vier,
   envia-se o ID; **se não for reaproveitamento, o campo vai vazio** — "ele vai trazer o que
   veio"; o JSON de exemplo colocado na EF serve de referência, mas **o campo que importa é só
   o `simulation_id`**.
4. **Simplicidade de implementação (00:08:33 – 00:08:44):** "a gente já tem o campo, já retorna
   esse campo lá, então é só levantar ele no build do plugin e passar ele para frente"
   (transcrição automática; ver [`incertezas.md`](incertezas.md)).
5. **Layout relacionado (00:07:00):** a EF traz a tabela de campos do serviço com origens
   `ETRAINSS` (`codeUser` → `ETRAINSS.ETCODUSU`, `loginUser` → `ETRAINSS.ETLOGIN`,
   `legalRepresentCPF` → `ETRAINSS.ETCPFREPRE…`, `signTreaty` → `ETRAINSS.ETASSINAROG…`),
   mostrando o padrão de mapeamento campo-a-campo adotado
   ([`00:07:00`](capturas/03-tabela-layout-etrainss.png)).

## 5. Encerramento e combinados (00:08:47 – 00:09:21)

- **Zé envia o Gantt dos dois projetos na segunda-feira** (`00:08:47 – 00:08:53`).
- Os dois itens são do **pacote 4**; o Gantt será criado **separado** e os demais projetos do
  pacote serão acrescentados depois (`00:08:54 – 00:09:02`).
- Ao enviar, **avisar a equipe** para posicionar "certinho no mapa" (`00:09:04 – 00:09:10`) e
  dar um toque no **Gabriel** para incluir as horas dele no Gantt (`00:09:13 – 00:09:19`).

## 6. Classificação por categoria

| Categoria | Aplica? | Onde |
|---|---|---|
| `SISTEMAS` | sim | ServCom, plugins de envio e de consulta de reaproveitamento, layout `ETRACPD`/`ETRAINSS` (§§2 e 4) |
| `NEGOCIO` | sim | CNPJ do empregador na formalização digital (`00:00:14 – 00:00:46`); reaproveitamento/pro rata (`00:05:40 – 00:06:16`) |
| `PROCESSOS` | sim | complemento da EF com o nome do campo (`00:01:27 – 00:02:12`); Gantt dos dois projetos (`00:08:47 – 00:09:21`) |
| `SQL` | menção, sem texto | ver abaixo |
| `INFRA_E_ACESSO` | não aplicável | nenhum acesso, ambiente ou credencial demonstrado (só problema de áudio do notebook em `00:02:18 – 00:02:40`) |
| `DÚVIDA_OU_CONFLITO` | sim | campo de origem do CNPJ ainda desconhecido (`00:01:27 – 00:01:34`); número do item confundido na fala (`00:04:53 – 00:04:58`) |

**Sobre `SQL`:** em `00:01:36` há a menção "é só a gente colocar lá no select", mas nenhuma
consulta é escrita, exibida ou executada — registrada como menção em
[`../SQL/INDICE_SQL.md`](../SQL/INDICE_SQL.md), sem categoria SQL para este vídeo.
