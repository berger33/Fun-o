# Capturas — Gravando 2026-07-08 182343.mp4

**Revisão de privacidade (obrigatória, feita antes de publicar):** todas as imagens abaixo foram recortadas **dentro da janela do documento/tela demonstrada**. Ficaram **fora** do recorte: participantes da reunião (câmeras/avatares), a faixa de identificação do sistema (usuário/servidor/versão — o usuário já aparece desfocado na origem), a barra de endereço com o caminho do ambiente, o valor da OS (desfocado na origem), a barra de tarefas com data/hora da estação e a telemetria da ferramenta de PDF. As capturas foram conferidas em ampliação depois do recorte. Nenhuma credencial, token ou dado pessoal aparece nas imagens.

Cada arquivo abaixo foi rotulado após conferir o timestamp **no próprio quadro** (o timestamp foi impresso no nome do quadro de origem durante a amostragem).

## Capturas publicadas

| # | Arquivo | Timestamp | Contexto | O que comprova | Onde é usada |
|---|---|---|---|---|---|
| 01 | [`capturas/01-documento-incidente-tolerancia.png`](capturas/01-documento-incidente-tolerancia.png) | `00:03:12` | Documento `Incidente01.pdf` em tela cheia, aberto fora do compartilhamento. | A regra escrita (“Tolerância mínimo e máximo deveriam permitir valores entre 0 e 99. Porém, o sistema está permitindo entre 0 e 100”), a seção **Evidência** com a caixa `Limites do Valor Solicitado` (campos em `100,00`) e a seção “De acordo com a EF: Detalhamento dos Campos”. O cabeçalho do documento aparece **em branco** (sem OS, cliente ou analista). | [`guia_de_estudo.md`](guia_de_estudo.md) §2.5; [`procedimentos.md`](procedimentos.md) Fluxo C |
| 02 | [`capturas/02-evidencia-limites-tolerancia.png`](capturas/02-evidencia-limites-tolerancia.png) | `00:03:12` | Ampliação (2,2×) da caixa de evidência dentro do mesmo documento. | Leitura dos rótulos e valores: `Valor mínimo solicitado 0,00`, `Valor máximo solicitado 0,00`, `(%) Tolerância mínimo 100,00`, `(%) Tolerância máximo 100,00`, `Aplicar tolerância em: NaoSelecionado`, botões `Confirmar`/`Cancelar`/`Voltar`. | [`guia_de_estudo.md`](guia_de_estudo.md) §2.5; [`glossario.md`](glossario.md) |
| 03 | [`capturas/03-importar-modelo-decisao.png`](capturas/03-importar-modelo-decisao.png) | `00:07:35` | Diálogo **Importar Modelo de Decisão** da aplicação Autorizador Web. | Campos `Arquivo de Importação de Modelo de Decisão: Estaira112233.xml`, `Nº Modelo: 9999` com descrição `teste_tolerancia` e os botões `Confirmar`/`Cancelar`/`Voltar` (cursor sobre `Confirmar`). | [`procedimentos.md`](procedimentos.md) Fluxo B; [`glossario.md`](glossario.md) |
| 04 | [`capturas/04-ws-autorizador-estrutura.png`](capturas/04-ws-autorizador-estrutura.png) | `00:02:36` | Conteúdo da pasta `...\WS\WSAutorizador` no Explorador de Arquivos. | Composição do pacote do serviço Web: `bin`, `Config` (`09/09/2025 11:35`), `Estreia`, `Web References`, `Dados.dat`, `Global.asax`, `inst.dat`, `Web.Config`, `WSAutorizador.asmx`, `WsRegChaveLicenca.asmx`. A barra de endereço ficou fora do recorte. | [`guia_de_estudo.md`](guia_de_estudo.md) §2.1 |
| 05 | [`capturas/05-menu-servicos-configuracao.png`](capturas/05-menu-servicos-configuracao.png) | `00:06:10` | Submenu **Decisão** aberto dentro do menu `Serviços` da aplicação Autorizador Web. | O caminho de navegação e as opções `Tabela de Modelos`, `Tabela de Decisão`, `Relacionamento Modelo X Produto`, `Exportar Modelo Decisão`, `Importar Modelo Decisão`, `Visualizador de Fluxo Decisão`. O submenu-pai (`Gerenciamento de Bloqueios`, `Campos Editáveis`, `Campos Obrigatórios`, `Configuração de Processo`, `Decisão`, ...) aparece em segundo plano. | [`procedimentos.md`](procedimentos.md) Fluxo B |

## Capturas deliberadamente omitidas

| Tema | Timestamp aproximado | Motivo |
|---|---|---|
| Janela de reunião com participantes e lista de conversas | `00:00:00–00:00:18`; `00:08:25–00:08:35` | Imagens de pessoas e conversa de trabalho; não são didáticas para o conteúdo técnico. |
| Terminal escuro com operação de transferência | `00:01:55–00:02:15`; `00:03:40–00:05:05` | Conteúdo ilegível nos quadros amostrados — publicar uma imagem ilegível não agrega. |
| Listagem de arquivos em `...\bin` com bibliotecas internas | `00:05:10–00:05:30` | Reproduz grande quantidade de nomes internos de binários sem valor didático que já não esteja na captura 04. |
| Faixa de identificação do sistema (usuário/servidor/versão) | `00:02:25–00:06:15` | Referência de infraestrutura; foi recortada das capturas 04 e 05. |
| Lista de anotações sobre a área de trabalho | `00:10:20` | Texto ilegível; não é possível sanitizar com confiança. |

## Nota de manutenção

Se novas capturas forem produzidas a partir desta gravação, repetir o mesmo recorte mínimo (documento/tela), conferir o quadro ampliado antes de rotular o timestamp e atualizar a tabela acima. Ver a política em `PRIVACIDADE.md` e `materiais/PRIVACIDADE_E_RETENCAO.md`.
