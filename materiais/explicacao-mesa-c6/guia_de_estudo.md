> **Fonte:** ASR `faster-whisper large-v3`, sem VAD, 1.394 segmentos. O MP4/áudio/telas não foram revisados neste lote. Os tópicos abaixo são fala transcrita, não procedimento ou política vigente.

# Guia de estudo — explicacao mesa c6.mp4

- **Categoria:** `SISTEMAS`, `PROCESSOS`, `NEGOCIO`, `INFRA_E_ACESSO`, `DÚVIDA_OU_CONFLITO`.
- **Sistemas/áreas citados:** Autorizador, Empregador, SIC, Web Access, API/Test API, bases locais/compartilhadas, Planner, Gantt, Excel e ferramenta chamada Geradoc. Nomes/telas/configuração não foram conferidos visualmente.
- **Assunto:** ambientação de CQ, ciclo de projeto/teste e escrita de EPT; orientação sobre configuração de ambiente e execução de treinamento no Autorizador.
- **Confiança da extração:** **média** para os tópicos gerais; baixa para nomes, siglas, caminhos, configuração e detalhes do exemplo. ASR sem VAD tem falas de baixa inteligibilidade e quatro cues repetindo “Legenda Adriana Zanotto”.
- **Estado:** `em revisão`; material não aprovado para uso operacional.

## 1. Integração entre módulos e averbação (00:00:00–00:03:02)

A conversa afirma que mudanças podem envolver Autorizador e Empregador e que configuração em ambos pode ser necessária; menciona plugin, esteira e averbação. O interlocutor admite conhecer mais o “truncador” do que todos os módulos e diz não ter feito desaverbação nesse contexto. Não é uma especificação de integração nem define quando testar cada módulo.

## 2. Organização do trabalho de CQ (00:04:08–00:22:47)

O instrutor descreve colaboração com desenvolvimento e negócios, leitura da EF, alinhamentos sobre divergências, planejamento de sprints, cards/Planner e Gantt, estimativa de horas, reuniões/dailies e comunicação com desenvolvimento antes de abrir incidente. O relato também cita participação do cliente/banco em checkpoints. Nomes, responsabilidades, frequência, cadência e ferramentas não foram validados; não tratar como política atual.

## 3. Elaborar e manter uma EPT (00:22:51–00:33:10)

A orientação geral é ler a EF e escrever cenários de teste, pré-condições, ações e resultados esperados, depois passar o conteúdo a Excel/geração de documento e atualizá-lo conforme o teste evolui. O exemplo verbal é uma configuração de recálculo que preservaria um valor líquido original quando o valor recalculado fosse inferior; são citados dois processos/parametrizações e casos de configuração e comparação. Isso é um exemplo apresentado na conversa, não regra de negócio validada. Template, passos, campos, fórmula e resultado precisam da EF vigente.

A fala descreve evidências com data/hora e capturas de pontos relevantes; nenhum arquivo, planilha ou imagem foi conferido/produzido neste lote.

## 4. Ambientes, versões e configuração (00:33:11–00:45:04)

O interlocutor descreve uma máquina compartilhada/servidor e uma base de servidor com UDLs diferentes, além de pastas de aplicações e bases que podem atender a testes simultâneos. A fala contém instruções inconsistentes sobre apagar pastas, preservar/alterar `config`, copiar versões e qual ambiente utilizar. **Não seguir nenhuma dessas instruções até haver runbook atual, identificação do ambiente, autorização e rollback.** Nomes de máquinas e pastas presentes no TXT não foram confirmados.

## 5. Treinamento prático (00:46:20–00:57:29)

A transcrição enumera atividades: cadastrar usuário e direitos; produto/convênio; criar esteira e relacionar processos; cadastrar proposta; avançar controles; testar integração e API; comparar bases/ambientes. O interlocutor corrige a ordem entre simulação e inclusão da proposta e sugere copiar uma configuração para evitar interferir em teste alheio. Nenhum passo foi executado; a sequência e acesso privilegiado devem ser confirmados com material oficial.

## Limites e segurança

- A frase repetida pode ser erro do ASR, fala ou elemento visual; não foi confirmada.
- A palavra “SQL” e a menção a consultar tabela/banco não trazem query literal. Nenhum SQL foi executado.
- A fonte contém nomes e rótulos internos de máquina/pasta e menção genérica a login/senha; nenhum valor literal de credencial foi reconhecido no ASR. A tela não foi revisada.
- Não foram alterados arquivos de ambiente, pastas, perfis, bancos, APIs ou propostas; sem testes ou capturas.

Ver [`procedimentos.md`](procedimentos.md), [`perguntas.md`](perguntas.md), [`incertezas.md`](incertezas.md) e [`metadados.md`](metadados.md).
