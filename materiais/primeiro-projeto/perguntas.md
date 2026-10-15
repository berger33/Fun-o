# Perguntas e respostas — Primeiro projeto.mp4

1. **Qual é a mudança central discutida? (00:00:33–00:01:02)**

   Acrescentar consulta/download de documentos GED pela operação, inclusive quando a requisição não leva número de proposta, preservando o caminho conhecido por proposta.

2. **Como é chamado o novo endpoint? (00:01:37–00:02:14)**

   A fala o chama de “Documentos anexados simplificado”; nome formal e rota devem ser confirmados na EF.

3. **Qual método HTTP é lido para a listagem? (00:02:06–00:02:14)**

   A transcrição registra `GET`. Não foi feita chamada real.

4. **Quais identificadores são citados como parâmetros? (00:02:25–00:03:18)**

   Número de proposta e número de operação. A leitura oral descreve obrigatoriedade condicional, mas o contrato formal deve ser conferido.

5. **Qual regra preliminar é proposta para esses parâmetros? (00:03:00–00:03:42)**

   Pelo menos um deles deve ser informado; a fala recomenda testar cada alternativa e considera incorreto obter sucesso sem nenhum. O que ocorre quando ambos são enviados precisa de confirmação.

6. **Que informação deve aparecer no retorno? (00:03:52–00:04:23)**

   Uma lista de arquivos com referências de armazenamento/ID e nome/extensão. As propriedades exatas devem ser obtidas na EF/Anexo I.

7. **O novo endpoint simplificado deve retornar dados do checklist? (00:04:41–00:05:09; 00:06:56–00:07:37)**

   Não, segundo a explicação: deve listar apenas arquivos anexados no GED associados à proposta ou operação, não informações de checklist.

8. **Como o endpoint existente é descrito? (00:00:52–00:01:02; 00:07:37–00:07:54)**

   Como uma API que hoje consulta/download por número da proposta e usa o perfil GED configurado no Autorizador. Confirmar isso na versão atual.

9. **Como o sistema resolveria uma chamada apenas por operação? (00:07:54–00:08:29)**

   A fala diz que o sistema buscaria internamente no back-office o número de proposta correspondente, porque o perfil GED usa a proposta como identificador principal. A regra e os dados necessários precisam de validação.

10. **É preciso enviar a proposta junto com a operação? (00:08:12–00:08:36)**

    A orientação oral diz que não, pois a busca interna faria a associação. Isso depende de o vínculo existir e da regra aprovada no back-office.

11. **O que é mencionado sobre download por operação? (00:08:42–00:09:16)**

    É citada a inclusão de parâmetro de número da operação para possibilitar download; não está claro se isso pertence a um endpoint separado ou ao mesmo fluxo.

12. **Quais sistemas são mencionados para preparar o teste? (00:09:18–00:10:22)**

    Autorizador, subsite, Gdoc e Web API. A fala afirma que a API seria a aplicação modificada, mas não demonstra versões ou implantação.

13. **A conversa determina quais versões usar? (00:10:29–00:10:42)**

    Sugere versões aprovadas/mais recentes; é uma fala contextual, não substitui a política de release ou a aprovação do ambiente.

14. **O vídeo fornece SQL para encontrar o número da operação? (00:02:35–00:02:57)**

    Não. A pessoa menciona que enviou uma consulta, mas não a lê nem a mostra; não reproduzir SQL por inferência.

15. **O que a fala recomenda registrar como evidência? (00:13:12–00:15:18)**

    Versão, caminho do cenário, associação do objeto de teste à requisição e retorno/métodos da API. Evidências devem ser autorizadas e sanitizadas.

16. **O que significam as opções “N” e “W” citadas? (00:13:12–00:16:02)**

    Não é explicado. A orientação varia conforme aplicação/ficha e não deve ser transformada em procedimento sem documentação vigente.

17. **Houve teste validado ou análise visual nesta etapa? (00:00:00–00:17:53)**

    Não. O pacote se baseia no ASR; MP4, EF, telas e chamadas não foram conferidos neste lote.
