> **Fonte:** transcrição automática `faster-whisper large-v3` sem VAD. O MP4, áudio e telas não foram revisados neste lote. A transcrição integral foi preservada por instrução expressa do responsável, mas a qualidade do reconhecimento é insuficiente para inferir conteúdo técnico.

# Guia de estudo — projeto EPT.mp4

- **Categoria:** `DÚVIDA_OU_CONFLITO` (não foi possível atribuir conteúdo confiável às demais categorias)
- **Sistema:** não determinável pela saída ASR disponível.
- **Assunto:** qualidade/cobertura da transcrição; título do arquivo, isoladamente, não comprova que o vídeo explique uma EPT.
- **Confiança da extração:** **muito baixa**. São 73 segmentos; 69 repetem “Legenda Adriana Zanotto” em cadência de cerca de 30 segundos. A execução anterior com VAD teria reconhecido somente um segmento.
- **Cobertura temporal:** áudio `00:36:16.70`; último cue SRT/VTT `00:36:00–00:36:29.98`, além do fim do arquivo. O JSON registra `788.8 s` de transcrição sem definir a medida.
- **Estado:** **em revisão**; não usar como material de EPT, evidência de sistema, transcrição fiel ou prova de silêncio.

## Resultado que pode ser afirmado

A saída copiada contém uma frase repetida — “Legenda Adriana Zanotto” — e algumas expressões curtas como “Obrigado”, “Obrigado por assistir” e “E aí”. O padrão pode representar alucinação do ASR, reconhecimento de texto/crédito recorrente ou outra condição da fonte, mas nada disso foi confirmado por escuta/imagem. Não é possível distinguir fala real, ruído, legenda visível ou falha do modelo neste lote.

## Orientação para revisão

1. Confirmar que `projeto EPT.mp4` é o arquivo correto do manifesto e não uma fonte trocada ou corrompida.
2. Revisar o vídeo/áudio integralmente, prestando atenção a fala não reconhecida e à frase repetida. Não inferir o assunto pelo nome do arquivo.
3. Comparar os dois resultados de origem: o passe com VAD (1 segmento) e o passe sem VAD (73 segmentos). Eles indicam que o ASR não está estável para esta fonte.
4. Se houver fala técnica, gerar uma nova transcrição com configuração revisada e revisão humana; manter o material atual como registro do passe integral sem VAD.
5. Só então elaborar guia/procedimentos sobre o assunto real. Nenhuma descrição de fluxo técnico pode ser sustentada por este ASR.

A transcrição completa está em [`transcricao.md`](transcricao.md); limitações e perguntas estão em [`incertezas.md`](incertezas.md) e [`perguntas.md`](perguntas.md).
