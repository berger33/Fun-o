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

As duas verificações rodam automaticamente em cada push/PR pelo workflow `.github/workflows/auditar-materiais.yml`, que faz checkout **sem** baixar LFS.

Workflows auxiliares para ambientes sem acesso ao host de conteúdo do LFS (uma gravação por vez, nunca a coleção):

- `.github/workflows/transferir-gravacao.yml` — baixa **um** objeto do LFS no runner, confere tamanho/SHA-256 contra o manifesto e publica blocos < 100 MB em ramo temporário `entrega/*`, removido depois. **Atenção:** apagar o ramo não remove os objetos do servidor — ver [`materiais/PRIVACIDADE_E_RETENCAO.md`](materiais/PRIVACIDADE_E_RETENCAO.md).
- `.github/workflows/transcrever-gravacao.yml` — transcreve **uma** gravação com timestamps e publica o texto no mesmo tipo de ramo temporário (os pesos do modelo são alcançáveis no runner). Para acionar **somente** a transcrição, configure `transcricao/tarefa.json`; sua alteração não dispara a ponte de partes do vídeo. Também aceita `workflow_dispatch` com campos opcionais e pode baixar/reconstruir somente as partes do vídeo selecionado quando a fonte estiver dividida. `transferencia/tarefa.json` continua compatível, mas alterações nele podem disparar tanto a transcrição quanto a transferência de partes.

**Materiais restritos** (documentação interna, informação de cliente, nomes/imagens de pessoas) **não** devem ser publicados neste repositório: mantenha-os em área privada fora do Git e registre a pendência em `materiais/CONFLITOS_E_VALIDACAO.md` sem revelar o conteúdo.

## Integridade, privacidade e limites de publicação

Não invente conteúdo ausente. Diferencie fala/observação, síntese e inferência. Minimize nomes, dados de clientes, credenciais e dados pessoais nos materiais derivados; mascare segredos de modo irreversível em qualquer print ou omita a captura se não puder sanitizar com confiança. Este repositório é público: antes de enviar novos derivados, verifique se o material pode ser compartilhado publicamente pela empresa. Não publique documentação interna restrita, informação de clientes ou fluxos confidenciais sem autorização do responsável pela divulgação.

Quatro vídeos excedem o limite individual do Git LFS e estão armazenados como partes binárias exatas. Consulte [`RECUPERAR_VIDEOS.md`](RECUPERAR_VIDEOS.md) para reconstrução geral e [`BAIXAR_VIDEO_SOB_DEMANDA.md`](BAIXAR_VIDEO_SOB_DEMANDA.md) para baixar somente um piloto.
