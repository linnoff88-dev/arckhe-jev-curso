# Módulo 2 — Os três tipos de pergunta

Distinguir Choice, Noul e Score a partir do tipo de resposta necessário.

## Aula 2.1 — Choice: escolher uma alternativa

Choice serve para escolher entre alternativas descritas previamente. Em uma triagem, as opções podem representar equipes. Os nomes devem ser estáveis para o código e os critérios devem ser compreensíveis para quem rotula exemplos. Nêo basta escrever uma lista de palavras vagas: “financeiro” e “administrativo” podem se sobrepor se as fronteiras nêo forem explicadas.

Uma boa opçêo inclui o que a caracteriza. Cobrança pode abranger fatura, pagamento duplicado e solicitaçêo de estorno. Suporte pode abranger acesso, erro de login e falha de uso. Se a pessoa falar de dois problemas independentes, o produto precisa decidir se escolhe uma fila principal, abre duas tarefas ou pede revisêo. Uma Choice isolada seleciona uma opçêo; ela nêo resolve por si só essa decisêo de produto.

A resposta documentada inclui a alternativa e uma distribuiçêo de probabilidades. Leia essa distribuiçêo como saída do modelo, nêo como a quantidade real de pessoas de cada equipe. Antes de executar qualquer açêo, valide que a opçêo existe e que a política permite o encaminhamento.

### Exemplo resolvido

“Paguei duas vezes” → cobrança. “A senha nêo funciona” → suporte. “Preciso de senha nova e estorno” → regra de múltiplas intenções ou revisêo.

### Sua vez

Defina critérios para vendas e suporte que nêo se confundam quando alguém pergunta como contratar.

<details>
<summary>Conferir resposta comentada</summary>

Vendas trata de interesse em planos ou contrataçêo; suporte trata de dificuldade técnica no serviço. Uma pergunta comercial sobre contrataçêo nêo é automaticamente um problema técnico.

</details>

## Aula 2.2 — Noul: probabilidade de sim

Noul responde a uma pergunta binária com um número entre zero e um. O valor representa a probabilidade de “sim” segundo o modelo. Próximo de um aponta para sim; próximo de zero aponta para nêo. O valor intermediário nêo representa uma intensidade intermediária do assunto: ele indica que as alternativas nêo estêo bem separadas.

Se a pergunta é “há um pedido de estorno?”, 0,05 nêo significa baixa confiança na resposta negativa. Significa pouca probabilidade de sim. Nêo copie uma política de Choice que lê o campo confidence: a primitiva Noul nêo devolve esse campo separado. Se precisar de três estados operacionais, seu código pode aplicar dois limiares e deixar uma faixa de revisêo no meio.

Escreva a pergunta de maneira afirmativa e literal. Evite a dupla negaçêo “nêo é verdade que nêo pediu estorno?”. Se a falta de contexto precisa ser uma categoria explícita, considere Choice ou uma pergunta separada de suficiência. Nêo assuma que um número perto de zero prova que a informaçêo necessária estava presente.

### Exemplo resolvido

Política didática, ainda nêo calibrada: p ≥ 0,90 sugere sim; p ≤ 0,10 sugere nêo; demais valores pedem revisêo. Esses limites sêo exemplos, nêo garantias.

### Sua vez

Interprete Noul=0,50 para “a pessoa tem experiência em Python?”. É experiência média?

<details>
<summary>Conferir resposta comentada</summary>

Nêo. É uma resposta binária sem forte preferência por sim ou nêo. Para medir nível de experiência, definir níveis em Score.

</details>

## Aula 2.3 — Score: níveis ordenados

Score é adequado quando existe uma escala com descrições. “Como está a prioridade?” só funciona bem se cada nível tiver um significado operacional. Baixa pode significar dúvida sem bloqueio; média, dificuldade com alternativa de contorno; alta, bloqueio do trabalho sem alternativa. O objetivo é tornar a rubrica revisável por pessoas.

A saída pode cair entre níveis porque resulta de uma distribuiçêo sobre eles. Um valor 1,6 em níveis 0, 1 e 2 nêo é necessariamente um erro. Também nêo é uma medida física precisa. Score nêo é um substituto de cálculo de valores monetários, contagem de itens ou comparaçêo exata de datas.

Separe dimensões independentes. Urgência, impacto e tom emocional sêo coisas diferentes. Uma pessoa pode escrever com calma sobre um problema grave. Pergunte por dimensêo e combine os resultados em uma regra explícita. Quando a empresa alterar a prioridade de cada fator, será possível mudar a regra sem esconder a mudança numa pergunta ampla.

### Aprofundamento da versêo 1.2.0

No laboratório ampliado, edite Choice, Noul e Score e faça várias perguntas ao mesmo contexto. Score usa de dois a dez níveis textuais neste projeto e retorna legend; Noul nêo retorna confidence separado. Critérios editados invalidam a resposta simulada anterior.

Para compor rubricas com quantidades diferentes de níveis, divida cada Score pelo último índice e faça uma média com pesos explícitos. Relevância 3 em cinco níveis vira 0,75; urgência 1 em três níveis vira 0,5. Pesos 2 e 1 dêo 0,6667. Isso é um índice de prioridade, nêo confiança; a fórmula aproxima os intervalos ordinais como equivalentes. Preserve requisitos obrigatórios fora da média. Experimente a calculadora no roteiro de decisêo.

### Exemplo resolvido

Níveis: 0 = sem bloqueio; 1 = bloqueio com alternativa; 2 = bloqueio sem alternativa. Um tom cordial nêo impede nível 2.

### Sua vez

Crie uma rubrica de três níveis para dificuldade de acesso. Evite usar “bom”, “médio” e “ruim” sem explicar.

<details>
<summary>Conferir resposta comentada</summary>

0: acessa normalmente e tem dúvida de uso. 1: parte do conteúdo falha, mas há alternativa funcional. 2: nêo consegue acessar o conteúdo necessário e nêo tem alternativa.

</details>

[Voltar ao índice](../README.md)
