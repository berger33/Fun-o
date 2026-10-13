> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste** (não há dado real de cliente ou de pessoa). Preservados
> conforme instrução: o nome **Função Sistemas** e os **nomes dos operadores**. Não são
> publicadas **imagens de pessoas** (câmeras/participantes) — as capturas ficam restritas às
> telas do documento.

# Procedimentos — Apresentação projeto 19-18.mp4


Os "procedimentos" abaixo são **os fluxos descritos/demonstrados na reunião** (não houve execução
de sistema). Cada passo traz o timestamp de origem. Nada foi executado durante a análise.

## Fluxo A — Geração da CCB de refinanciamento com as novas variáveis (fluxo-alvo da mudança)

- **Pré-condições (ditas/indicadas):** existir **refinanciamento com múltiplos contratos** vinculados
  à mesma operação (refim) **[00:00:25, 00:01:00]**; documento de CCB gerado pelos módulos
  **SIC Minutas**/**Web Autorizador** **[00:05:03]**.
- **Sequência descrita:**
  1. Sistema monta o agrupamento "contratos/operação" do documento **[00:00:40]**.
  2. **Variável 1** — números dos contratos de origem passam a ser exibidos **na mesma linha**,
     sequenciais, **lado a lado, separados por ponto e vírgula** **[00:00:49 – 00:00:56; 00:05:03,
     item II]**.
  3. **Variável 2** — credor: se **o mesmo** em todas as operações de origem, exibir **uma única
     vez**; se **diferentes**, exibir todos, também **separados por ponto e vírgula**
     **[00:01:00 – 00:01:37; 00:02:54 – 00:03:12; 00:05:03, item III]**.
  4. **Variável 3** — saldo devedor: exibir a **somatória** dos saldos devedores de todos os
     contratos relacionados ao refinanciamento (hoje, cada operação mostra o seu)
     **[00:01:37 – 00:01:55]**.
  5. Emitir/gerar o documento com as variáveis atualizadas **[00:01:55 – 00:02:09]**.
- **Resultado esperado:** CCB de refinanciamento com contratos e credores em linha única separados por
  `;` e saldo devedor somado **[00:00:49, 00:01:49]**.
- **Exceções/condições:** credores **distintos** → todos aparecem (não deduplica) **[00:01:25]**;
  credor **igual** → nunca repetir **[00:01:32]**.
- **Conferência demonstrada:** comparação visual com a **Figura 1** do documento (exemplo de CCB de
  refinanciamento, página 1) e com a página de reprot **[00:03:18, 00:05:03, 00:06:18]**.

## Fluxo B — Uso pela jornada de contratação (item 2 do escopo)

- **Pré-condições:** API de formalização atualizada com as novas variáveis **[00:02:09]**.
- **Sequência:** durante a **jornada de contratação**, o usuário gera a CCB, que sai com as variáveis
  atualizadas **[00:02:13 – 00:02:25]**.
- **Resultado esperado:** CCB emitida pela jornada reflete contratos/credor/saldo devedor no formato
  novo **[00:02:21]**.
- **Observação de escopo:** o documento restringe a entrega ao módulo **Web Autorizador**
  **[00:00, item 1.3]** — conciliar com a menção a "SIC Minutas do Autorizador" e "jornada de
  contratação" (ver `incertezas.md`, item 4).

## Fluxo C — Tratamento da dúvida técnica aberta (processo de trabalho, como ocorreu na reunião)

1. Dúvida levantada: **como distinguir/parametrizar o credor** por operação **[00:03:34 – 00:03:56]**.
2. Resposta preliminar: a variável **não discrimina a operação**; apenas concatena credores
   **[00:04:00 – 00:04:37]**.
3. Dificuldade de áudio → dúvida enviada **pelo chat** da reunião **[00:04:37 – 00:05:47]**.
4. Encaminhamento: **verificar no fonte/query** se existe parametrização de credor (suspeita de que
   esteja no convênio) **[00:06:12 – 00:06:22]**.
5. Hipótese registrada: "**não é uma parametrização**" — informação viria da proposta
   **[00:06:34 – 00:06:38]**.
6. **Ação combinada:** enviar a resposta depois e **alinhar com desenvolvimento** **[00:06:39 –
   00:06:48]**.
- **Resultado:** **pendente** ao final do vídeo. **Não** tratar como resolvido.

## Fluxo D — Estimativa e fechamento de esforço (processo de planejamento)

1. Confirmar que as horas permanecem as que já haviam sido passadas **[00:06:54]**.
2. Item 1 (variáveis): **28 h** de desenvolvimento **[00:07:02, 00:07:21]**.
3. Item 2 (API de formalização): **6 h** **[00:07:13, 00:07:24]**.
4. CQ: citado "21" no início da confirmação e "ok para o CQ também" pelo participante E
   **[00:07:04, 00:07:29]**.
5. Plano de teste: "**21, 3 e 16**" **[00:07:32]** — sem detalhamento (registrado como ambiguidade).
6. Encerramento **[00:07:42]**.

## O que **não** foi demonstrado (não inferir)

- Nenhuma execução de sistema, nenhum SQL executado, nenhuma tela de produto além do **documento de
  especificação** e do **chat da reunião**.
- Nenhuma tela de configuração de variáveis, de geração de CCB ou do módulo SIC Minutas.
- Não foi mostrado o **código-fonte** ou a **query** mencionada em 00:06:12–00:06:22 (alguém apenas
  disse que seria possível verificar).
- Perfis/permissões de usuário **não** foram discutidos.