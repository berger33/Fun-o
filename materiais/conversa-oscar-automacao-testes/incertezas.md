# Incertezas e pendências — automação de testes e trilha de estudo (Oscar)

## 1. Autoria das falas não é determinável

- O recorte **não** indica quem enviou cada mensagem. Diálogos alternados sem citação (“sim”, “é tenho
  esse pensamento tbm”) não permitem atribuir autoria com segurança.
- **Consequência:** este pacote trata as falas como **posições do diálogo**, não como declarações de
  uma pessoa específica. Nenhum nome de pessoa é vinculado a opinião, proposta ou dificuldade.
- **Se houver necessidade de citar pessoas** (ex.: em contexto de feedback), confirmar com os
  participantes antes — não usar este material como registro de autoria.

## 2. A PoC com Cypress é intenção, não plano (`[M09]`–`[M12]`)

- “quero passar um Cypress aqui na função pra ver se funciona” — não há: aprovação, escopo, ambiente,
  versão da ferramenta, prazo, responsável, critério de sucesso.
- Também **não** há registro de que a ferramenta tenha sido instalada, testada ou apresentada a alguém.
- **Validar antes de qualquer uso:** se/quando a PoC acontecer, este pacote deve receber o resultado
  (o que foi automatizado, esforço, ganho e limitações).

## 3. PSA e PEGEUT permanecem indefinidos (`[M20]`–`[M26]`)

- A fonte diz apenas que existe **uma configuração** difícil de achar e que ninguém do diálogo tem
  experiência.
- **Não** há: o que é PSA, o que é PEGEUT, qual é o módulo, qual é o parâmetro, qual é o sintoma exato,
  em que ambiente e qual é a urgência real.
- **Ação:** manter como **lacuna de cobertura** do acervo e pedir material (gravação/treinamento) —
  registrado em [`../CONFLITOS_E_VALIDACAO.md`](../CONFLITOS_E_VALIDACAO.md).
- **Não** alterar configuração de PSA/PEGEUT com base nesta conversa: ela não descreve nenhum passo.

## 4. “Assumi a pauta de colega” (`[M21]`)

- Frase ambígua: pode significar assumir **atividade/fila de trabalho** do colega, ou assumir um
  **conjunto de itens de pauta** (reunião). A fonte não esclarece. Ambas as leituras foram preservadas
  no glossário com o sentido aproximado.

## 5. Escopo do “testes padrão” (`[M09]`, `[M10]`)

- “alguns testes padrão — tipo api e etc” **não** delimita quais casos entrariam na automação. A
  escolha do primeiro alvo é inferência do analista (Fluxo A de [`procedimentos.md`](procedimentos.md)),
  **não** decisão da fonte.

## 6. Sem data, sem duração e sem ambiente

- O recorte não tem carimbo de data/hora; os dois blocos foram separados por encerramento de
  expediente, o que sugere dias ou turnos distintos — **não** se pode afirmar quantos.
- Nenhum ambiente, versão, ferramenta da Função ou repositório é citado.

## 7. Menção ao “arena” e à faculdade (`[M18]`, `[M06]`, `[M07]`)

- `[M18]` cita conectores de uma ferramenta de assistente em tom jocoso: **não** é instrução técnica nem
  política de uso. `[M06]`/`[M07]` são contexto pessoal de formação.
- Ambos foram mantidos na transcrição por fidelidade; **nada** neles deve ser tratado como processo.

## 8. Mascaramento

- Não foi necessário mascarar identificadores diretos: o recorte não contém CPF, CNPJ, telefone,
  e-mail, matrícula, endereço, host ou credencial. Varredura automática
  (`tools/validar_materiais.py`) sem achados.
