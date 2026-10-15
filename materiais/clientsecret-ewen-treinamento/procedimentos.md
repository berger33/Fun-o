> **Plano de validação, não runbook.** Nenhuma operação abaixo foi executada ou validada contra o MP4. A gravação descreve credenciais, licenças e permissões; seguir exclusivamente procedimentos atuais aprovados por Segurança/Infra/desenvolvimento.

# Procedimentos a validar — ClientSecret EWEN TREINAMENTO.mp4

## Fluxo A — Criar/rotacionar Client Secret com segurança (relato em 00:08:22–00:13:18)

1. Confirmar API, ambiente de teste, titular técnico, escopos necessários, solicitante e autorização formal. Não usar produção para exercício.
2. Consultar a política vigente de expiração, rotação e revogação. A sugestão oral de “data bem longa” não é política e não deve ser adotada por inferência.
3. Gerar o segredo apenas no portal oficial e guardar em cofre corporativo aprovado, com acesso mínimo. Não registrar segredo em Git, chat, documentação, captura, prompt ou log.
4. Como a fala informa que o valor não seria exibido novamente, validar o fluxo de recuperação/rotação e confirmar o armazenamento antes de sair da tela; nunca expor o valor na evidência.
5. Revogar imediatamente qualquer credencial de teste que tenha sido copiada para local não aprovado; nenhuma credencial foi copiada nesta análise.

## Fluxo B — Configurar e executar cenário no Test API (relato em 00:13:18–00:17:48; tentativa adicional em 00:20:03–00:23:55)

1. Confirmar ferramenta, endpoint, API, método, schema, Client ID e perfil com documentação oficial da versão. O ASR lê números de Client ID diferentes em `00:15:09` e `00:21:12`; não usar nenhum sem fonte autorizada.
2. Separar o segredo do Client ID; inserir o segredo somente no mecanismo seguro oferecido pela ferramenta, sem colocá-lo em URL, JSON do cenário, arquivo commitado ou captura.
3. Usar massa fictícia, sandbox e escopo mínimo; revisar o request e o destino antes de enviar.
4. Executar apenas após autorização e registrar evidência sanitizada, mascarando segredos/identificadores reais conforme política de segurança vigente. Este vídeo não confirma sucesso do cenário.

## Fluxo C — Solicitar/instalar licença de API ou método (relato em 00:35:30–00:42:19)

1. Abrir solicitação formal ao grupo/responsável autorizado, identificando produto, API/método, ambiente, versão, dependências e rollback.
2. Obter o artefato de licença por repositório/canal autenticado aprovado; validar assinatura, integridade, origem, versão e autorização antes da instalação. Não copiar caminho/arquivo de máquina pessoal sem aprovação.
3. Se a instalação exigir código/contrassenha, usar apenas o portal/canal oficial e compartilhar o mínimo necessário com o responsável autorizado; não colar código em material público ou chat aberto.
4. Confirmar resultado, auditoria e métodos liberados em ambiente de teste. A fala relata instalação bem-sucedida, mas isso não foi verificado.

## Fluxo D — Atualizar privilégios de usuário/API (relato em 00:09:06–00:11:14, 00:18:01–00:20:05, 00:34:21–00:35:19 e 00:42:48–00:45:44)

1. Verificar matriz formal de funções e conceder somente o direito específico necessário ao usuário de teste.
2. Não elevar para `Supervisor` por conveniência; exigir aprovação de acesso privilegiado, prazo e auditoria quando indispensável.
3. Confirmar na documentação da versão a diferença entre opções `A`/`M`, “direitos por rotina” e métodos; a transcrição é insuficiente e o produto não foi inspecionado.
4. Validar remoção/expiração do acesso temporário após o teste. Não alterar produção com base no relato.

## Fluxo E — Entender CTC/CIP antes de qualquer teste (00:45:51–00:47:12)

1. Consultar EF/documentação vigente e identificar formatos, estados, confirmação/recibo, idempotência, controles de reenvio e responsabilidades de cada sistema.
2. Projetar teste com arquivos sintéticos e parceiro/simulador autorizado; revisar segurança, rejeições e reconciliação.
3. O vídeo declara que o interlocutor não testou suficientemente CTC; nenhum ciclo foi executado neste lote. Não usar a fala como especificação.

## Bloqueios

- Credencial, licença, código de ativação, perfil privilegiado ou endpoint sem autorização formal → interromper e consultar Segurança/Infra.
- Não fazer query SQL: nenhuma instrução SQL literal foi reproduzida nem executada; “SQL Result” não é query.
- Confirmar termos `CloudSecret`/`ClientSecret`, `WPWebService`, nomes das telas e valores do ASR antes de qualquer orientação de produção.
