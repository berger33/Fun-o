#!/usr/bin/env python3
"""Camada de conhecimento explicado do material de estudo.

Aqui fica a **síntese autoral** de cada tema: a explicação do conhecimento, escrita para ser lida
e entendida — sem transcrição de trechos, sem marca de tempo e sem apontar em que momento da fonte
algo foi dito. Cada tema é um bloco HTML (classes `.sintese`, `.destaque`, `.aviso`) que o gerador
insere no início do capítulo correspondente.
"""

SINTESES: dict[str, str] = {}

# ----------------------------------------------------------------------------- domínio

SINTESES["negocio"] = """
<h3>O domínio em que esse trabalho acontece</h3>
<p>Todo o sistema gira em torno de <b>consignado</b>: crédito com parcela descontada direto da folha.
Isso explica quase tudo o que aparece nas telas — existe um <b>empregador</b> ou órgão que paga, um
<b>convênio</b> que define o que pode ser emprestado e a que custo, uma <b>margem</b> disponível para
descontar e uma <b>operação</b> (o contrato) que precisa ser <b>averbada</b> — registrada junto ao
pagador — antes de valer.</p>

<h4>Convênio, produto e condição de crédito</h4>
<p>O <b>convênio</b> é o cadastro que autoriza o trabalho com um pagador, e o <b>produto</b> é a
modalidade de crédito oferecida dentro dele. Juntos, eles determinam os números que a proposta
precisa respeitar: <b>valor mínimo e máximo</b> que se pode solicitar, <b>tolerância</b> aceita em
relação a esses limites, prazo em parcelas, taxas e <b>política de despesas e tarifas</b>. A
política de despesas é um catálogo próprio, ligado ao convênio, que define o que pode ser cobrado do
cliente na operação — o <b>IOF</b>, as tarifas e as despesas de <b>seguro</b>. Na prática, quando
alguém questiona o motivo de a proposta ter ficado com aquele valor, a resposta costuma estar nessa
combinação: convênio, produto, condição de crédito e política de despesas.</p>

<h4>Montagem da proposta: onde os valores se encontram</h4>
<p>A <b>proposta sintetizada</b> é a tela onde a operação toma forma: cliente, empregador, margem
disponível, condição escolhida e a lista de despesas. É nela que aparecem o valor financiado, o valor
de parcela, o IOF e as despesas de seguro, e é dela que saem os números que depois serão conferidos
no payload enviado à API ou à instituição. Entender essa tela é o pré-requisito para testar qualquer
integração: quem não sabe de onde o valor veio não consegue dizer se o valor final está certo.</p>

<h4>Averbação, desaverbação e os estados da operação</h4>
<p>Depois de formalizada, a operação passa a viver em uma máquina de estados. Ela pode estar
<b>averbada</b> (registrada e válida), <b>cancelada</b>, <b>reprovada</b> ou <b>liquidada</b> (quitada).
Esses estados não são burocracia: eles decidem o que pode ser feito a seguir. Uma operação liquidada
não serve como origem de um refinanciamento; uma proposta só admite exclusão de averbação em
determinadas condições; o <b>cancelamento</b> pede motivo, histórico financeiro (parcelas em aberto)
e a despesa de seguro vinculada. A trilha completa — pedir cancelamento, obter desaverbação e
excluir a averbação — envolve componentes diferentes, e misturar as etapas é o erro mais comum.</p>

<h4>Refinanciamento: substituir contratos por um novo</h4>
<p>No <b>refinanciamento</b>, um contrato novo absorve um ou mais contratos antigos — as <b>operações
originais</b>. Isso muda o documento (a cédula passa a mostrar vários contratos, credores e a soma
dos saldos) e muda a regra de elegibilidade: só entram operações que o negócio aceita absorver. Há
casos em que o novo contrato <b>reaproveita o seguro</b> já pago na operação anterior, aplicando a
parte proporcional ao novo prêmio — é o <b>reaproveitamento</b>, que envolve uma simulação própria e
um identificador que precisa viajar até o envio.</p>

<h4>Portabilidade: dois fluxos que precisam andar juntos</h4>
<p>Na <b>portabilidade</b>, o cliente transfere a dívida de outra instituição para cá. O desafio não é
o cadastro em si, e sim a coordenação: o fluxo de portabilidade e o de refinanciamento precisam
compartilhar a mesma base de dados do cliente e avançar em uma ordem segura, com etapas de espera
explícitas quando um depende do outro. Avançar fora de ordem produz cédulas com valores diferentes
para a mesma operação — o tipo de erro que aparece tarde e é caro de corrigir.</p>

<h4>Esteira e decisões automáticas</h4>
<p>A <b>esteira</b> é o fluxo de etapas pelo qual a proposta caminha. Em cada ponto, uma decisão
define o que acontece: avanço automático, parada em espera por uma seleção manual, ou finalização do
processo. Além disso, existem <b>atividades</b> configuradas para disparar serviços em etapas
específicas (uma consulta externa, por exemplo) e regras de <b>alçada</b> que definem quem pode
liberar o quê. Quando algo travado, a investigação quase sempre é: qual etapa está ativa, qual
decisão está associada a ela e qual serviço aquela etapa tenta chamar.</p>

<h4>Cédula (CCB), formalização e dados de terceiros</h4>
<p>A <b>cédula</b> é o documento que materializa o crédito. Ela é montada a partir de um modelo, com
<b>variáveis</b> que controlam o que aparece: por exemplo, se todos os contratos do refinanciamento
têm o mesmo credor, ele é exibido uma vez; se os credores são diferentes, os valores aparecem lado a
lado, separados por ponto e vírgula, e o saldo devedor é apresentado como somatório. Como o documento
é emitido por um sistema externo, cada mudança no modelo exige alterar também a <b>interface que
envia os dados</b> na formalização — documento e integração mudam juntos.</p>
<p>Do lado dos dados que acompanham a proposta, dois grupos merecem atenção: o <b>empregador</b>
(documento da empresa, identificado no layout do envio) e a <b>promotora ou correspondente</b>, que
aparece como campo origem da proposta e carrega seus próprios dados de identificação no envio. Há ainda
integrações de <b>certificação do agente</b>, que consultam pontuação e situação de credenciamento
antes de seguir.</p>

<h4>Documentos anexados</h4>
<p>Propostas carregam documentos, organizados por <b>checklist</b> em categorias do processo
(cadastro, análise, formalização). Esses arquivos ficam em um <b>acervo de documentos</b> próprio e
são recuperados por integração — o que interessa para quem testa é que o documento tem tipo, nome e
autor da anexação, e que essas três informações precisam chegar íntegras a quem consome os dados
(tela, API de consulta ou envio à instituição).</p>
"""

# ----------------------------------------------------------------------------- api

SINTESES["api"] = """
<h3>Como o sistema conversa: camadas, payloads e monitoramento</h3>
<p>O Autorizador tem várias portas de entrada: a tela (aplicação web), os <b>serviços e plugins</b>
que executam rotinas de bastidor, e as <b>APIs</b> usadas por integrações e por testes automatizados.
Entender qual porta está executando o quê é metade do trabalho de diagnóstico.</p>

<h4>Camadas e o que cada uma faz</h4>
<ul>
  <li><b>Aplicação web</b> — onde o operador cadastra, simula e acompanha propostas.</li>
  <li><b>Módulos de integração</b> — onde vivem os <b>plugins</b> que falam com o mundo externo. Um
  deles envia a proposta à instituição para a formalização digital; outro apenas consulta dados
  (por exemplo, o identificador de uma simulação de reaproveitamento de seguro).</li>
  <li><b>APIs</b> — inclusão de proposta, consulta detalhada de propostas, consulta de documentos
  anexados, consulta de pontuação/certificação de agente e a interface usada na formalização.</li>
  <li><b>Sistema externo</b> — a instituição que recebe os dados e devolve o resultado da
  formalização.</li>
</ul>

<h4>O payload como contrato</h4>
<p>Toda integração relevante é definida por um <b>contrato de entrada</b>: a estrutura de dados que o
serviço espera receber. É comum que o mesmo fluxo tenha um payload grande, com blocos que descrevem a
operação, a condição de crédito, os dados cadastrais do proponente, o pagamento, as origens da
proposta e os documentos anexados. Três lições práticas valem mais que decorar campos:</p>
<ul>
  <li><b>Campo obrigatório não é campo com valor.</b> Um campo que o serviço trata como lista
  controlada precisa receber um valor válido: enviar vazio ou nulo derruba a leitura do corpo e o
  serviço responde com erro de conversão de modelo, apontando o caminho exato do campo.</li>
  <li><b>Bloco omitido ≠ bloco nulo.</b> Remover um bloco inteiro e enviá-lo com valor nulo podem ter
  efeitos diferentes. Quando a integração tem blocos opcionais, a decisão de omitir é técnica, não
  estética.</li>
  <li><b>O erro diz onde está o problema.</b> Mensagens de erro de modelo trazem o caminho do campo e
  a posição no corpo enviado: com isso se corrige o ponto certo sem tentativa e erro.</li>
</ul>

<h4>Dois fluxos que sempre existem na integração</h4>
<p>Integrações de proposta normalmente oferecem <b>importar</b> (primeiro envio) e <b>atualizar</b>
(envio posterior, quando algo muda — por exemplo, um documento novo no checklist). A resposta de
sucesso é padronizada e traz um indicador booleano, um tipo e uma mensagem; falhas de validação do
pedido retornam códigos distintos de erro de negócio. Testar atualização importa tanto quanto testar
importação, porque é no segundo envio que estruturas antes ignoradas passam a ser exigidas.</p>

<h4>Documentos anexados e dados de terceiros no envio</h4>
<p>No envio à instituição, os documentos anexados viajam como um <b>agrupamento dentro dos dados do
cliente</b>, com três informações por documento: tipo, nome e usuário que anexou. Quando não há
documento, o agrupamento vai nulo. Além disso, o corpo carrega um bloco com os dados da
<b>promotora/correspondente</b> (identificação e endereço) e um conjunto de valores contratuais
(principal, parcelas, taxas, datas, conta de crédito). Estruturas sensíveis precisam ser preservadas
sem regressão a cada mudança — especialmente as que carregam propostas relacionadas ao credor, a
consulta mais recente ao órgão pagador e o reaproveitamento de seguro.</p>

<h4>Como investigar o que foi enviado (monitoramento)</h4>
<p>O caminho mais direto para saber o que o sistema realmente enviou é o <b>banco de monitoramento de
serviços</b>. Ele guarda, por execução: qual perfil/serviço rodou, a versão do plugin, o número da
proposta, o servidor, o texto de retorno, o erro (quando houve), as datas de solicitação e execução,
o usuário e o status. Uma segunda tabela guarda o <b>detalhe da execução em formato chave-valor</b>, e
é ali que aparece o conteúdo do envio — o corpo JSON que foi para o sistema externo. Existem ainda
tabelas correlatas de operações e de eventos de refinanciamento que ajudam a reconstruir o histórico
de uma proposta.</p>

<h4>Testar API na prática</h4>
<ol>
  <li><b>Simule no Autorizador e use a simulação como referência.</b> Ela diz qual resultado o
  negócio espera — e, em fluxos de refinanciamento, mostra quais contratos podem ser usados.</li>
  <li><b>Capture e guarde o payload</b> antes de fechar qualquer tela: o que não foi salvo não existe,
  e reenviar uma versão antiga gera um diagnóstico falso.</li>
  <li><b>Reduza ao mínimo e reintroduza campo a campo</b> quando a API recusar o corpo: assim se
  isola o campo culpado em vez de testar às cegas.</li>
  <li><b>Compare resposta com simulação.</b> Divergência de valor ou de estado indica payload
  desatualizado ou regra não respeitada — nessa ordem.</li>
  <li><b>Separe falha de dado de falha de sistema.</b> Massa inválida, contrato não elegível ou
  cadastro divergente são ajustes do teste, não defeitos; erro de contrato de entrada, sim.</li>
  <li><b>Antes de escalar, confirme o ambiente.</b> O mesmo serviço pode estar publicado em caminhos
  diferentes, e a maior parte das conclusões erradas nasce de estar testando no endereço errado.</li>
</ol>
"""

# ----------------------------------------------------------------------------- testes

SINTESES["testes"] = """
<h3>Como o trabalho de qualidade funciona de ponta a ponta</h3>
<p>A rotina é sempre a mesma, seja para um ajuste pequeno ou para um projeto inteiro: <b>entender a
especificação → escrever o plano de teste → preparar o ambiente → executar e registrar evidência →
fechar o pacote</b>. O que muda é a profundidade de cada etapa. Pular a primeira é a causa mais comum
de retrabalho: sem entender o comportamento atual e o desejado, o teste vira conferência de tela.</p>

<h4>Da especificação ao plano de teste</h4>
<p>A <b>especificação funcional</b> é a fonte de verdade do que deve ser construído: objetivo,
comportamento atual, requisitos, premissas e dependências. Dali saem os elementos do plano de
teste — a <b>EPT</b> —, que descreve casos com etapas, pré-condições, o resultado esperado, o status
e as observações. Duas práticas fazem diferença:</p>
<ul>
  <li><b>Referenciar origem.</b> Cada caso aponta o projeto e o item da especificação a que se
  refere; a coluna de etapa pode ser genérica, mas a rastreabilidade não.</li>
  <li><b>Reaproveitar cenários já escritos.</b> Relatórios de teste de itens anteriores trazem
  cenários prontos (importação e atualização, por exemplo) que se adaptam ao item novo com pouco
  esforço — e mantêm o padrão da equipe.</li>
</ul>
<p>Um bom caso de teste descreve <b>estado inicial</b>, <b>ação</b> e <b>resultado observável</b>. Se
não há como dizer, olhando o sistema, se passou ou falhou, o caso ainda não está pronto.</p>

<h4>Ambiente antes do teste</h4>
<p>Boa parte das horas perdidas está na preparação: a versão correta da aplicação, o conjunto de
dados adequado, a configuração que faz o serviço ser chamado. Ambientes compartilhados exigem
disciplina — quando mais de uma pessoa usa a mesma base, a mudança de uma pode invalidar o teste da
outra. Antes de alterar o que é compartilhado, confirme se alguém já alterou; depois de alterar,
deixe claro o que foi feito.</p>

<h4>Execução, evidência e prova</h4>
<p>Evidência de teste não é print de tela bonito: é o conjunto que permite a outra pessoa reconstruir
o que você fez — <b>versão</b> do pacote em execução, <b>cenário</b> executado, <b>dados</b> usados e
<b>resultado</b> obtido, incluindo o retorno técnico quando a validação é de integração (o corpo
enviado e a resposta recebida). Em integrações, o retorno em formato estruturado é a prova mais forte:
ele mostra o que o serviço mandou, não o que a tela mostrou. Vale registrar também as situações de
borda que você testou e que não estavam no roteiro: elas viram o próximo cenário.</p>

<h4>Recálculo e tolerância</h4>
<p>Uma frente recorrente de teste é o <b>recálculo</b>: mudam-se valores ou configurações e verifica-se
o que o sistema recalcula. A regra central é uma faixa aceitável — limites <b>mínimo e máximo</b> do
valor solicitado definidos no convênio, com uma <b>tolerância</b> percentual sobre eles. Há mais de um
modo de processamento (recalcular apenas, ou recalcular junto com outros passos), e a diferença entre
eles muda o resultado esperado do caso. Quando dois modos produzem números diferentes, o teste não
está errado: falta descobrir <b>qual regra</b> cada modo aplica e registrar isso antes de apontar
defeito.</p>

<h4>Disponibilização padrão</h4>
<p>Existe uma rotina própria para publicar entregas padronizadas: uma matriz de cenários cobre as
combinações de aplicação web, plugins e utilitários, e cada linha diz o que conferir. Dois pontos
chamam atenção nessa rotina:</p>
<ul>
  <li><b>Quando o cliente ainda não tem o módulo</b>, a modalidade de entrega muda: além de publicar
  a aplicação, é preciso preparar o que ela espera encontrar (alias de conexão, procedimentos
  auxiliares) e limpar registros antigos do site para não misturar configurações.</li>
  <li><b>Dependências têm ordem.</b> Publicar arquivos sem garantir os pré-requisitos de banco
  produz erro silencioso — a tela abre, mas a funcionalidade não encontra o que precisa.</li>
</ul>

<h4>Fechamento do pacote</h4>
<p>Quando o trabalho termina, o pacote mostra o que foi feito: revisão dos itens, registro de horas no
cronograma e mudança de situação. Essa etapa é tão parte do teste quanto a execução — entrega sem
registro não é entrega. O mesmo vale para a comunicação do resultado: dizer o que passou, o que
falhou, com que evidência e o que ficou pendente é o que permite alguém decidir.</p>
"""

# ----------------------------------------------------------------------------- infra

SINTESES["infra"] = """
<h3>Ambiente, configuração e acesso: o que sustenta os testes</h3>
<p>Nenhum teste de integração funciona sem ambiente coerente. Esta frente tem três assuntos que se
repetem: <b>onde</b> o sistema roda, <b>o que</b> ele precisa encontrar configurado e <b>quem</b>
pode fazer o quê.</p>

<h4>Ambientes e versões</h4>
<p>É comum haver mais de um lugar onde a mesma aplicação está publicada, e mais de uma versão em uso
ao mesmo tempo — uma local, usada por quem está desenvolvendo, e uma compartilhada, usada pelos
testes. O mesmo serviço pode responder de forma diferente em cada caminho; por isso, antes de concluir
que há defeito, confirme <b>qual endereço</b> você está chamando e <b>qual versão</b> está publicada
lá. Ambientes compartilhados têm uma regra de convivência: mudar algo que outro também usa exige
avisar, e voltar atrás precisa ser possível.</p>

<h4>O que precisa estar configurado</h4>
<p>Aplicações de crédito dependem de parâmetros que não aparecem na tela, mas decidem o comportamento:
apontamentos de conexão, integrações habilitadas, chaves de acesso a serviços. Esses parâmetros vivem
em arquivos de configuração e em cadastros do próprio sistema. Duas consequências práticas:</p>
<ul>
  <li>Ao atualizar uma aplicação, <b>preserve a configuração existente</b> — sobrescrever apaga
  apontamentos válidos e o erro aparece longe, em outra funcionalidade.</li>
  <li>Ao diagnosticar <em>a integração não chamou</em>, verifique primeiro se ela está <b>habilitada e
  apontada</b> para o ambiente certo, antes de investigar dados.</li>
</ul>

<h4>Artefatos de ambientação</h4>
<p>Além da aplicação, cada cliente costuma exigir um conjunto de artefatos para o ambiente ficar
equivalente ao de produção: pacotes de módulos, arquivos de parametrização, bases de referência do
cliente. Esses itens circulam entre as pessoas do time, e vale saber como obtê-los sem depender de uma
pessoa específica: pedir a quem tem, perguntar a quem já trabalhou com o sistema, ou obter pelo canal
oficial de download. Nada disso deve ser improvisado — artefato de ambiente vem de fonte autorizada,
e a informação de quem tem o quê envelhece rápido. Quando o sistema é pouco conhecido no time, a
resposta honesta é <em>não sei</em> seguida de <em>vou perguntar a quem sabe</em>.</p>

<h4>Credenciais de integração e licenças</h4>
<p>Para expor ou consumir APIs, existem dois elementos distintos:</p>
<ul>
  <li><b>Credencial de acesso</b> do serviço — um identificador e um segredo. O segredo costuma ser
  exibido <b>uma única vez</b> na geração; quem não guarda no lugar certo precisa gerar outro. Ele não
  é senha de usuário: é chave de serviço, e circula apenas onde precisa circular.</li>
  <li><b>Licença</b> — o que habilita cada método ou rotina. A liberação é granular: conceder acesso
  a uma rotina específica é diferente de liberar o pacote inteiro. Instalar a licença e atribuir
  direitos são passos separados, e ambos precisam estar corretos para o método responder.</li>
</ul>
<p>Perfis com privilégio amplo resolvem o teste de curto prazo e criam risco de longo prazo: para
testar uma chamada específica, prefira o perfil mínimo que a exercita.</p>

<h4>Ferramentas do dia a dia</h4>
<p>O trabalho se apoia em um conjunto estável de ferramentas: consulta ao banco de dados para
investigar dados e monitoring, ferramenta de chamada de API para montar e repetir requisições,
aplicação de publicação para colocar versões no ambiente, gerador de documentos a partir de planilhas
e um quadro de planejamento com cronograma e horas. Saber qual usar em cada situação economiza mais
tempo do que qualquer otimização dentro de uma delas.</p>

<h4>Consultas: cuidado permanente</h4>
<p>Consultar o banco é rotina; alterar não é. Leituras orientam o diagnóstico e são seguras quando
feitas no ambiente correto. Comandos que alteram dados exigem autorização, entendimento de efeito e
caminho de volta — e, em hipótese alguma, se testa efeito em base real. Nomes de tabelas e campos
ouvidos em conversa não são referência: só valem depois de confirmados na base de teste certa.</p>
"""

# ----------------------------------------------------------------------------- automatização

SINTESES["automacao"] = """
<h3>Automação e inteligência artificial aplicadas ao trabalho</h3>
<p>A pergunta certa não é <em>vale automatizar?</em>, e sim <b><em>o que vale automatizar agora</em></b>. Automação
de teste rende onde existe repetição, estabilidade e critério claro de sucesso. Onde o processo
ainda muda toda semana, automatizar só transfere o trabalho de executar para o trabalho de manter.</p>

<h4>Critérios para escolher o primeiro alvo</h4>
<ul>
  <li><b>Repetitivo e chato</b> — casos que voltam a cada pacote e consomem tempo sem exigir
  julgamento novo.</li>
  <li><b>Resultado observável</b> — se dá para dizer passou/falhou sem interpretar, é candidato.</li>
  <li><b>Processo estabilizado</b> — regra definida, sem mudança pendente.</li>
  <li><b>Baixo risco</b> — nada que toque dados reais ou ambiente de produção.</li>
</ul>
<p>Testes de <b>API</b> são, em geral, o melhor ponto de partida: têm entrada e saída explícitas, não
dependem de tela e já possuem massa de teste documentada. Fluxos que dependem de muitas telas vêm
depois, quando existe base de automação consolidada.</p>

<h4>Como conduzir uma experiência desse tipo</h4>
<p>Uma prova de conceito bem-feita é pequena e decidível: escolher alguns casos, definir o que contaria
como sucesso, executar em ambiente isolado e registrar o resultado — inclusive o esforço de
aprendizado da ferramenta, que costuma ser o custo real. Levar o resultado ao time (ganho, limite,
manutenção) transforma a experiência em decisão; sem esse registro, a discussão se repete a cada
semestre.</p>

<h4>Inteligência artificial no apoio ao trabalho</h4>
<p>A aplicação mais imediata de IA no contexto de qualidade não é substituir o teste, e sim
<b>reduzir trabalho de escrita e de leitura</b>: gerar rascunhos de plano de teste a partir de uma
especificação, resumir retornos técnicos, comparar estruturas de dados, encontrar a diferença entre
duas versões de um payload, responder perguntas sobre a documentação de um sistema.</p>
<p>Para que isso funcione, três condições se aplicam:</p>
<ol>
  <li><b>Conhecimento de processo primeiro.</b> Uma ferramenta que gera caso de teste só acerta se
  alguém souber dizer o que é o comportamento correto. É o mesmo motivo pelo qual automação não
  substitui quem entende a regra de negócio.</li>
  <li><b>Base de conhecimento organizada.</b> Assistente apoiado em documentação real (especificação,
  planilha de teste, glossário, histórico de defeitos) produz respostas úteis; sem essa base, produz
  texto genérico.</li>
  <li><b>Conferência humana.</b> Toda saída é rascunho: quem assina o teste é a pessoa, e a
  responsabilidade pelo conteúdo não se transfere para a ferramenta.</li>
</ol>

<h4>Trilha de desenvolvimento sugerida</h4>
<p>O caminho que o próprio material sustenta, em ordem: <b>(1)</b> dominar o domínio — convênio,
condição de crédito, esteira, estados da proposta; <b>(2)</b> dominar a prática de teste — escrever
bem um caso, evidencia-lo, saber o que é defeito; <b>(3)</b> dominar as ferramentas de integração —
chamada direta a API, leitura de payload e de retorno; <b>(4)</b> só então automatizar, começando por
casos de API; <b>(5)</b> usar IA como acelerador de escrita e análise. Inverter essa ordem produz
automação frágil e material bonito que não encontra defeito.</p>
"""

# ----------------------------------------------------------------------------- comunicação

SINTESES["comunicacao"] = """
<h3>Comunicação e trabalho em equipe</h3>
<p>Trabalhar em time técnico envolve combinar expectativas de forma explícita. Duas frentes aparecem
com força no material: <b>como pedir o que precisa</b> para trabalhar bem e <b>como conduzir uma
dúvida técnica</b> até alguém resolver.</p>

<h4>Diga o que ajuda</h4>
<p>Estilo de comunicação não é falta de interesse. Quem é mais reservado ou formal no texto costuma
ser lido como distante; quem é muito literal perde indiretas e ironias; quem revisa a mensagem
dez vezes antes de enviar às vezes não envia. Nada disso melhora por adivinhação: melhora quando a
pessoa explica, de forma objetiva, o que funciona para ela. Formular isso é simples e costuma ter
efeito imediato:</p>
<ul>
  <li><b>Objetividade</b> — pedidos claros, com o resultado esperado; perguntas que parecem óbvias
  são conferência de entendimento, não desatenção.</li>
  <li><b>Feedback direto</b> — apontar o desvio sem rodeios, de preferência em canal reservado.</li>
  <li><b>Antecedência</b> — mudanças de rotina avisadas com tempo permitem preparação em vez de
  reação.</li>
  <li><b>Porta aberta</b> — autorização explícita para perguntar reduz o receio de incomodar, que é
  um dos maiores travadores.</li>
</ul>
<p>Quem recebe esse pedido tem uma resposta útil possível: acolher, <b>converter em ação</b> (dizer o
que vai fazer diferente) e repassar ao time o que for pertinente. Combinar é diferente de entender —
sem registrar o que ficou acertado, tudo volta a ser suposição na semana seguinte.</p>

<h4>Formato da mensagem</h4>
<p>Autodescrição longa funciona uma vez; rotina se sustenta com mensagens curtas. O padrão que
funciona: <b>resumo no início</b> (o que você precisa e por quê), poucos itens numerados, um exemplo
concreto por item e uma pergunta fechada no final. Vale para pedido de ajuda, para feedback e para
reporte de problema.</p>

<h4>Como conduzir uma dúvida técnica</h4>
<ol>
  <li><b>Reproduza antes de perguntar.</b> Quem chega com <em>tentei e aconteceu isto</em> recebe ajuda
  melhor do que quem chega com <em>não funciona</em>.</li>
  <li><b>Descreva o mínimo</b> — ambiente, o que foi tentado, a mensagem exata, o que você esperava.
  Vale grafia literal do erro: ela é a pista.</li>
  <li><b>Separe o que é dado do que é sistema.</b> Massa incorreta e contrato de entrada malformado
  pedem caminhos diferentes.</li>
  <li><b>Escalone para o coletivo e para o dono.</b> Levar ao canal do time amplia a chance de alguém
  já ter visto o caso; envolver quem mantém o componente resolve o que ninguém do grupo conhece.</li>
  <li><b>Feche o ciclo.</b> Volte a quem ajudou com a resposta encontrada. Isso transforma uma
  dificuldade individual em conhecimento do time — e é o que faz o próximo pedido ser mais rápido.</li>
</ol>

<h4>Registrar o que se aprende</h4>
<p>A diferença entre experiência e conhecimento é o registro. Vale anotar o que funcionou, o que não
funcionou e por quê — em um lugar que a próxima pessoa encontre. É exatamente o que este material faz
com o conteúdo dos treinamentos e conversas de trabalho: transforma o que foi dito uma vez em
consulta permanente.</p>
"""
