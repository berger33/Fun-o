# Conflitos e validações pendentes

Atualizado em **2026-10-13**.

## Conflitos entre gravações

Nenhum conflito **de regras de negócio** entre gravações distintas foi identificado nos 2 vídeos concluídos até o momento (`Apresentação projeto 19-18.mp4` e `Gravando 2026-07-07 155307.mp4`). Há duplicidade de **arquivo** confirmada no manifesto:

### Duplicidades confirmadas por objeto LFS (2026-10-13)

| Arquivos | Objeto LFS (oid, prefixo) | Evidência | Ação adotada |
|---|---|---|---|
| `Gravando 2026-08-24 124650.mp4` = `Gravando 2026-08-24 161729.mp4` | `1b9b6afd8564…` | Mesmo `oid` nos dois ponteiros versionados (`tools/checar_manifesto.py`) | Analisar uma única vez e apontar a segunda entrada para o mesmo material; o plano proíbe fundir gravações **diferentes**, não cópias byte-idênticas. |
| `Jonas EPT explicação.mp4` = `jonas2309.mp4` | `f99bd7955fbc…` | Mesmo `oid` nos dois ponteiros versionados | Idem. |

Consequência para a contagem: 24 arquivos no manifesto correspondem a **22 conteúdos distintos**.

## Pendências técnicas e operacionais registradas por vídeo

1. **`Apresentação projeto 19-18.mp4`** (ver [`apresentacao-projeto-19-18/incertezas.md`](apresentacao-projeto-19-18/incertezas.md)):
   - **Parametrização/identificação do credor por operação (00:03:34 – 00:06:45):** ficou em aberto na reunião verificar no fonte/query (suspeita de convênio × informação da proposta).
   - **Conciliação de escopo de módulos (00:00:00 × 00:05:03):** item 1.3 cita **Web Autorizador**, item I cita **SIC Minutas do Autorizador** e a fala cita **API de formalização / jornada de contratação**.
   - **Distribuição de horas do plano de teste (00:07:32):** valores falados `"21, 3 e 16"` sem explicação da quebra.
2. **`Gravando 2026-07-07 155307.mp4`** (ver [`gravando-2026-07-07-155307/incertezas.md`](gravando-2026-07-07-155307/incertezas.md)):
   - **Procedimento técnico de "subir na base" e "mudar a pastinha" (00:01:18 – 00:01:24):** apenas mencionado verbalmente na ligação; deverá ser complementado quando demonstrado nos vídeos mais longos da fila.
   - **Sigla falada "IPT" × tag escrita `[EPT]` (00:00:01 – 00:00:51):** o ASR transcreveu "IPT", enquanto a tela mostra `[EPT]` no item `570023`.
3. **`Gravando 2026-10-07 152044.mp4`** (ver [`gravando-2026-10-07-152044/incertezas.md`](gravando-2026-10-07-152044/incertezas.md)):
   - **Erro de reconhecimento automático ("doutor Isabel" × "Autorizador", 00:01:31):** corrigido na transcrição limpa com base nas abas abertas do **Autorizador Web**.
   - **Continuação da consulta em `Política de Despesas e Tarifas` (00:03:41 – 00:04:10):** o vídeo encerra logo após o orientador indicar a consulta da política `98` em si.
4. **`Liberação padrão - Glauco.mp4`** (ver [`liberacao-padrao-glauco/incertezas.md`](liberacao-padrao-glauco/incertezas.md)):
   - **Divergência entre texto da planilha `Liberacao_Padrao_V30.xlsx` e instrução oral de Glauco (linha 86, 00:02:35 – 00:02:43):** a linha 86 da planilha diz apenas `"Criação de procedures: .NET - com a opção C, sem erros."`, mas Glauco alerta expressamente que esse texto está desatualizado e que é necessário também fazer/conferir se a opção **`W`** existe lá.

## Diretrizes já validadas pelo responsável

- **Dados de teste e nomes (resolvido em 2026-10-13):** o responsável confirmou que todos os dados exibidos nas gravações são fictícios/de teste e autorizou a publicação dos materiais derivados preservando o nome **Função Sistemas** e os **nomes dos operadores** (Jonas, William, Gabriel, Michelle, Felipe, Zé, Santana, etc.), mantendo a omissão de fotos/câmeras de pessoas.
- **Retenção de objetos no GitHub:** os ramos temporários de ponte são removidos imediatamente após a coleta; detalhes em [`PRIVACIDADE_E_RETENCAO.md`](PRIVACIDADE_E_RETENCAO.md).

## Pendências de `PROJETO 14-08.mp4` (2026-10-13)

- **Campo de origem do CNPJ (`ETRACPD.*`) desconhecido:** aguardar retorno do Zé e o complemento da EF (`00:01:27–00:03:00`).
- **Número do item 2:** fala oscila entre 556776/556576/55676; a tela confirma **OS 556576** — validar se existe OS 556776 distinta.
- **Gantt do pacote 4:** envio prometido para segunda-feira, com as horas do Gabriel (`00:08:47–00:09:21`) — conferir recebimento fora desta biblioteca.
