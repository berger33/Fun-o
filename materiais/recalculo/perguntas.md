# Perguntas de validação — `recalculo.mp4`

O arquivo é uma conversa de treinamento/depuração, não uma especificação. Responder com a EF/EPT vigente, evidência visual e responsáveis de negócio, CQ e desenvolvimento.

## Regra de tolerância

1. Qual EF/projeto e requisito correspondem aos casos mencionados como “2.1”, “3.2”, “caso 3” e “caso 2” (`00:00:21–00:00:35; 00:03:31–00:03:41`)?
2. Qual é a fórmula aprovada para aplicar a tolerância aos limites inferior e superior (`00:11:46–00:13:15; 00:59:49–01:01:16`)?
3. O percentual é calculado sobre o limite ou sobre o valor solicitado? Aplica-se para fora dos limites, para dentro, ou de outra forma?
4. Os limites são inclusivos? Como são tratados arredondamento, casas decimais, moeda e valores exatamente na borda?
5. Qual comportamento é esperado com tolerância zero e quando o parâmetro está ausente/desativado?
6. Os exemplos de 2.990/2.995/3.000, 1% e 10% correspondem a algum caso aprovado ou foram apenas ilustrações? Qual valor é o correto na EF?

## Modos, fluxo e sistema

7. O que significam exatamente as opções chamadas pelo ASR de “somente recálculo” e “ambos”? Qual regra diferencia os modos (`00:21:00–00:30:23`)?
8. Qual é a sequência oficial de proposta, recálculo, análise e eventual averbação? Quais estados/transições deveriam ser observados (`00:30:52–00:33:32; 01:03:01–01:05:59`)?
9. A condição é configurada no convênio, na proposta ou em ambos? Qual tela/campo e qual fonte oficial confirmam isso (`00:14:54–00:15:10`)?
10. A regra deve ser verificada via UI, API/plugin ou ambos? Qual endpoint, payload e schema vigentes? O pacote não contém JSON validado.
11. Quais cenários negativos e positivos são obrigatórios na EPT, e qual resultado/mensagem é esperado para cada um?

## Resultado, versão e ambiente

12. Em quais passos a gravação aparenta falhar por não considerar tolerância, e em quais aparenta passar? Há evidência original que permita comparar entrada, configuração e resultado (`00:23:42–00:30:23; 00:48:30–00:54:12`)?
13. Qual versão estava instalada em cada tentativa, e o que significa a referência a uma versão “5.5” e outra versão mais nova (`00:37:37–00:38:00`)?
14. Quais são os ambientes/servidores aprovados e qual deles foi usado? Houve cópia de arquivos ou alteração de versão? Quem é responsável pelo ambiente (`00:37:37–00:39:28`)?
15. Existe dependência de versão, configuração ou dado da proposta que explique a diferença entre “somente recálculo” e “ambos”?
16. O relato de que o teste “funcionou” em `00:52:35–00:54:12` refere-se a qual configuração, modo, versão e proposta? Qual foi o resultado observável?

## Fonte e evidências

17. Qual é o resultado correto do cenário final sugerido — limites 1.000/3.000, tolerância 1% e proposta 2.500 (`01:06:30–01:07:03`)? Esse cenário é exigido pela EF?
18. Há gravação de tela, log ou evidência do fluxo que permita confirmar que a proposta passou pelo estado de recálculo esperado?
19. O último cue termina 27,72 s após a duração de áudio declarada e há longos trechos de aparente áudio não técnico. A origem desses segmentos e a transcrição devem ser revisadas por uma pessoa?
20. Qual procedimento aprovado rege a criação e limpeza dos dados de teste, a atualização da versão e a proteção de uma base compartilhada?
