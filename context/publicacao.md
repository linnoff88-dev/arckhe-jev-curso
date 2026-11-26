# Publicaçêo verificada — 18/09/2026

- Aplicaçêo: https://inematds.github.io/jev/guia/ (HTTP 200).
- Laboratório: https://inematds.github.io/jev/app/.
- Curso com 36 aulas e oito laboratórios em Markdown: https://github.com/inematds/jev-curso.
- Portal/PRO: ambos cadastrados; curso indica explicitamente formato Markdown. A versêo HTML aguarda resposta do usuário à escolha v5/v2, enviada nesta sessêo.

Pushes confirmados: aplicaçêo `4078bb2`, curso `8c64a88`, portal `78fa905`, inemabuscas `6dd5c9a`, INEMAPRO `9d0011b`.

Verificaçêo: 14 testes Python; fluxo de navegador desktop/mobile; revisêo visual aprovada; build portal, TypeScript e 7 testes; 41 testes da base; classificaçêo das duas entradas confirmada. Workflow Pages concluído. Nenhuma consulta ao Vercel.

Limite: sem TYPESAFE_API_KEY nos arquivos autorizados. O cliente real tem validaçêo e retries testados com respostas controladas; nenhuma qualidade ou latência Jev real foi medida. Dataset de referência contém 24 tickets fictícios; baseline lexical 20 acertos. Materiais recebidos nunca foram versionados.

## Continuidade técnica

Publicaçêo dos catálogos foi isolada em `/tmp/jev-publicacao/{portal,inemabuscas,inemapro-mono}` por ediçêo concorrente de outro curso. Ramos `publish-jev-20260918` foram enviados ao main remoto com integraçêo das atualizações concorrentes. Os diretórios originais com alterações existentes foram preservados.

ATENÇêO: no inemabuscas, o remote `origin` aponta para outro projeto (INEMAPRO). O destino correto é o remote `inemabuscas`, upstream `inemabuscas/main`. Nêo usar origin nesse repo.

Ao escolher a versêo visual do curso: ler a skill correspondente, gerar HTML a partir de `conteudo/curso.json`, verificar aprendizagem/navegaçêo e publicar Pages. Atualizar a URL do card e migrar enrichment de `curso:inematds-jev-curso` para o ID derivado da nova URL, preservando relacionados.

## Atualizaçêo de evidência — 19/09/2026

O limite histórico de credencial acima foi superado no projeto Jev: dez consultas reais por OpenRouter foram registradas. O curso v1.3.0 documenta essa integraçêo e os 17 pacotes; sete novos pacotes têm apenas testes controlados. Nêo há benchmark independente.

## Curso HTML v2 — 20/09/2026

Push inicial 6d4bdaf. As 18 páginas responderam HTTP 200 com v1.4.0 no GitHub Pages. Checagem estática preserva 36 aulas e 72 etapas. Teste de navegador cobre notas, temas, progresso, dúvidas, quiz, retomada, importaçêo, roteiro, prévia, celular, armazenamento bloqueado e leitura sem JavaScript. Nêo foram feitas novas chamadas Jev reais.
