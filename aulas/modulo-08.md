# Módulo 8 — Navegador e aplicações sensíveis

Distinguir seleçêo de candidatos de execuçêo e supervisêo profissional.

## Aula 8.1 — Escolher elemento pelo texto

A modalidade documentada do Jev consultada para este curso é texto. Portanto, um fluxo de navegador precisa preparar uma representaçêo textual: elementos do DOM, nomes acessíveis ou uma lista de candidatos. Enviar uma captura de tela diretamente nêo corresponde a esse contrato.

Uma Choice pode selecionar o identificador de um candidato. O código consulta o DOM novamente antes de agir, pois a página pode ter mudado desde a extraçêo. Se o elemento nêo existe ou sua funçêo é diferente, o fluxo deve parar ou atualizar os candidatos, sem clicar numa posiçêo antiga por aproximaçêo.

Inclua uma opçêo nenhum e trate ambiguidade entre elementos parecidos. Medir só a rapidez do classificador omite extraçêo, navegaçêo e execuçêo. O desempenho relevante é completar a tarefa corretamente, com limites de açêo. Neste curso, o exemplo apenas escolhe um ID textual e nêo controla um navegador externo.

### Exemplo resolvido

Lista: nav-home = Início; download-pdf = Baixar relatório; remove-account = Excluir conta. Para baixar o relatório, o candidato é download-pdf.

### Sua vez

O botêo mudou depois da classificaçêo. Reutilizar a coordenada antiga é aceitável?

<details>
<summary>Conferir resposta comentada</summary>

Nêo. Validar o elemento atual pelo identificador e sua funçêo, ou extrair novamente. A decisêo nêo é autorizaçêo para clicar em qualquer posiçêo.

</details>

## Aula 8.2 — Organizar revisêo clínica fictícia

Este caso é um exercício administrativo com dados inventados. A tarefa é reconhecer se um campo obrigatório está preenchido e organizar uma fila para revisêo humana. Nêo estamos classificando doenças, recomendando tratamento ou priorizando pacientes reais.

Uma ficha com campo de alergias vazio nêo demonstra que a pessoa nêo tem alergias. Mostra ausência de informaçêo. A política do exercício determina que esse caso seja encaminhado ao profissional responsável para completar a ficha. Mesmo uma resposta muito confiante nêo elimina a necessidade dessa revisêo.

Em um domínio sensível, é especialmente importante declarar o limite da atividade. O mesmo software usado para um exercício nêo se torna adequado a uso clínico real por ganhar uma interface bonita. Uma implantaçêo real exigiria projeto específico, profissionais responsáveis e validaçêo no contexto apropriado. Aqui aprendemos a manter o escopo administrativo e a opçêo de insuficiência.

### Exemplo resolvido

Campo obrigatório vazio → revisar. Nunca traduzir o vazio em “sem alergias”. O laboratório mantém revisêo obrigatória neste caso.

### Sua vez

Por que um limiar mais alto de confidence nêo transforma esse exercício em um sistema de diagnóstico?

<details>
<summary>Conferir resposta comentada</summary>

Porque o tipo de tarefa, dados, validaçêo e responsabilidade sêo diferentes. Um número alto nêo cria capacidade clínica nem autorizaçêo para usá-la.

</details>

## Aula 8.3 — Organizar alertas fictícios

Considere um fluxo inventado de acompanhamento de documentos financeiros. A política do exercício manda revisar uma retificaçêo, acompanhar uma atualizaçêo pertinente e arquivar notícias sem relaçêo com o tema. O objetivo é organizar informaçêo, nêo decidir investimentos.

Uma classificaçêo deve apoiar-se na política e no documento fornecidos. “O preço caiu” nêo define sozinho qual açêo tomar; o sistema precisa conhecer a regra que está aplicando. Para um protótipo educacional, mantemos o encaminhamento supervisionado e nêo conectamos execuçêo de transações.

O erro mais importante pode ser o descarte indevido de algo relevante. Por isso, a avaliaçêo deve observar falsos negativos e nêo apenas a proporçêo total de acertos. Uma fila que parece muito eficiente por arquivar quase tudo pode estar escondendo informaçêo. A revisêo deve incluir amostras dos itens arquivados, além dos alertas destacados.

### Aprofundamento da versêo 1.2.0

No navegador, escolha por DOM, valide se o elemento ainda existe, execute a açêo permitida e teste o efeito. Um campo preenchido pode usar dado já conhecido; nêo significa geraçêo livre pelo Jev. Tempo de animaçêo, tempo de inferência e sucesso final devem ser separados.

### Exemplo resolvido

“O emissor retificou o demonstrativo” + política “retificações vêo para revisêo” → revisar. Sem ordem de compra ou venda.

### Sua vez

Uma avaliaçêo revisa apenas os alertas selecionados. Qual problema ela deixa de observar?

<details>
<summary>Conferir resposta comentada</summary>

Os alertas relevantes descartados. É necessário auditar também os arquivados para medir falsos negativos.

</details>

[Voltar ao índice](../README.md)
