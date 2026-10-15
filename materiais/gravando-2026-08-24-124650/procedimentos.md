> **Status:** planejamento de teste/evidência derivado de ASR; não é runbook aprovado e não foi executado. Use a EPT/EF vigente para a sequência final.

# Procedimentos — Gravando 2026-08-24 124650.mp4

## Fluxo A — Verificar uma alteração no plugin e no JSON (sandbox)

**Objetivo:** conferir que a alteração esperada está presente no retorno JSON do plugin para um cenário de proposta, sem quebrar o fluxo existente (**00:00:00–00:02:12**).

### Pré-condições

- EPT/EF aprovadas, propriedade/resultado esperado do JSON identificados e procedimento de esteira confirmado.
- Ambiente de teste isolado, versões autorizadas de Autorizador, subsite e plugin; rollback conhecido.
- Dados sintéticos aprovados para proposta, convênio e classificação necessária; sem identificadores reais.
- Autorização para consultar o retorno do plugin em ferramenta apropriada, com política de armazenamento de evidências.

### Plano de execução (não realizado nesta análise)

1. Conferir que o documento do teste, o cadastro sintético e a proposta descrevem o mesmo cenário. A conversa detecta uma divergência de promotora entre a evidência e a proposta (**00:04:00–00:04:19**); os valores originais foram omitidos.
2. Registrar a versão aprovada e o cenário, sem capturar caminhos/hosts internos ou dados pessoais.
3. Criar/usar a proposta sintética com os pré-requisitos definidos na EPT. A fala cita convênio e um valor exemplificativo, mas eles não são critérios aprovados (**00:03:10–00:05:09; 00:09:34–00:09:55**).
4. Percorrer as etapas da esteira seguindo a sequência oficial, não a numeração instável reconhecida pelo ASR (**00:10:12–00:12:23**).
5. Acionar o plugin pelo evento/etapa definido na especificação; confirmar execução e retorno pela ferramenta autorizada.
6. Comparar somente a propriedade/resultado definido na EF com o JSON observado; verificar regressões nos campos que o teste cobre (**00:01:12–00:01:51; 00:12:57–00:13:18**).
7. Registrar esperado versus observado e uma evidência legível e sanitizada. Parar se a versão, etapa, proposta ou resultado não corresponder ao cenário.

**Resultado deste lote:** nenhum teste executado ou payload validado.

## Fluxo B — Preparar evidência legível (proposta)

1. Confirmar o formato de evidência exigido pela equipe e manter somente telas necessárias para provar o cenário.
2. Incluir versão aprovada, contexto mínimo da proposta de teste, execução do plugin e resultado JSON pertinente (**00:11:15–00:13:18**).
3. Usar somente ferramenta de geração/compartilhamento autorizada. Geradoc é citado como opção para gerar documento a partir de planilha, mas o fluxo não foi demonstrado (**00:16:01–00:17:25**).
4. Conferir legibilidade, remover dados pessoais/identificadores/endpoints e verificar os limites de arquivo vigentes antes do envio.

Nenhuma captura foi produzida neste lote. Não executar “exportar/criar documento” em ambiente real com base apenas na fala.

## Fluxo C — Bloqueio de dados/SQL

A gravação inclui um intervalo não transcrito na cópia pública que trata de informação pessoal e de um procedimento de banco. Não há consulta SQL literal nos materiais públicos. Se o cenário de teste depender de uma liberação de dados, **interromper** e pedir ao responsável um método autorizado, ambiente, dados sintéticos e rollback. Não usar consultas repassadas por chat nem reproduzir alterações a partir do ASR.

## Exceções

- Etapas 2/3/4 ou rótulos de esteira não coincidem com EPT → interromper e confirmar o fluxo.
- JSON não contém o campo esperado ou a proposta/cadastro diverge → registrar como falha do cenário, sem alterar dados.
- Identificador não autorizado ou necessidade de escrita em base → não prosseguir; solicitar fixture sintética por canal aprovado.
- Nenhuma evidência pode conter segredo, dado pessoal ou identificador de cliente.
