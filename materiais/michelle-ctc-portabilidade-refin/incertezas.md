# Incertezas e pendências — MICHELLE CTC PORTABILIDADE REFIN.mp4

## 1. O desenho não é do cliente-alvo (confirmado na fonte)

- A apresentadora declara em `00:00:05–00:00:23` que o fluxograma é desenho dela para **outro cliente** (“Não é exatamente do C6”) e repete a ressalva em `00:15:34–00:16:07` (“é só um exemplo de como funciona”).
- Consequência: nomes, mnemônicos (`CTCACIPROPREF`, `CTCAGANREFIN`, `AJREFPORT`, `AGAPREXT`, `ACNCALLBACK`), ordem das caixas e o parâmetro `G_AVERERR` descrevem **o exemplo**. Nada disso foi confirmado como configuração vigente do C6.
- **Pendência:** obter o fluxo/EF vigentes do cliente-alvo antes de reutilizar qualquer elemento.

## 2. Dependência × independência entre portabilidade e refim (não resolvido)

- Formulação com dependência: as esteiras “têm que andar em conjunto” (`00:00:24–00:00:36`) e a portabilidade “para… até que todas as propostas de refinanciamento estejam… com status de integrada” (`00:03:15–00:03:36`).
- Formulação sem dependência: o banco “não quer” a dependência e quer “continuar andando a esteira de portabilidade” após o acionamento (`00:07:50–00:08:29`).
- **Pendência:** decisão de negócio sobre a regra de sincronização, os status de bloqueio/liberação e o caso de **várias portabilidades para um mesmo refim** (a regra da “última proposta” é do desenho de exemplo, `00:02:00–00:02:30`).

## 3. Nomes de processos: tela × fala

- **Confirmados pela tela** (grafias literais do desenho): `CTC – Aciona Esteira de Refinanciamento (CTCACIPROPREF)`, `CTC – Aguarda Analise do Refin de Portabilidade (CTCAGANREFIN)`, `CTC – Atualizar Proposta com NU da Portabilidade`, `CTC - Verificação de Alteração de Saldo e Prazo`, `CTC - Validação de Refinanciamento de Portabilidade Após retorno da CIP (AJREFPORT)`, `Tem Refin Vinculado?`, `Analise de Crédito`, `Aguarda Aprovação Externa (AGAPREXT)`, `Acionamento de Callback (ACNCALLBACK)`.
- **Só falados** (sem caixa legível nos 218 quadros examinados): “aguarda alteração unificada” / “aguarda tela unificada”, “CTC aciona esteira externa”, “CTC permite acionar”, “remessa (online)”, “liberação” e o status “integrada”. No intervalo em que “unificada” é dito (`00:03:00–00:03:15`), o enquadramento está sobre `Tem Refin Vinculado?` → `CTC – Aciona…` (quadros dirigidos de `00:02:55–00:03:40`); portanto **não é possível afirmar** se existe uma caixa com esse nome em região nunca ampliada do desenho.
- **Leitura com cautela:** o parâmetro da nuvem foi lido como **`G_AVERERR`** em dois quadros independentes (`00:02:25` e `00:15:35`), mas a imagem é uma captura de compartilhamento (1186×710); confirmar a grafia exata no ambiente antes de citá-lo como parâmetro real.
- **Variações do ASR resolvidas pelo contexto/tela** (mantidas no texto bruto): “Porsche” (`00:10:00`) e “exportabilidade” (`00:10:49`) = portabilidade; “refino/refém” = refim/refin; “guarda” = aguarda; “font” = fonte (código-fonte); “MEI” (`00:15:17`/`00:15:34`) provavelmente “do meio” / “e-mail”; “a Siona” (`00:01:51`) inaudível como nome — provavelmente início de frase (“esse aqui que tem a configuração é o aguarda”).

## 4. Cenário de teste e cadastros

- O teste é **apenas combinado verbalmente** (`00:06:22–00:16:39`); nenhum cadastro, pop-up, número de proposta ou configuração de esteira é mostrado.
- Não foram definidos: convênios/produtos concretos, dados de teste, critério de aceite, evidências esperadas nem restauração da esteira.
- “Pular o CTC” decorre de ausência de configuração/acesso naquele ambiente (`00:09:23–00:09:50`); não valida nem autoriza contornar a integração fora de sandbox aprovado.
- O relato de que o cliente “não estava conseguindo” e a hipótese de “configurando errado” (`00:13:55–00:14:18`) são falas de segunda mão; a causa não é diagnosticada na gravação.

## 5. Conteúdo visual não legível ou não enquadrado

- Os **rótulos verticais das duas faixas** do fluxograma (visíveis no zoom afastado de `00:07:00–00:09:20`) não são legíveis nos quadros amostrados; a atribuição “faixa da portabilidade × faixa do refim” vem da sequência das caixas e da fala.
- Caixas à **direita de `CTCAGANREFIN`** ficam parcialmente cobertas pela coluna de participantes em `00:03:20–00:03:55`; foram registradas apenas quando legíveis em outros enquadramentos.
- O título completo do arquivo do desenho é legível só em parte (`…portabilidade-Refin - Port.drawio.png`); o início do nome não é registrado como dado.
- Nenhuma tela de sistema (Autorizador, cadastro, pop-up de refinanciamento) é aberta em toda a gravação — confirmações sobre telas reais **não** podem ser extraídas deste vídeo.

## 6. Cobertura de áudio e transcrição (conferido)

- Duração do contêiner: `00:16:56.62`. Último segmento de ASR: `00:16:48.56–00:16:50.26`; áudio em silêncio (limiar `-60 dB`) a partir de `00:16:50.28`, com ruído breve não verbal em ~`00:16:55.7`.
- Nível global baixo (média `-51,8 dB`, pico `-31,0 dB`); com `silencedetect` a `-60 dB` (41 regiões ≥ 1 s), **nenhum trecho audível > 4 s ficou sem segmento de ASR**; maior pausa entre segmentos: 3,0 s (`00:00:02.40–00:00:05.40`).
- Os quatro artefatos brutos da ponte desta retomada conferem: TXT/SRT/VTT **byte a byte idênticos** aos da execução anterior; o `transcricao_meta.json` difere só no tempo de processamento (`951.3` × `958.0` s).
- Permanece pendente a **escuta humana integral**: termos de baixa confiança do ASR estão listados no §3 e não foram “corrigidos” no texto bruto.

## 7. Privacidade — decisões tomadas neste lote

- **Não publicadas:** imagens/nomes completos dos participantes (câmeras/avatares e a barra de título da reunião com sobrenomes) — recortados de todas as capturas.
- **Recortadas para fora das capturas:** coluna de participantes, barra de ferramentas da reunião, barra de tarefas com data/hora da estação e título da janela do visualizador.
- **Não reproduzidos nos textos:** sobrenomes dos participantes, nomes de cliente (o desenho é de um cliente não nomeado), identificadores de proposta e qualquer valor. Nomes de operadores citados (Michelle, Gabriel, Matheus/Santana, William, Zé) são preservados conforme autorização de 2026-10-13.
- Nenhuma credencial, token, senha ou chave aparece na gravação analisada nem nas capturas publicadas.

## 8. Pendências para validação humana

1. Confirmar o fluxo vigente do C6 e a existência/semântica da etapa de espera “unificada” e do status que libera a portabilidade.
2. Decidir a regra de dependência (§2) e o tratamento de múltiplas portabilidades por refim.
3. Executar o teste combinado em sandbox aprovado e registrar evidências (na gravação, ele é apenas delegado).
4. Conferir, em fonte oficial, os mnemônicos e o parâmetro lidos do desenho de exemplo antes de qualquer referência operacional.
5. Escuta humana da transcrição nos trechos de baixa confiança do ASR (§§3 e 6).
