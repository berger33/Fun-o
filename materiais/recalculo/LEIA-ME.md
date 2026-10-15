# Pacote preliminar — `recalculo.mp4`

**Estado: em revisão.** Este pacote organiza uma transcrição automática e uma análise de estudo/teste. Não é especificação aprovada, resultado de validação nem runbook de produção.

## Fonte e escopo

- **Vídeo:** `recalculo.mp4`, dividido em duas partes LFS no repositório.
- **Tamanho declarado do original reconstruído:** `2434086989` bytes.
- **SHA-256 declarado:** `d8f2ed3de2a8b79512df333327a3d03c5c88c6ab4f2a626156561be75fb27bda`.
- **Procedência:** o README da execução anterior informa que as duas partes foram reconstruídas no runner e que tamanho/SHA-256 de cada parte foram conferidos contra `partes-videos.json`. Esta sessão não baixou, reconstruiu, re-hasheou nem inspecionou o MP4; usa os artefatos ASR dessa execução como fonte secundária.
- **ASR informado:** `faster-whisper` / `large-v3`, português, 1.043 segmentos, VAD desativado.
- **Áudio declarado:** `01:10:50.82`. O último cue SRT/VTT (`01:10:48.560–01:11:18.540`) ultrapassa a duração declarada em 27,72 s.
- **Referência de execução:** GitHub Actions run `38600117592`; auditoria da configuração `38600117590`; auditoria após integração `38607455403` (todas reportadas como concluídas no README de origem).

## Arquivos

- [`transcricao_bruta.txt`](transcricao_bruta.txt), [`transcricao.srt`](transcricao.srt), [`transcricao.vtt`](transcricao.vtt) e [`transcricao_meta.json`](transcricao_meta.json): artefatos ASR copiados sem alteração.
- [`transcricao.md`](transcricao.md): cabeçalho editorial seguido do TXT ASR integral.
- [`guia_de_estudo.md`](guia_de_estudo.md): síntese didática, distinguindo relato e inferência.
- [`procedimentos.md`](procedimentos.md): plano de validação proposto, não executado.
- [`perguntas.md`](perguntas.md), [`glossario.md`](glossario.md) e [`incertezas.md`](incertezas.md): pontos para confirmação e terminologia provisória.
- [`metadados.md`](metadados.md): procedência, integridade e limites da extração.
- [`capturas.md`](capturas.md): registra por que nenhuma captura foi incluída.

## Preservação e limites

Os artefatos originais de ASR foram preservados integralmente, sem cortes ou mascaramento, conforme a instrução expressa do responsável registrada em [`../PRIVACIDADE_E_RETENCAO.md`](../PRIVACIDADE_E_RETENCAO.md) §13. A saída automática inclui trechos conversacionais e áudio aparentemente não relacionado; as análises se concentram no assunto de recálculo/tolerância sem alterar a fonte. A transcrição não confirma o conteúdo visual, os valores configurados, a versão do sistema nem o resultado de um teste reproduzível.

Nenhuma proposta, convênio, conta, configuração, ambiente ou dado foi criado/alterado nesta sessão. Nenhuma API ou SQL foi executado. Revisão humana do áudio/vídeo e validação contra a EF vigente continuam pendentes.
