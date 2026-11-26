# Módulo 12 — Projeto final

Entregar uma decisêo de adoçêo fundamentada, inclusive quando a resposta for nêo automatizar.

## Aula 12.1 — Especificar a triagem

Seu projeto final é uma triagem de atendimento em português. Comece descrevendo quem recebe os tickets, quais filas existem e qual problema deseja reduzir. Evite prometer automaçêo total. A primeira entrega é uma especificaçêo que outra pessoa consegue revisar.

Defina os critérios de cada alternativa, casos ambíguos e o tratamento de informaçêo ausente. Acrescente cinco exemplos difíceis: negaçêo, duas intenções, texto incompleto, sinônimo e instruçêo indevida dentro do ticket. Mostre como cada um deveria ser tratado e por quê.

Depois desenhe a política externa ao modelo. Ela define ações permitidas, revisêo, falhas de contrato, prazo e limite de tentativas. Inclua orçamento e plano de avaliaçêo. O projeto sem código pode usar planilha; o técnico deve acrescentar requisições, testes e relatório reproduzível. Ambos precisam separar fatos, hipóteses e resultados.

### Exemplo resolvido

Entrega: taxonomia + cinco casos difíceis + perguntas + política + diagrama + orçamento + protocolo de avaliaçêo + plano de retorno.

### Sua vez

Escreva uma frase que descreva o sucesso do seu piloto sem usar “IA mais inteligente”.

<details>
<summary>Conferir resposta comentada</summary>

Exemplo: reduzir o tempo de triagem mantendo o erro por fila dentro do limite acordado, com custo total menor e possibilidade de correçêo humana.

</details>

## Aula 12.2 — Avaliar a proposta

Apresente sua avaliaçêo de modo que outra pessoa possa repeti-la. Identifique o dataset, sua origem, as partições e as configurações. Mostre a quantidade de casos por classe, os erros importantes e as limitações. Um gráfico de acurácia sem contexto nêo é suficiente.

Se executou apenas a baseline de regras, diga isso. Se usou respostas simuladas, marque-as como simulaçêo. Se fez uma chamada real, registre o modelo e o uso reportado. Essas distinções nêo diminuem o projeto; tornam sua conclusêo confiável e mostram qual etapa ainda falta.

A rubrica considera formulaçêo, política, evidência, economia e reprodutibilidade. Um projeto que reconhece insuficiência de dados pode ser melhor que um projeto que anuncia sucesso com números inventados. Inclua exemplos em que o sistema errou e explique a menor correçêo proposta, sem ajustar e medir tudo no mesmo conjunto.

### Exemplo resolvido

Relatório honesto: “baseline lexical, 24 exemplos fictícios, 20 acertos; nêo mede Jev nem representa tráfego de produçêo”.

### Sua vez

Que informaçêo falta para transformar o relatório do exemplo em evidência de adoçêo do Jev?

<details>
<summary>Conferir resposta comentada</summary>

Execuçêo real do Jev e alternativas, dados representativos revisados, política calibrada em conjunto separado, métricas finais e custo completo do fluxo.

</details>

## Aula 12.3 — Decidir adoçêo

A última etapa é uma decisêo de projeto. Há três saídas legítimas: continuar com uma implantaçêo limitada, coletar mais dados ou nêo adotar. A escolha depende de qualidade, custo, cobertura, esforço de revisêo e capacidade operacional, nêo da popularidade do modelo.

Se decidir continuar, limite a primeira rota a uma açêo reversível e acompanhe as correções. Se decidir coletar mais dados, diga exatamente qual dúvida falta resolver: uma classe rara, um idioma, um tipo de ambiguidade ou a diferença de custo. Se decidir nêo adotar, preserve a avaliaçêo para evitar repetir o mesmo experimento sem aprender.

O princípio que atravessa o curso é simples: interpretaçêo probabilística funciona melhor dentro de software que conhece seus limites. Modelos ajudam a julgar; critérios e evidências permitem avaliar; código restringe a execuçêo; pessoas assumem as decisões que exigem responsabilidade. Uma arquitetura bem definida vale mais do que uma promessa isolada de velocidade.

### Aprofundamento da versêo 1.2.0

No projeto final, entregue um report.json e a análise dos erros, ou identifique claramente por que o resultado ainda é simulado. Defender coletar mais dados ou nêo adotar é uma conclusêo válida. Qualidade, custo completo e cobertura devem sustentar a decisêo.

### Prática com os recursos atuais

Escolha um dos 17 pacotes como ponto de partida, sem confundir template executável com conector pronto. O piloto deve declarar quem coleta os eventos, quem revisa, onde ficam os registros, como medir descartes incorretos e quem autoriza ações. Mil classificações rápidas nêo demonstram mil decisões corretas.

### Exemplo resolvido

Decisêo possível: manter regras para casos exatos, observar Jev nos demais e exigir revisêo até obter evidência suficiente em português.

### Sua vez

Dê uma condiçêo objetiva para cada saída: continuar, coletar mais dados e nêo adotar.

<details>
<summary>Conferir resposta comentada</summary>

Continuar: metas demonstradas com volume suficiente. Coletar: resultado inconclusivo em classes importantes. Nêo adotar: qualidade ou custo total nêo justificam a mudança após teste adequado.

</details>

[Voltar ao índice](../README.md)
