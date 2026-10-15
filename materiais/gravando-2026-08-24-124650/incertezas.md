# Incertezas e validações pendentes — Gravando 2026-08-24 124650.mp4

## 1. Cenário e comportamento do plugin

- A alteração de sistema/propriedade JSON que está sendo testada não é identificada (**00:00:00–00:02:12**). Confirmar EF/EPT, campo esperado, contrato de retorno e regressões.
- As palavras reconhecidas como **“JSON”** aparecem com grafias instáveis (“Jason”, “Jzão”, “Jzão”); conferir áudio e artefato real.
- Nome/versão do plugin, parâmetro, evento de execução e corpo de resposta não aparecem com precisão.
- O ASR registra uma divergência entre os identificadores de promotora mostrados no documento/print e na proposta (**00:04:00–00:04:19**). Os valores foram omitidos; confirmar apenas com dados sintéticos autorizados.

## 2. Etapas e regra de negócio

- Há correções/oscilações entre etapa 2, 3 e 4 ao falar da criação/avanço da proposta e do plugin (**00:10:12–00:12:23**). A ordem deve vir da EPT/esteira aprovada.
- CPD é expandido verbalmente como consignado privado e associado ao retorno do Crivo (**00:04:54–00:05:02**); a regra funcional e campos não são detalhados.
- “Rotina de proposta”, “80”, “Estacionário de teste” e outras expressões estão sujeitas a erro de ASR e não foram confirmadas em tela.
- `N/W` não é explicado nesta gravação; não inferir efeito a partir de outras gravações.

## 3. Sanitização e privacidade

- O intervalo `00:06:01.19–00:09:31.31` foi removido da transcrição pública por conter material pessoal e procedimento de acesso/alteração de base não necessário ao guia. Nenhum identificador pessoal, consulta ou comando foi copiado.
- Identificadores de teste de promotora foram substituídos por marcador em `00:04:02` e `00:04:06`; um valor exemplificativo foi substituído em `00:09:39`.
- O commit upstream que contém transcrições integrais segue acessível por SHA; ver [`../PRIVACIDADE_E_RETENCAO.md`](../PRIVACIDADE_E_RETENCAO.md) §§9–10.

## 4. Evidências e ferramentas

- O fluxo de geração com Geradoc, a ferramenta de apresentação e seus formatos/templates não foram demonstrados integralmente (**00:13:33–00:17:25**).
- O limite de tamanho de documento é um relato de experiência, não uma política validada (**00:15:00–00:15:13**).
- Não há captura/tela no material atual, nem payload verificável; todas as recomendações de evidência são verbais.

## 5. Cobertura e duplicidade

- ASR de 352 segmentos; áudio declarado `00:18:45.82`; último segmento `00:18:36.76–00:18:40.08`.
- MP4 e imagens não foram revisados visualmente nem por escuta integral nesta etapa.
- `Gravando 2026-08-24 161729.mp4` tem o mesmo OID LFS que esta gravação e será coberto por referência após validação do mesmo conteúdo.
- Nenhum teste ou consulta SQL foi executado; não há SQL literal nos materiais públicos.
