# Perguntas e respostas — Gravando 2026-09-22 111258.mp4

As respostas seguem a gravação. Quando a fala e a tela divergem, a resposta registra as duas fontes. Ver [`incertezas.md`](incertezas.md).

1. Qual é o nome do agrupamento novo e onde ele fica? (`00:02:30` – `00:03:05`)
   O agrupamento se chama **`attachment_document`**. Ele é implementado no módulo **ServCon**, no serviço (plugin) **Envio da Proposta ao Sistema Externo**, dentro do objeto **`Client`** (RFP001 `001.1` e especificação, [`capturas/01-rfp001-necessidade-solucao.png`](capturas/01-rfp001-necessidade-solucao.png) e [`capturas/02-especificacao-funcionamento.png`](capturas/02-especificacao-funcionamento.png)).

2. Quais campos o agrupamento `attachment_document` terá? (`00:03:05`; falado em `00:02:43`–`00:02:58`)
   Três campos: **`document_type`** (identificação do tipo de documento), **`document_name`** (indicador do nome do documento anexado) e **`user`** (usuário responsável pela anexação).

3. O que deve ser enviado quando não houver documento anexado? (`00:03:50`)
   O agrupamento deve ser enviado como **`null`**, conforme o Funcionamento II da especificação. A fala confirma: "a gente tem que enviar nulo" (`00:03:48`).

4. Quando um campo não existe na base, o que fazer? (`00:03:43` – `00:03:48`)
   Enviar **nulo** para aquele campo. A fala diz que a implementação não deve criar a informação, apenas resgatá-la (`00:03:25`–`00:03:29`).

5. Por que o novo agrupamento é necessário? (`00:02:22` – `00:02:40`)
   Segundo a fala, o cliente precisa dessas informações na **jornada de formalização** dele, e o plugin é o meio que ele usa. *Justificativa falada; não confirmada por documento de negócio.*

6. O agrupamento segue qual padrão de nome? (`00:02:43` – `00:02:46`)
   Segue o **padrão em inglês** usado pelo **C6** (a janela da reunião é do projeto *C6 Consig*).

7. `document_type` deve ser o código ou a descrição do tipo de documento? (`00:04:02` – `00:05:08`)
   **Não resolvido.** A conclusão falada é **código** (`00:04:49`), mas há ressalva de que a descrição foi pedida ao cliente (`00:05:00`–`00:05:08`). Validar antes de implementar.

8. Onde o agrupamento obtém as informações do documento? (`00:05:13` – `00:05:20`)
   Segundo a fala, do **SIC**, que precisa ter o código do perfil. A tela não demonstra essa busca.

9. Quando a execução é por web service, o que mais precisa estar configurado? (`00:05:22` – `00:05:34`)
   O **código do perfil** precisa estar configurado também no web service. A fala diz que a rotina conhecida até então é só pela tela do Autorizador, o que pode levar à falta da configuração (`00:05:38`–`00:05:44`).

10. O documento de teste do cliente precisa mencionar algo? (`00:06:12` – `00:06:30`)
    Sim: detalhar um passo no documento de teste mostrando que o perfil está configurado, para que o cliente não abra erro (`00:06:23`–`00:06:30`).

11. Quem faz o teste e o que deve ser mostrado? (`00:06:52` – `00:07:01`)
    Jonas e William, em conjunto (`00:06:55`–`00:06:56`). A anotação falada é "mostrar as procurações lá do web service" (`00:07:01`), expressão incerta.

12. Em que momento o projeto é apresentado? (`00:06:02` – `00:06:35`)
    Geralmente na **review**, que é feita ao fechar o pacote de versão. A dúvida "depois da versão entregue ou só da versão entregue?" não foi resolvida na gravação (`00:05:55`–`00:06:12`).

13. O que precisa existir antes de iniciar o desenvolvimento de um item? (`00:07:30` – `00:07:39`)
    Segundo a fala, o item precisa estar aberto para que o início do desenvolvimento seja marcado; "sem o item eu não consigo iniciar".

14. O que significa a sigla IP no item do documento? (`00:07:30`)
    **Não definida na gravação.** Registrar como "IP" até confirmação (ver [`glossario.md`](glossario.md)).

15. Os nomes "Zé", "Léo" e "Gleison" são responsáveis pelo projeto? (`00:03:00` – `00:07:05`)
    A gravação só os cita como pessoas a consultar ou a chamar. Não confirma o papel de cada um.
