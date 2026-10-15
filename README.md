# Função — biblioteca de treinamento

Este repositório reúne gravações de treinamento e um processo para convertê-las em material de estudo rastreável para o trabalho diário na Função Sistemas. Os vídeos são fontes primárias: preserve o conteúdo e registre dúvidas, cortes e partes inaudíveis.

## Comece aqui

1. Leia [`PLANO_EXTRACAO_ARENA.md`](PLANO_EXTRACAO_ARENA.md) para conhecer as etapas, categorias, revisão de prints e critérios de conclusão.
2. Use [`BAIXAR_VIDEO_SOB_DEMANDA.md`](BAIXAR_VIDEO_SOB_DEMANDA.md) para obter somente o vídeo do lote atual. O endpoint de conteúdo do GitHub pode mostrar um ponteiro LFS de 134 bytes; baixe os bytes via Git LFS em um clone.
3. Cole o prompt de início do Arena.ai fornecido junto com o plano; o roteiro operacional está em [`ROTEIRO_ARENA.md`](ROTEIRO_ARENA.md).
4. Use [`manifesto.csv`](manifesto.csv) para identificar cada vídeo. Produza um diretório por vídeo em `materiais/`, sem combinar gravações diferentes. Atualize [`STATUS.md`](STATUS.md) e registre timestamps `HH:MM:SS` em toda afirmação específica.
5. Publique documentos e prints apenas após revisar privacidade e diffs. Não publique segredos ou dados pessoais nos materiais derivados.

## Conteúdo esperado por gravação

- `transcricao.md`, `guia_de_estudo.md`, `procedimentos.md`, `perguntas.md`, `glossario.md`, `incertezas.md` e `metadados.md`.
- `capturas.md` e `capturas/` quando imagens sanitizadas ajudarem a ensinar uma tela ou procedimento.
- Classificação consistente por SQL, sistemas, processos, negócio, infraestrutura/acesso e dúvidas/conflitos.

Os índices transversais em `materiais/` conectam gravações, consultas SQL, sistemas, processos e glossário, sempre preservando a origem detalhada.

## Ferramentas (`tools/`)

| Comando | Para que serve |
|---|---|
| `python3 tools/baixar_objeto_lfs.py "ARQUIVO.mp4"` | Baixa **um único** objeto LFS pela API do repositório (com retomada e conferência de tamanho/SHA-256), sem `git lfs pull` geral. `--verificar` só confere. |
| `python3 tools/checar_manifesto.py` | Confere `manifesto.csv` e `partes-videos.json` contra os arquivos locais: ponteiros, tamanhos, partes e objetos LFS repetidos. Não baixa nada. |
| `python3 tools/validar_materiais.py` | Auditoria do §6 do plano: arquivos obrigatórios, metadados, timestamps, perguntas, links e varredura de privacidade (CPF/CNPJ, e-mail, telefone, segredos). Nunca imprime o valor sensível encontrado. Saída: 0 ok, 1 falhas, 2 achado de privacidade. |
| `python3 tools/transcrever.py --video "ARQUIVO.mp4"` | Transcreve com timestamps (`faster-whisper`), gerando `transcricao_bruta.txt`, `.srt`, `.vtt` e `transcricao_meta.json`. Precisa dos pesos do modelo — rode no runner do CI. |
| `python3 tools/reconstruir_videos.py` | Reconstrói os quatro vídeos divididos (exige todas as partes). |
| `python3 tools/gerar_base_conhecimento_html.py` | Gera o **material de estudo em HTML único** (`saida/index.html`): cada capítulo temático abre com a **explicação do assunto** (síntese autoral) e segue com o detalhamento por origem — guias, procedimentos, glossários, perguntas, pendências, índices e trilhas. O texto **explica** o conhecimento: não há marcas de tempo, trechos citados de fala nem nomes de arquivo, ligação interna ou jargão de controle do acervo. A limpeza acontece **antes** de escrever a saída e o gerador **falha** se algum resquício passar. |
| `python3 tools/servir_material.py` | Serve o material gerado em `0.0.0.0:8000` (rota `/download` para baixar o arquivo). Não expõe nada além da pasta de saída; listagem de diretório desativada. |

As duas verificações rodam automaticamente em cada push/PR pelo workflow `.github/workflows/auditar-materiais.yml`, que faz checkout **sem** baixar LFS.

Workflows auxiliares para ambientes sem acesso ao host de conteúdo do LFS (uma gravação por vez, nunca a coleção):

- `.github/workflows/transferir-gravacao.yml` — baixa **um** objeto do LFS no runner, confere tamanho/SHA-256 contra o manifesto e publica blocos < 100 MB em ramo temporário `entrega/*`, removido depois. **Atenção:** apagar o ramo não remove os objetos do servidor — ver [`materiais/PRIVACIDADE_E_RETENCAO.md`](materiais/PRIVACIDADE_E_RETENCAO.md).
- `.github/workflows/transcrever-gravacao.yml` — transcreve **uma** gravação com timestamps e publica o texto no mesmo tipo de ramo temporário (os pesos do modelo são alcançáveis no runner).

**Materiais restritos** (documentação interna, informação de cliente, nomes/imagens de pessoas) **não** devem ser publicados neste repositório: mantenha-os em área privada fora do Git e registre a pendência em `materiais/CONFLITOS_E_VALIDACAO.md` sem revelar o conteúdo.

## Material de estudo em HTML (leitura e download)

Para ler o acervo inteiro como um só documento — e não como dezenas de arquivos — gere a base de
conhecimento:

```bash
python3 tools/gerar_base_conhecimento_html.py     # cria saida/index.html
python3 tools/servir_material.py                  # serve em http://localhost:8000
```

O documento é **autocontido** (CSS e busca embutidos, sem dependência de rede), tem índice lateral,
busca instantânea, blocos recolhíveis e estilo de impressão. Ele não cita nomes de arquivos nem
ligações internas: as fontes aparecem por rótulo descritivo com selos de categoria e de
confiabilidade. A pasta `saida/` é artefato de build e **não** entra no Git.

**Como o material foi escrito.** O objetivo é aprender o assunto, não acompanhar o registro: cada
capítulo temático começa com uma explicação autoral do domínio (regras, fluxo, nomenclatura) e só
depois desce ao detalhe por origem. Nada no texto aponta *quando* algo foi dito — os carimbos de
tempo, as âncoras de mensagem, as datas de análise e a narrativa de captura (ASR, transcrição,
amostragem de tela) foram removidos na limpeza, e as falas citadas saem inteiras em vez de saírem
apenas as aspas. Quando a fonte indicava horário como **dado** de negócio — um `SELECT` com coluna de
data, um payload com timestamp — o valor permanece, porque ali ele é conteúdo técnico e não
referência de vídeo.

A verificação é parte do gerador: ele recusa a saída se encontrar marca de tempo, aspas de citação,
âncora de mensagem, nome de arquivo de mídia, caminho de pasta do acervo ou jargão interno (LFS,
manifesto, ponteiro, checksum, commit). Basta rodar `python3 tools/gerar_base_conhecimento_html.py` e
conferir a linha de resumo.

## Fontes textuais (conversas de trabalho)

A biblioteca aceita um segundo tipo de fonte primária: **recortes de conversa de trabalho** (chat/Teams),
analisados com **âncoras `[Mnn]`** (índice da mensagem) em vez de timestamps de mídia — conversa não tem
`HH:MM:SS`. As regras estão em [`materiais/CONVENCOES_FONTES_TEXTUAIS.md`](materiais/CONVENCOES_FONTES_TEXTUAIS.md)
e o auditor (`tools/validar_materiais.py`) reconhece o pacote que se declara `**Tipo de fonte:** conversa`
em `metadados.md`.

- **Síntese do lote de conversas:** [`materiais/ANALISE_CONVERSAS_2026-10-15.md`](materiais/ANALISE_CONVERSAS_2026-10-15.md).
- **Trilhas de estudo derivadas:** [`materiais/TRILHAS_DE_ESTUDO.md`](materiais/TRILHAS_DE_ESTUDO.md).
- **Material pessoal/restrito** (contexto privado que não deve ser publicado) fica em `restrito/`,
  **ignorado pelo Git** — ver [`restrito/LEIA-ME.md`](restrito/LEIA-ME.md). Nunca usar `git add -f` nessa pasta.

## Integridade, privacidade e limites de publicação

Não invente conteúdo ausente. Diferencie fala/observação, síntese e inferência. Minimize nomes, dados de clientes, credenciais e dados pessoais nos materiais derivados; mascare segredos de modo irreversível em qualquer print ou omita a captura se não puder sanitizar com confiança. Este repositório é público: antes de enviar novos derivados, verifique se o material pode ser compartilhado publicamente pela empresa. Não publique documentação interna restrita, informação de clientes ou fluxos confidenciais sem autorização do responsável pela divulgação.

Quatro vídeos excedem o limite individual do Git LFS e estão armazenados como partes binárias exatas. Consulte [`RECUPERAR_VIDEOS.md`](RECUPERAR_VIDEOS.md) para reconstrução geral e [`BAIXAR_VIDEO_SOB_DEMANDA.md`](BAIXAR_VIDEO_SOB_DEMANDA.md) para baixar somente um piloto.
