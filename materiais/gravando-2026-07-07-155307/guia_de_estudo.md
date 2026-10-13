> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Gabriel, William, Santana). Não são publicadas **imagens de pessoas**
> (avatares/fotos de perfil) nem identificadores de máquina na captura derivada.

# Guia de estudo — Gravando 2026-07-07 155307.mp4

**Categoria:** `PROCESSOS`, `SISTEMAS`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO`
**Sistema:** módulo **Autorizador** (contexto de itens C6 Consig — parâmetro para margem de tolerância) e ambiente de base/pastas compartilhadas de CQ
**Assunto:** orientação operacional para iniciar testes em projeto do Autorizador usando a **EPT** já escrita, alinhamento com o responsável pela frente de **API** (Santana) e cuidado ao subir base/alterar pasta compartilhada sem conflitar com outro operador
**Fonte:** `Gravando 2026-07-07 155307.mp4` (56195092 bytes), gravação de 2026-07-07 ~15:49 (BRT), duração 00:01:39.14 — SHA-256 `e2a73df2…`
**Confiança da extração:** **alta** — áudio claro do interlocutor principal (embora a outra ponta da ligação não tenha sido capturada em 00:01:02–00:01:13) e tela perfeitamente legível em 1364×766.

## 1. Objetivo e público

- **Objetivo do vídeo:** registrar a passagem de orientação rápida para um operador que escreveu a
  **EPT** mas ainda não tem experiência prática na execução de testes do módulo **Autorizador**,
  indicando por onde começar, com quem alinhar a parte de **API** e qual verificação fazer antes de
  subir a base e trocar a pasta de trabalho.
- **Público/pré-requisitos:** operadores de CQ/testes da **Função Sistemas** atuando na mesa/equipe
  de projetos do **Autorizador**.

## 2. Contexto visual dos itens de trabalho (00:00:00 – 00:00:07)

Na conversa de Teams com **Gabriel**, são exibidos dois itens de trabalho relacionados ao mesmo tema
funcional (**Implementação de Parâmetro para Margem de tolerância**):

| Item exibido no chat | Tipo / tag visível | Timestamp na tela |
|---|---|---|
| `C6 Consig - 558139 - [ÁGIL] (I) Implementação de Parâmetro para Margem de tolerância` | Item principal `[ÁGIL] (I)` | 00:00:00 – 00:01:39 |
| `C6 Consig - 570023 - [EPT] [[ÁGIL] (I) Implementação de Parâmetro para Margem de tolerância` | Item de `[EPT]` vinculado | 00:00:07 – 00:01:39 |

Ver recorte em [`capturas/01-itens-de-trabalho-c6.png`](capturas/01-itens-de-trabalho-c6.png).

## 3. Diretrizes operacionais passadas na chamada (00:00:01 – 00:01:32)

1. **Iniciar pela EPT existente (00:00:01 – 00:00:13):** pegar e utilizar a **EPT** já disponível
   no item para dar início à execução dos testes.
2. **Divisão de escopo e apoio mútuo com Santana (00:00:14 – 00:00:39):**
   - **Santana** já está atuando no mesmo projeto, especificamente na frente de **API**
     **[00:00:14 – 00:00:18]**.
   - O orientador fará a ponte para que Santana ajude o operador e vice-versa, podendo acionar
     diretamente tanto Santana quanto o próprio orientador em caso de dúvidas **[00:00:20 – 00:00:39]**.
3. **Ganho de experiência prática no Autorizador (00:00:41 – 00:00:59):**
   - Como o operador ainda não tem experiência no módulo **Autorizador**, executar na prática os
     testes da **EPT que ele mesmo escreveu** serve para "pegar o *feeling*" do módulo
     **[00:00:41 – 00:00:59]**.
4. **Cuidado ao subir base e trocar pasta compartilhada (00:01:14 – 00:01:24):**
   - O procedimento habitual citado é: **"sobe na minha base, muda a pastinha"** **[00:01:18 – 00:01:19]**.
   - **Regra crítica de conferência prévia:** antes de mudar a pasta/subir na base, **conferir se
     Santana já não fez essa alteração** **[00:01:21 – 00:01:24]**, evitando sobrescrever ou
     desconfigurar o ambiente em uso pelo colega.
   - Na barra de mensagem fixada do chat (**[00:00:00]**), observa-se a referência às pastas de
     trabalho compartilhadas (`Arquivos e SPRINTS: \\<host-interno>\Mesa_C6 Arquivos` e
     `Sites: \\<host-interno>\C6 UDL Base`).
5. **Próximo passo combinado (00:01:27 – 00:01:32):** o orientador falará primeiro com Santana e, em
   seguida, fará uma ligação conjunta com os dois operadores (**"ligo pra vocês dois juntos"**).

## 4. Erros, cuidados e ressalvas

- **Conflito de ambiente compartilhado:** nunca trocar a pasta ou subir base compartilhada sem antes
  verificar se outro operador que atua no mesmo projeto (neste caso, Santana na frente de API) já
  alterou o apontamento **[00:01:21]**.
- **Limitação da fonte:** o vídeo não demonstra na tela o passo a passo técnico de como "subir a
  base" ou "mudar a pastinha" (apenas menciona a rotina verbalmente e exibe o atalho fixado no topo
  do chat). Não deduzir comandos ou telas não mostrados.

## 5. Resumo em uma frase

Em **00:01:39**, o vídeo registra a orientação para iniciar os testes dos itens `558139`/`570023`
(**Implementação de Parâmetro para Margem de tolerância**) no módulo **Autorizador** a partir da
**EPT** já redigida, atuando em conjunto com **Santana** (responsável pela parte de **API**) e
verificando previamente se ele já alterou a base/pasta compartilhada antes de modificá-la.
