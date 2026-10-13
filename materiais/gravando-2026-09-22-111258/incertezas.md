# Incertezas — Gravando 2026-09-22 111258.mp4

Lacunas, contradições, dados omitidos e validações humanas necessárias. Nada aqui foi resolvido por suposição.

1. **`document_type`: código ou descrição? (DÚVIDA_OU_CONFLITO)**
   - Fala em `00:04:02`–`00:04:08`: "é o código ou a descrição?" → "Na minha análise... é o código" (outra voz) e "a descrição é o nome" (`00:04:12`).
   - Fala em `00:04:45`–`00:04:49`: "Pra mim tem que ser o código" → "o tipo de documento é o código".
   - Fala em `00:05:00`–`00:05:08`: "pedi pra ele deixar a descrição... é só ficar atento... na implementação pra colocar o código".
   - **Conflito:** a equipe do cliente pediu descrição; a conclusão falada é código. Não há tela que confirme. **Validação humana necessária** com o responsável pela análise da RFP001 antes de implementar.

2. **Campos já existentes na base? (DÚVIDA_OU_CONFLITO)**
   - Fala em `00:03:10`–`00:03:29`: "a gente já tem esses campos sim", "vale consultar", "vocês podem me chamar depois". A própria fala indica que a conferência não foi feita (`00:03:00`–`00:03:07`: "não sei se é o Zé ou o Gleison").
   - **Validação pendente:** confirmar, com a base, onde estão `document_type`, `document_name` e `user`.

3. **Configuração do código do perfil no web service e no SIC (INFRA_E_ACESSO)**
   - A fala cita risco de falha por falta de configuração (`00:05:22`–`00:05:44`). Nenhum valor de perfil foi mostrado. **Não registrar valores.** Validar a configuração pelo canal autorizado.

4. **"Mostrar as procurações lá do web service" (`00:07:01`)** — expressão ambígua na transcrição automática. Pode ser "permissões" ou outro termo; não foi confirmada na tela. Não interpretar como permissão concedida.

5. **Considerações da especificação (`00:04:10`, página 3)** — o texto completo da seção *Considerações* não foi lido em tamanho real; a miniatura mostra itens sobre funcionalidades sem alteração e referência a anexos. **Validação necessária:** ler a página 3 completa do PDF `DS586780 (3)`.

6. **Anexo I (métodos de integração de importação de proposta)** — título visível em miniatura, aprox. `00:04:00`–`00:05:00`. O conteúdo do anexo não foi lido em tamanho real e não foi demonstrado. Não inferir o conteúdo.

7. **Páginas além da 3 do PDF (41 páginas)** — a gravação mostra só as páginas 2 e 3 (e miniaturas posteriores). Demais páginas não foram analisadas.

8. **"Explodiu" / prazo / item em vermelho (`00:07:52`–`00:08:27`)** — trecho sem tela de planejamento; o sentido não é confirmado.

9. **Sigla "IP" (`00:07:30`)** — não definida na gravação.

10. **Tipo de documento para a importação (`00:05:55`–`00:06:12`)** — a dúvida "depois da versão entregue ou só da versão entregue?" não tem resposta na gravação. Decisão não tomada.

11. **Qualidade do áudio e da transcrição** — a fala tem sobreposição de vozes, cortes, risadas e conversa paralela (ex.: `00:00:22`–`00:01:20`, `00:08:36`–`00:08:41`). Vários trechos tiveram atribuição de falante não confirmada. Termos corrigidos contra a tela estão em [`transcricao.md`](transcricao.md) (*Notas de revisão*).

12. **Trechos da grade de participantes e da barra de tarefas** — a gravação tem muitos quadros sem conteúdo instrutivo (grade de participantes, microfone mudo, avisos do Teams). Esses quadros foram amostrados (1 a cada 10 s) e não contêm conteúdo técnico, mas não foram analisados quadro a quadro.

13. **Retenção dos bytes da gravação** — esta análise foi feita a partir de cópias da ponte temporária que continuam acessíveis pelo SHA dos commits (ver [`../PRIVACIDADE_E_RETENCAO.md`](../PRIVACIDADE_E_RETENCAO.md) e a nota em `STATUS.md`). Pedido de remoção ao GitHub Support pendente para o responsável.

14. **Identificação de falantes** — a atribuição de falas a pessoas segue o primeiro nome dito na transcrição, sem confirmação visual. Não há como confirmar quem fala em cada trecho apenas pela tela.
