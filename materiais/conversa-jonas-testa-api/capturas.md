> **Fonte textual** fornecida pelo responsável em **2026-10-15**; CPF e hospedeiros mascarados.

# Capturas — depuração no Test API (Jonas)

**Nenhuma captura foi produzida.** A fonte é **texto** e o recorte **não contém imagens**: o que existe
de evidência técnica é reproduzido literalmente em bloco de código em [`transcricao.md`](transcricao.md)
(o retorno da API em `[M13]` e os dois caminhos de endpoint em `[M04]`/`[M05]`).

## Revisão de privacidade e sanitização

- Não houve imagem a sanitizar; portanto nenhuma captura foi revisada ou omitida por privacidade.
- Mascaramentos aplicados **ao texto**: CPF de `[M01]` → `[DADO PESSOAL OMITIDO]`; hospedeiros de rede
  → `<servidor>` (estrutura do caminho preservada). Registro em [`incertezas.md`](incertezas.md) item 6.
- Varredura automática de privacidade executada (`tools/validar_materiais.py`): sem achados.

## O que uma captura útil precisaria mostrar

Se o autor do teste puder documentar visualmente depois (com sanitização), o que fecharia a lacuna
deste pacote seria:

- a **tela do Test API** com os campos preenchidos (e o mesmo payload no JSON), para materializar a
  diferença entre “campo da ferramenta” e “campo do corpo”;
- a **resposta completa** da API (o recorte mostra só `MENSAGEM`/`CODIGO`);
- os **dois caminhos** publicados, para registrar qual é o ambiente válido de teste.
