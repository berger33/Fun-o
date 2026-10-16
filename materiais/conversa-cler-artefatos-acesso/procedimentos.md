> **Fonte textual** fornecida pelo responsável em **2026-10-15**; sem identificadores diretos a
> mascarar. Nomes de colegas preservados conforme autorização registrada em
> [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md).

# Procedimentos — artefatos e acessos (Cler)

**Nada foi executado nesta análise** (nenhum pedido formal, download, acesso ou alteração de
ambiente). O que segue é o **método observado** na conversa, com as lacunas explícitas.

## Fluxo A — Obter um artefato de ambientação

| Item | Conteúdo |
|---|---|
| **Objetivo** | Conseguir o artefato necessário para montar/atualizar o ambiente de teste |
| **Pré-condições** | Saber **qual** artefato falta (aqui: pacote do Web Empregador, `[M01]`) e para qual finalidade |
| **Entradas** | Nome do artefato/módulo; contexto do que está sendo montado |
| **Fonte** | `[M01]`, `[M03]`, `[M04]` |
| **Resultado esperado** | Artefato obtido por caminho autorizado — ou responsável/área identificada para obtê-lo |

1. Identifique explicitamente **o que falta** e **para quê** (“o do Web empregador… é só isso que
   falta”, `[M01]`).
2. Peça **ao colega que provavelmente tem**, com contexto e sem prazo imposto (“No seu tempo”, `[M01]`).
3. Se a resposta for “não tenho”:
   - pergunte **quem tem** (`[M03]`: “esse eu acho que só a carool”);
   - considere a alternativa indicada de **obter por download** (`[M03]`) — **somente** pelo caminho
     autorizado, que a fonte **não** informa ([`incertezas.md`](incertezas.md) item 2);
   - **valide** com a área responsável pela ambientação antes de usar qualquer artefato obtido.
4. **Validação:** o artefato corresponde ao módulo e à versão do ambiente-alvo (a fonte não trata de
   versão — não presumir).
5. **Exceções:** se o artefato não existir para o sistema em questão, cair no Fluxo B.

## Fluxo B — Descobrir a config/artefato de um sistema desconhecido (caso SETHI)

| Item | Conteúdo |
|---|---|
| **Objetivo** | Descobrir se um sistema tem artefato próprio ou usa o de outro |
| **Pré-condições** | Sistema identificado (SETHI); ausência de documentação acessível |
| **Entradas** | Nome do sistema; nome da suposta dependência (DIG) |
| **Fonte** | `[M08]`, `[M09]`, `[M12]`, `[M14]` |
| **Resultado esperado** | Resposta obtida **com a fonte** (quem confirmou) e **pendência de validação** registrada |

1. Formule a dúvida de modo verificável — exatamente como na conversa: **“tem UDL própria ou usa o
   DIG?”** (`[M09]`).
2. Pergunte a quem **já trabalhou com o sistema**; se ninguém tiver trabalhado (Cler: “nunca mexi com
   esse”, `[M09]`), vá para quem **conhece o cadastro/ambientação** (`[M12]`: “vou perguntar pro
   Giraldi”).
3. Registre a resposta **como relato**, com autor e data aproximada: “**DIG A**, confirmei com ele”
   (`[M14]`).
4. **Validação obrigatória antes do uso:** documento, tela ou runbook que confirme o artefato/caminho.
   Uma confirmação verbal **não** é configuração homologada ([`incertezas.md`](incertezas.md) item 3).
5. **Encerramento correto do ciclo:** devolver a resposta a quem ajudou/procurou (`[M14]`→`[M15]`).

## Fluxo C — Fechar o ciclo de um pedido entre colegas

| Item | Conteúdo |
|---|---|
| **Objetivo** | Manter o canal de ajuda vivo e o conhecimento circulando |
| **Fonte** | `[M01]`, `[M04]`, `[M13]`, `[M14]`, `[M15]`, `[M17]` |
| **Resultado esperado** | Pedido atendido ou redirecionado, com agradecimento e retorno do resultado |

1. Peça com contexto e respeite o tempo do colega (`[M01]`).
2. Agradeça mesmo quando a resposta for “não tenho” (`[M04]`, `[M13]`).
3. **Volte com a resposta encontrada** (`[M14]`) — quem ajudou aprende junto, e o próximo pedido fica
   mais fácil.
4. Mantenha o vínculo (a conversa também tem mensagens pessoais, `[M16]`), mas **não** transforme o
   canal pessoal em canal oficial de pedido de acesso.

## Sequência mínima resumida

```
identificar o artefato e a finalidade  →  pedir a quem tem  →  se não tiver: quem tem? / via de download autorizada
        →  se o sistema é desconhecido: perguntar a quem conhece  →  registrar relato + pendência de validação
        →  fechar o ciclo com quem ajudou
```
