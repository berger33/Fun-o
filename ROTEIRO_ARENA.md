## Preparação obrigatória

Antes de iniciar a análise, baixe todos os objetos Git LFS. Leia `partes-videos.json` e execute `python tools/reconstruir_videos.py` para recompor e validar os quatro vídeos divididos. Confirme a conclusão do script e só então analise cada vídeo original listado em `manifesto.csv`, sem tratar fragmentos `.partNNN` como gravações separadas. Se a validação falhar, interrompa a análise do vídeo afetado e registre o problema.
# Roteiro de análise para Arena.ai

## Objetivo

Analise **cada vídeo individualmente** desta coleção e transforme todo o conteúdo instrutivo audível e visível em material de estudo completo, fiel à fonte, pesquisável e verificável. Não encerre após um resumo superficial: percorra o vídeo do início ao fim, inclusive demonstrações na tela, ressalvas, perguntas, respostas, exemplos, exceções e etapas repetidas que acrescentem informação.

## Regras de execução

1. Leia `manifesto.csv` e `STATUS.md`. Faça uma gravação por vez e marque seu estado; não misture falas ou procedimentos de arquivos diferentes.
2. Confirme o nome do arquivo e a duração. Assista/analise a gravação integralmente, em ordem. Use trechos menores quando necessário para manter precisão e retome do último timestamp confirmado.
3. Para cada fato importante, procedimento, definição, exemplo ou ressalva, anote timestamp `HH:MM:SS`. A transcrição deve cobrir toda fala compreensível; marque `[inaudível HH:MM:SS–HH:MM:SS]` em vez de adivinhar.
4. Separe: **(a)** conteúdo explícito no vídeo, **(b)** síntese didática, **(c)** inferência sua. Identifique inferências e não as apresente como regra ensinada.
5. Preserve números, nomes de campos, ordem das ações, condições, exceções e consequências conforme a fonte. Se algo parecer errado, contraditório ou desatualizado, registre como ponto a validar, sem corrigir silenciosamente.
6. Não invente telas, passos, definições ou respostas. Quando a imagem estiver ilegível, o falante não puder ser identificado ou houver ambiguidade, registre a limitação em `incertezas.md`.
7. Trate credenciais, tokens, senhas, chaves, dados bancários/documentais e dados pessoais com minimização: não transcreva valores secretos. Use `[SEGREDO OMITIDO]` ou `[DADO PESSOAL OMITIDO]`, mantendo contexto e timestamp suficientes para localizar o trecho. Não inclua esses valores em perguntas, respostas, exemplos ou nomes de arquivos.
8. Ao final, faça uma auditoria de cobertura comparando a duração total com os timestamps da transcrição e do guia. Todo intervalo instrutivo deve estar coberto ou explicitamente marcado como não instrutivo/inaudível.

## Arquivos obrigatórios por vídeo

Crie `materiais/<slug-do-arquivo>/` contendo:

### `transcricao.md`
Transcrição integral com timestamps regulares e em cada mudança de assunto/etapa. Identifique os falantes como `Instrutor`, `Participante 1` etc. quando não souber seus nomes. Descreva elementos visuais relevantes entre colchetes, com timestamp. Remova segredos conforme a regra 7.

### `guia_de_estudo.md`
Inclua título, objetivo do treinamento, público/pré-requisitos, visão geral, conceitos explicados, explicação didática de todas as etapas, exemplos do vídeo, erros e cuidados citados, resumo final e referência temporal em cada seção. Uma pessoa que não assistiu ao vídeo deve conseguir estudar o conteúdo sem perder os detalhes instrutivos.

### `procedimentos.md`
Para cada fluxo demonstrado, descreva pré-condições, dados/insumos necessários (sem valores pessoais), sequência numerada, decisões e ramificações, resultado esperado, exceções/erros e timestamp. Mantenha fluxos separados.

### `perguntas.md`
Crie pelo menos 10 perguntas de revisão ou uma por conceito/etapa relevante se houver menos de 10. Inclua resposta, justificativa breve e timestamp(s). Cubra compreensão, ordem de passos, aplicação em cenário e exceções. Não crie fatos externos.

### `glossario.md`
Liste siglas, termos técnicos e nomes de campos exatamente como aparecem (salvo dado pessoal), explicando apenas o significado sustentado pelo vídeo; timestamp para cada termo.

### `incertezas.md`
Registre lacunas, trechos inaudíveis/ilegíveis, possíveis contradições, conteúdo possivelmente sensível omitido e perguntas que exigem validação humana. Se não houver, escreva `Nenhuma identificada`, após conferir.

### `metadados.md`
Registre nome original, tamanho conforme manifesto, duração, cobertura temporal, data da análise, ferramenta/modelo usado, idioma e limitações. Não declare validação por ferramenta que não foi usada.

## Controle de qualidade

Antes de marcar `concluído` em `STATUS.md`, verifique: (1) vídeo percorrido até o final; (2) transcrição cobre toda fala inteligível; (3) guia cobre demonstrações e exceções; (4) procedimentos respeitam a ordem mostrada; (5) perguntas têm respostas rastreáveis; (6) todas as afirmações específicas têm timestamp; (7) segredos/dados pessoais foram minimizados; (8) incertezas foram registradas. Se qualquer item falhar, marque `em revisão` e explique.

## Relatório final

Ao terminar a coleção, atualize `STATUS.md` com contagem de concluídos, em revisão e pendentes; liste obstáculos e vídeos que precisam de revisão humana. Não alegue que a coleção está completa enquanto houver pendências.

