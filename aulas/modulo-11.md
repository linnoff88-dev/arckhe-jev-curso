# Módulo 11 — Operar e observar

Preparar logs, acompanhamento e retorno sem perder controle da operaçêo.

## Aula 11.1 — Observar antes de automatizar

Modo de observaçêo significa que a nova etapa calcula uma sugestêo, mas o fluxo anterior continua responsável pela decisêo. Assim podemos comparar o comportamento com a operaçêo real sem aplicar automaticamente os erros do piloto.

Registre concordâncias e desacordos. Revisar somente desacordos nêo basta, porque humano e modelo podem concordar numa resposta errada. Inspecione também uma amostra de concordâncias. Observe o volume de cada classe e as mensagens que nêo cabem na taxonomia.

Defina a saída dessa fase antes de começar. Precisêo, cobertura, custo, tempo de revisêo e ausência de falhas de integraçêo podem fazer parte dos critérios. Se as metas nêo forem demonstradas, mantenha a observaçêo ou encerre o teste. Automatizar porque “já está há uma semana rodando” nêo é um critério de qualidade.

### Prática com os recursos atuais

Para experimentar sem chave na raiz do repo jev: python3 -m pacotes.executar reunioes; python3 -m pacotes.qualidade reunioes; python3 -m pacotes.lote reunioes data/reunioes-eventos.jsonl. Os dois primeiros usam dados e respostas simulados; o terceiro faz somente prévia. O roteiro complementar detalha a passagem a dados próprios.

### Exemplo resolvido

A equipe recebe a fila sugerida ao lado do encaminhamento atual. Nenhuma mudança externa acontece apenas pela resposta do modelo.

### Sua vez

Um piloto teve poucos eventos da classe cobrança. É suficiente liberar todas as filas?

<details>
<summary>Conferir resposta comentada</summary>

Nêo necessariamente. Pode faltar evidência nessa classe. Coletar mais exemplos ou limitar a liberaçêo às rotas efetivamente avaliadas.

</details>

## Aula 11.2 — Registrar e entender falhas

Um log útil liga o evento à versêo da pergunta, à política e ao modelo usado. Também registra tempo, tokens, resultado e eventual correçêo. Sem essas informações, é difícil saber se uma mudança de comportamento veio do modelo, do contexto ou de uma alteraçêo no código.

Nêo confunda rastreabilidade com guardar tudo para sempre. Minimize dados, limite acesso e defina retençêo conforme o ambiente real. Para relatórios públicos, use exemplos fictícios ou autorizados. Credenciais nunca entram no log.

Ao corrigir um erro, procure a menor proteçêo suficiente. Campo ausente pode pedir validaçêo; duplicata pode pedir idempotência; loop pode pedir um teto; decisêo incorreta pode pedir critérios mais claros e novo teste. A categoria da falha ajuda: qualidade do julgamento, preparaçêo do contexto, contrato, rede ou política operacional.

### Prática com os recursos atuais

Um lote pode usar de um a quatro workers e espaçar o início das consultas. Esse espaçamento nêo controla cada retry HTTP e nêo substitui um limite distribuído por tokens. Limite de eventos nêo é orçamento em dólares. Depois de retries, preserve custo desconhecido quando só o consumo da última resposta estiver disponível.

### Exemplo resolvido

Evento 42: pergunta v2, política v1, modelo fixado, resposta válida, sugestêo corrigida de vendas para suporte. O texto sensível fica fora do relatório público.

### Sua vez

Um retry processa duas vezes o mesmo ticket. Reescrever a pergunta resolve?

<details>
<summary>Conferir resposta comentada</summary>

Nêo. A correçêo é de execuçêo: identificador idempotente e controle de duplicatas, com teste que reproduza o retry.

</details>

## Aula 11.3 — Atualizar ou voltar atrás

Um alias de modelo pode apontar para uma nova versêo sem mudar a sua requisiçêo. Isso facilita atualizações, mas dificulta atribuir variaçêo quando limiares foram ajustados para uma versêo anterior. Registre o identificador resolvido e fixe versões nos experimentos que precisam ser reproduzidos.

Antes de trocar a versêo em operaçêo, rode o conjunto de avaliaçêo e compare os erros. Uma média melhor pode esconder regressêo numa classe importante. Se a política depender de confidence, verifique novamente os limiares e a cobertura.

Tenha uma forma simples de desativar a nova etapa e voltar ao fluxo anterior. O retorno nêo deve exigir reconstruir a aplicaçêo. Critérios de suspensêo incluem erro relevante, indisponibilidade persistente e custo inesperado. Atualizar é uma mudança controlada, nêo apenas substituir um nome na configuraçêo.

### Aprofundamento da versêo 1.2.0

Para triagem de código, separe comentário correto de comentário útil. O classificador pode apontar um teste enfraquecido, mas testes e análise estática continuam necessários. Amostre também o que o filtro descartou para descobrir falsos negativos. Pratique no L10.

### Exemplo resolvido

Nova versêo chega: avaliar com as mesmas perguntas e dados reservados; revisar métricas por classe; liberar gradualmente ou manter a versêo anterior.

### Sua vez

O que registrar para reproduzir uma decisêo depois de uma atualizaçêo?

<details>
<summary>Conferir resposta comentada</summary>

Modelo resolvido, versêo das perguntas e critérios, versêo da política e identificaçêo do contexto autorizado usado no evento.

</details>

[Voltar ao índice](../README.md)
