> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste** (não há dado real de cliente ou de pessoa). Preservados
> conforme instrução: o nome **Função Sistemas** e os **nomes dos operadores**. Não são
> publicadas **imagens de pessoas** (câmeras/participantes) — as capturas ficam restritas às
> telas do documento.

# Capturas — Apresentação projeto 19-18.mp4

**Revisão de privacidade:** todas as imagens foram recortadas da tela compartilhada do
**documento** (Word), **removendo** a moldura da reunião (câmeras dos participantes, painel de
chat, nomes de canais internos e barra de tarefas do computador). Nenhuma imagem de pessoa foi
publicada. Os valores de exemplo do documento foram declarados **fictícios** pelo responsável
("Teste INSS", números de contrato 9048… e saldo 1.897,00), portanto foram preservados como
registrados na fonte. Nenhuma credencial, token, CPF/CNPJ ou dado real foi identificado nas
imagens finais.

| Arquivo | Timestamp | Contexto | O que comprova | Utilidade didática | Privacidade |
|---|---|---|---|---|---|
| `01-documento-objetivo-escopo.png` | 00:00:00 | Página 1 do documento de especificação (cabeçalho "Função Sistemas" fora do recorte) | Objetivo (1.1), Situação Atual (1.2) e Limites do Escopo (1.3): adequar a exibição de operações originais e saldo devedor na CCB do INSS em refinanciamento com múltiplos contratos; entrega no módulo **Web Autorizador** | Fixa o problema e o escopo antes de descrever as variáveis | Revisada: só o corpo do documento; sem pessoas, sem chat, sem barra de tarefas |
| `02-funcionamento-item-I.png` | 00:04:55 (mesma página de 00:05:03) | Seção "Funcionamento", item I | "criação de novas variáveis no módulo **SIC Minutas** do Autorizador" | Localiza **onde** a mudança é implementada | Revisada: idem |
| `03-figura1-exemplo-ccb.png` | 00:03:18 | Figura 1 do documento — "Cédula de Crédito bancário INSS refinanciamento - Página 1" | Bloco de exemplo com as três informações do pedido: **(i) Contrato/Operação Original** (vários números), **(ii) Credor Original** e **(iii) Saldo Devedor (estimado)** | Mostra na prática quais campos o modelo de CCB exibe hoje (base para o antes/depois das variáveis) | Revisada: recorte da figura; valores declarados fictícios pelo responsável |

## Como as capturas foram produzidas

- Extração de quadro com `ffmpeg` 7.0.2 no timestamp indicado, recorte em escala 3× (lanczos) e
  gravação em PNG comprimido — **sem** qualquer alteração do arquivo original.
- Comando aplicado (exemplo para o quadro 01):

```bash
ffmpeg -ss 00:00:00 -i "Apresentação projeto 19-18.mp4" -frames:v 1 \
  -vf "crop=530:225:150:340,scale=1060:-1:flags=lanczos" \
  -y capturas/01-documento-objetivo-escopo.png
```

- O recorte foi conferido imagem por imagem (só a área do documento); a conferência incluiu a
  região ampliada para garantir que nenhum elemento da reunião entrou na moldura.

## Capturas deliberadamente omitidas

- **Câmeras/participantes do Teams (00:00 / 00:06:18 / 00:07:48)** — imagens de pessoas;
  não publicadas por decisão de privacidade, mesmo com autorização de nomes.
- **Painel de chat da reunião (00:07:40)** — contém nomes completos, foto de perfil e mensagens
  internas; registrado em `transcricao.md` apenas como ocorrência, sem reproduzir conteúdo.
- **Barra de tarefas e título da janela** — identificam aplicação/nome do evento; recortados.

## Referência nos procedimentos

- `01` abrange o contexto do **Fluxo A** (objetivo/escopo) em [`procedimentos.md`](procedimentos.md).
- `02` sustenta o passo 1 do **Fluxo A** (onde criar as variáveis) e o **Fluxo B** (API/jornada).
- `03` é a evidência visual citada nos passos 2 a 4 do **Fluxo A** (contratos, credor, saldo).
