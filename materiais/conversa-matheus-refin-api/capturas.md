> **Fonte textual** fornecida pelo responsável em **2026-10-15**; identificadores diretos mascarados.

# Capturas — refinanciamento pela API (Matheus)

**Nenhuma captura foi produzida**, por dois motivos objetivos:

1. A fonte é **texto**: a conversa traz um payload JSON (reproduzido em bloco de código em
   [`transcricao.md`](transcricao.md)) e **nenhuma imagem** anexada ao recorte.
2. A única imagem referenciada na conversa — `[M19]`, “tipo noa usa esses”, com o exemplo de contratos
   que não podem ser usados — **não foi fornecida**. Não há, portanto, como documentar o critério
   visual (“em vermelhinho”) com evidência de tela; o critério está registrado por **fala** em
   [`glossario.md`](glossario.md) e [`procedimentos.md`](procedimentos.md) Fluxo B.

## Revisão de privacidade e sanitização

- Não houve captura a sanitizar.
- Todo o material publicado passou por mascaramento de identificadores diretos
  (`[DADO PESSOAL OMITIDO]`) e por varredura automática de privacidade (`tools/validar_materiais.py`);
  a lista do que foi omitido está em [`incertezas.md`](incertezas.md) item 6.
- **Imagens deliberadamente não incluídas:** o print de contratos citado em `[M19]`. Se ele for
  disponibilizado, deve ser revisado e mascarado antes de qualquer publicação (dados de cliente,
  números de operação e nomes).

## O que uma captura útil precisaria mostrar

Para fechar a lacuna deste pacote, seria útil (em material futuro, já sanitizado):

- a **tela de simulação** com a lista de contratos e a sinalização dos não utilizáveis;
- a **resposta da API** para o cenário com operação quitada;
- o **retorno de sucesso** da inclusão de uma proposta de refin, para comparar com a simulação.
