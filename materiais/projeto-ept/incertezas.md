# Incertezas e limitações — projeto EPT.mp4

1. **Fonte audiovisual não revisada:** o MP4 não foi baixado ou ouvido/visto neste lote. Não se pode afirmar que o vídeo esteja silencioso, que não haja fala ou que a repetição seja alucinação.
2. **Baixa confiança do ASR:** 69 dos 73 segmentos do passe sem VAD repetem “Legenda Adriana Zanotto” em intervalos regulares de ~30 s; essa regularidade pode refletir erro de reconhecimento, conteúdo audível/visual ou outra condição da fonte.
3. **Passes divergentes:** o README de origem relata um passe `large-v3` com VAD que reconheceu apenas um segmento em 36 minutos e um segundo passe sem VAD que gerou 73. O primeiro resultado não está nesta pasta para comparação; conteúdo e timestamp dele não foram verificados localmente.
4. **Poucas frases distintas:** além da frase repetida, o ASR registra “Obrigado”, “Obrigado por assistir” e “E aí”. Sem escuta, não confirmar que sejam fala real, nem deduzir tema a partir delas.
5. **Discrepância de duração:** a fonte tem `2176.70 s` (`00:36:16.70`); o último cue SRT/VTT começa em `00:36:00` e termina em `00:36:29.98`, excedendo o áudio em `13.28 s`.
6. **Campo de duração ambíguo:** JSON registra `duracao_transcricao_s: 788.8` (`00:13:08.8`), sem definição; não coincide à primeira vista com a janela de cues, que cobre mais de 36 minutos.
7. **Cobertura desconhecida:** saída automática não permite localizar intervalos sem fala nem estimar quanta fala foi omitida; não interpretar os intervalos vazios como silêncio.
8. **Assunto e título:** “projeto EPT” é o nome do arquivo; não há evidência suficiente de que a gravação realmente trate de um projeto/EPT, tampouco dados para identificar sistema, EF, fluxo ou requisitos.
9. **Termos próprios:** “Adriana Zanotto” aparece no texto gerado pelo ASR; identidade, grafia e contexto não foram confirmados. O original foi mantido conforme instrução de preservação, sem tratar esse nome como dado de operador confirmado.
10. **Execuções:** `filtro_vad: false`, `duracao_transcricao_s`, precisão dos limites e motivo da frase recorrente carecem de esclarecimento. Os metadados e notas de origem são a única documentação local consultada; parâmetros completos do modelo não estão neste pacote.
11. **Privacidade:** varredura automatizada do TXT não detectou URL, e-mail, padrão de CPF/CNPJ ou termos de credencial. Isso não substitui revisão do MP4, que não foi feita.
12. **Validação:** nenhum teste, consulta, chamada de API, mudança de configuração, análise de tela ou procedimento de negócio foi realizado/confirmado neste lote.

**Próxima ação:** confirmar a fonte, recuperar o passe com VAD e revisar o vídeo/áudio integralmente antes de criar conteúdo técnico. Ver [`perguntas.md`](perguntas.md) e [`procedimentos.md`](procedimentos.md).
