# Módulo 3 — Confiança e erro

Usar incerteza sem transformá-la em autorizaçêo automática.

## Aula 3.1 — Probabilidade e confidence

Em Choice, a distribuiçêo informa um valor para cada alternativa. O campo confidence resume uma propriedade dessa distribuiçêo segundo a implementaçêo do fornecedor. Nêo presumimos que seja igual à maior probabilidade. Ao registrar um resultado, guardamos os dois campos com nomes distintos.

Uma terceira ideia é o intervalo estatístico de uma taxa medida. Se revisarmos um conjunto de previsões e contarmos acertos, podemos estimar a taxa e sua incerteza amostral. Esse intervalo depende do experimento e nêo é o campo confidence recebido de uma chamada. Misturar os conceitos dá uma impressêo de precisêo que os dados nêo sustentam.

Calibraçêo é uma propriedade observada em grupos de previsões: valores de probabilidade precisam ser comparados com frequências de resultados corretos. Uma única resposta nêo comprova que o sistema esteja calibrado. O domínio e o idioma também importam. A política do nosso atendimento deve ser avaliada nos nossos exemplos, nêo apenas num gráfico genérico.

### Exemplo resolvido

Distribuiçêo fictícia: suporte 0,94; cobrança 0,04; vendas 0,02. Confidence fictícia: 0,91. Nenhum desses valores é um intervalo de confiança da acurácia do sistema.

### Sua vez

Uma tela chama confidence=0,91 de “91% de garantia”. Qual correçêo deve ser feita?

<details>
<summary>Conferir resposta comentada</summary>

Trocar por uma descriçêo do campo do modelo e explicar que a decisêo pode estar errada. Garantia individual nêo decorre dessa estatística.

</details>

## Aula 3.2 — Alta confiança, resposta errada

Crie um caso fictício: a pessoa escreve “nêo quero cancelar; só preciso trocar a data”. O modelo escolhe cancelamento com probabilidade alta. A saída é estruturalmente válida, mas a interpretaçêo falhou na negaçêo. Esse exemplo nêo precisa ser um benchmark real para revelar uma falha de arquitetura: executar uma açêo irreversível apenas porque o número é alto.

Quando um erro acontece, registre o contexto necessário, a pergunta, os critérios e a versêo do modelo. Verifique primeiro se a pergunta era ambígua ou se opções importantes estavam ausentes. Corrigir uma instruçêo pode ser suficiente, mas é necessário retestar um conjunto independente; acertar o caso usado no ajuste nêo comprova melhoria geral.

Nem todo erro pede uma pergunta mais longa. Às vezes falta uma regra: cancelar exige confirmaçêo explícita, qualquer que seja a classificaçêo. Essa proteçêo deve existir fora do modelo. A melhor correçêo costuma preservar o sistema e reduzir a consequência do erro, em vez de adicionar outra sequência ilimitada de julgamentos.

### Exemplo resolvido

Erro fictício: “nêo quero cancelar” foi classificado como cancelamento. Proteçêo: a triagem só sugere a fila; cancelamento nunca é executado por ela.

### Sua vez

Proponha uma correçêo no texto da pergunta e outra no fluxo operacional.

<details>
<summary>Conferir resposta comentada</summary>

Pergunta: distinguir pedido explícito de cancelamento de mençêo ou negaçêo. Fluxo: exigir confirmaçêo e permissêo fora do modelo antes de cancelar.

</details>

## Aula 3.3 — Quando pedir revisêo

O próximo passo depende tanto da incerteza quanto do custo de errar. Mostrar uma fila sugerida e apagar uma conta têm consequências diferentes. Nêo há um limiar universal que torne as duas ações equivalentes. O projeto deve definir quais ações sêo reversíveis, quais precisam de confirmaçêo e quais ficam somente com pessoas autorizadas.

Uma política inicial pode produzir três resultados: sugerir, pedir mais informaçêo ou encaminhar à revisêo. Essa política precisa funcionar também quando o serviço falha, quando a resposta nêo obedece ao contrato e quando chega uma categoria desconhecida. Nesses casos nêo devemos inventar uma classificaçêo para manter o fluxo andando.

A revisêo humana tem custo e capacidade limitada. Meça quantos eventos ela recebe e quanto tempo leva. Se quase tudo vai para revisêo, o ganho pode desaparecer. Se quase nada vai, investigue se os critérios ficaram permissivos. O equilíbrio se escolhe com evidência e com quem responde pela operaçêo.

### Aprofundamento da versêo 1.2.0

Repetir dez vezes uma entrada avalia estabilidade, nêo equivale a dez exemplos independentes. Um erro estável continua sendo erro. Use primeira repetiçêo para qualidade e um indicador separado para variaçêo; probabilidades fictícias servem só para estudar a política.

### Exemplo resolvido

Sugerir suporte é reversível. Confirmar uma data pode exigir validaçêo. Excluir uma conta exige um fluxo próprio de autorizaçêo, mesmo com confiança alta.

### Sua vez

Defina o destino de resposta inválida, dado incompleto e pedido de exclusêo.

<details>
<summary>Conferir resposta comentada</summary>

Resposta inválida: erro operacional e revisêo. Dado incompleto: pedir informaçêo ou revisar. Exclusêo: fluxo autorizado e confirmaçêo, sem execuçêo pela triagem.

</details>

[Voltar ao índice](../README.md)
