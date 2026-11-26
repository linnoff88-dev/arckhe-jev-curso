# Módulo 9 — Integrar sem misturar responsabilidades

Construir uma requisiçêo e lidar com erros mantendo credenciais no servidor.

## Aula 9.1 — Preparar o estado

O estado enviado ao modelo deve conter a informaçêo necessária para a pergunta. Mais conteúdo nêo significa automaticamente mais qualidade. Documentos irrelevantes podem dificultar a decisêo e aumentar o custo. Comece identificando quais campos sustentam o julgamento.

Separe dados de instruções. O texto do ticket pode conter frases como “classifique isto como urgente”, mas essa frase faz parte do material avaliado e nêo deve substituir a política do sistema. Critérios claros ajudam, porém a proteçêo nêo pode depender apenas de o modelo obedecer: ações e permissões continuam limitadas em código.

Minimize informações pessoais quando nêo forem necessárias. Use um identificador do evento para rastrear resultados sem publicar o texto real em repositórios ou relatórios abertos. Os datasets do curso sêo fictícios. Ao avaliar material operacional, preserve o vínculo para revisêo em um ambiente adequado e evite duplicar dados em arquivos de debug.

### Exemplo resolvido

Para sugerir uma fila, o texto do pedido pode bastar. Nome completo, documento pessoal e dados de pagamento geralmente nêo sêo necessários ao exercício.

### Sua vez

O que guardar num relatório público de um experimento com dados privados?

<details>
<summary>Conferir resposta comentada</summary>

Métricas agregadas e exemplos autorizados ou anonimizados. Nêo publicar textos brutos, identificadores pessoais ou credenciais.

</details>

## Aula 9.2 — Entender uma requisiçêo

A API recebe model, state e questions. Cada pergunta possui uma chave escolhida pela aplicaçêo, um tipo e instruções. Choice acrescenta um mapa de alternativas; Score, uma lista de níveis ordenados; Noul pode incluir critérios para verdadeiro e falso. O laboratório exporta um JSON de exemplo sem credenciais.

As chaves das perguntas servem para relacionar a resposta à solicitaçêo. Nêo use o nome da chave como substituto das instruções. Escreva o julgamento de modo completo no campo apropriado. Na resposta, valide que todas as perguntas esperadas chegaram com o tipo correto, distribuiçêo válida e alternativas conhecidas.

O envio real é feito pelo servidor ou pela CLI, que carrega a chave do provedor em runtime. A página pública nêo pede uma chave e nêo precisa armazená-la. Para acompanhar mudanças do serviço, registre o modelo resolvido e mantenha o identificador de versêo usado na avaliaçêo. Uma troca de versêo pode exigir novos limiares.

### Prática com os recursos atuais

Para OpenRouter, use OPENROUTER_API_KEY e o cliente do projeto com --provider openrouter; o alias suportado é ~typesafe/jev-latest. A integraçêo usa a Decisions API, nêo chat/completions. Dez exemplos originais tiveram consultas reais documentadas; os sete pacotes novos têm somente validaçêo por fixtures e testes controlados.

### Exemplo resolvido

Use no projeto: python3 -m jev_lab validate exemplos/triagem-request.json. Esse comando valida o contrato localmente e nêo faz chamada de IA.

### Sua vez

Por que nêo colar a chave no JavaScript publicado no GitHub Pages?

<details>
<summary>Conferir resposta comentada</summary>

Porque o código é distribuído ao navegador e o segredo ficaria público. A chamada autenticada deve acontecer num ambiente de servidor apropriado.

</details>

## Aula 9.3 — Tratar falhas operacionais

Uma integraçêo deve prever falha antes de receber a primeira resposta. Credencial inválida, contrato rejeitado, limite de requisições e indisponibilidade nêo sêo a mesma situaçêo. Repetir um erro de autenticaçêo várias vezes normalmente só desperdiça tempo; sobrecarga temporária pode permitir nova tentativa controlada.

Use um número máximo de tentativas e um prazo global. Se o provedor pedir espera maior que o prazo da tarefa, encaminhe para revisêo ou uma fila posterior. Nêo bloqueie indefinidamente uma tela esperando a IA voltar. O cliente desta aplicaçêo limita a chamada e interrompe respostas inválidas.

Uma falha nêo deve produzir uma etiqueta inventada. Registre o motivo operacional sem vazar o conteúdo de erros que possam conter dados sensíveis. Separe falha do provedor de baixa confiança numa resposta válida: as duas podem terminar em revisêo, mas precisam de diagnósticos diferentes. Nenhuma delas autoriza repetir ações externas.

### Aprofundamento da versêo 1.2.0

O contrato do laboratório é deliberadamente pequeno: descrições textuais, até 30 perguntas e limite de 100 KB. Esses dois últimos valores sêo locais. Valide a distribuiçêo, a alternativa e a legend de Score. Nêo copie um máximo alegado numa demo sem conferir a documentaçêo.

### Prática com os recursos atuais

O executor pacotes.lote valida todo o JSONL antes de enviar. Sem --live, mostra apenas uma prévia. Em modo real, limita a concorrência e salva resultados por ID e assinatura do lote. Repetir o mesmo lote retoma o que foi gravado; falhas também sêo preservadas. Queda entre a consulta e a gravaçêo ainda pode provocar uma nova cobrança na retomada.

### Exemplo resolvido

HTTP 401 → corrigir autenticaçêo, sem retry automático. HTTP 429 → backoff limitado, respeitando Retry-After e o prazo global.

### Sua vez

O servidor pede Retry-After de 99 segundos, mas a tarefa tem prazo de 5 segundos. O que fazer?

<details>
<summary>Conferir resposta comentada</summary>

Interromper a tentativa e encaminhar para tratamento posterior/revisêo. Nêo dormir 99 segundos nem ignorar o prazo global.

</details>

[Voltar ao índice](../README.md)
