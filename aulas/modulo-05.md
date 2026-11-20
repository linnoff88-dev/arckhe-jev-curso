# Módulo 5 — Atendimento e transcrições

Aplicar decisões a mensagens e distinguir ausência de evidência de resposta negativa.

## Aula 5.1 — Encaminhar tickets

Comece pela definição das filas. O exemplo do laboratório usa suporte para dificuldade técnica, cobrança para assuntos de pagamento e vendas para interesse em contratação. Uma mensagem que não permite distinguir essas intenções fica em insuficiente. As equipes reais podem precisar de outra taxonomia, mas a regra deve ser explícita.

Para avaliar, use textos variados. “Paguei duas vezes” e “o dinheiro saiu em duplicidade” expressam algo próximo com palavras diferentes. Uma baseline lexical pode reconhecer a primeira e perder a segunda. Isso torna útil comparar um modelo, sem presumir que ele vencerá em todas as classes.

O resultado da triagem é uma sugestão. A interface deve deixar a pessoa corrigir e registrar essa correção sem perder o histórico. Não invente uma mensagem para o cliente nem confirme um estorno a partir da classificação. A aplicação desta entrega não executa essas ações: ela ajuda a testar a decisão antes de conectá-la a uma operação.

### Prática com os recursos atuais

Aplicação ampliada: caixa de entrada, comentários do YouTube e comunidades podem compartilhar o mesmo núcleo, mas precisam de critérios próprios. Um recibo não é uma dúvida de suporte; uma manifestação de insatisfação não comprova intenção de sair. No projeto, esses fluxos estão nos pacotes caixa-entrada, comentarios-youtube e comunidades.

### Exemplo resolvido

Abra o caso “Triagem de atendimento” no laboratório. A resposta simulada sugere cobrança e explica por que essa sugestão não autoriza um estorno.

### Sua vez

Classifique: “não consigo entrar”, “quanto custa participar?” e “olá, preciso de ajuda”.

<details>
<summary>Conferir resposta comentada</summary>

Suporte, vendas e insuficiente, respectivamente. A última mensagem não oferece uma intenção específica.

</details>

## Aula 5.2 — Vendas e agendamento juntos

Uma transcrição pode registrar várias coisas ao mesmo tempo. A pessoa pode demonstrar interesse comercial, marcar uma reunião e pedir material de acompanhamento. Forçar essas dimensões a competir numa única Choice remove informação útil: escolher agendamento não significa que deixou de ser uma conversa comercial.

Pergunte cada fato separadamente. Houve interesse comercial explícito? Houve confirmação de agendamento? Existe pedido de follow-up? Defina também o que conta como confirmação: “podemos falar amanhã?” é uma proposta; “confirmado para amanhã às 10” tem outro valor. Essas distinções devem aparecer nos critérios e nos exemplos de rotulagem.

Depois, o código combina as respostas. Duas etiquetas podem gerar duas tarefas, mas a criação precisa evitar duplicatas. Se a data ou o fuso estiverem ausentes, uma etiqueta positiva de agendamento não basta para gravar um evento no calendário. Extração, validação e ação continuam etapas diferentes.

Identifique quem falou cada frase. Se o atendente pergunta se o cliente quer comprar e o cliente diz que só precisa recuperar a senha, a oferta não prova intenção de compra. Se o cliente pede preço e correção de acesso, duas perguntas atômicas podem registrar as duas intenções. Compare essas fronteiras com a transcrição ausente: ausência de texto deve continuar como informação insuficiente.

### Exemplo resolvido

“Tenho interesse no plano de equipe. Confirmo a conversa de amanhã às 10.” → intenção comercial e agendamento podem ser positivos juntos.

### Sua vez

Que dado ainda falta antes de criar automaticamente um evento a partir da frase do exemplo?

<details>
<summary>Conferir resposta comentada</summary>

Precisamos resolver a data absoluta de “amanhã”, o fuso, os participantes e eventuais regras de autorização. A etiqueta de agendamento não fornece tudo isso.

</details>

## Aula 5.3 — Informação faltante

Uma frase incompleta exige cuidado. “Combinado” pode confirmar uma reunião, aceitar o envio de material ou encerrar a conversa. Sem as mensagens anteriores, não sabemos. Um modelo pressionado a responder apenas sim ou não pode escolher uma alternativa mesmo quando falta o objeto da confirmação.

Trate suficiência como parte do produto. Uma opção insuficiente pode levar a buscar o trecho anterior, pedir esclarecimento ou encaminhar à revisão. Essa estratégia não garante que o modelo sempre detecte a lacuna, mas evita que o fluxo precise adivinhar quando ela aparece.

Dados ausentes também podem surgir na preparação. Uma transcrição truncada, um anexo ignorado ou uma busca que recuperou o trecho errado mudam o que o modelo consegue decidir. Ao investigar erros, compare a fonte com o estado efetivamente enviado. Às vezes a menor correção está no extrator, não na pergunta.

### Aprofundamento da versão 1.2.0

Separe assunto e intenção: “Wi-Fi” pode aparecer em um pedido para consultar um chamado existente. Para pedidos de vendas e agendamento juntos, use duas etiquetas e avalie se falta confirmação de horário. O texto transcrito pode perder uma negação; revise casos de fronteira.

### Prática com os recursos atuais

Em reuniões, pergunte separadamente se há decisão, próxima ação, responsável e prazo. A existência desses sinais não extrai automaticamente a tarefa nem resolve datas. Em notas transcritas, preserve intenções simultâneas: uma mensagem pode conter tarefa e ideia. Na seleção de cortes, avalie clareza textual; retenção real exige dados de audiência.

### Exemplo resolvido

“Confirmado!” sem contexto → insuficiente. “Confirmo nossa reunião de sexta às 14h” → evidência explícita, ainda sujeita à validação da data e do fuso.

### Sua vez

Um resumo removeu a negação “não” antes da análise. Corrigir só a pergunta resolve?

<details>
<summary>Conferir resposta comentada</summary>

Não. A informação de entrada foi alterada. Corrigir a preparação do contexto e retestar o fluxo completo.

</details>

[Voltar ao índice](../README.md)
