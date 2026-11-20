# Roteiro complementar — da pergunta ao fluxo

Acompanha o curso v1.3.0 e o projeto Jev v1.6.1. Execute os comandos na raiz do clone **jev**, não no clone do curso. Este roteiro complementa as 36 aulas e os 12 laboratórios.

## 1. Escolha o problema

O projeto tem 17 pacotes: os dez iniciais e sete novos para caixa de entrada, comentários do YouTube, comunidades, reuniões, cortes por transcrição, notas e curadoria.

```bash
git clone https://github.com/inematds/jev.git
cd jev
python3 -m pacotes.executar --list
python3 -m pacotes.executar reunioes
```

Identifique a decisão principal e as perguntas auxiliares. No pacote de reuniões, pergunte se há decisão, próximo passo, responsável e prazo. Não confunda “há um responsável” com extrair seu nome, nem “há prazo” com calcular uma data.

**Exercício:** “Precisamos melhorar o tutorial; conversamos depois.” É suficiente para criar uma tarefa atribuída e agendada?

**Resposta:** não. Pode indicar intenção, mas falta encaminhamento explícito. Jev classifica sinais; a aplicação ainda precisa confirmar a tarefa e resolver calendário.

## 2. Leia as métricas de todas as perguntas

```bash
python3 -m pacotes.qualidade reunioes
python3 -m pacotes.qualidade cortes
```

Esses comandos usam fixtures inventadas e referências autorais. Confira `origins: ["simulation"]`. Choice mede acerto de rótulo; Noul mede acurácia e Brier; Score mede erro absoluto e erro normalizado. O relatório também mostra cobertura e erros.

**Exercício:** se houver erro de contrato em metade dos registros, basta mostrar Brier baixo nos restantes?

**Resposta:** não. Brier considera respostas válidas, mas a cobertura caiu. Falhas permanecem no denominador da acurácia. Apresentar só o subconjunto válido esconderia problemas operacionais.

## 3. Prepare um lote sem consumir API

```bash
python3 -m pacotes.lote reunioes data/reunioes-eventos.jsonl
```

Confira `mode: preview` e `calls: 0`. Cada linha contém `id` e `state`. O executor recusa IDs duplicados e entradas inválidas antes de consultar o provedor. Não precisa de banco ou serviço de filas para esse exercício.

**Exercício:** dois eventos com o mesmo ID e textos diferentes podem ser tratados como a mesma ocorrência?

**Resposta:** não neste lote; o executor os rejeita. Corrija a identificação na origem antes de enviar.

## 4. Entenda a passagem ao modo real

Com chave configurada no backend e dados autorizados:

```bash
python3 -m pacotes.lote reunioes data/reunioes-eventos.jsonl --live --provider openrouter --workers 2 --interval 1 --out runs/reunioes.jsonl
```

O modo real envia dados e consome créditos. Repetir o mesmo comando retoma resultados gravados, incluindo erros. Queda entre resposta e gravação ainda pode repetir consumo; não há garantia de cobrança única. Não modifique o lote ou o template para reutilizar o mesmo checkpoint.

O intervalo controla o início das consultas, não cada retry interno. Compare concorrência e condições equivalentes ao avaliar velocidade. Um lote rápido não comprova qualidade, calibração ou ganho universal.

## 5. Faça a entrega do piloto

Defina, com referência humana independente:

- Perguntas e alternativas, inclusive insuficiência.
- Dados mínimos e autorização de envio.
- Rótulos esperados por pergunta, sem copiar a previsão do modelo.
- Métricas de qualidade, cobertura, custo completo e latência.
- Revisão de falsos negativos entre itens descartados.
- Critério para adotar, coletar mais evidência ou não automatizar.

Para Codex e Claude Code, a skill `jev-decidir` consulta o cliente como ferramenta. No OpenPCBot v3, `/jev observar` usa o gateway próprio e só compara sugestões; `/ajuda jev` explica o recurso. Os pacotes de notas e reuniões ainda não são novos comandos nativos do bot.

[Instruções completas de integração e formato de referência](https://github.com/inematds/jev/blob/main/docs/11-fluxos-praticos.md) · [Pacotes](https://github.com/inematds/jev/tree/main/pacotes) · [Voltar ao curso](../README.md).
