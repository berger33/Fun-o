> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste**. Preservados conforme instrução: o nome **Função Sistemas** e
> os **nomes dos operadores** (Gabriel, William, Santana). Não são publicadas **imagens de pessoas**
> (avatares/fotos de perfil) nem identificadores de máquina na captura derivada.

# Capturas — Gravando 2026-07-07 155307.mp4

**Revisão de privacidade:** a imagem publicada foi recortada exclusivamente sobre as duas mensagens
de itens de trabalho no painel central da conversa (`crop=675:84:472:528`), **removendo** avatares e
fotos de pessoas, a barra lateral de conversas do Teams, a barra superior com caminhos de rede UNC
(`\\<host-interno>\...`) e a barra de tarefas do Windows. Nenhuma credencial, senha, token ou CPF/CNPJ
consta na imagem.

| Arquivo | Timestamp | Contexto | O que comprova | Utilidade didática | Privacidade |
|---|---|---|---|---|---|
| `01-itens-de-trabalho-c6.png` | 00:01:38 | Área central do chat do Teams após o envio do segundo item (em 00:00:07) | Identificação dos dois itens vinculados: `C6 Consig - 558139 - [ÁGIL] (I) Implementação de Parâmetro para Margem de tolerância` e `C6 Consig - 570023 - [EPT] [[ÁGIL] (I) Implementação de Parâmetro para Margem de tolerância` | Conecta a orientação falada ("pegar a EPT que tá lá e iniciar") aos códigos exatos do item ágil (`558139`) e da respectiva `[EPT]` (`570023`) | Sanitizada por recorte: apenas os dois blocos de texto dos itens; sem fotos/avatares e sem caminhos de servidor |

## Como a captura foi produzida

```bash
ffmpeg -ss 00:01:38 -i "Gravando 2026-07-07 155307.mp4" -frames:v 1 \
  -vf "crop=675:84:472:528,scale=1350:-1:flags=lanczos" \
  -y capturas/01-itens-de-trabalho-c6.png
```

## Capturas deliberadamente omitidas

- **Lista lateral do Teams e avatares dos operadores (00:00:00 – 00:01:39)** — contém fotos de
  perfil de pessoas; omitida conforme política de privacidade.
- **Faixa de mensagem fixada no topo do chat (00:00:00 – 00:01:39)** — contém nome de host de rede
  interno (`\\<host-interno>\...`); documentada de forma mascarada no texto e em `incertezas.md`.

## Referência nos procedimentos

- `01-itens-de-trabalho-c6.png` comprova as pré-condições e o passo 1 do **Fluxo A** em
  [`procedimentos.md`](procedimentos.md).
