> **Leitura preliminar de ASR, não regra de negócio nem runbook.** O MP4, o áudio e as telas não foram revistos nesta sessão. Não altere convênio, proposta, configuração ou ambiente, e não execute chamadas, com base somente nesta transcrição.

# Guia de estudo — `recalculo.mp4`

- **Categoria:** `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO` (nenhum SQL demonstrado).
- **Sistema:** Autorizador/Web Autorizador, API/plugin, convênio e condições de crédito, proposta, recálculo e esteira; nomes de tela, campos e arquitetura não foram conferidos visualmente.
- **Assunto:** treinamento/depuração de casos de teste para limites mínimo/máximo de valor e margem de tolerância em um fluxo descrito como “somente recálculo” ou “ambos”. A conversa alterna entre configuração do convênio, proposta, API e versão/ambiente.
- **Fonte:** ASR `faster-whisper large-v3` copiado byte a byte da referência; vídeo/áudio/telas não revistos nesta sessão.
- **Confiança da extração:** média para o tema geral; baixa para regra, fórmula, nomes de campos, identificadores, resultados e sequência operacional. O material é ASR sem VAD, não revisado contra a gravação.
- **Cobertura declarada:** áudio `01:10:50.82`; 1.043 segmentos; último cue `01:10:48.560–01:11:18.540`, cujo fim excede o áudio declarado em 27,72 s. A métrica `duracao_transcricao_s: 2527.5` não tem definição conhecida. Não inferir que lacunas sejam silêncio.
- **Estado:** **em revisão**. Nenhum teste foi executado nesta análise.

## 1. Objetivo pedagógico aparente

A sessão tenta demonstrar a outro analista como criar cenários em torno de recálculo e tolerância, observando a relação entre limite configurado no convênio, valor solicitado na proposta, modo de execução da atividade e passagem pela esteira. O apresentador começa anunciando que fará um caso e depois o outro analista continuará (**00:00:21–00:01:34**). Os rótulos de caso são inconsistentes no próprio ASR (“2.1”, “3.2”, “caso 3” e depois “caso 2”); confirme a EPT/EF antes de associar esse trecho a um caso numerado.

## 2. Configuração e valores citados

A conversa menciona convênio, “Condições de crédito”, valor mínimo/máximo e tolerância. Um exemplo usa aproximadamente 1.000 e 3.000; em seguida os participantes debatem se uma proposta de 2.990 deve passar quando há tolerância de 1% e se a configuração deve ser alterada no convênio, não na proposta (**00:03:31–00:04:00; 00:11:46–00:15:10**). Isso é um exemplo falado, não uma especificação confirmada.

Outros números e explicações não se harmonizam completamente: há referências a 2.995 com 1%, a uma tolerância de 10%, a um mínimo de 1.000 que poderia admitir 900 quando a tolerância fosse 10%, e a uma configuração final sugerida de mínimo 1.000, máximo 3.000 e 1% nos dois limites (**00:19:16–00:20:45; 00:59:49–01:01:16; 01:06:30–01:07:03**). O material não estabelece com segurança:

- se a tolerância é aplicada para dentro ou para fora de cada limite;
- se o percentual usa o valor mínimo, o máximo ou o valor solicitado como base;
- se a regra vale para os limites inferior e superior de forma simétrica;
- arredondamento, inclusividade, precedência ou tratamento de percentual zero.

Consulte a EF e o responsável de negócio antes de escrever o resultado esperado.

## 3. Modos de atividade e resultados que precisam ser reconciliados

A sessão compara os modos chamados pelo ASR de “somente recálculo” e “ambos”. Em alguns pontos, os participantes suspeitam que o modo “somente recálculo” não esteja considerando a tolerância, enquanto “ambos” teria comportamento diferente (**00:21:00–00:30:23**). A conversa também menciona uma análise/etapa posterior e a expectativa de que uma condição dentro da tolerância não gere apontamento, mas que uma condição fora dela exija verificação (**00:30:52–00:33:32**).

Mais tarde, há uma afirmação de que o teste “funcionou”, seguida por novas verificações e por uma explicação didática dos limites (**00:48:30–00:54:12; 00:59:49–01:03:41**). Como não há evidência visual ou registro de entrada/saída, a fala não permite concluir se o erro foi corrigido, se os modos eram equivalentes ou qual cenário passou.

## 4. Ambiente e versão

A conversa relaciona parte da investigação a uma versão considerada antiga e propõe obter uma versão mais nova; também menciona uso de máquina/servidor compartilhado e duas bases/servidores (**00:23:42–00:24:31; 00:37:37–00:39:28**). Isso pode explicar divergências de resultado, mas é apenas hipótese verbal. Não copiar binários, trocar servidor, conectar a base ou alterar pastas/configuração sem runbook autorizado, inventário do ambiente, backup e rollback. Versão, host, banco, plugin e responsável não foram verificados.

## 5. Modelo seguro para transformar a conversa em casos de teste

A contribuição didática aproveitável é estruturar uma matriz com pré-condições, modo de atividade, configuração, valor solicitado, resultado esperado e evidência. Os números falados servem apenas para ilustrar perguntas — não devem ser copiados como dados/critério sem aprovação.

Após confirmar a EF, considerar casos sintéticos para: abaixo do limite inferior; no limite; dentro e fora da tolerância; no limite superior; e acima do limite. Separar “somente recálculo” de “ambos” e qualquer rota de API/UI somente se a especificação definir que são dimensões independentes. Confirmar o estado final da proposta/esteira e as mensagens esperadas. O plano está em [`procedimentos.md`](procedimentos.md); questões pendentes em [`perguntas.md`](perguntas.md) e [`incertezas.md`](incertezas.md).

## 6. Trechos não técnicos e limites de interpretação

O ASR registra conversas paralelas/pessoais e aparente áudio de mídia não relacionada durante partes da gravação, especialmente em trechos aproximadamente entre `00:34:20` e `00:59:36`. Não é possível determinar sem ouvir/ver a fonte se são falas ao fundo, mídia reproduzida ou erro de reconhecimento. O trecho final “Legenda Adriana Zanotto” também pode ser texto de legenda ou reconhecimento espúrio. A transcrição original foi mantida completa por orientação expressa; esses trechos não sustentam requisitos de produto.

## Resumo

A gravação parece ser um treinamento prático de CQ para investigar uma regra de recálculo com limites e tolerância, comparando dois modos de atividade e diferentes versões/ambientes. A própria conversa contém dúvidas e resultados aparentes divergentes; a fórmula, a configuração correta, os casos numerados e a correção observada continuam sem confirmação. Trate todo detalhe operacional como pendente da EF, de revisão audiovisual e de um teste autorizado.
