> **Fonte:** ASR `faster-whisper large-v3`; vídeo, áudio e telas não foram revisados neste lote. Preservei a transcrição integral conforme a instrução expressa do responsável (2026-10-14). O conteúdo é orientação verbal; validar método, template e critérios com o padrão de CQ/EF vigentes.

# Guia de estudo — Como fazer EPT.mp4

- **Categorias:** `PROCESSOS`, `SISTEMAS`, `NEGOCIO`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO` (sem SQL demonstrado)
- **Sistema/artefatos:** Autorizador Web e Web API de Consulta de Propostas; EF e documentação de API; planilha EPT e exemplos prévios. Nomes de tela, rota e schema não verificados visualmente.
- **Assunto:** método para transformar uma EF em casos e passos de teste completos, incluindo preparação de dados/ambiente, pré-condições, etapas e resultados esperados. A demonstração usa uma API com novos objetos de despesa e reaproveitamento de seguro; depois é apresentado um exercício de recálculo com margem de tolerância.
- **Confiança da extração:** média para a orientação geral; baixa para grafias de siglas, nomes/campos, números e detalhes da EF, pois há 854 segmentos automáticos sem revisão de áudio/telas.
- **Duração/limite:** áudio declarado `00:35:47.18`; último cue `00:35:43.14`. O JSON declara `1651.5 s` de duração de transcrição, sem explicar o cálculo. Não presumir que lacunas sejam silêncio.
- **Estado:** **em revisão**; este guia sintetiza a fala e não aprova EPT, regra, parâmetro ou procedimento operacional.

## 1. Objetivo pedagógico

A mensagem central é que uma EPT não deve apenas dizer “verificar se o campo aparece”. Deve explicitar como preparar o cenário e percorrer o caminho até o resultado, de modo que outra pessoa — mesmo sem conhecer o projeto — consiga reproduzir o teste (**00:06:18–00:08:05; 00:31:16–00:32:06**).

A conversa recomenda ler a EF para entender objetivo, comportamento atual, requisitos e premissas; identificar dependências; preparar proposta/configuração necessárias; separar cenários, casos e etapas; registrar o passo a passo e o resultado esperado; e revisar o documento com outra pessoa (**00:27:25–00:31:13; 00:33:15–00:34:54**). O formato e os nomes de colunas precisam ser confirmados no template vigente.

## 2. Demonstração: resposta de API com despesa e reaproveitamento

No início, os participantes percorrem uma EF já existente para uma API de consulta detalhada de proposta. A fala diz que a mudança acrescenta ao retorno novos dados de despesa e um objeto de reaproveitamento, e que a chamada recebe número da proposta e usuário (**00:02:12–00:06:18**). A grafia/rota e os nomes de campos não podem ser tratados como contrato: o ASR reconhece termos de forma inconsistente, e a EF/documentação anexada não foi inspecionada.

O exemplo de teste mostra a lógica de **montar pré-condições compatíveis com a saída**: se o retorno esperado inclui uma despesa, preparar uma proposta com a despesa; se inclui reaproveitamento, preparar um caso de refinanciamento que tenha reaproveitamento (**00:06:28–00:07:08**). A demonstração relata configuração de despesa/política, gravação de proposta, uso de refinanciamento e comparação da resposta da API com a tela (**00:15:09–00:21:18**). Trata-se de um exemplo explicado na gravação, não de evidência validada neste pacote.

## 3. Construção da EPT

A orientação apresentada é:

1. **Ler a EF do começo:** entender objetivo, estado atual, requisito, premissas e dependências antes de escrever passos (**00:27:40–00:30:21**).
2. **Separar os casos e itens:** identificar projeto, número do caso e item da EF que está sendo testado; iniciar caso novo de forma visualmente distinta no modelo demonstrado (**00:09:17–00:12:47**).
3. **Definir pré-condições e premissas:** registrar o que deve existir antes do teste; a fala diz que algumas partes podem seguir o padrão do template, mas não lista todas as exceções (**00:09:58–00:10:05; 00:26:47–00:27:16**).
4. **Escrever cada etapa explicitamente:** registrar navegação, ação e sequência, inclusive a configuração/preparação anterior ao teste principal; separar passos conforme muda o caso ou a etapa (**00:11:04–00:12:47; 00:23:14–00:24:24**).
5. **Definir resultado esperado:** descrevê-lo conforme a EF e a documentação da API; o exemplo compara os campos/documentação da resposta ao requisito (**00:13:05–00:15:06**).
6. **Usar referências como aprendizado, não como cópia:** a fala recomenda olhar EPT anterior e escrever com as próprias palavras, no padrão da equipe; não reutilizar conteúdo sem conferir projeto, configuração e resultado (**00:08:57–00:09:14; 00:25:39–00:27:16; 00:33:15–00:33:56**).
7. **Revisar:** após concluir, ler com o responsável e corrigir etapas faltantes ou sem sentido (**00:34:39–00:35:14; 00:35:41**).

O ASR diz que a planilha tem seis colunas e cita nomes como cenário, pré-condição, premissa, descrição e resultado esperado; a enumeração completa e o significado de cada coluna não estão claros (**00:09:17–00:10:05**). Confirmar no modelo oficial, sem reconstruir a estrutura por inferência.

## 4. Exercício: recálculo e margem de tolerância

Na parte final, a pessoa pede que o analista leia outra EF e prepare uma EPT. A descrição verbal do objetivo é alterar validações de recálculo para considerar limitadores mínimo/máximo de valor solicitado configurados no convênio e uma tolerância percentual; o comportamento atual é descrito como rígido, bloqueando diferenças pequenas (**00:27:25–00:29:36**).

A fala também aponta uma dependência de uma implementação anterior que precisaria estar pronta antes do teste e diz para verificar configuração/ambiente relacionado (**00:30:01–00:31:13**). O número ouvido nessa fala é incerto e não deve ser usado para localizar ou aprovar requisito sem conferência visual da EF. Valores numéricos usados para explicar o reaproveitamento de seguro são exemplos da conversa, não critérios de aceite para o exercício.

## 5. Como aplicar sem transformar a fala em regra

- Tratar a conversa como aula de elaboração, não como runbook de Autorizador, convênio ou ambiente.
- Confirmar template atual, sequência do fluxo, ambiente e dados de teste com a equipe de CQ.
- Converter cada objetivo da EF em cenários verificáveis e cada cenário em pré-condições, etapas observáveis e resultados esperados específicos.
- Incluir apenas preparações necessárias e autorizadas; não criar convênio, proposta, perfil, configuração ou massa real sem instrução aprovada.
- Conferir cada resultado no contrato/schema vigente e na EF, não somente no relato do vídeo.
- Para tolerância, separar cenários abaixo/dentro/acima dos limites somente depois de confirmar fórmula, arredondamento, precedência e configuração oficial; o vídeo não fornece especificação completa.
- Revisar campos, grafias, identificadores e dependências contra a EF e a tela original, pois este pacote não contém revisão visual.

O roteiro seguro e seus bloqueios estão em [`procedimentos.md`](procedimentos.md); dúvidas em [`incertezas.md`](incertezas.md).
