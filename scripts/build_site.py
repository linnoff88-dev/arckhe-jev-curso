"""Renderiza o curso v2 a partir das aulas autorais; sem dependências externas."""
from pathlib import Path
from html import escape as e
import json, re, shutil
R=Path(__file__).resolve().parents[1]
modules=json.loads((R/'conteudo/curso.json').read_text())
checks=json.loads((R/'conteudo/checagens.json').read_text())
tracks=['Entender','Aplicar','Construir e avaliar']
colors=['#34d399','#60a5fa','#a78bfa']

def para(text):
    # Fonte autoral: Markdown simples, escapado antes da marcaçêo.
    if text.startswith('### '):return '<h3>'+e(text[4:])+'</h3>'
    text=e(text)
    text=re.sub(r'`([^`]+)`',r'<code>\1</code>',text)
    text=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',text)
    return '<p>'+text+'</p>'

def identity(m):
    return f'{(m["number"]-1)//4+1}-{(m["number"]-1)%4+1}'
def path(m):return 'curso/trilha'+identity(m)[0]+'/modulo-'+identity(m)+'.html'
def meter(scope):return f'<div class="meter" data-inema-meter="{scope}"><span data-inema-meter-frac>0/72</span> etapas · <span data-inema-meter-pct>0%</span><div class="bar"><i data-inema-meter-fill></i></div></div>'

def diagram(uid,labels,color):
    parts=[f'<svg viewBox="0 0 760 156" role="img" aria-label="{e(" → ".join(labels))}"><defs><filter id="g{uid}"><feGaussianBlur stdDeviation="1.8"/></filter></defs>']
    for i,label in enumerate(labels):
        x=12+i*250
        parts.append(f'<rect x="{x}" y="36" width="236" height="78" rx="12" fill="none" stroke="{color}"/><text x="{x+118}" y="81" text-anchor="middle" fill="currentColor" font-size="18">{e(label)}</text>')
        if i<2:parts.append(f'<path d="M{x+236} 75h14" stroke="#22d3ee" stroke-width="3"/><circle cx="{x+243}" cy="75" r="3" fill="#22d3ee" filter="url(#g{uid})"/>')
    return '\n'.join(parts)+'</svg>'

def page(dest,title,body,track=None):
    rel='../'*len(Path(dest).parts[:-1]); manifest={'course':'jev-curso','tracks':[]}
    for i,t in enumerate(tracks):manifest['tracks'].append({'n':str(i+1),'title':t,'modules':[{'id':identity(m),'title':m['title'],'topics':6,'href':rel+path(m)} for m in modules[i*4:i*4+4]]})
    head=(R/'assets/head.html').read_text().replace('{rel}',rel)
    nav=''.join(f'<a href="{rel}curso/trilha{i+1}/index.html"><span class="desktop">{i+1}. {t}</span><span class="mobile">T{i+1}</span></a>' for i,t in enumerate(tracks))
    html=f'''<!doctype html><html lang="pt-BR" class="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">{head}
<title>{e(title)} · Jev na prática</title><meta name="inema-course" content="jev-curso"><meta name="description" content="Curso Jev: 36 aulas, exemplos resolvidos e prática guiada. Decisões estruturadas com avaliaçêo e limites explícitos."><link rel="stylesheet" href="{rel}assets/course.css"></head><body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a><header><nav aria-label="Navegaçêo principal"><a class="brand" href="{rel}index.html"><b>◈</b> INEMA.CLUB</a>{nav}<button data-inema-cycle="theme" aria-label="Alternar tema">◐ Tema</button><button data-inema-journey-open>Minha jornada <span data-inema-journey-badge></span></button></nav></header>
<main id="conteudo">{body}</main><footer><a href="{rel}index.html">Jev na prática</a> · v1.5.0 · <a href="https://inema.club">Portal</a> · <a href="https://inematds.github.io/jev/guia/">Projeto e pacotes</a> · <a href="https://docs.typesafe.ai/models">Modelos oficiais</a><p>Exemplos educacionais. Progresso e anotações ficam neste navegador; exporte sua jornada para guardar uma cópia. Nenhuma atividade chama API.</p></footer>
<script type="application/json" data-inema-manifest>{json.dumps(manifest,ensure_ascii=False)}</script><script src="{rel}assets/learn.js"></script><script src="{rel}assets/course.js"></script></body></html>'''
    p=R/dest;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(html)

def card(m,rel):
    mid=identity(m);url=rel+path(m)
    topics=''.join(f'<li><a href="{url}#topico-{i*2+1}">{e(l["title"])}</a><p><strong>O que é:</strong> {e(l["body"][0])}</p><p><strong>Por que aprender:</strong> {e(m["goal"])}</p><p><strong>Conceitos-chave:</strong> contexto, critérios e evidência aplicados à aula {l["id"]}.</p></li>' for i,l in enumerate(m['lessons']))
    return f'<article class="card" id="modulo-{mid}"><span class="eyebrow">Módulo {m["number"]:02} · 3 aulas · 6 etapas</span><h2>{e(m["title"])}</h2><p>{e(m["goal"])}</p>{meter("modulo:"+mid)}<details><summary>Explorar as aulas</summary><ol>{topics}</ol></details><div class="actions"><a class="button" href="{url}">Ver conteúdo completo →</a><button data-preview="{url}">Prévia em janela</button></div></article>'

intro='''<section class="hero"><span class="eyebrow">CURSO V2 · DECISÕES E AVALIAÇêO</span><h1>Uma decisêo melhor.<br><em>Um passo de cada vez.</em></h1><p class="lead">Aprenda a escolher onde usar Jev, desenhar critérios claros e testar o resultado antes de automatizar. Leve uma decisêo do seu trabalho do primeiro exemplo ao projeto final.</p><div class="actions"><a class="button" href="curso/trilha1/modulo-1-1.html">Começar a primeira aula →</a><a href="#trilhas">Explorar as trilhas</a></div><div class="stats"><span><b>36</b> aulas completas</span><span><b>12</b> laboratórios</span><span><b>3</b> trilhas progressivas</span><span><b>18h</b> percurso estimado</span></div></section>'''
body=intro+meter('curso')+'<section class="card"><h2>Estude do seu jeito</h2><p>Comece sem código nas trilhas 1 e 2. A trilha 3 usa JSON, terminal e Python. Cada aula tem explicaçêo e prática: sêo 72 etapas de leitura, sem aumentar as 36 aulas. Selecione texto para anotar, marque dúvidas e use Minha jornada para exportar seu progresso. Nêo há prova bloqueando a próxima aula.</p><p><a href="pratica.html">Abrir meu roteiro de decisêo</a> · <a href="materiais/index.html">Materiais e laboratórios</a></p></section><section id="trilhas"><h2>Escolha seu ponto de partida</h2><div class="grid">'
for i,t in enumerate(tracks):body+=f'<article class="card" style="--trail:{colors[i]}"><span class="eyebrow">TRILHA {i+1}</span><h2>{t}</h2><p>{["Entenda as perguntas, os erros e o custo completo.","Aplique os critérios em atendimento, documentos e agentes.","Integre, compare alternativas e desenhe um piloto supervisionado."][i]}</p>{meter("trilha:"+str(i+1))}<a class="button" href="curso/trilha{i+1}/index.html">Ver os quatro módulos →</a></article>'
body+='</div></section><section class="card"><h2>O que você terá ao final</h2><p>Uma decisêo especificada, casos de fronteira, uma referência humana separada do ajuste e uma política de observaçêo. Você também saberá reutilizar os 17 pacotes do projeto e distinguir demonstraçêo de evidência.</p><p>Os exemplos sêo fictícios. O curso nêo mede a qualidade do Jev em seus dados; ensina como fazer essa avaliaçêo.</p><a href="https://github.com/inematds/jev/blob/main/docs/12-piloto-e-composicao.md">Roteiro e composiçêo de pontuações no projeto</a></section>'
page('index.html','Jev na prática',body)

flows=[['Tarefa','Decisêo','Próximo passo'],['Contexto','Rubrica','Resposta'],['Previsêo','Referência','Erro'],['Entrada','Processo','Custo total'],['Mensagem','Intençêo','Equipe'],['Documento','Evidência','Revisêo'],['Pedido','Roteador','Especialista'],['Estado textual','Alternativas','Supervisor'],['Evento','Validaçêo','Registro'],['Referência','Teste separado','Métricas'],['Observaçêo','Revisêo','Adoçêo'],['Especificar','Avaliar','Decidir']]
for ti,t in enumerate(tracks):
    ms=modules[ti*4:ti*4+4]
    body=f'<section class="hero"><span class="eyebrow">TRILHA {ti+1} · 4 MÓDULOS</span><h1>{t}</h1><p class="lead">{e(ms[0]["goal"])}</p>{diagram("trilha"+str(ti),["Entender","Experimentar","Registrar"],colors[ti])}{meter("trilha:"+str(ti+1))}</section><h2>Mapa da trilha</h2><div class="map">'+''.join(f'<a href="#modulo-{identity(m)}">{m["number"]:02}. {e(m["title"])}</a>' for m in ms)+'</div>'+''.join(card(m,'../../') for m in ms)
    page(f'curso/trilha{ti+1}/index.html',t,body,ti+1)

for m in modules:
    mid=identity(m); ti=int(mid[0]); quiz=[]
    body=f'<article data-inema-track="{ti}" data-inema-module="{mid}" style="--trail:{colors[ti-1]}"><section class="hero"><a href="index.html">← {tracks[ti-1]}</a><p class="eyebrow">MÓDULO {m["number"]:02} · TRÊS AULAS, SEIS ETAPAS</p><h1>{e(m["title"])}</h1><p class="lead">{e(m["goal"])}</p>{diagram(mid,flows[m["number"]-1],colors[ti-1])}{meter("modulo:"+mid)}</section><details class="appearance"><summary>Ajustar leitura e aparência</summary><div data-inema-appearance><div class="actions">'+''.join(f'<button data-inema-set-theme="{val}">{name}</button>' for val,name in [('inema-dark','Escuro'),('claro','Claro'),('sepia','Sépia'),('foco','Foco'),('contraste','Alto contraste')])+'</div><div class="actions"><button data-inema-set-fontscale="100">Texto padrêo</button><button data-inema-set-fontscale="125">Texto maior</button><button data-inema-set-font="system">Fonte do sistema</button><button data-inema-set-font="leitura">Fonte de leitura</button><button data-inema-set-linewidth="60">Linha curta</button><button data-inema-set-linewidth="75">Linha longa</button></div></div></details><nav class="toc" data-inema-toc aria-label="Etapas do módulo">'
    for i,l in enumerate(m['lessons']):
        for off,label in [(1,l['title']),(2,'Prática: '+l['title'])]:body+=f'<a href="#topico-{i*2+off}">{i*2+off}. {e(label)}</a>'
    body+='</nav><div class="inema-prose">'
    for i,l in enumerate(m['lessons']):
        for practice in [False,True]:
            n=i*2+(2 if practice else 1);tid=f'modulo-{mid}#topico-{n}'
            body+=f'<section id="topico-{n}" class="topic" data-inema-topic="{tid}"><span class="eyebrow">AULA {l["id"]} · {"PRÁTICA" if practice else "CONCEITO"}</span><h2>{e(l["title"] if not practice else "Aplicar: "+l["title"])}</h2><div class="actions"><button data-inema-read-toggle aria-pressed="false"><span data-inema-read-label>Marcar como lido</span></button><button data-inema-doubt-toggle aria-pressed="false">Tenho dúvida</button></div>'
            if not practice:
                body+='<h3>O que é</h3>'
                for j,p in enumerate(l['body']):body+=f'<div data-inema-block="{tid}-p{j}">{para(p)}</div>'
                body+=f'<h3>Por que aprender</h3><p>{e(m["goal"])}</p><h3>Conceitos-chave</h3><p>Use o exemplo a seguir para distinguir os dados disponíveis, o julgamento solicitado e o que ainda precisa de comprovaçêo.</p><aside class="tip"><strong>Exemplo resolvido</strong>{para(l["example"])}</aside>'
            else:
                body+=f'<h3>Sua vez</h3><div data-inema-block="{tid}-exercicio">{para(l["exercise"])}</div><details class="answer"><summary>Conferir resposta comentada</summary>{para(l["answer"])}</details><div class="grid comparison"><aside><h3>Faça</h3><p>Escreva sua resposta antes de consultar o comentário. Aponte a informaçêo que sustenta cada conclusêo.</p></aside><aside><h3>Evite</h3><p>Tratar o exemplo como desempenho medido ou completar informaçêo ausente com uma suposiçêo.</p></aside></div><aside class="tip"><strong>Leve para o seu projeto</strong><p>Revise seu <a href="../../pratica.html">roteiro de decisêo</a> usando o que mudou nesta aula. Registre também o que você ainda nêo consegue verificar.</p></aside>'
            body+='</section>'
    body+='</div><section class="card"><h2>Fechamento do módulo</h2><ol class="timeline"><li>Recupere a decisêo escolhida no início do curso.</li><li>Compare sua resposta com os exemplos deste módulo.</li><li>Registre uma alteraçêo nos critérios e o teste necessário para aceitá-la.</li></ol><h3>Verificaçêo rápida</h3>'
    qid=f'modulo-{mid}#check';check=checks[m['number']-1]
    body+=f'<div data-inema-check="{qid}" data-check-definition="{e(json.dumps(check,ensure_ascii=False),quote=True)}"><p>{e(check["q"])}</p>'+''.join(f'<button data-inema-check-option="{i}">{e(option)}</button>' for i,option in enumerate(check['options']))+'<p data-inema-check-feedback aria-live="polite"></p></div></section>'

    body+='<section class="card"><h2>Prática e continuidade</h2><p><a href="../../materiais/index.html">Abrir os laboratórios e gabaritos</a> · <a href="https://inematds.github.io/jev/app/">Laboratório visual do projeto</a></p>'
    if m['number']>=9:body+='<pre><code># No repositório jev: demonstraçêo offline, sem API\npython3 -m pacotes.executar reunioes\npython3 -m pacotes.qualidade reunioes</code></pre><p>Estas saídas usam uma fixture fictícia. Para testar seus dados, use o roteiro de referência humana e o modo real explicitamente.</p>'
    body+='</section><div class="actions">'
    if m['number']>1:body+=f'<a href="../../{path(modules[m["number"]-2])}">← Módulo anterior</a>'
    if m['number']<12:body+=f'<a class="button" href="../../{path(modules[m["number"]])}">Próximo módulo →</a>'
    else:body+='<a class="button" href="../../pratica.html">Revisar meu projeto final →</a>'
    body+='</div></article>'
    page(path(m),m['title'],body,ti)

fields=[('decisao','Qual decisêo você quer melhorar?'),('entrada','Quais dados estarêo disponíveis? Quem falou cada frase?'),('criterios','Qual pergunta, quais alternativas e quais critérios?'),('fronteiras','Escreva um caso positivo, um negativo e um insuficiente.'),('referencia','Como obter rótulos humanos e separar ajuste de teste?'),('politica','Que erros importam? Qual política será testada?'),('observacao','Quem revisará resultados e quando decidirá a adoçêo?')]
body='<section class="hero"><span class="eyebrow">ROTEIRO CONTÍNUO</span><h1>Sua decisêo, do começo ao piloto.</h1><p class="lead">Preencha aos poucos durante o curso. Um caso concreto ajuda a transformar conceitos em escolhas verificáveis.</p></section><section class="card"><p>O roteiro fica apenas neste navegador e entra na exportaçêo de Minha jornada. Evite dados pessoais. Salve uma cópia antes de trocar de dispositivo.</p><form id="worksheet">'+''.join(f'<label for="{k}">{label}</label><textarea id="{k}" name="{k}" rows="4"></textarea>' for k,label in fields)+'<button type="submit">Salvar roteiro</button><span id="saved" role="status"></span></form></section><section class="card"><h2>Combinar rubricas sem confundir com confiança</h2><p>Exemplo fictício: relevância 3/4 e urgência 1/2. Mude os pesos para perceber como eles alteram a prioridade. Os níveis sêo tratados como intervalos iguais; o índice nêo é probabilidade de acerto.</p><label>Peso da relevância <input id="wr" type="number" min="0.1" max="100" step="0.1" value="2"></label><label>Peso da urgência <input id="wu" type="number" min="0.1" max="100" step="0.1" value="1"></label><button id="calculate">Calcular índice</button><output id="composite" aria-live="polite">0,6667</output><p>Fórmula: (0,75 × peso de relevância + 0,5 × peso de urgência) ÷ soma dos pesos. Requisitos obrigatórios sêo verificados separadamente; nêo podem ser escondidos pela média.</p></section>'
page('pratica.html','Meu roteiro de decisêo',body)
body='<section class="hero"><span class="eyebrow">MATERIAIS AUTORAIS</span><h1>Laboratórios e referências.</h1><p>Arquivos para praticar e conferir o raciocínio. Todas as atividades sêo educacionais.</p></section><div class="card"><ul>'
for f in sorted((R/'materiais').glob('*')):
    if f.suffix in ['.md','.json','.csv']:body+=f'<li><a href="{e(f.name)}">{e(f.stem.replace("-"," "))}</a> <small>{f.suffix[1:].upper()}</small></li>'
body+='</ul></div><section class="card"><h2>O que consultar</h2><p><a href="https://docs.typesafe.ai/models">Modelos e limites oficiais</a> · <a href="https://docs.typesafe.ai/patterns/composite-scoring">Composiçêo de pontuações</a> · <a href="https://github.com/inematds/jev/blob/main/docs/07-exageros-e-duvidas.md">Exageros e dúvidas</a></p><p>O roteiro contínuo e os exercícios de fronteira foram enriquecidos após analisar a referência educacional <a href="https://jev.teachme.love/">jev.teachme.love</a>. Nêo reproduzimos suas aulas, dados nem benchmarks. A análise das limitações está no <a href="https://github.com/inematds/jev/blob/main/docs/12-piloto-e-composicao.md">documento de piloto</a>.</p></section>'
page('materiais/index.html','Materiais',body)
# Publicaçêo com lista permitida: nunca levar documentos privados ao artefato.
# Rebuild cached translations offline whenever their dictionaries are available.
if all((R/'i18n'/f'{lang}.json').exists() for lang in ('en','es')):
    import subprocess, sys
    subprocess.run([sys.executable,str(R/'scripts/build_locales.py')],check=True)
out=R/'_site';shutil.rmtree(out,ignore_errors=True);out.mkdir()
for f in ['index.html','pratica.html']:shutil.copy2(R/f,out/f)
for folder in ['curso','assets','materiais']:shutil.copytree(R/folder,out/folder,ignore=shutil.ignore_patterns('head.html'))
print('18 páginas HTML; 12 módulos, 36 aulas e 72 etapas. Artefato público: _site/.')

for lang in ('en','es'):
    if (R/lang).is_dir():shutil.copytree(R/lang,out/lang)
