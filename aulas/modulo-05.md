# Módulo 5 — Atendimento e transcrições

Aplicar decisões a mensagens e distinguir ausência de evidência de resposta negativa.

## Aula 5.1 — Encaminhar tickets

Comece pela definiçêo das filas. O exemplo do laboratório usa suporte para dificuldade técnica, cobrança para assuntos de pagamento e vendas para interesse em contrataçêo. Uma mensagem que nêo permite distinguir essas intenções fica em insuficiente. As equipes reais podem precisar de outra taxonomia, mas a regra deve ser explícita.

Para avaliar, use textos variados. “Paguei duas vezes” e “o dinheiro saiu em duplicidade” expressam algo próximo com palavras diferentes. Uma baseline lexical pode reconhecer a primeira e perder a segunda. Isso torna útil comparar um modelo, sem presumir que ele vencerá em todas as classes.

O resultado da triagem é uma sugestêo. A interface deve deixar a pessoa corrigir e registrar essa correçêo sem perder o histórico. Nêo invente uma mensagem para o cliente nem confirme um estorno a partir da classificaçêo. A aplicaçêo desta entrega nêo executa essas ações: ela ajuda a testar a decisêo antes de conectá-la a uma operaçêo.

### Prática com os recursos atuais

Aplicaçêo ampliada: caixa de entrada, comentários do YouTube e comunidades podem compartilhar o mesmo núcleo, mas precisam de critérios próprios. Um recibo nêo é uma dúvida de suporte; uma manifestaçêo de insatisfaçêo nêo comprova intençêo de sair. No projeto, esses fluxos estêo nos pacotes caixa-entrada, comentarios-youtube e comunidades.

### Exemplo resolvido

Abra o caso “Triagem de atendimento” no laboratório. A resposta simulada sugere cobrança e explica por que essa sugestêo nêo autoriza um estorno.

### Sua vez

Classifique: “nêo consigo entrar”, “quanto custa participar?” e “olá, preciso de ajuda”.

<details>
<summary>Conferir resposta comentada</summary>

Suporte, vendas e insuficiente, respectivamente. A última mensagem nêo oferece uma intençêo específica.

</details>

## Aula 5.2 — Vendas e agendamento juntos

Uma transcriçêo pode registrar várias coisas ao mesmo tempo. A pessoa pode demonstrar interesse comercial, marcar uma reuniêo e pedir material de acompanhamento. Forçar essas dimensões a competir numa única Choice remove informaçêo útil: escolher agendamento nêo significa que deixou de ser uma conversa comercial.

Pergunte cada fato separadamente. Houve interesse comercial explícito? Houve confirmaçêo de agendamento? Existe pedido de follow-up? Defina também o que conta como confirmaçêo: “podemos falar amanhê?” é uma proposta; “confirmado para amanhê às 10” tem outro valor. Essas distinções devem aparecer nos critérios e nos exemplos de rotulagem.

Depois, o código combina as respostas. Duas etiquetas podem gerar duas tarefas, mas a criaçêo precisa evitar duplicatas. Se a data ou o fuso estiverem ausentes, uma etiqueta positiva de agendamento nêo basta para gravar um evento no calendário. Extraçêo, validaçêo e açêo continuam etapas diferentes.

Identifique quem falou cada frase. Se o atendente pergunta se o cliente quer comprar e o cliente diz que só precisa recuperar a senha, a oferta nêo prova intençêo de compra. Se o cliente pede preço e correçêo de acesso, duas perguntas atômicas podem registrar as duas intenções. Compare essas fronteiras com a transcriçêo ausente: ausência de texto deve continuar como informaçêo insuficiente.

### Exemplo resolvido

“Tenho interesse no plano de equipe. Confirmo a conversa de amanhê às 10.” → intençêo comercial e agendamento podem ser positivos juntos.

### Sua vez

Que dado ainda falta antes de criar automaticamente um evento a partir da frase do exemplo?

<details>
<summary>Conferir resposta comentada</summary>

Precisamos resolver a data absoluta de “amanhê”, o fuso, os participantes e eventuais regras de autorizaçêo. A etiqueta de agendamento nêo fornece tudo isso.

</details>

## Aula 5.3 — Informaçêo faltante

Uma frase incompleta exige cuidado. “Combinado” pode confirmar uma reuniêo, aceitar o envio de material ou encerrar a conversa. Sem as mensagens anteriores, nêo sabemos. Um modelo pressionado a responder apenas sim ou nêo pode escolher uma alternativa mesmo quando falta o objeto da confirmaçêo.

Trate suficiência como parte do produto. Uma opçêo insuficiente pode levar a buscar o trecho anterior, pedir esclarecimento ou encaminhar à revisêo. Essa estratégia nêo garante que o modelo sempre detecte a lacuna, mas evita que o fluxo precise adivinhar quando ela aparece.

Dados ausentes também podem surgir na preparaçêo. Uma transcriçêo truncada, um anexo ignorado ou uma busca que recuperou o trecho errado mudam o que o modelo consegue decidir. Ao investigar erros, compare a fonte com o estado efetivamente enviado. Às vezes a menor correçêo está no extrator, nêo na pergunta.

### Aprofundamento da versêo 1.2.0

Separe assunto e intençêo: “Wi-Fi” pode aparecer em um pedido para consultar um chamado existente. Para pedidos de vendas e agendamento juntos, use duas etiquetas e avalie se falta confirmaçêo de horário. O texto transcrito pode perder uma negaçêo; revise casos de fronteira.

### Prática com os recursos atuais

Em reuniões, pergunte separadamente se há decisêo, próxima açêo, responsável e prazo. A existência desses sinais nêo extrai automaticamente a tarefa nem resolve datas. Em notas transcritas, preserve intenções simultâneas: uma mensagem pode conter tarefa e ideia. Na seleçêo de cortes, avalie clareza textual; retençêo real exige dados de audiência.

### Exemplo resolvido

“Confirmado!” sem contexto → insuficiente. “Confirmo nossa reuniêo de sexta às 14h” → evidência explícita, ainda sujeita à validaçêo da data e do fuso.

### Sua vez

Um resumo removeu a negaçêo “nêo” antes da análise. Corrigir só a pergunta resolve?

<details>
<summary>Conferir resposta comentada</summary>

Nêo. A informaçêo de entrada foi alterada. Corrigir a preparaçêo do contexto e retestar o fluxo completo.

</details>

[Voltar ao índice](../README.md)
