# Transcrição preliminar — projeto EPT.mp4

Esta pasta contém a saída automática de reconhecimento de fala, ainda não revisada integralmente contra o áudio nem com as imagens. Não é uma especificação ou procedimento validado.

- **Fonte:** `projeto EPT.mp4`
- **Tamanho conferido:** 1246682448 bytes (igual ao `manifesto.csv`)
- **SHA-256 da fonte:** `57f4232365d3ef9291aa2773793d812dcade581b71c273da0a61a0bec97c0a52` (igual ao OID do ponteiro LFS)
- **Duração do áudio:** 2176,70 s (`00:36:16.70`); último segmento reconhecido em `00:36:00`
- **Transcrição automática:** `faster-whisper`, modelo `large-v3`, idioma detectado `pt`, 73 segmentos; filtro VAD desativado (`filtro_vad: false` nos metadados)
- **Execução:** GitHub Actions run `38584641492`; auditoria de configuração run `38584641428`
- **Arquivos:** [`transcricao_bruta.txt`](transcricao_bruta.txt), [`transcricao.srt`](transcricao.srt), [`transcricao.vtt`](transcricao.vtt) e [`transcricao_meta.json`](transcricao_meta.json)
- **Estado no `STATUS.md`:** em análise; revisão humana, análise visual e demais materiais pendentes.

## Escopo e cuidados para revisão

A primeira execução, com filtro VAD, reconheceu somente um segmento em 36 minutos de áudio; por isso, a gravação foi reprocessada sem VAD e esta pasta contém a saída comparativa de 73 segmentos. Os artefatos preservam essa saída automática integralmente, sem cortes ou mascaramento posterior, conforme orientação do responsável em 2026-10-14. Sem o filtro, trechos sem fala também podem gerar reconhecimento espúrio: revisar o áudio inteiro, confirmar nomes, números e termos técnicos e conferir tanto possíveis alucinações quanto fala não reconhecida. Nenhuma imagem foi publicada nesta etapa.
