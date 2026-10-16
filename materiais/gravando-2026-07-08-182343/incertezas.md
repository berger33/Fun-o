# Incertezas e pendências — Gravando 2026-07-08 182343.mp4

## 1. Instruções incompatíveis sobre arquivos/configuração (confirmado na fonte)

- **00:00:33 (fala):** “a gente vai dar um CTRL A, apagar tudo, menos a config” — e a tela em `00:00:35` mostra 10 itens / 1,46 MB selecionados.
- **00:02:34 (fala):** “apaga config”, dita ao tratar do pacote do WS.
- **00:03:09–00:03:24 (fala):** recomenda copiar a pasta `config` como backup e afirma que ela já contém parâmetros configurados (SIC, GDOK, API em `00:02:58–00:03:04`).

**Decisão deste material:** nenhuma exclusão, substituição ou limpeza de `bin`, `Config`, `Estreia` ou `Web References` deve ser executada com base nesta gravação. A rotina precisa ser confirmada com o responsável técnico.

## 2. Componentes e “AWS”

- A fala de `00:04:03–00:04:27` distingue casos de atualização (API × autorizador × “caso do SIC”), mas a matriz não é demonstrada.
- **00:04:26:** a palavra reconhecida foi “AWS”. Pode ser o próprio “WS”, outra sigla ou erro de reconhecimento. Não é possível resolver pelo texto nem pela tela (nenhuma tela de componentes é aberta).
- **Não confirmado:** se “aplicação Web + WS sempre juntos” é regra oficial, e o que compõe cada pacote.

## 3. Opção “N” e menus não explicados

- **00:03:41:** “a gente roda sempre com N aqui, tá?” — não há diálogo evidente no quadro desse instante; não tratar como opção padrão de nenhuma caixa.
- Os agrupamentos de `Serviços` citados (`Configuração de Processo`, `Campos Editáveis`, `Gerenciamento de Bloqueios`, `Perfil de Consulta Externa`, `Fila de Provisão de Recálculo`, ...) aparecem apenas como lista; nenhum foi aberto ou explicado.

## 4. Erro durante a cópia

- **00:03:40–00:05:05:** há mensagens em vermelho em janela escura durante a cópia (janela interna “Copiando 335 itens... 13% concluído”, ~19,4 MB/s, 331 itens restantes).
- **00:04:29–00:04:39:** a fala classifica o erro como “genérico” e afirma que “não interfere em nada”. O texto do erro **não é legível** nos quadros amostrados e o efeito não é verificado.
- Não registrar essa avaliação como diagnóstico válido.

## 5. Conteúdo visual não legível (não registrado como conteúdo)

- Terminal escuro sobre a área de trabalho em `00:01:55–00:02:15` (título e mensagens ilegíveis).
- Mensagens em vermelho em `00:03:45–00:05:05`.
- Retângulo com lista de anotações sobre a área de trabalho em `00:10:20` (fonte pequena, ilegível na amostragem).
- O `Nº Modelo` digitado no diálogo de exportação (`00:06:20–00:06:50`) está legível apenas em parte; por isso **não** é usado como dado neste material.

## 6. Conversa escrita no chat (reunião)

- Nos primeiros segundos (`00:00:01–00:00:18`) há mensagens no chat da reunião; apenas parte é legível na amostragem e **não** foi usada como fonte neste material.
- Em `00:07:40–00:07:55` a janela de chat (`Chat | Fabio Lemos Leite`) exibe a mensagem sobre o item 1.1/EF e a orientação de “Michelle de negócios”; o que está legível coincide com a fala de `00:04:49–00:05:26` e `00:07:47–00:08:03`.
- **00:00:13 / 00:00:17:** a fala cita “pasta do Gabriel”; é referência de trabalho entre colegas, sem valor operacional. O caminho de rede visto na tela **não** é reproduzido nos derivados.

## 7. Cobertura de áudio e transcrição (conferido)

- Duração do contêiner: `00:10:23.63`. Último segmento de ASR: `00:08:19.57–00:08:20.29`.
- **Silêncio digital confirmado:** de `00:08:28.08` a `00:10:23.63` o nível é `-91,0 dB` (sem áudio). Entre `00:08:20` e `00:08:28` há apenas ruído de fundo (`-56,4 dB` médio).
- **Cobertura:** varredura com limiar de `-50 dB` e duração mínima de 1 s não encontrou nenhum trecho audível com mais de 4 s sem segmento de ASR. Isso não substitui escuta humana, mas indica que a transcrição cobre toda a fala acima do limiar.
- Permanece pendente de validação humana: a **correspondência exata** entre algumas palavras do ASR e os rótulos de tela (por exemplo “Tolerância, 999” em `00:07:31`, que na tela corresponde ao `Nº Modelo 9999`), e a leitura do chat nos primeiros segundos.

## 8. Privacidade — decisões tomadas neste lote

- **Não publicadas:** quadros com participantes (câmeras/avatares) — ex.: `00:00:00–00:00:18` e `00:08:25–00:08:35`.
- **Recortadas para fora das capturas:** faixa de identificação do sistema (usuário/versão/servidor, com o usuário desfocado na origem), barra de endereço com o caminho completo do ambiente, valor da OS (desfocado na origem), rodapé com data/hora da estação e qualquer área de reunião.
- **Não publicadas:** telemetria da sessão exibida pela ferramenta de PDF (“Fidomínio... Acesso à Internet... Ethernet”).
- **Não reproduzidos nos textos:** caminho completo do host, valor da OS, identificadores de proposta/contrato e nomes de clientes. Nomes de operadores citados na gravação (Gabriel, Fabio, Michelle) são preservados conforme autorização de 2026-10-13.
- Nenhuma credencial, token, senha ou chave aparece nas capturas publicadas.

## 9. Pendências para encerrar a revisão

1. Conferência humana da transcrição contra o áudio (escuta dirigida), principalmente nos trechos de fala sobreposta.
2. Validação, por responsável técnico, da rotina de atualização (Fluxo D de [`procedimentos.md`](procedimentos.md)) e do conceito de “esteira/modelo de decisão” no vocabulário oficial.
3. Confirmação do desfecho do incidente de tolerância (corrigido/não corrigido) — a gravação não mostra a conclusão.
4. Definição de retenção para os ramos temporários usados na transferência (ver `materiais/PRIVACIDADE_E_RETENCAO.md`).
