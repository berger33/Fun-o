# Perguntas de estudo — Jonas EPT explicação.mp4

Perguntas para fixação e verificação de aprendizado, com respostas resumidas e referência de timestamp (`HH:MM:SS`). Dados de teste e caminhos internos mascarados.

1. **Como descobrir no banco se o plugin de envio de proposta ao sistema externo foi executado para uma proposta?**
   Consultar `FCSMONITOREMPR..ECONSULT` com junção a `TBPERFCON` (`CSIDPFCON = PRIDPFCON`) filtrando pela descrição do serviço (`PRDESCPFCON LIKE '%Servico de Envio da Proposta ao Sistema Externo%'`) e ordenando por `CSIDCONS DESC`. (`00:02:50`–`00:03:40`)

2. **Por que filtrar por `PRDESCPFCON` em vez de `CSNRPROP`?**
   Porque o filtro por nome do serviço localiza o evento sem depender do número da proposta; na demonstração o filtro por `CSNRPROP` aparece comentado no editor. (`00:03:00`)

3. **O que é a tabela `ECONSULTD` e como ela é usada?**
   É a tabela de **detalhe** da consulta (`ECONSULT`), em formato chave-valor: `CDIDCONS` (id da consulta), `CDCONTROLE` (sequencial), `CDCAMPO` (nome do campo) e coluna de conteúdo. Passa-se o `CSIDCONS` do evento (ex.: `84942`) para ver o detalhe — inclusive o **JSON do payload** enviado. (`00:03:11`–`00:03:42`, `00:05:40`)

4. **Qual valor deve ser usado no filtro `CDIDCONS` da `ECONSULTD`?**
   O `CSIDCONS` da linha correspondente em `ECONSULT` — na demonstração, `84942` da linha "Serviço de Envio de Proposta ao Sistema Externo". (`00:03:14`)

5. **Em qual objeto do payload JSON o novo agrupamento de documentos anexados deve entrar?**
   Dentro do objeto **`client`** ("acima de client / ele vai estar / em client"). (`00:04:33`–`00:05:23`)

6. **Quais campos a Especificação Funcional define para o agrupamento de documentos anexados (tela desta gravação)?**
   O bloco "Início do objeto `attached_document`" com `document_type` (Tipo do documento) e `document_name` (Nome do documento). *Atenção:* a gravação de 2026-09-22 registrou o nome do objeto como `attachment_document` — conflito em validação. (`00:04:20`)

7. **Que campos de corban (promotora) a EF mostra e de onde vêm os valores?**
   `phone` ("Telefone Corban", até 9 caracteres) e `phone_area_code` ("DDD Corban", até 3 caracteres), "de acordo com o cadastro da Origem 3 da proposta". (`00:05:00`)

8. **Como conferir que o payload copiado do banco corresponde à proposta testada?**
   Comparar os valores de contrato do JSON (`contract_amount`, `contract_parcel_amount`, `contract_net_amount`, `contract_parcel_quantity`) com os "Dados da Operação" da Proposta Sintetizada — no vídeo: 2.000,00 / 89,47 / 2.078,59 / 30. (`00:02:00`, `00:04:30`–`00:05:20`)

9. **Quais informações preencher no cabeçalho do caso de teste da EPT?**
   Número do projeto, item da EF e a etapa — sendo que a etapa "pode ser bem genérica". (`00:05:52`–`00:06:11`, `00:07:38`–`00:07:44`)

10. **Qual rotina do Autorizador deve ser usada nas etapas de anexo de documento da EPT?**
    A rotina "Anexar/Consultar Documentação" do módulo Web Autorizador. (`00:07:54`)

11. **Quais dois cenários de teste o Relatório de Testes traz para este item?**
    Importação de proposta com documentos anexados (fluxo `/proposal/import`) e atualização de proposta já existente (fluxo `/proposal/update`), ambos com ao menos um documento anexado no checklist. (`00:09:00`–`00:09:30`)

12. **Qual é o resultado esperado de sucesso da integração e como se caracteriza a falha?**
    Sucesso: `200 OK` com `success=true`, `type=ok`, `message=proposal imported` e `details` conforme o padrão do serviço, com o objeto `Client` contendo o agrupamento com campos do documento e do usuário corretos. Falha: agrupamento ausente no update, com nome incorreto, campos incompletos ou regressão nos demais blocos; erro de validação da request segue o tratamento padrão com `400 BadRequest` ou `409 Conflict`. (`00:09:20`)

13. **Quais estruturas do payload devem ser verificadas quanto à regressão?**
    `corbanData`, `Credor associatedProposals`, `last_ConsultINSS` e `Insurance_reuse`. (`00:09:20`)

14. **Quais consultas complementares estavam preparadas no banco `FCSPROPEMPR` e qual a ressalva sobre elas?**
    `SELECT * FROM CLOGREFIN`, `SELECT * FROM CLOGREFIND`, `SELECT * FROM EREAPSEG WHERE EPRNRPROP='…'` e `SELECT * FROM CCOMP WHERE CSNRPROP=…` — estavam no editor mas **não foram executadas nem explicadas** na gravação (finalidade não documentada). (`00:00:00`)

15. **Onde ficam a EF e o Relatório de Testes usados para montar a EPT?**
    Na "pasta doc" do compartilhamento de rede da equipe (`Mesa_C6`; servidor mascarado) — arquivos `D586780` (PDF) e `Relatorio_de_Testes_586780` (Word). (`00:08:27`–`00:08:30`)

16. **Que ajuste pendente Jonas apontou no final?**
    A parte do **número da proposta** no envio ao sistema externo ("a única coisa que a gente tem que ajustar é aquela parte do… número da proposta… mandar ela pro sistema externo") — detalhe do ajuste não explicado. (`00:09:31`–`00:09:39`)

17. **Por que esta chamada aconteceu, segundo o chat exibido?**
    O colega perguntou "consegue falar?" e Jonas preferiu mostrar ao vivo: "eu te mostro aqui melhor do que ficar mandando msg". (`00:09:00`–`00:09:20`)

18. **Quem são os destinatários naturais deste material no processo de CQ?**
    O analista que vai montar/executar a EPT do item (no caso, o interlocutor da chamada) — a gravação é uma demonstração de "como fazer" para ele. (`00:00:03`, `00:09:42`)
