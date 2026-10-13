# Função — biblioteca de treinamento

Este repositório reúne gravações de treinamento e um processo para convertê-las em material de estudo rastreável para o trabalho diário na Função Sistemas. Os vídeos são fontes primárias: preserve o conteúdo e registre dúvidas, cortes e partes inaudíveis.

## Comece aqui

1. Leia [`PLANO_EXTRACAO_ARENA.md`](PLANO_EXTRACAO_ARENA.md) para conhecer as etapas, categorias, revisão de prints e critérios de conclusão.
2. Cole o prompt de início do Arena.ai fornecido junto com o plano; o roteiro operacional está em [`ROTEIRO_ARENA.md`](ROTEIRO_ARENA.md).
3. Use [`manifesto.csv`](manifesto.csv) para identificar cada vídeo. O identificador é o nome do arquivo, sem extensão.
4. Produza um diretório por vídeo em `materiais/`, sem combinar gravações diferentes. Atualize [`STATUS.md`](STATUS.md) e registre timestamps `HH:MM:SS` em toda afirmação específica.
5. Publique documentos e prints apenas após revisar privacidade e diffs. Não publique segredos ou dados pessoais nos materiais derivados.

## Conteúdo esperado por gravação

- `transcricao.md`, `guia_de_estudo.md`, `procedimentos.md`, `perguntas.md`, `glossario.md`, `incertezas.md` e `metadados.md`.
- `capturas.md` e `capturas/` quando imagens sanitizadas ajudarem a ensinar uma tela ou procedimento.
- Classificação consistente por SQL, sistemas, processos, negócio, infraestrutura/acesso e dúvidas/conflitos.

Os índices transversais em `materiais/` conectam gravações, consultas SQL, sistemas, processos e glossário, sempre preservando a origem detalhada.

## Integridade e privacidade

Não invente conteúdo ausente. Diferencie fala/observação, síntese e inferência. Minimize nomes, dados de clientes, credenciais e dados pessoais nos materiais derivados; mascare segredos de modo irreversível em qualquer print ou omita a captura se não puder sanitizar com confiança.

Quatro vídeos excedem o limite individual do Git LFS e estão armazenados como partes binárias exatas. Consulte [`RECUPERAR_VIDEOS.md`](RECUPERAR_VIDEOS.md) para reconstruí-los antes da análise.
