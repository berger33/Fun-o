# Perguntas de validação — Como fazer EPT.mp4

A gravação é uma orientação e um exemplo didático, não uma especificação aprovada. As perguntas precisam ser respondidas com o template/EF vigentes e pelos responsáveis de CQ, desenvolvimento e negócio.

## Método e template

1. Qual é o template de EPT vigente e quais são, exatamente, seus cabeçalhos? O ASR diz “seis colunas”, mas não enumera todos com clareza.
2. Como a equipe define número de projeto, caso, item da EF, cenário e etapa? Qual é a convenção oficial para reiniciar numeração ao abrir caso novo?
3. Quais pré-condições e pós-condições podem ser reaproveitadas entre casos e quais precisam ser específicas do projeto?
4. Qual nível de detalhe é obrigatório para navegação, ações, validação e evidência? Há padrão para captura, logs e payloads?
5. Quem revisa/aprova a EPT antes da execução e qual é a forma oficial de registrar comentários e versão?
6. Exemplos antigos podem ser consultados em qual repositório? Como verificar que não contêm fluxo, nomes de campo ou passos desatualizados?

## Demonstração da API de proposta detalhada

7. Qual EF e projeto correspondem ao exemplo inicial? O pacote não contém a EF ou a documentação citada.
8. Qual é o nome/rota oficial do endpoint “Consulta de Propostas Detalhada” e quais entradas (número da proposta, usuário ou outras) são obrigatórias?
9. Quais são os nomes, tipos, origem e nulabilidade dos objetos de despesa e reaproveitamento? Quais campos exatos devem ser comparados?
10. Qual configuração de despesa/política e quais pré-condições de refinanciamento são necessárias segundo a EF? Qual é o ambiente de teste autorizado?
11. Qual comportamento é esperado sem despesa, sem reaproveitamento, com ambos e em caso de erro/ausência de dados?
12. O que constitui a evidência válida de saída: resposta do endpoint, documentação de API, tela do Autorizador ou combinação? Como sanitizar dados antes de armazenar evidência?

## Exercício de recálculo/margem de tolerância

13. Qual é a EF e o identificador exato do projeto citado em `00:30:13–00:30:21`? A leitura numérica do ASR é incerta.
14. Qual implementação anterior é pré-requisito, e como confirmar que está disponível no ambiente de teste?
15. Como se calculam limites mínimo/máximo e tolerância percentual? Limites são inclusivos? Como tratar arredondamento, precedência, valor exatamente na borda e configurações ausentes?
16. Quais cenários e resultados esperados o negócio exige para valores abaixo, dentro e acima dos limites?
17. Quais dados de proposta/convênio podem ser criados em sandbox e quem autoriza a preparação da massa?

## Cobertura da fonte

18. O áudio declarado tem `00:35:47.18` e o último cue termina em `00:35:43.14`; a duração ASR declarada é `1651.5 s` sem definição. Há fala não reconhecida nos intervalos sem segmentos? Quem revisará áudio/telas integralmente?
