# Função — biblioteca de treinamento

Este repositório reúne gravações de treinamento e um processo para convertê-las em material de estudo rastreável. Os vídeos são fontes primárias: preserve o que foi dito/mostrado e marque dúvidas, cortes e partes inaudíveis.

## Comece aqui

1. Leia [`ROTEIRO_ARENA.md`](ROTEIRO_ARENA.md) antes de analisar qualquer gravação.
2. Use [`manifesto.csv`](manifesto.csv) para identificar cada vídeo. O identificador é o nome do arquivo, sem extensão.
3. Produza um diretório por vídeo em `materiais/`, usando o nome do vídeo como slug seguro. Não combine gravações diferentes.
4. Atualize [`STATUS.md`](STATUS.md) ao iniciar e concluir cada item.
5. Compare cada afirmação do material com o vídeo e inclua timestamps `HH:MM:SS`.

## Estrutura esperada por gravação

- `transcricao.md` — transcrição integral, com timestamps e identificação de falantes quando possível.
- `guia_de_estudo.md` — objetivos, conceitos, explicação passo a passo, exemplos, termos e resumo.
- `procedimentos.md` — processos ensinados, pré-requisitos, entradas, ações, decisões, resultados e exceções.
- `perguntas.md` — perguntas de revisão e respostas fundamentadas nos timestamps.
- `glossario.md` — vocabulário e siglas contextualizados.
- `incertezas.md` — trechos inaudíveis, ambiguidades, divergências e pontos que exigem confirmação humana.
- `metadados.md` — arquivo fonte, duração, data de análise, ferramenta/modelo e limitações.

## Integridade e privacidade

Não invente conteúdo ausente. Diferencie explicitamente observação, fala literal, resumo e inferência. Registre nomes de clientes, documentos, credenciais ou dados pessoais apenas quando forem necessários para entender o procedimento; mascare valores secretos e minimize dados identificáveis nos materiais derivados. Como os vídeos originais foram autorizados para este repositório público, não replique segredos em transcrições ou exemplos.


Quatro vídeos excedem o limite individual do Git LFS e estão armazenados como partes binárias exatas. Consulte [RECUPERAR_VIDEOS.md](RECUPERAR_VIDEOS.md) para reconstruí-los antes da análise.
