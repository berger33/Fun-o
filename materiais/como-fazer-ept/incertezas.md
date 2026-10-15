# Incertezas e pendências — Como fazer EPT.mp4

Status: **em revisão**. Este material se baseia somente em ASR `large-v3`; o áudio e as telas não foram revistos neste lote.

1. **Dois contextos/projetos:** o início demonstra uma EPT de API com objetos de despesa e reaproveitamento; a parte final propõe um exercício de EPT sobre recálculo/margem de tolerância. Confirmar se pertencem a demandas diferentes e quais EFs são as fontes oficiais de cada caso.
2. **Colunas do modelo:** o ASR menciona seis colunas e cita cenário, pré-condição, premissa, descrição e resultado esperado, mas não identifica cada coluna com segurança nem a distinção entre caso, item, etapa e referência. Conferir a planilha modelo aprovada.
3. **Siglas e grafias:** “IPT” pode ser reconhecimento de EPT; `Nexo`, “UTE/UTPT”, nomes de rotina, campos e endpoint não foram confirmados visualmente.
4. **Contrato da API:** a fala cita objeto `Despesa`, `Reaproveitamento`, número de proposta e usuário; não fornece o schema completo, campos, tipos, nulabilidade ou rota. Validar na EF e na documentação vigentes.
5. **Exemplo de reaproveitamento:** regra geral descrita é um desconto de seguro anterior em refinanciamento; valores numéricos ouvidos são explicação didática. Não os usar como massa, regra ou resultado esperado.
6. **Exercício de margem de tolerância:** a fórmula percentual, limites inclusivos, arredondamento, precedência entre mínimo/máximo e percentual, ausência de configuração e resultados de borda não são resolvidos.
7. **Dependência e ID:** a transcrição identifica verbalmente uma implementação/projeto anterior como pré-requisito; o identificador é incerto no ASR. Confirmar a dependência e sua disponibilidade na EF antes de montar a EPT.
8. **Fidelidade dos exemplos:** a pessoa que ensina diz que um teste anterior estava “bem errado” em relação ao método preferido. A demonstração é didática e não deve ser copiada como EPT aprovada.
9. **Duração/cobertura:** duração de áudio `2147.18 s` (`00:35:47.18`); último cue SRT/VTT termina em `00:35:43.14`. O JSON registra `duracao_transcricao_s: 1651.5`, sem explicar se é soma de fala, tempo processado ou outra medida; existem intervalos sem segmentos ao longo da transcrição.
10. **Fonte primária:** MP4 não foi baixado nem conferido quadro a quadro; não se confirmou o conteúdo das planilhas, EF, documentação de API, telas ou exemplos numéricos.
11. **Privacidade/inteireza:** a transcrição foi preservada sem cortes/mascaramento conforme instrução expressa do responsável (ver [`../PRIVACIDADE_E_RETENCAO.md`](../PRIVACIDADE_E_RETENCAO.md) §13). Isso não altera a necessidade de proteger credenciais/dados pessoais reais, nem significa revisão visual.

## Critérios para sair de revisão

- Revisar áudio e telas integrais, incluindo todos os intervalos sem segmentos.
- Obter EF, schema, EPT modelo e documentos citados por canal autorizado; confirmar que o exemplo e o exercício são demandas distintas.
- Confirmar fórmula/regras da tolerância, dependência de projeto, campos/rota da API e matriz de preparação de dados.
- Submeter o guia/EPT a CQ e ao responsável funcional; só depois executar, se autorizado, em sandbox com dados sintéticos.
