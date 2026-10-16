> **Status:** observações verificadas na fonte primária (vídeo conferido byte a byte). Continuam **sem** autorização para alterar ambiente, configuração ou dados. Onde a gravação é contraditória, o passo está marcado como bloqueado.

# Procedimentos — Gravando 2026-07-08 182343.mp4

A gravação mostra **duas coisas úteis** (caminho de menu e diálogos de modelo de decisão) e **uma rotina informal** de atualização de pacote que **não** tem os elementos mínimos de um runbook. Use este documento para reconhecer telas e riscos, não para executar.

## Fluxo A — Reconhecer o pacote WebAutorizador / WS (observação)

- **Pré-condições:** acesso de leitura à área compartilhada do ambiente de teste (o ambiente exato deve ser confirmado pelo mecanismo corporativo; caminhos de host não são reproduzidos aqui).
- **Entrada:** a pasta-raiz do pacote do ambiente (`00:00:20–00:00:35`).
- **Sequência observada:**
  1. Abrir a raiz do pacote e entrar em `Web Site` (`00:00:20–00:00:32`).
  2. Abrir **`WebAutorizador`** (`00:00:35–00:00:52`). Conteúdo lido: `bin`, `Config`, `Estreia`, `Web References`, `Dados.dat`, `Global.asax`, `inst.dat`, `Web.Config`, `WSAutorizador.asmx`, `WSAutorizador.XmlSerializers.dll`, `WsRegChaveLicenca.asmx` (10 itens / 1,46 MB na seleção visível).
  3. Abrir **`...\WS\WSAutorizador`** (`00:02:36`): mesma estrutura, com `Config` de `09/09/2025 11:35` e binários de `08/07/2026`.
- **Decisão registrada pela fala:** a aplicação Web e o serviço Web são tratados como **um par** — “atualizou um, tem que atualizar o outro” (`00:02:25–00:02:32`). **Não confirmado** como regra oficial de pacote.
- **Validação:** nenhuma. A gravação não mostra teste final, versão publicada nem conferência de integridade.
- **Resultado:** apenas o reconhecimento da estrutura de pastas e arquivos.
- **Exceções:** a matriz de exceções citada (“quando é caso do SIC... aí é só o autorizador”; “o AWS não atualiza”) não é demonstrada (`00:04:03–00:04:27`).

## Fluxo B — Importar/exportar modelo de decisão (esteira) — **verificado visualmente**

- **Objetivo:** criar/atualizar um **modelo de decisão** (“esteira”) por importação de arquivo, no contexto do teste de tolerância (`00:05:26`; `00:07:53–00:08:03`).
- **Pré-condições:** aplicação `Autorizador Web` acessível e permissão para `Serviços → Decisão` (**não demonstrada**); arquivo de modelo disponível (`Estaira112233.xml` no exemplo).
- **Sequência observada (com timestamps):**
  1. Abrir o menu **`Serviços`** (`00:05:45–00:06:15`).
  2. Posicionar em **`Decisão`** e abrir o submenu (`00:06:15`): `Tabela de Modelos`, `Tabela de Decisão`, `Relacionamento Modelo X Produto`, `Exportar Modelo Decisão`, `Importar Modelo Decisão`, `Visualizador de Fluxo Decisão`.
  3. Opcional: **`Exportar Modelo Decisão`** — diálogo com `Nº Modelo` (`00:06:20–00:06:50`), usado na conversa para levar/levar de volta o modelo (“exportou”, `00:06:34`).
  4. **`Importar Modelo Decisão`** (`00:06:55–00:07:35`):
     - campo **`Arquivo de Importação de Modelo de Decisão`** = `Estaira112233.xml`;
     - campo **`Nº Modelo`** = `9999` e descrição = `teste_tolerancia`;
     - `Confirmar` → pergunta “**Confirma a importação da nova esteira ‘9999 - teste’?**” → confirmação do operador;
     - mensagem de retorno: “**As informações foram salvas**” (e, no quadro, o aviso “Nenhuma sugestão”).
- **Validação:** a única validação é a mensagem de sucesso da própria tela. Não há conferência do conteúdo importado, vínculo a proposta, nem teste funcional subsequente.
- **Resultado:** modelo `9999` (`teste_tolerancia`) criado/atualizado na base de teste — **segundo a mensagem do sistema**.
- **Exceções:** nenhuma demonstrada. O aviso “Nenhuma sugestão” não foi explicado.
- **Bloqueio:** **não** executar esta importação em ambiente produtivo nem com arquivos de origem desconhecida; o exemplo usa identificadores de teste.

## Fluxo C — Registrar incidente de tolerância (não é execução de sistema)

- **Objetivo:** documentar divergência entre a regra da EF (**0 a 99**) e o comportamento da tela (**aceita 0 a 100**) na faixa de valor solicitado (`00:03:00–00:03:22`; evidência anexa e encaminhamento a “Michelle de negócios” em `00:07:40`).
- **Entradas:** documento de incidente (cabeçalho em branco no quadro), print da tela `Limites do Valor Solicitado` com os campos de tolerância em 100,00, e citação do trecho da EF.
- **Sequência observada:** abrir o documento com a regra e o print da evidência; apontar os campos divergentes; encaminhar ao responsável de negócio antes de tratar como defeito confirmado.
- **Validação:** comparação campo a campo entre o texto da EF (0–99, opcional, 2 casas decimais) e o que a tela aceitou (0–100).
- **Resultado:** incidente registrado/encaminhado (a conclusão do caso **não** aparece na gravação).
- **Cuidados:** o documento e esta análise não devem publicar OS, cliente, responsáveis ou dados de proposta.

## Fluxo D — Atualizar/limpar o pacote em ambiente de teste — **BLOQUEADO**

> Não executar. Os passos abaixo descrevem **somente** o que foi dito/mostrado, para fins de reconhecimento e para orientar a obtenção de um runbook oficial.

- **Menções na gravação:** selecionar tudo e apagar, preservando `config` (`00:00:33`); apagar a config do WS (`00:02:34`); copiar a pasta `config` como backup (`00:03:09–00:03:24`); rodar sempre com “N” (`00:03:41`).
- **Contradições:** ver [`incertezas.md`](incertezas.md) §§1–3. As duas primeiras falas brigam com a terceira.
- **Erro durante a operação:** mensagens em vermelho foram chamadas de “erro genérico” que “não interfere em nada” (`00:04:29–00:04:39`) — sem diagnóstico e sem verificação de efeito.
- **Resultado:** desconhecido. Nenhuma publicação, smoke test ou rollback é demonstrado.
- **O que faltaria para virar runbook:** pacote e versão oficiais; ambiente autorizado; ordem entre aplicação Web, WS e API; procedimento de backup/restauração testado; critério de sucesso e rollback; definição do que é “variável/SIC” e do que é pacote.

## Verificações que continuam obrigatórias

- Fazer **backup testável** da configuração antes de qualquer alteração e confirmar a restauração.
- Não apagar `bin`, `Config`, `Estreia` ou `Web References` com base nesta gravação.
- Registrar versão atual e pretendida de cada componente do par Web/WS antes de atualizar.
- Confirmar por evidência não sensível o resultado de uma importação de modelo (por exemplo, reexportar e comparar), em vez de confiar só na mensagem de sucesso.
- Tratar “AWS”, “N” e os números falados como **não confirmados**.

Nenhum SQL foi demonstrado, ditado ou executado nesta gravação.
