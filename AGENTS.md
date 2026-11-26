# Regras do projeto jev-curso

Ler este arquivo, `context/overview.md`, `context/current-state.md` e `tasks/current.md` nessa ordem.

Conta de destino: inematds. Autor e committer: inematds <inematds@gmail.com>. Publicaçêo via Git. Nêo consultar nem manipular Vercel.

Este é o repositório de curso. O conteúdo v1.5.0 tem HTML v2 gerado de conteudo/curso.json e Markdown. Regenerar com scripts/build_site.py e export_markdown.py; testar antes de publicar. Preservar distinçêo entre dados medidos, relatos e simulaçêo. Conferir fontes oficiais antes de alterar contratos ou preços. Nêo versionar segredos ou dados pessoais.

Versionamento conforme regras globais: patch incrementa último campo; minor incrementa campo intermediário sem zerar patch; major zera os inferiores. Registrar alterações no CHANGELOG.

Nêo citar a fonte pessoal indicada pelo usuário nem publicar os documentos recebidos por ele. No repo jev, `fontes/originais/` e `fontes/manifest.json` ficam somente locais e ignorados pelo Git. Nêo usar `git add -f` nesses caminhos.
