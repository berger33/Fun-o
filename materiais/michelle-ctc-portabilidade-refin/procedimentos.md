> **Status:** fonte primária conferida byte a byte; o conteúdo demonstrado é um **fluxograma de outro cliente** e uma **conversa de desenho de teste**. Nenhuma configuração, cadastro ou integração é executada na gravação. Nada aqui autoriza alterar esteiras, parâmetros ou ambientes.

# Procedimentos — MICHELLE CTC PORTABILIDADE REFIN.mp4

A gravação contém **um mecanismo descrito** (Fluxo A, lido do desenho de exemplo) e **um teste proposto** (Fluxo B, apenas falado). Não há demonstração em tela de sistema, nem resultado esperado aprovado. Use este documento para reconhecer o mecanismo e preparar a validação — não para executar.

## Fluxo A — Mecanismo de coordenação no desenho de exemplo (observação)

- **Objetivo (do desenho):** coordenar a proposta de portabilidade e a(s) proposta(s) de refinanciamento vinculadas, de modo que a CCB só seja gerada com valores já validados (`00:03:36–00:04:59`). ⚠️ Desenho de **outro cliente** (`00:00:05–00:00:23`).
- **Pré-condições (no desenho):** proposta de portabilidade cadastrada e retornada do CTC/Núclea (`00:00:36–00:00:58`); refinanciamento vinculado à portabilidade (`00:01:07`).
- **Sequência lida da tela:**
  1. Faixa da portabilidade: `Envio/Aguarda Retorno da Núclea` → `CTC – Atualizar Proposta com NU da Portabilidade` → `CTC - Verificação de Alteração de Saldo e Prazo` (divergência → `Pendente` → `Recálculo de PMT e Prazo da Portabilidade`) — `00:00:36–00:00:58`; capturas em [`capturas.md`](capturas.md).
  2. Losango **`Tem Refin Vinculado?`** — sem refim, a proposta “seguirá o fluxo de uma portabilidade "pura"” (nuvem do desenho); com refim, segue pelo ramo **Sim** (`00:01:00–00:01:22`).
  3. **`CTC – Aciona Esteira de Refinanciamento (CTCACIPROPREF)`**: processo sem tela que só aciona o refim quando passa por ele a **última** portabilidade vinculada; a anotação do desenho exige o parâmetro de rotina **`G_AVERERR`** desligado para não validar a averbação nesse momento (`00:01:11–00:02:30`; captura 02).
  4. A esteira do refim anda (faixa própria: `Início da Esteira` → `Analise de Crédito` → … → `CTC - Validação de Refinanciamento de Portabilidade Após retorno da CIP (AJREFPORT)` → `Notifica as Condições Aprovadas` → documentos no SIC/CCB), enquanto a portabilidade…
  5. …**para** em **`CTC – Aguarda Analise do Refin de Portabilidade (CTCAGANREFIN)`**, “que permite o bloqueio da proposta de portabilidade de acordo com a situação da proposta de refinanciamento vinculada a ela” (nuvem do desenho; `00:03:15–00:03:36`; captura 03).
- **Decisões registradas:** quem decide a parada é a **próxima etapa configurada** após o acionamento — o processo de acionamento, por si, “só aciona, ele não valida” (`00:05:31–00:06:00`).
- **Validação:** nenhuma. O desenho não é executado e o fluxo do cliente-alvo não é exibido.
- **Resultado:** compreensão do mecanismo; nada pode ser transplantado para o C6 sem o fluxo vigente.

## Fluxo B — Teste proposto na conversa — **NÃO EXECUTADO**

- **Objetivo do teste:** verificar se, apontando a etapa seguinte ao acionamento para a espera desejada pelo banco, a portabilidade consegue **continuar andando sem dependência** do refim (`00:07:47–00:08:29`).
- **Pré-condições combinadas verbalmente:**
  - ambiente de teste da equipe (sem CTC configurado — limitação declarada em `00:09:23–00:09:30`);
  - **duas esteiras** distintas (a equipe não separa esteiras por tipo de proposta: `00:11:14–00:11:29`), obtidas com **convênios e produtos diferentes** para portabilidade e refim (`00:11:00–00:11:57`);
  - uma “esteirinha bem pequenininha”: `Analise de Crédito` + processo de acionamento + etapa de aguardo (e, se fizer sentido, notificação/liberação), **sem** os processos de CTC que chamam a integração real (`00:14:21–00:15:28`).
- **Sequência falada:**
  1. Cadastrar a portabilidade na **tela de cadastro normal** e gravar; no **pop-up**, aceitar fazer o refinanciamento da proposta; gravar o refim; ao final o sistema mostra **dois números de proposta** (`00:12:48–00:13:18`).
  2. Andar com as **duas propostas até a análise de crédito**, “não vou averbar nem nada” (`00:06:39–00:07:02`; `00:10:22–00:10:28`).
  3. Deixar o **refim parado na análise de crédito** (“ele pode estar na análise de crédito… não precisa estar nenhum [outro processo]”, `00:07:02–00:07:22`).
  4. Na esteira da portabilidade, **pular os processos de CTC** de atualização/envio e colocar o processo de acionamento (“CTC atualiza, envio, tudo isso aqui você pula; você só vai colocar isso aqui, aciona esteira de referenciamento”, `00:09:38–00:09:50`).
  5. Configurar como próxima etapa (“verdadeira”) a espera em discussão — na fala, o **“aguarda tela unificada”** no lugar do “aguarda análise de refim de portabilidade” do desenho (`00:07:22–00:07:47`).
  6. Observar se, após o acionamento, a portabilidade **anda para a próxima etapa sem parar** por dependência do refim (`00:07:47–00:08:36`).
- **Responsáveis combinados:** Santana executa, William acompanha para aprender; andamento reportado por mensagem ao grupo (`00:08:47–00:09:23`; `00:13:36–00:13:45`). Sem urgência (`00:13:47–00:13:54`).
- **Validação prevista:** apenas observação do comportamento das duas propostas; **não há critério de aceite escrito, massa de teste definida nem forma de restaurar a esteira** registrados na conversa.
- **Exceções e bloqueios:**
  - não é possível exercitar o CTC real naquele ambiente (“você não vai usar nada [do CTC]… você vai pular”, `00:09:28–00:09:32`) — limitação do teste, **não** autorização para contornar integração fora de sandbox aprovado;
  - a etapa de espera correta para o C6 (“aguarda alteração/tela unificada”) **não aparece no desenho** e não foi confirmada em sistema;
  - o comportamento com **várias portabilidades para um mesmo refim** (regra da “última proposta”, `00:02:00–00:02:30`) não entra no cenário combinado.

## O que falta para aprovar qualquer procedimento

1. Obter o **fluxo e a configuração vigentes do cliente-alvo** (o desenho exibido é de outro cliente — `00:00:05–00:00:23`).
2. Confirmar **nomes oficiais e mnemônicos** dos processos no ambiente (os lidos da tela pertencem ao desenho de exemplo) e a existência/semântica da etapa “unificada”.
3. Decidir, com o negócio, a **regra de dependência** entre portabilidade e refim, incluindo o caso de múltiplas portabilidades e o status que libera o avanço (a fala cita “integrada”, sem confirmação).
4. Definir pré-condições, entradas, resultados esperados, critérios de parada, restauração da esteira e evidências — e só então executar em sandbox aprovado.

Nenhum SQL foi demonstrado, ditado ou executado nesta gravação; nenhuma tela de produto foi aberta.
