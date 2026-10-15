# Incertezas e pendências — Primeiro projeto.mp4

## 1. Contrato do endpoint

- O ASR registra o rótulo **“Documentos anexados simplificado”** e o método `GET` (**00:02:00–00:02:25**), mas não fornece rota, parâmetros codificados, formato de request/response, autenticação ou código HTTP.
- A regra de dois parâmetros é lida como “condicionalmente obrigatórios”: um pode ser omitido se o outro for informado (**00:03:00–00:03:42**). Confirmar na EF se ambos podem ser enviados, qual resposta ocorre para cada combinação e como tratar identificadores conflitantes.
- “Nenhum parâmetro” é considerado inválido pela explicação, mas status e corpo de erro não são descritos (**00:03:33–00:03:42**).
- A lista de resposta é resumida como IDs de armazenamento/arquivo e nome/extensão (**00:03:52–00:04:23**); a grafia dos campos não foi lida com confiança. Conferir a tabela completa e o Anexo I da EF.
- Número da operação para download é mencionado como parâmetro novo, mas não fica claro se a chamada de download é um segundo endpoint ou parte do endpoint simplificado (**00:08:42–00:09:16**).

## 2. Relação GED, back-office e checklist

- A fala diz que o perfil GED usa número de proposta como identificador e que a consulta por operação faz uma busca interna do número correspondente no back-office (**00:07:37–00:08:29**). Não especifica resultado quando o mapeamento falta, é ambíguo ou diverge.
- A explicação diferencia arquivos GED do checklist e afirma que o endpoint simplificado não deve retornar informações de checklist (**00:04:41–00:05:09; 00:06:56–00:07:37**). Validar a distinção na EF e os casos limítrofes.
- A chave verbal `perfil gdoc` pode ter grafia diferente. Nenhum valor ou URL foi reproduzido; confirmar somente na documentação autorizada.
- A orientação de consultar uma base para encontrar o número de operação não inclui o `SELECT` prometido, nem tabelas/campos (**00:02:35–00:02:57**). Não inventar query nem usar uma base de produção.

## 3. Montagem do ambiente e evidências

- Autorizador, subsite, Gdoc, IES e Web API são citados sem versões, rotas, dependências completas ou tela demonstrativa (**00:09:18–00:11:36**).
- “Versões aprovadas/mais recentes” é uma recomendação oral, não a política de release da organização (**00:10:29–00:10:42**).
- Menções a opções “N” e “W” e a geração de `PROC` não esclarecem o efeito técnico nem quais componentes devem usá-las (**00:13:12–00:16:02**). Confirmar procedimento vigente antes de gerar artefatos ou assumir que uma opção é obrigatória.
- Evidências sugeridas (versão, caminho, associação à requisição e retorno) não foram produzidas; não há teste concluído (**00:14:16–00:15:18**).

## 4. Sanitização e cobertura

- Um identificador de cliente e um nome de base/ambiente foram substituídos por marcadores na transcrição pública; os valores omitidos não devem ser reutilizados sem validação/autorização.
- O trecho após `00:16:15.94` foi omitido desta cópia porque é uma conversa não técnica, fora do escopo de aprendizagem; preservou-se um marcador temporal até `00:17:48.66`.
- O MP4, a EF, telas e requisições não foram inspecionados nesta etapa. O arquivo de entrada tem 274 segmentos ASR; o último encerra em `00:17:48.66` e a duração declarada é `00:17:53.66`.
- Nenhum SQL literal, payload, endpoint URL, evidência de execução ou captura de tela foi fornecido nesta análise.

## 5. Próximas validações necessárias

1. Revisar áudio e telas quadro a quadro em ambiente autorizado; corrigir erros do ASR sem adivinhar campos.
2. Obter a EF/Anexo I aprovados e fixar o contrato completo de listagem/download.
3. Definir matriz de parâmetros, casos de vínculo ausente/conflitante e resposta de erro.
4. Confirmar perfil GED e associação operação→proposta no back-office.
5. Definir sandbox, versões, dados sintéticos, evidências e rollback.
6. Confirmar opções `N`/`W` com a documentação responsável.
7. Fazer revisão de divulgação pública antes de marcar o material como concluído.
