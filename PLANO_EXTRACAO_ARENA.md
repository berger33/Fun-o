# Plano de extração e organização do conhecimento — Função Sistemas

## Resultado esperado

Converter todas as gravações do repositório em uma biblioteca de referência de trabalho: conteúdo completo, organizado por assunto, com instruções reproduzíveis, exemplos SQL, guias de sistemas e processos, evidências visuais úteis e ligação de cada afirmação à gravação e ao timestamp de origem.

A gravação é a fonte primária. O material serve como apoio operacional; não substitui validação de regras que possam ter mudado. Não deduza procedimentos ausentes nem transforme uma tela demonstrada em autorização de acesso.

## Princípios

- Cobertura integral, um vídeo de cada vez; mantenha origem e timestamps em todos os documentos.
- Separe transcrição, observação da tela, explicação didática e inferência.
- Preserve nomes, ordem, condições, valores de exemplo e exceções ensinados, exceto dados sensíveis, que devem ser omitidos ou mascarados.
- Mantenha informação conflitante em evidência com as duas fontes e timestamps; não escolha uma versão sem confirmação.
- Não publique senhas, tokens, chaves, dados pessoais ou dados de clientes. Para qualquer trecho sensível, deixe nota neutra e timestamp em `incertezas.md`; não inclua o valor nem em prints, histórico, exemplos ou nomes de arquivo.
- Use screenshots apenas quando acrescentarem orientação visual; cada imagem deve ter legenda, timestamp, origem e descrição do que comprova.
- Produza documentos em Markdown e imagens em PNG/JPG comprimido, sem sacrificar legibilidade.

## Etapas de execução

### 0. Preparar e verificar as fontes

1. Clone/atualize o repositório e leia `README.md`, `ROTEIRO_ARENA.md`, `manifesto.csv`, `STATUS.md`, `PRIVACIDADE.md` e `RECUPERAR_VIDEOS.md`.
2. Baixe os objetos Git LFS. Reconstrua os vídeos fragmentados com `python tools/reconstruir_videos.py`; use apenas originais reconstruídos, nunca `.partNNN` como vídeo independente.
3. Confirme a lista de fontes, nomes, durações e legibilidade. Registre falhas sem declarar o respectivo vídeo analisado.
4. Não copie segredos para arquivos temporários que serão enviados ao GitHub. Se um segredo aparecer na tela, pause a captura/transcrição daquele trecho e registre apenas a ocorrência e o timestamp.

### 1. Inventário e fila de análise

1. Confira cada linha do `manifesto.csv` com o arquivo correspondente.
2. Atualize `STATUS.md` com todos os vídeos e estados `pendente`, `em análise`, `em revisão` ou `concluído`.
3. Analise cada gravação integralmente e em ordem. Salve checkpoints de timestamp para permitir retomada.
4. Não funda gravações, mesmo quando repetirem o mesmo treinamento. A repetição pode ser uma versão posterior ou conter diferenças.

### 2. Extração completa por vídeo

Para cada fonte, crie `materiais/<slug>/` e os documentos prescritos no `ROTEIRO_ARENA.md`: transcrição, guia de estudo, procedimentos, perguntas, glossário, incertezas e metadados.

Registre todas as falas instrutivas, demonstrações de tela, exemplos, decisões, ressalvas, perguntas e respostas. A transcrição cobre toda fala compreensível. Marque trechos inaudíveis ou ilegíveis com timestamp, sem completar por suposição.

### 3. Classificação do conteúdo

Classifique cada unidade de conhecimento com uma ou mais categorias e tags consistentes:

- `SQL`: consultas e comandos, funções, filtros, junções, agrupamentos, subconsultas, tabelas, colunas, esquemas, relacionamentos, parâmetros, erros, desempenho e regras de negócio mencionadas.
- `SISTEMAS`: sistema/módulo/tela, finalidade, navegação, campos, ações, estados, mensagens, permissões mencionadas, integrações e dependências.
- `PROCESSOS`: rotina operacional, sequência, responsáveis/funções quando ditas, pré-condições, decisões, exceções, resultado e conferência.
-`NEGOCIO`: conceitos, regras, cálculos, cadastros, eventos e vocabulário da Função Sistemas sustentados pelo vídeo.
- `INFRA_E_ACESSO`: configuração ou acesso técnico mencionado. Nunca guardar credenciais nem sugerir contornar controles.
- `DÚVIDA_OU_CONFLITO`: informação incerta, contraditória, potencialmente desatualizada ou dependente de confirmação.

Inclua no início dos guias uma linha de metadados com `Categoria`, `Sistema`, `Assunto`, `Fonte` e `Confiança da extração` (`alta`, `média` ou `baixa`, com justificativa curta). Categorias não são mutuamente exclusivas.

#### Requisitos adicionais para SQL

Quando houver SQL, registre o trecho exatamente como aparece ou é falado, com formatação e explicação linha a linha. Identifique o dialeto somente se for explicitamente conhecido ou claramente sustentado; caso contrário use`não identificado`. Documente objetivo, tabelas/colunas citadas, parâmetros, filtros, junções, saída esperada, contexto de negócio, timestamp e limitações.

Separe consultas somente de leitura de comandos que alteram dados. Para `INSERT`, `UPDATE`, `DELETE`, DDL ou comandos potencialmente destrutivos, sinalize claramente o efeito descrito e a necessidade de validação/autorização operacional; não execute nenhum comando. Masque valores sensíveis e substitua-os por placeholders explicados. Não “corrija” SQL do vídeo sem manter a forma original e identificar separadamente a sugestão como hipótese a validar.

#### Requisitos para sistemas e processos

Para cada tela ou fluxo relevante, documente nome visível do sistema/módulo, objetivo, caminho de navegação mostrado, pré-requisitos mencionados, sequência, campos obrigatórios e seus significados, decisões, validações, mensagens de erro, resultado e como o usuário confirma a conclusão. Marque explicitamente campos ou etapas não legíveis/não demonstrados. Registre papel/perfil apenas quando dito ou mostrado; não inferir permissões.

### 4. Capturas de tela com critério

Inclua captura quando ajudar a identificar uma tela, campo, sequência, estado, resultado ou mensagem que seria difícil descrever só em texto. Não faça captura decorativa nem uma imagem por timestamp.

Salve imagens em `materiais/<slug>/capturas/` com nomes ordenáveis (`01-tela-inicial.png`). Adicione `capturas.md` com arquivo, timestamp, contexto, descrição, utilidade didática e referência no procedimento correspondente. Use recorte legível e inclua contexto suficiente para localizar a região.

Antes de salvar qualquer captura, revise a imagem inteira e o recorte ampliado para identificar nomes, e-mails, CPF/CNPJ, telefones, clientes, dados financeiros, URLs privadas, hosts, usuário, senha, tokens, chaves, IDs ou informações internas restritas. Mascare irreversivelmente o conteúdo sensível na cópia derivada e confira a imagem final. Se não puder sanitizar com confiança, não inclua a captura; documente a omissão em `incertezas.md`. Nunca altere a gravação original.

### 5. Construir a biblioteca transversal

Depois de extrair os vídeos, mantenha os seguintes documentos na raiz de `materiais/`:

- `INDICE.md`: lista de gravações e links, por categoria, sistema e assunto, com estado de revisão.
- `SQL/INDICE_SQL.md`: catálogo de consultas/conceitos com objetivo, origem/timestamp, tabelas citadas, tipo (`leitura`/`alteração`) e link para a análise detalhada. Não duplicar consulta sem indicar todas as fontes.
- `SISTEMAS/INDICE_SISTEMAS.md`: catálogo de sistemas, módulos e telas, com links para procedimentos e capturas pertinentes.
- `PROCESSOS/INDICE_PROCESSOS.md`: rotinas em ordem de execução, pré-requisitos, resultado, exceções e fontes.
- `GLOSSARIO_GERAL.md`: termos e siglas consolidados, definição sustentada, categoria e todas as fontes/timestamps relevantes.
- `CONFLITOS_E_VALIDACAO.md`: divergências entre vídeos, possíveis mudanças de versão e perguntas para validação humana, com evidências.

Índices devem apontar para a fonte detalhada, não remover nuance nem converter hipótese em regra. Quando possível, acrescente ligações entre consulta SQL, tela/processo que a contextualiza e vídeos correlatos.

### 6. Revisão de qualidade e privacidade

Para cada vídeo, antes de marcar `concluído`, valide:

1. A fonte foi vista/analisada do início ao fim e a transcrição cobre a fala inteligível.
2. Cada conteúdo técnico e afirmação específica tem timestamp rastreável.
3. SQL foi preservado fielmente, categorizado por efeito e não executado.
4. Passos, condições, campos, erros e exceções demonstrados foram cobertos.
5. Prints escolhidos acrescentam valor, estão legíveis, sanitizados e têm legenda/timestamp.
6. Incertezas e contradições estão registradas, sem resolução inventada.
7. Busca por segredos e dados pessoais foi feita no material derivado e nos prints.
8. Links entre índice, documentos e imagens funcionam.

Estados: `pendente` (não iniciado), `em análise` (extração em curso), `em revisão` (extração feita, auditoria ou confirmação pendente), `concluído` (critérios acima cumpridos). Concluir não significa que uma regra de negócio atual foi validada pela empresa.

### 7. Publicar no GitHub em lotes revisáveis

1. Faça commits pequenos após cada vídeo ou lote coerente. Inclua os documentos e capturas sanitizadas; não reescreva nem substitua as gravações originais.
2. Antes de cada push, revise `git diff --check`, a lista de arquivos e o diff de texto/imagens para garantir que nenhum segredo ou dado pessoal foi incluído. Não envie chaves, dumps ou arquivos temporários.
3. Atualize `STATUS.md`, `materiais/INDICE.md` e os índices temáticos no mesmo lote em que os materiais forem concluídos.
4. Envie para o repositório público somente material aprovado pela verificação de privacidade. Registre commit, lote e data em `STATUS.md`.
5. Se encontrar segredo ativo em uma gravação já publicada, não o replique no derivado; sinalize a ocorrência com timestamp para decisão do responsável. Não coloque o valor sensível em issue, commit, log ou relatório.

## Critério de conclusão do plano

A coleção só pode ser anunciada como extraída quando cada vídeo do manifesto estiver `concluído`, todo conteúdo estiver categorizado e ligado a timestamps, os índices transversais estiverem atualizados, as capturas úteis estiverem sanitizadas, e pendências de confirmação estiverem listadas separadamente. Relate também limitações de qualidade de áudio/imagem, duração não processada, itens em revisão e commits publicados.

## Próxima ação

Abra o Arena com o repositório clonado e o Git LFS instalado/disponível. Cole o prompt de início que acompanha este plano. Execute um vídeo ou lote pequeno por vez, preserve os checkpoints e revise cada lote antes de seguir.
