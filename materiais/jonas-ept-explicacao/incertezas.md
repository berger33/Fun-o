# Incertezas — Jonas EPT explicação.mp4

Trechos que **não** puderam ser confirmados na gravação (fala esparsa, áudio de chamada, tela lida por OCR com fonte pequena). Nada aqui foi completado por suposição; o que está nos outros documentos como fato foi verificado contra a tela. Formato: item, evidência disponível e o que seria necessário para resolver.

1. **`attached_document` × `attachment_document` (conflito entre gravações).** A página de layout da EF exibida nesta gravação (`00:04:20`) lê-se consistentemente como "**Início do objeto `attached_document`**" (3 leituras independentes do quadro: `attached_document`, `attached document`). A gravação `Gravando 2026-09-22 111258` registrou o nome do objeto como `attachment_document` (página 3 da EF). Pode ser divergência real dentro da própria especificação ou erro de leitura em uma das gravações. **Para resolver:** reabrir o PDF da EF nas duas páginas e conferir a grafia; enquanto isso, o acervo registra as duas formas (ver [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md)).

2. **Números de proposta exibidos (leitura instável).** O número da proposta de teste aparece na grade `ECONSULT` (`CSNRPROP`, captura `02`), no filtro comentado, nos filtros de `EREAPSEG`/`CCOMP` e na tela `Aprovação/Consulta`. As leituras de OCR variam entre `000003264`, `000033264`, `010033264`, `800033264` (grade) e valores do tipo `8??83216?` (literais do editor). A gravação anterior teve comportamento análogo (`000033373` no editor × `800033373` na grade) e os dígitos exatos **não foram confirmados quadro a quadro**. Os documentos usam `000033264` como leitura aproximada da grade e `8??83216?` para os literais ilegíveis. **Para resolver:** zoom/validação humana na grade e no editor, ou conferência em tela do próprio sistema. Não usar esses literais como referência numérica.

3. **`SELECT TOP 100?`** — o valor do `TOP` da consulta principal lê-se como "TOP 100" em alguns quadros e não fecha em outros ("tOP 1Ee", "tOP 18B"); o resto da linha é legível. **Para resolver:** zoom/validação humana.

4. **"ele tá lá em digital" (`00:05:19`).** Expressão da fala no contexto da posição do agrupamento no payload; provável referência ao tipo de formalização (`formalization_type "D"` = digital) do payload exibido, mas a frase é truncada e não confirmada. Sentido exato desconhecido.

5. **Nomes de coluna com leitura parcial.** `ECONSULTD`: colunas `CDCONTROLE` e `CDCAMPO` confirmadas por zoom; a coluna de id lê-se `CDIDCONS` (padrão de nomenclatura `CD…`, mas lida também como `COIDCONS`/`CUIDCONS`); a coluna de conteúdo lê-se parcialmente (`C?CONTEUDO`) e a última coluna da grade (`ECONSULTD_?ROW…ID`) ficou ilegível. `ECONSULT`: colunas confirmadas na captura `02`. **Para resolver:** zoom/validação humana na grade.

6. **Finalidade de `CLOGREFIN`, `CLOGREFIND`, `EREAPSEG` e `CCOMP`.** Consultas preparadas no editor apontando o banco `FCSPROPEMPR`, mas **nenhuma execução ou explicação na gravação** (a fala não comenta essas linhas). Hipóteses pelos nomes (log de refinanciamento; reaproveitamento de seguro) **não foram confirmadas** e não devem ser tratadas como fato.

7. **Fala travada em trechos-chave.** "aqui ele já assinou o plugin" (`00:02:52`, provavelmente "chamou"), "tem esse CSI de cons" (`00:03:07`, contexto aponta para o registro de consulta em `ECONSULT`), "eu acho que aqui ele perdeu" (`00:05:17`), "pega aqui esse bloco anexei lá na" (`00:08:17`), "caras que tem a gera aqui" (`00:09:16`). Correções aplicadas apenas quando confirmáveis pela tela; os demais trechos ficaram como transcritos (ver *Notas de revisão* em [`transcricao.md`](transcricao.md)).

8. **"aqui ó que aí a gerou para mas de resto certo eu posso no autorizador no anexar documento já" (`00:07:54`).** Trecho travado; apenas a referência à rotina "anexar documento" do Autorizador é clara pelo contexto. O resto da frase não pôde ser reconstruído.

9. **"é de 880, ou é muito bom ou não é muito bom" (`00:09:16`).** Expressão incerta — "880" pode ser número de linhas, de item, ou erro do ASR. Sem correlato claro na tela. Mantida como transcrita.

10. **Ajuste do "número da proposta" (`00:09:31 – 00:09:39`).** Jonas diz que "a única coisa que a gente tem que ajustar é aquela parte do… número da proposta… mandar ela pro sistema externo", sem detalhar se o ajuste é na EPT, no Relatório de Testes ou no payload (ex.: campo ausente no JSON exibido). **Para resolver:** validar com a equipe ou em gravação futura.

11. **Outro item visível na planilha EPT ("C6 Consig - 59??8? - [ÁGIL] (I) …abilidade de Consulta de Saldo…").** Número e título com dígitos ilegíveis; aparece na área de premissas/premissas da planilha sem explicação na fala. Não relacionado ao item 586780 demonstrado.

12. **Segunda aba do navegador ("F586780.PDF").** Aba aberta ao lado de `D586780.PDF` (`00:00:40`), conteúdo nunca exibido — provavelmente outro PDF da OS 586780 (ex.: formulário/EF), não confirmado.

13. **"cadastro manual" (`00:00:11`) e "Boa, vou tirar com ela" (`00:01:18`).** Falas iniciais isoladas (sem tela correspondente legível no momento); "ela" é uma colega não identificada. Contexto exato desconhecido.

14. **Autora do Relatório de Testes.** O documento traz anotação "ler doc gerado pela [colega] e verificar se tem algum cenário válido para o nosso teste" e a fala diz "se ela colocou de uma forma diferente" (`00:09:29`); o nome não aparece legível. Preservado apenas o gênero da referência.

15. **Gravação começa no meio da reunião.** O cronômetro do Teams marca `04:13` em `00:00:00` — a demonstração começou ~4 min antes do início do arquivo; nenhum conteúdo anterior está disponível para análise.
