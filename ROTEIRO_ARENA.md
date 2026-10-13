# Roteiro de análise para Arena.ai

## Objetivo

Analise integralmente cada vídeo desta coleção e converta todo o conteúdo instrutivo audível e visível em material de estudo completo, categorizado e rastreável, voltado ao trabalho diário na Função Sistemas. Siga o plano detalhado em [`PLANO_EXTRACAO_ARENA.md`](PLANO_EXTRACAO_ARENA.md). Não encerre em resumos superficiais: cubra falas, demonstrações, consultas SQL, processos, ressalvas, perguntas, respostas, exemplos e exceções.

## Instruções de execução

1. Leia `README.md`, `PLANO_EXTRACAO_ARENA.md`, `BAIXAR_VIDEO_SOB_DEMANDA.md`, `manifesto.csv`, `STATUS.md`, `PRIVACIDADE.md` e `RECUPERAR_VIDEOS.md`.
2. Trabalhe em um vídeo por vez. Não execute `git lfs pull` sem filtro nem reconstrua todos os vídeos divididos. Baixe apenas o vídeo do lote atual seguindo `BAIXAR_VIDEO_SOB_DEMANDA.md`; para um vídeo dividido, baixe somente suas partes e faça reconstrução seletiva com checagem de tamanho e SHA-256 conforme `partes-videos.json`.
3. Confirme que os bytes locais correspondem ao tamanho esperado no manifesto (ou ao total definido em `partes-videos.json`). Um ponteiro LFS pequeno retornado pela API de conteúdo não é o vídeo: use o clone local e Git LFS. Se LFS não estiver disponível, pare e reporte o bloqueio concreto; não invente conteúdo.
4. Analise o arquivo original por inteiro e em ordem, retomando de checkpoint em `STATUS.md`. Para cada fato, conceito, procedimento, código ou tela relevante, registre fonte e timestamp `HH:MM:SS`. Separe transcrição/observação, síntese didática e inferência. Marque inaudível/ilegível em vez de adivinhar.
5. Categorize cada item como `SQL`, `SISTEMAS`, `PROCESSOS`,`NEGOCIO`, `INFRA_E_ACESSO` e/ou `DÚVIDA_OU_CONFLITO`. Use também sistema/módulo e assunto quando conhecidos.
6. Siga os requisitos específicos de SQL, sistemas e prints em `PLANO_EXTRACAO_ARENA.md`. Nunca execute SQL nem altere dados de sistemas. Identifique efeitos de comandos de alteração e marque validação operacional necessária.
7. Minimize dados pessoais e segredos. Não os copie para texto, código, captura, log, commit ou resposta; use `[SEGREDO OMITIDO]`/`[DADO PESSOAL OMITIDO]` e timestamp. Como o repositório é público, não publique documentação interna restrita, informação de clientes ou fluxos confidenciais sem autorização explícita da empresa. Prints derivados devem ser revisados e sanitizados antes de entrarem no Git.
8. Produza todos os arquivos obrigatórios por vídeo. Depois atualize os índices transversais descritos no plano. Mantenha links relativos funcionais e fonte detalhada sem duplicação silenciosa.
9. Faça controle de qualidade e verifique o diff antes de cada publicação. Envie ao GitHub em lotes pequenos revisáveis; descreva o lote e atualize `STATUS.md`. Se houver dúvida de privacidade/divulgação pública, não publique o material afetado; registre a pendência sem revelar o conteúdo e peça orientação ao responsável autorizado.
10. Não pare para perguntar sobre detalhes rotineiros: escolha a interpretação mais conservadora, documente incerteza e avance. Interrompa somente se a fonte não estiver disponível, a validação/reconstrução falhar, ou uma decisão humana for necessária para tratar privacidade, confidencialidade ou risco de exposição.

## Estrutura obrigatória por vídeo

Em `materiais/<slug>/`, crie:

- `transcricao.md` — toda fala compreensível com timestamps; falantes identificados genericamente se necessário; indicações visuais relevantes; segredos omitidos.
- `guia_de_estudo.md` — objetivo, público/pré-requisitos, metadados de categoria/sistema/assunto/confiança, conceitos, explicações, exemplos, erros/cuidados e resumo; seções ligadas a timestamps.
- `procedimentos.md` — pré-condições, entradas, sequência numerada, decisões, validações, resultado, exceções e timestamp; fluxos separados.
- `perguntas.md` — pelo menos 10 perguntas ou uma por conceito/etapa relevante se menos de 10; respostas com justificativa e timestamps.
- `glossario.md` — siglas, termos técnicos e campos com significado sustentado e timestamp.
- `incertezas.md` — lacunas, contradições, dados omitidos e validações humanas necessárias; ou`Nenhuma identificada` após revisão.
- `metadados.md` — nome original, tamanho conforme manifesto, duração, cobertura, data, ferramenta/modelo, idioma e limitações.
- `capturas.md` e `capturas/` — somente se imagens forem didaticamente úteis; cada captura com legenda, timestamp, contexto, finalidade e revisão de privacidade. Se não forem úteis, registre isso em `capturas.md`.

## Índices da biblioteca

Mantenha em `materiais/`:

- `INDICE.md`
- `SQL/INDICE_SQL.md`
- `SISTEMAS/INDICE_SISTEMAS.md`
- `PROCESSOS/INDICE_PROCESSOS.md`
- `GLOSSARIO_GERAL.md`
- `CONFLITOS_E_VALIDACAO.md`

Atualize os índices a cada lote. Cada entrada deve apontar ao vídeo, documento e timestamp que sustentam o tópico.

## Controle de qualidade e relatório

Antes de marcar cada vídeo como `concluído`, confira cobertura integral, timestamps, fidelidade de SQL e procedimentos, utilidade/legibilidade/sanitização dos prints, incertezas, privacidade/confidencialidade e links. Faça commits pequenos e publique no repositório só depois da revisão de conteúdo e divulgação pública permitida.

Ao concluir a coleção, informe totais concluídos/em revisão/pendentes, categorias encontradas, índices criados, capturas incluídas/omitidas, commits publicados e limitações. Nunca afirme conclusão se algum vídeo ou trecho instrutivo permanecer sem análise.
