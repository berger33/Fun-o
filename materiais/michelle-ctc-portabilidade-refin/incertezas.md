# Incertezas e pendências — MICHELLE CTC PORTABILIDADE REFIN.mp4

## 1. O diagrama não é do cliente-alvo

A apresentadora afirma que o desenho é de outro cliente, não exatamente do C6 (**00:00:05–00:00:23; 00:15:34–00:16:07**). Não usar nomes de etapas, ordem ou configuração do desenho como especificação do C6. É necessário obter o fluxo atual aprovado para o cliente-alvo.

## 2. Dependência entre portabilidade e refim

- No início, as esteiras são descritas como paralelas, mas precisam andar em conjunto (**00:00:24–00:00:36**).
- A explicação diz que a portabilidade deveria esperar o refim para conferir valores antes de gerar/avançar a CCB (**00:03:36–00:04:59**).
- Mais adiante, os participantes discutem permitir o avanço da portabilidade sem dependência rígida ou em etapas diferentes (**00:08:02–00:08:29; 00:10:34–00:12:14**).

**Pendência:** responsável de negócio deve definir a regra de sincronização, os status de bloqueio/liberação e o comportamento desejado quando houver mais de uma portabilidade para o mesmo refim.

## 3. Nome e função dos processos

- **“CTC aciona refim” / “CTC aciona esteira de financiamento” / “CTC aciona esteira externa”:** variantes reconhecidas em momentos diferentes; nome oficial e ponto de execução desconhecidos (**00:01:07–00:01:22; 00:06:47–00:07:02; 00:09:46–00:09:50; 00:11:49–00:11:57**).
- **“Aguarda análise de refim de portabilidade” × “aguarda alteração unificada”:** alternativas mencionadas sem configuração ou tela que confirme a escolha (**00:03:02–00:03:15; 00:07:25–00:07:47**).
- **“Guarda” × “aguarda”:** possível erro de ASR na descrição da etapa (**00:01:51–00:01:56; 00:08:24–00:08:29; 00:11:55–00:11:59**).
- **MEI:** aparece como sigla no trecho de CTC, sem definição (**00:15:17–00:15:28**).
- **CIP, remessa online e liberação:** são mencionadas sem explicar os contratos de integração nem os critérios de passagem (**00:04:01–00:04:59; 00:12:03–00:12:11**).

## 4. Cenário de teste e cadastros

- A criação de portabilidade com refim parece gerar duas propostas, mas a conversa alterna entre fluxo automático via popup e cadastros/esteiras separados (**00:06:22–00:06:53; 00:10:34–00:12:14; 00:12:50–00:13:18**).
- Não foram especificados convênios, produtos, dados de teste, critérios de aceite nem como restaurar a esteira.
- Os participantes sugerem pular etapas de CTC porque não estavam configuradas naquele momento (**00:06:39–00:06:49; 00:09:23–00:09:46**). Isso não valida nem autoriza contornar a integração em produção.
- A conversa não registra um teste concluído nem prova que a configuração proposta funcionou.

## 5. Cobertura e qualidade

- A transcrição tem 388 segmentos; o último vai de `00:16:48.56` a `00:16:50.26`, ante a duração de áudio declarada de `00:16:56.62`.
- A mídia e o desenho não foram inspecionados visualmente neste lote; a fala e os rótulos de processo precisam de conferência contra o áudio/tela.
- Termos possivelmente mal reconhecidos incluem “guarda/aguarda”, “exportabilidade”, “Porsche” (possível referência à portabilidade), “MEI” e nomes de etapas.
- Não há SQL, captura sanitizada ou evidência de execução nesta análise.

## 6. Próximas validações necessárias

1. Confirmar diagrama e regra atuais do cliente-alvo.
2. Confirmar nomes oficiais e semântica dos processos/status.
3. Definir se as propostas têm dependência obrigatória e como tratar múltiplas portabilidades.
4. Aprovar um cenário isolado em sandbox, sem contornar controles de produção.
5. Conferir a transcrição e a tela com a fonte antes de elevar a confiança ou marcar o material como concluído.
