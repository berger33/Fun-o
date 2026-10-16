# Perguntas e respostas — Gravando 2026-07-08 182343.mp4

1. **Qual é o assunto geral da gravação? (00:00:23–00:04:27; 00:05:26–00:08:03)**
   Uma passagem de orientação entre operadores sobre o pacote WebAutorizador/WS em ambiente de teste; no meio, a demonstração de exportação/importação de um **modelo de decisão** (esteira) ligada ao **teste de tolerância**.

2. **O que existe dentro da pasta `WebAutorizador`? (00:00:35–00:00:52)**
   `bin`, `Config`, `Estreia`, `Web References`, `Dados.dat`, `Global.asax`, `inst.dat`, `Web.Config`, `WSAutorizador.asmx`, `WSAutorizador.XmlSerializers.dll`, `WsRegChaveLicenca.asmx` — lidos da lista de arquivos (10 itens / 1,46 MB na seleção visível).

3. **O serviço Web tem a mesma estrutura? (00:02:36)**
   Sim: `...\WS\WSAutorizador` repete `bin`, `Config`, `Estreia`, `Web References`, `Dados.dat`, `Global.asax`, `inst.dat`, `Web.Config` e os `*.asmx`. A pasta `Config` aparece com data `09/09/2025 11:35`, anterior aos binários de `08/07/2026`.

4. **O que é dito sobre o par aplicação Web × serviço Web? (00:02:25–00:02:32)**
   “Aqui é o WebAutorizador... o WS também sempre vem junto. Atualizou um, tem que atualizar o outro.” É uma fala de rotina, não uma especificação oficial de pacote.

5. **O que a pasta de configuração contém, segundo a fala? (00:02:58–00:03:04)**
   Parâmetros de **SIC**, **GDOK** e **API**. Nenhum valor, arquivo ou credencial é mostrado.

6. **Qual cuidado a gravação recomenda com a configuração? (00:03:09–00:03:24)**
   Copiar a pasta `config` para a máquina como **backup**, com a justificativa de que uma falha de máquina poderia apagar tudo. O procedimento de backup/restauração não é demonstrado.

7. **As instruções de exclusão combinam entre si? (00:00:33; 00:02:34)**
   Não. Em `00:00:33` a orientação é apagar tudo menos a `config`; em `00:02:34`, no pacote do WS, é “apaga config”. As duas colidem com a recomendação de preservar/copiar a configuração — **nenhuma exclusão deve ser executada** com base nesta gravação.

8. **Qual é a regra de tolerância descrita no incidente? (00:03:00–00:03:22)**
   A EF define que `(%) Tolerância Mínimo` e `(%) Tolerância Máximo` são **opcionais**, aplicados sobre o valor mínimo/máximo solicitado, com **até 2 casas decimais** e aceitando **apenas valores entre 0 e 99**; o sistema estava aceitando **0 a 100**, e a evidência mostra `100,00` nos dois campos.

9. **Como o caso de tolerância foi encaminhado? (00:03:15; 00:07:40)**
   Registrado em documento (`Incidente01.pdf`) com a regra, o print da tela e a seção “De acordo com a EF”, e encaminhado à responsável de negócio (citada como “Michelle de negócios”), com a evidência já anexada.

10. **Qual caminho de menu leva ao modelo de decisão? (00:05:45–00:06:40)**
    `Serviços → Decisão`, com as opções `Tabela de Modelos`, `Tabela de Decisão`, `Relacionamento Modelo X Produto`, `Exportar Modelo Decisão`, `Importar Modelo Decisão` e `Visualizador de Fluxo Decisão`.

11. **Como foi feita a importação do modelo? (00:06:55–00:07:35)**
    Em `Importar Modelo Decisão`, com `Arquivo de Importação de Modelo de Decisão = Estaira112233.xml`, `Nº Modelo = 9999` e descrição `teste_tolerancia`; ao confirmar, o sistema perguntou “Confirma a importação da nova esteira ‘9999 - teste’?” e respondeu “As informações foram salvas”.

12. **A gravação confirma que a esteira importada funciona? (00:07:53–00:08:03)**
    Não. A conclusão é apenas a mensagem de sucesso da tela somada à percepção do interlocutor (“Parece que eu criei mesmo”). Não há reexportação, vinculação a proposta ou teste funcional.

13. **Qual foi a distinção feita entre atualizações de Autorizador, WS e API? (00:04:03–00:04:27)**
    A fala separa casos (“o autorizador é sempre esses dois... quando é caso do SIC... aí é só o autorizador”) e menciona que um componente “não atualiza” (reconhecido como “AWS”), mas a matriz não fecha e não é demonstrada.

14. **O erro visto durante a cópia foi comprovadamente inofensivo? (00:03:40–00:04:39)**
    Não. As mensagens em vermelho não são legíveis nos quadros amostrados, e a avaliação “é um erro genérico, não interfere em nada” é do interlocutor, sem diagnóstico nem verificação de efeito.

15. **O que é a opção “N” citada em 00:03:41?**
    Não é possível determinar — não há diálogo correspondente legível no quadro. Não se deve tratá-la como resposta padrão.

16. **Há SQL, API ou alteração de dados nesta gravação? (00:00:00–00:08:20)**
    Não. Nenhuma consulta, chamada de API ou alteração de dados é demonstrada; a importação de modelo é a única escrita verificável no sistema.

17. **Qual é o cuidado de privacidade aplicado a este material? (00:00:00–00:10:23)**
    As capturas foram recortadas no documento/tela: sem imagens de participantes, sem a faixa de identificação de usuário/servidor (desfocada na origem), sem o valor da OS e sem os campos de cliente/projeto preenchidos (estavam em branco). Ver [`capturas.md`](capturas.md).

18. **O que falta para transformar a rotina em procedimento aprovado? (00:02:34–00:04:39)**
    Resolver a contradição de exclusão; definir pacote/versão e ordem dos componentes; obter backup e rollback testados; estabelecer critério de sucesso da importação; e confirmar com o responsável técnico o significado de “AWS”, “N” e da matriz de alteração.
