# Transcrição preliminar — explicacao mesa c6.mp4

Esta pasta contém somente a saída automática de reconhecimento de fala. Ela ainda não foi conferida integralmente contra o áudio nem revisada com as imagens; não é documentação validada.

- **Fonte:** `explicacao mesa c6.mp4`
- **Tamanho conferido:** 1982033592 bytes (igual ao `manifesto.csv`)
- **SHA-256 da fonte:** `44344aaad2c507992b90790b981678729dac4abe7d20f0015ee533da74b54998` (igual ao OID do ponteiro LFS)
- **Duração do áudio:** 3461,57 s (`00:57:41.57`); último segmento reconhecido em `00:57:29`
- **Transcrição automática:** `faster-whisper`, modelo `large-v3`, idioma detectado `pt`, 1394 segmentos; filtro VAD desativado (`filtro_vad: false`)
- **Execução:** GitHub Actions run `38592430811`; auditoria após integração run `38599760998` concluída com sucesso (auditoria da configuração: `38592430977`)
- **Arquivos:** [`transcricao_bruta.txt`](transcricao_bruta.txt), [`transcricao.srt`](transcricao.srt), [`transcricao.vtt`](transcricao.vtt) e [`transcricao_meta.json`](transcricao_meta.json)
- **Estado no `STATUS.md`:** em análise; revisão humana, análise visual e demais materiais pendentes.

## Escopo e cuidados para revisão

A saída automática foi preservada integralmente, sem cortes ou mascaramento posterior, conforme orientação do responsável em 2026-10-14. Sem VAD, trechos sem fala também podem gerar reconhecimento espúrio; revisar o áudio inteiro e confirmar nomes, números e termos técnicos antes de reutilizar. Nenhuma imagem foi publicada nesta etapa.

## Análise preliminar deste lote

A fala apresenta o fluxo de trabalho de CQ na “mesa”: alinhamento com desenvolvimento/negócios, sprint/Planner/Gantt, leitura da EF, elaboração da EPT, execução e evidências, seguida de um treinamento para configurar proposta/esteira no Autorizador. Também explica ambientes/bases locais e compartilhados. Isso é relato de treinamento, não política operacional validada.

**Bloqueio de segurança:** a orientação sobre atualizar pastas de aplicação é internamente contraditória quanto a excluir/ preservar `config` e quais bases/máquinas usar. Não executar cópia, exclusão, instalação ou alteração de banco com base na transcrição; exigir runbook e ambiente formalmente autorizados. Nenhum SQL literal, valor literal de credencial ou URL foi reconhecido no ASR, mas há menção a login/senha, nomes de máquinas/pastas e dados de colegas; o MP4 não foi revisado visualmente.

O ASR sem VAD repete “Legenda Adriana Zanotto” em quatro cues entre `00:13:10–00:14:40`; revisar se é ruído/legenda ou reconhecimento espúrio. A transcrição integral permanece sem cortes/mascaramento conforme instrução de 2026-10-14; inclui nomes e conversa de trabalho. Ver [`../PRIVACIDADE_E_RETENCAO.md`](../PRIVACIDADE_E_RETENCAO.md) §§13 e 17. Nenhum teste/captura foi produzido.
