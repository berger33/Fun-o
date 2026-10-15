# Incertezas e validações pendentes — MCB - QISTA.mp4

## 1. Termos, nomenclatura e regras de negócio

- **Certificação / pontuação / limite 20 / suspensões:** são descritos verbalmente (**00:00:00–00:01:13**), sem tela ou referência à regra oficial. Confirmar escala, critérios, estados, prazo de suspensão e efeito na proposta.
- **Núclea:** revisar nome e relação exata com certificação dos agentes no processo-alvo (**00:00:00–00:00:16**).
- **“Promotora interna” e “promotora externa”:** a conversa sugere efeitos diferentes sobre validar o agente (**00:07:27–00:09:01**). Negócio deve informar a regra e os resultados esperados; não transformar a fala em requisito de produção.
- **MCB / QISTA:** a expansão das siglas e a relação entre módulo, produto e sistema não são explicadas.
- **“T-Lib” × “Telib” / tabela de liberações:** nomenclatura reconhecida pelo ASR, sem tela, nome de tabela verificável ou diagnóstico reproduzido (**00:03:54–00:04:20; 00:06:03–00:06:21**).
- **“TEORGS”, “teorg 1/2/3/4”, “Origem 3”:** reconhecimento e nomenclatura não foram conferidos; a pessoa diz que o cadastro pode variar por ambiente (**00:05:37–00:06:46; 00:07:42–00:07:59**).
- **“na F”** em referência a onde estaria uma validação (**00:08:18**): trecho não explica o sistema/documento referido.

## 2. Configuração e integração MCB

- Nome/ID da atividade que aciona a validação, configuração que associa esteira e atividade e ponto de execução da API não aparecem (**00:01:13–00:01:24; 00:02:22–00:02:52**).
- A conversa menciona API de consulta de pontuação e app settings, mas não fornece URL, versão, contrato, autenticação, origem do pacote ou procedimento de publicação (**00:02:12–00:02:19; 00:10:02–00:10:42**).
- Os códigos candidatos **`190`** e **`061`** precisam de conferência na fonte/documentação vigente antes de qualquer referência (**00:10:02–00:10:18**).
- Não foi definida a resposta para agente não certificado, pontuação baixa, agente suspenso, API indisponível, cadastro ausente ou erro de mapeamento.
- Recomendações circunstanciais sobre versão “em última”, ambiente local, UDL e publicação um a um não identificam o ambiente alvo nem constituem procedimento de release (**00:09:09–00:12:08; 00:13:49–00:14:37**).

## 3. Cadastro e erro “produto não encontrado”

- A causa de ausência de formas de liberação é atribuída pela pessoa a um erro em sua base local; isso não confirma causa geral ou equivalente no ambiente do destinatário (**00:03:54–00:04:20; 00:06:03–00:06:21**).
- Confirmar a navegação e o cadastro oficial de promotora/origem no WebTabelas para cada versão (**00:04:22–00:05:59; 00:06:25–00:07:59**).
- “Produto não encontrado” é relacionado a origens e a três tabelas correlacionadas, que não são nomeadas (**00:14:29–00:15:24**). Não inferir tabelas nem realizar correções no banco.
- A menção a `INSERT`/`UPDATE` é condicional e genérica (**00:02:54–00:03:09**). Não há comandos, alvo, autorização, backup, validação ou rollback.

## 4. Cobertura da fonte e confiança

- A pasta inclui transcrição automática de 199 segmentos; último segmento em `00:15:41.94–00:15:45.12`, diante da duração de áudio declarada de `00:15:46.97`.
- O campo `duracao_transcricao_s: 556.8` de `transcricao_meta.json` não está documentado; pode representar soma dos trechos reconhecidos, não timestamp final. Não interpretar como duração do vídeo.
- A mídia não foi baixada nem re-hashada nesta etapa, e não houve escuta humana integral ou inspeção visual. O ponteiro local/manifesto/metadados coincidem; a execução anterior registra a conferência de bytes.
- A transcrição automática contém jargões e nomes candidatos; até conferência humana, todos os fatos deste pacote são provisórios. Sem captura, SQL executado ou teste validado.

## 5. Próximas validações necessárias

1. Conferir o áudio/tela com o MP4 em ambiente autorizado e corrigir a transcrição com timestamps.
2. Conferir certificação, pontuação, limites, estados e regra interna/externa em especificação vigente.
3. Confirmar componentes, versão, esteira/atividade, contrato da API e erros esperados com engenharia.
4. Confirmar cadastro de promotora/origens por versão e diagnosticar “produto não encontrado” com responsável técnico.
5. Definir teste isolado, dados sintéticos, evidências, critérios de parada e rollback antes de qualquer configuração.
6. Revisar divulgação de detalhes de sistemas internos antes de marcar como concluído/publicável.
