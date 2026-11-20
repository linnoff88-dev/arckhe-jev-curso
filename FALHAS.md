# Falhas corrigidas

| 2026-09-20 | Leitura sem clicar em marcar-lido não salvava o ponto atual | Salvar a âncora quando o tópico entra no scrollspy | infra |

| 2026-09-20 | Jornada e tema no cabeçalho não recebiam eventos; extração do head incluía comentário | Delegar cliques no body e extrair a tag real do snippet | prompt + infra |

| 2026-09-20 | Camada v2 não retomava módulo externo e descartava campos adicionais na exportação | Navegar pelo manifesto e preservar extras validados | infra |

| data | o que quebrou | menor correção | prompt / infra |
|---|---|---|---|
| 2026-09-21 | Palavra longa no título do módulo 3-1 extrapolava celular em PT/ES | Permitir quebra e hifenização no h1 | infra |
| 2026-09-21 | Tradução alterou diretório exemplos/ em comando textual de EN/ES | Restaurar caminho literal em revisão e validar tokens técnicos | prompt |
| 2026-09-18 | verificação Git acusou finais CRLF dos CSVs | padronizar arquivos e exportador em LF | infra |
