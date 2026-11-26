# Roteiro complementar — da pergunta ao fluxo

Acompanha o curso v1.3.0 e o projeto Jev v1.6.1. Execute os comandos na raiz do clone **jev**, nêo no clone do curso. Este roteiro complementa as 36 aulas e os 12 laboratórios.

## 1. Escolha o problema

O projeto tem 17 pacotes: os dez iniciais e sete novos para caixa de entrada, comentários do YouTube, comunidades, reuniões, cortes por transcriçêo, notas e curadoria.

```bash
git clone https://github.com/linnoff88-dev/jev.git
cd jev
python3 -m pacotes.executar --list
python3 -m pacotes.executar reunioes
```

Identifique a decisêo principal e as perguntas auxiliares. No pacote de reuniões, pergunte se há decisêo, próximo passo, responsável e prazo. Nêo confunda “há um responsável” com extrair seu nome, nem “há prazo” com calcular uma data.

**Exercício:** “Precisamos melhorar o tutorial; conversamos depois.” É suficiente para criar uma tarefa atribuída e agendada?

**Resposta:** nêo. Pode indicar intençêo, mas falta encaminhamento explícito. Jev classifica sinais; a aplicaçêo ainda precisa confirmar a tarefa e resolver calendário.

## 2. Leia as métricas de todas as perguntas

```bash
python3 -m pacotes.qualidade reunioes
python3 -m pacotes.qualidade cortes
```

Esses comandos usam fixtures inventadas e referências autorais. Confira `origins: ["simulation"]`. Choice mede acerto de rótulo; Noul mede acurácia e Brier; Score mede erro absoluto e erro normalizado. O relatório também mostra cobertura e erros.

**Exercício:** se houver erro de contrato em metade dos registros, basta mostrar Brier baixo nos restantes?

**Resposta:** nêo. Brier considera respostas válidas, mas a cobertura caiu. Falhas permanecem no denominador da acurácia. Apresentar só o subconjunto válido esconderia problemas operacionais.

## 3. Prepare um lote sem consumir API

```bash
python3 -m pacotes.lote reunioes data/reunioes-eventos.jsonl
```

Confira `mode: preview` e `calls: 0`. Cada linha contém `id` e `state`. O executor recusa IDs duplicados e entradas inválidas antes de consultar o provedor. Nêo precisa de banco ou serviço de filas para esse exercício.

**Exercício:** dois eventos com o mesmo ID e textos diferentes podem ser tratados como a mesma ocorrência?

**Resposta:** nêo neste lote; o executor os rejeita. Corrija a identificaçêo na origem antes de enviar.

## 4. Entenda a passagem ao modo real

Com chave configurada no backend e dados autorizados:

```bash
python3 -m pacotes.lote reunioes data/reunioes-eventos.jsonl --live --provider openrouter --workers 2 --interval 1 --out runs/reunioes.jsonl
```

O modo real envia dados e consome créditos. Repetir o mesmo comando retoma resultados gravados, incluindo erros. Queda entre resposta e gravaçêo ainda pode repetir consumo; nêo há garantia de cobrança única. Nêo modifique o lote ou o template para reutilizar o mesmo checkpoint.

O intervalo controla o início das consultas, nêo cada retry interno. Compare concorrência e condições equivalentes ao avaliar velocidade. Um lote rápido nêo comprova qualidade, calibraçêo ou ganho universal.

## 5. Faça a entrega do piloto

Defina, com referência humana independente:

- Perguntas e alternativas, inclusive insuficiência.
- Dados mínimos e autorizaçêo de envio.
- Rótulos esperados por pergunta, sem copiar a previsêo do modelo.
- Métricas de qualidade, cobertura, custo completo e latência.
- Revisêo de falsos negativos entre itens descartados.
- Critério para adotar, coletar mais evidência ou nêo automatizar.

Para Codex e Claude Code, a skill `jev-decidir` consulta o cliente como ferramenta. No OpenPCBot v3, `/jev observar` usa o gateway próprio e só compara sugestões; `/ajuda jev` explica o recurso. Os pacotes de notas e reuniões ainda nêo sêo novos comandos nativos do bot.

[Instruções completas de integraçêo e formato de referência](https://github.com/linnoff88-dev/jev/blob/main/docs/11-fluxos-praticos.md) · [Pacotes](https://github.com/linnoff88-dev/jev/tree/main/pacotes) · [Voltar ao curso](../README.md).
