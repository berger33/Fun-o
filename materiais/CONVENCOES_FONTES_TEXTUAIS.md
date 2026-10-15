# Convenções para fontes textuais (conversas, chats e mensagens)

Criado em **2026-10-15** para acomodar um segundo tipo de fonte primária na biblioteca: além das
gravações de vídeo, o acervo passa a receber **conversas de trabalho** (chat/Teams/WhatsApp) fornecidas
pelo responsável. O [`PLANO_EXTRACAO_ARENA.md`](../PLANO_EXTRACAO_ARENA.md) foi escrito para vídeo;
estas convenções mantêm os mesmos critérios (cobertura, rastreabilidade, privacidade, revisão) sem
inventar o que a fonte não tem — **não existe timestamp em um chat**.

## 1. O que muda em relação a uma gravação

| Critério (vídeo) | Adaptação para conversa |
|---|---|
| Fonte primária | O recorte da conversa, como fornecido. Pode ser parcial: registrar isso em `metadados.md` e `incertezas.md`. |
| Rastreabilidade | **Âncora `[Mnn]`** = índice da mensagem na `transcricao.md` (`[M01]`, `[M02]`, …). Toda afirmação nos derivados cita a âncora. |
| Timestamp `HH:MM:SS` | **Não se aplica.** A data/hora é registrada como “não registrada no recorte” quando o chat não traz carimbo de tempo. **Nunca inventar horário.** |
| Duração, resolução, ASR | Não se aplicam; substituídos por “natureza da fonte” (texto digitado, áudio transcrito, print colado). |
| Capturas | Só existem se a conversa tiver trazido imagens. Prints **de terceiros** só entram após revisão; se não houver imagem, `capturas.md` declara a ausência. |

## 2. Estrutura obrigatória por conversa

Em `materiais/<slug>/`, os mesmos arquivos do roteiro: `transcricao.md`, `guia_de_estudo.md`,
`procedimentos.md`, `perguntas.md`, `glossario.md`, `incertezas.md`, `metadados.md` e `capturas.md`.
`metadados.md` deve declarar, no topo, a linha:

```
- **Tipo de fonte:** conversa (texto)
```

É essa linha que faz o `tools/validar_materiais.py` auditar o pacote por **âncoras `[Mnn]`** em vez de
exigir `HH:MM:SS`. Sem a declaração, o pacote continua sendo cobrado como gravação.

## 3. Transcrição

1. Reproduza **todas** as mensagens do recorte, na ordem recebida, cada uma com sua âncora `[Mnn]`.
2. Identifique o autor quando o recorte permitir (`autor:`). Quando a autoria não for determinável,
   escreva `autoria não determinada` em vez de atribuir a alguém.
3. Marque o que é **fala transcrita de áudio**, **texto digitado** ou **print colado** — os três têm
   confiabilidade diferente.
4. Não reordene nem “conserte” a conversa. Erros de digitação do interlocutor podem ser a evidência
   (ex.: quando alguém escreve `testa api` em vez de `Test API`).
5. Trechos sem valor de conhecimento (cumprimentos) permanecem para preservar contexto e ordem.

## 4. Privacidade

1. **Identificadores diretos são mascarados** no material publicado: CPF, CNPJ, RG/documento,
   telefone, e-mail, matrícula, endereço/CEP, dados bancários pessoais, nomes de familiares e
   terceiros não autorizados. Use `[DADO PESSOAL OMITIDO]` (ou um marcador equivalente explicado).
   Valores de **negócio** que não identificam pessoas (prazos, taxas, códigos de produto/convênio)
   permanecem — são o conteúdo de estudo.
2. **Mascarar campo ≠ perder conhecimento.** O que se preserva é a *estrutura* e o *significado*:
   em um JSON de teste, os nomes dos campos e a lógica são o material; os valores pessoais não.
3. **Conteúdo pessoal sensível** (saúde, condição clínica, medicação, relato íntimo): não vai para o
   repositório público. A versão íntegra fica em `restrito/` (fora do Git) e o que é publicado é a
   parte profissional/comunicacional, com o motivo registrado em
   [`CONFLITOS_E_VALIDACAO.md`](CONFLITOS_E_VALIDACAO.md) e [`PRIVACIDADE_E_RETENCAO.md`](PRIVACIDADE_E_RETENCAO.md).
4. Hospedeiros de rede interna (`\\\\servidor\pasta`, nomes curtos de máquina, URLs internas):
   mascarados por higiene de infraestrutura, como já se faz nas gravações, preservando a
   **estrutura do caminho**, que é o que ensina (ex.: `http://<servidor>/C6/Api/<Endpoint>/`).
5. Nomes de operadores da Função permanecem, conforme autorização registrada em
   [`CONFLITOS_E_VALIDACAO.md`](CONFLITOS_E_VALIDACAO.md).

## 5. Confiança e inferência

- O índice de uma conversa mede **ordem**, não tempo decorrido: mensagens podem estar separadas por
  dias. Não inferir prazos a partir da posição.
- Fala/escrita do interlocutor = **fonte**; conclusão do analista = **inferência**, sempre rotulada.
- Quando duas conversas permitem completar uma informação (ex.: o valor de um campo que uma delas
  não mostra), a ligação entra como **hipótese a validar**, com as duas âncoras citadas — nunca como
  fato.

## 5.1. Fonte não obtida (pacote legitimamente vazio)

Quando a fonte primária **não** foi obtida (bloqueio de download, LFS indisponível etc.), o pacote
existe para **registrar o bloqueio**, não para produzir conteúdo. Nesse caso, declarar em
`metadados.md`:

```
- **Fonte obtida:** não
```

Com essa declaração, o `tools/validar_materiais.py` registra a ausência de rastreabilidade como
**aviso** (e não como falha), porque não há timestamp a exigir de uma fonte que não foi analisada.
Os demais critérios continuam valendo — inclusive a proibição de afirmar conteúdo que a fonte não
sustenta. **Nunca** inventar um timestamp “de referência” só para satisfazer o auditor: o estado
correto é `em revisão`, com o bloqueio documentado.

## 6. Estado do material

Conversas seguem os mesmos estados de [`STATUS.md`](../STATUS.md) (`pendente`, `em análise`,
`em revisão`, `concluído`). Uma conversa só vai a `concluído` quando: todas as mensagens do recorte
estiverem transcritas com âncora, o conteúdo de conhecimento estiver extraído e ligado às âncoras, a
varredura de privacidade estiver limpa e as pendências humanas estiverem listadas em `incertezas.md`.
