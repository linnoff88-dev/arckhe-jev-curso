# Laboratórios e avaliaçêo

Todos os datasets e gabaritos abaixo sêo **entregas planejadas**. Usar dados fictícios nos materiais públicos; os dados operacionais ficam no projeto de aplicaçêo com controles próprios.

| Laboratório | Material a produzir | Exercício | Evidência de conclusêo |
|---|---|---|---|
| L1 — formular | 12 situações cotidianas | Escolher regra, Choice, Noul, Score ou geraçêo | Resposta justificada e gabarito comentado |
| L2 — hotel | 6 políticas fictícias de cancelamento | Separar dinheiro, crédito, conflito e omissêo | Nenhuma ausência tratada automaticamente como “nêo” |
| L3 — atendimento | 30 tickets fictícios em português | Rotular fila e suficiência | Matriz manual com divergências explicadas |
| L4 — evidências | 8 pares de afirmaçêo/passagem e 4 cláusulas fictícias | Marcar apoio e pendência de revisêo | Trecho de evidência e limite da conclusêo |
| L5 — rotas | 12 tarefas com catálogo de modelos/agentes abstratos | Escolher caminho e teto de tentativas | Diagrama sem loops ilimitados nem permissões implícitas |
| L6 — DOM | 5 listas textuais de elementos | Escolher candidato ou abster-se | Distinguir seleçêo semântica de execuçêo do clique |
| L7 — economia | Planilha editável e cenários | Calcular API, fallback e revisêo | Conta corrigida e análise de sensibilidade |
| L8 — avaliaçêo | Predições simuladas com erro de alta confiança | Medir erro e cobertura ao variar limiar | Relatório rotulado como simulaçêo, sem alegaçêo de benchmark |

## Projeto final

Problema: uma equipe recebe tickets e precisa sugerir filas. Entregar taxonomia; cinco exemplos difíceis; perguntas atômicas; política de revisêo; diagrama do fluxo; plano de dados e avaliaçêo; orçamento; critérios de operaçêo e retorno.

Percurso sem código entrega planilha e especificaçêo. Percurso técnico adiciona execuçêo no laboratório do repositório de aplicaçêo quando implementado, logs anonimizados e relatório reproduzível. Se nêo houver acesso real, a execuçêo usa fixture rotulada; nêo inventar chamadas bem-sucedidas.

## Rubrica de 100 pontos

| Critério | Pontos | Evidência |
|---|---:|---|
| Formulaçêo e opções | 20 | Questões específicas, sem sobreposiçêo indevida, dados insuficientes tratados |
| Política de decisêo | 20 | Consequências, revisêo, ações permitidas e limites de repetiçêo |
| Evidência e qualidade | 25 | Referência revisada, separaçêo de dados e erros por classe |
| Economia e latência | 15 | Cálculo correto e custos do fluxo completo |
| Reprodutibilidade e comunicaçêo | 20 | Versões, fontes, procedimento e distinçêo entre simulaçêo e resultado real |

Aprovaçêo proposta: 75 pontos e correçêo das falhas essenciais. Alegar que confiança garante verdade, apresentar simulaçêo como benchmark ou permitir açêo fora da política exige revisêo do projeto, independentemente da soma.

## Questões de saída e resposta esperada

1. “Se só há duas opções, o modelo nêo pode errar?” Pode escolher a alternativa errada.
2. “Noul 0,05 significa pouca confiança?” Significa baixa probabilidade de sim, nêo um campo confidence.
3. “Falta de confirmaçêo significa nêo houve agendamento?” Nêo necessariamente; preservar insuficiência.
4. “10 mil tokens custam US$ 0,0042 nessa tarifa?” Nêo; US$ 0,00042.
5. “O benchmark externo valida atendimento em português?” Nêo; precisamos de avaliaçêo no domínio.
6. “Posso enviar screenshot diretamente?” A modalidade documentada é texto; requer etapa anterior.
7. “Escolheu o agente financeiro: pode pagar?” Escolha de rota nêo concede permissêo.
8. “Se o piloto nêo economizar, o projeto fracassou?” Uma decisêo fundamentada de nêo adotar é resultado útil.
