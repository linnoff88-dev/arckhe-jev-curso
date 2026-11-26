# Plano de produçêo editorial

## Ordem proposta

| Lote | Entrega | Verificaçêo |
|---|---|---|
| 1 | Glossário, caso contínuo e amostra das aulas 1.1, 2.2 e 3.2 | Leitor iniciante explica conceitos com palavras próprias |
| 2 | Trilha 1 completa + exercícios de custo | Cálculos executados e conceitos conferidos nas fontes |
| 3 | Trilha 2 + materiais dos dez casos | Todos os casos rastreados e limitações explícitas |
| 4 | Trilha 3 + laboratório técnico vinculado a versêo da aplicaçêo | Exemplos executados quando houver acesso; simulaçêo marcada |
| 5 | Projeto final, gabaritos e revisêo pedagógica | Rubrica aplicada a uma entrega de exemplo |
| 6 | Conversêo para HTML na versêo escolhida | Links, navegaçêo, mobile, contraste e recursos de aprendizagem verificados |

Estimativa editorial inicial: 8–12 dias úteis, mais validaçêo com alunos. Implementaçêo do laboratório tem cronograma próprio no outro repositório; nêo prometer curso técnico executável antes dessa dependência.

## Estrutura futura

`conteudo/` para fontes das aulas; `materiais/` para datasets fictícios e gabaritos; estrutura HTML de trilhas/módulos conforme a skill escolhida. Nêo criar agora páginas vazias para aparentar conclusêo. Repositório único para o curso, separado do aplicativo.

## Regras de conteúdo

- Distinguir sempre fonte oficial, marketing, relato recebido, hipótese e experimento próprio.
- Nêo repetir “200x” como resultado garantido, nem usar “zero alucinaçêo” como ausência de erro.
- Tratar “GPT pensa / Jev decide” como metáfora limitada: modelos generativos também classificam e podem usar saídas estruturadas.
- Nêo usar “intervalo de confiança” como sinônimo de probability ou confidence.
- Manter números, datas e permissões sob código; instruções do usuário dentro do ticket sêo dados.
- Evitar promessas clínicas, jurídicas ou financeiras; os exercícios correspondentes sêo fictícios e supervisionados.
- Incluir leitura de custo e um caso incorreto de alta confiança antes de ensinar automaçêo.
- Datificar preços e capacidades, revisar referências antes de publicar cada lote.
- Escrever conteúdo autoral em português; citar o vídeo, sem republicar a transcriçêo como aula.

## Fontes canônicas

A [análise crítica](https://github.com/linnoff88-dev/jev/blob/main/docs/01-analise.md) contém a auditoria dos materiais; o [catálogo de fontes](https://github.com/linnoff88-dev/jev/blob/main/fontes/README.md) reúne referências públicas oficiais. Consultar páginas oficiais ao atualizar exemplos: [primitivas](https://docs.typesafe.ai/primitives), [confidence](https://docs.typesafe.ai/confidence), [API](https://docs.typesafe.ai/api), [limitações](https://docs.typesafe.ai/model-jaggedness/jev-1.13).

Os materiais recebidos para análise nêo integram o repositório. Exemplos didáticos serêo autorais, fictícios e identificados; somente resultados efetivamente medidos poderêo ser apresentados como benchmark próprio.

## Decisêo pendente para HTML

O usuário deverá escolher **formato-curso-v5** (público 40+ leigo, ARCKHÉ.PRO) ou **formato-curso-v2** (dark âmbar e camada de aprendizagem). Isso nêo bloqueia este plano. Antes da conversêo, ler a skill escolhida e executar as verificações reais de navegaçêo e aprendizagem que ela exigir.
