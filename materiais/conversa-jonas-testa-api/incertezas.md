# Incertezas e pendências — depuração no Test API (Jonas)

## 1. A ordem das mensagens não reconstrói as tentativas

- O recorte chega fora de um fio linear: em `[M06]` o operador já relata uma crítica, e a pergunta de
  `[M07]` (“vc preencheu os campos no test API?”) vem **depois**.
- Nenhuma requisição enviada é reproduzida: **não se sabe qual campo foi preenchido/removido em cada
  tentativa**, nem qual retorno corresponde a qual tentativa.
- **Consequência:** o material descreve o **método** (reduzir → observar → reintroduzir), e **não** uma
  sequência exata de comandos. Não usar como passo a passo cronológico.

## 2. Enum `SubTipoRefin`: catálogo desconhecido (âncoras `[M13]`, `[M14]`)

- A fonte prova que `null` **não** é aceito, mas **não** informa quais valores são válidos.
- O valor `"NaoDefinido"` vem da **outra conversa** do acervo (um envio que passou), não desta. A
  ligação está registrada como **hipótese** em [`guia_de_estudo.md`](guia_de_estudo.md) §3.
- **Validação humana necessária:** confirmar o enum com o responsável pela API antes de padronizar.

## 3. Código de erro `100000002` sem catálogo

- Não há lista de códigos, nem indicação de que esse código seja específico de erro de modelo. O
  índice de erro não deve ser usado como referência até existir catálogo.

## 4. Qual publicação do endpoint é a vigente?

- Aparecem dois caminhos (`Mesa C6/Regressivo 540791/…` e `C6/Api/…`). A fonte **não** diz qual é o
  oficial, se um substitui o outro ou se convivem. **Hospedeiros mascarados**; a estrutura do caminho
  foi mantida.
- **Validar** com o time de ambiente antes de fixar qualquer caminho em documentação de teste.

## 5. Desfecho do caso não registrado

- O recorte termina em `[M24]` (“eu to tentando fazer aqui tbm”), sem resposta final, sem registro de
  incidente e sem confirmação de correção. **Nada neste pacote afirma que o problema foi resolvido.**

## 6. Mascaramento aplicado nesta publicação (registro do que foi omitido)

- **CPF** da proposta citado em `[M01]` → `[DADO PESSOAL OMITIDO]`.
- **Hospedeiros de rede interna** das duas URLs → `<servidor>`, preservando o restante do caminho
  (área, pasta de regressivo, aplicação e serviço), que é o conteúdo de estudo.
- Nenhum segredo, token, senha ou credencial aparece na fonte; a varredura automática
  (`tools/validar_materiais.py`) não encontrou achados nos derivados.

## 7. Pareamento proposta × payload (`[M01]`, `[M02]`)

- A frase “A proposta nova que criei foi com esse cpf” sugere que a proposta foi criada com **outro**
  CPF em relação ao que se estava usando. A fonte **não** explica se isso gerou erro, se o payload
  precisava apontar para aquela proposta, nem como o vínculo é feito. O Fluxo D de
  [`procedimentos.md`](procedimentos.md) é **conferência preventiva**, marcada como inferência.

## 8. “O que dá a entender que seria o próximo passo” (`[M19]`)

- A frase é ambígua: pode significar (a) que o campo pedido pela API é o **próximo campo obrigatório**
  a preencher, ou (b) que a API estaria **evoluindo** e o modelo mudou. As duas leituras cabem; nenhuma
  é confirmada na conversa.

## 9. Autoria de mensagens curtas

- `[M02]`, `[M10]` e `[M12]` (“eesquece”, “certo”, “Ah, ok”) não têm autoria determinável no recorte.
  Foram mantidas em ordem, sem atribuição.

## 10. Versão da API não informada

- Não há identificação de versão, commit ou build da publicação testada — o que impede afirmar que o
  comportamento observado vale para a versão atual.

## 11. Relação com a conversa do Matheus

- As duas conversas tratam do **mesmo fluxo** (refin pela API) e citam as **mesmas pessoas** (William,
  Matheus, Santana), mas **não** há elemento que prove que aconteceram no mesmo dia ou na mesma
  sequência. O cruzamento é temático, não factual.
