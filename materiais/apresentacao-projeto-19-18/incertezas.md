> **Publicação autorizada pelo responsável em 2026-10-13.** Os dados da gravação foram
> declarados **fictícios/de teste** (não há dado real de cliente ou de pessoa). Preservados
> conforme instrução: o nome **Função Sistemas** e os **nomes dos operadores**. Não são
> publicadas **imagens de pessoas** (câmeras/participantes) — as capturas ficam restritas às
> telas do documento.

# Incertezas e pendências — Apresentação projeto 19-18.mp4


## 1. Autorização de divulgação — resolvida pelo responsável (2026-10-13)

- A gravação exibe: **nome de cliente/instituição** (`C6 Consig`, nos títulos da reunião e do documento),
  **número de ordem de serviço interna** (`OS 552267`), **nomes de participantes** e **nomes de
  canais/times internos**, além do **conteúdo de uma especificação funcional** (tela compartilhada
  do documento com regras de negócio e figura com números de contrato de exemplo) e de **estimativas
  internas de esforço**.
- Em **2026-10-13**, o responsável pela divulgação declarou que **todos os dados da gravação são
  fictícios/de teste** e autorizou a publicação dos materiais derivados no repositório, instruindo a
  preservar o nome **Função Sistemas** e os **nomes dos operadores** (como Michelle, Zé, Felipe,
  Gabriel, William, Jonas).
- **Cuidado mantido:** imagens de **câmeras/fotos de participantes**, painel lateral de chat com
  avatares e barra de tarefas pessoal foram **recortados/omitidos** das capturas publicadas em
  [`capturas/`](capturas/).

## 2. Tornar público é irreversível — inclusive em ramos apagados

- Durante a transferência, o vídeo original foi servido ao sandbox por um **ramo temporário**
  (`entrega/*`), já **apagado** do repositório.
- **Verificado:** o commit desse ramo **continua acessível pelo SHA-256**, inclusive de forma
  **anônima** (sem token), pela API e pelo fetch do GitHub — comportamento padrão de repositórios
  GitHub para commits de ramos removidos. Ou seja, apagar o ramo **não** removeu os bytes do servidor.
- **Recomendação:** solicitar ao GitHub Support, por escrito, a remoção dos objetos órfãos
  (referenciando o repositório, o SHA do commit e a data), se desejado. Ver [`../PRIVACIDADE_E_RETENCAO.md`](../PRIVACIDADE_E_RETENCAO.md).
- **Atenção:** os objetos de Git LFS usados pelo repositório (os vídeos) permanecem igualmente
  acessíveis por quem tiver acesso ao repositório — a *remoção* de LFS também é irreversível e deve
  ser avaliada com o responsável.

## 3. Valores de exemplo da Figura 1 (dados fictícios de teste)

- A figura do documento ([`capturas/03-figura1-exemplo-ccb.png`](capturas/03-figura1-exemplo-ccb.png))
  mostra uma tabela de exemplo com **(i) Contrato/Operação Original:** `9048421935;9048421936;9048421937;9048421938`,
  **(ii) Credor Original:** `Teste INSS` e **(iii) Saldo Devedor (estimado):** `1.897,00`. Conforme
  confirmação do responsável em 2026-10-13, tratam-se de valores fictícios de teste da especificação.

## 4. Conciliar módulo x escopo

- O documento diz que as implementações serão disponibilizadas para o módulo **Web Autorizador**
  (item 1.3), enquanto a fala cita **"SIC Minutas do Autorizador"** (item I) e a **"jornada de
  contratação"** (item 2). Pode ser o mesmo conjunto de módulos com nomenclatura sobreposta, ou dois
  pontos distintos de configuração. **Requer confirmação** antes de virar procedimento.

## 5. Estimativas de CQ e plano de teste ambíguas

- Foram falados "**21** do CQ" **[00:07:04]** e depois "**21, 3 e 16** para o plano de teste"
  **[00:07:32]**, sem explicar a que corresponde cada valor (por pessoa? por etapa? por item?).
  Registrado como falado; **não** interpretar.

## 6. Falante incerto e áudio ruim

- **[00:03:48 – 00:04:37]**: fala sobreposta — a atribuição de quem disse "vai só aparecer os dois,
  não vai discriminar a operação em si" é **incerta** (aparenta ser o participante B, mas não há
  confirmação visual inequívoca).
- **[00:04:37 – 00:05:47]**: ruído de televisão/microfone aberto, com repetição pedida; trechos
  inaudíveis. **Não** completar por suposição.
- Transcrição automática (faster-whisper large-v3) revisada, mas termos técnicos e números foram
  conferidos apenas onde havia contexto suficiente; "cooperação" no **[00:01:45]** foi lido como
  "operação" (erro típico do modelo).

## 7. Itens não demonstrados

- Nenhuma tela de produto (SIC Minutas/Web Autorizador) foi mostrada; **nenhum** perfil/permissão foi
  discutido; **nenhuma** consulta SQL foi executada ou escrita — a menção a "query/fonte"
  **[00:06:12]** foi apenas um encaminhamento de verificação futura. Por isso **não** há ficha SQL
  desta gravação.