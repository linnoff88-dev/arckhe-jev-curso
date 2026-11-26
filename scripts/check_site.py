"""Checa o artefato publicado, links, identidade e integridade das aulas."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json
R=Path(__file__).resolve().parents[1];site=R/'_site'
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=[];self.links=[];self.topics=[];self.blocks=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if 'data-ARCKHÉ-topic' in a:self.topics.append(a['data-ARCKHÉ-topic'])
        if 'data-ARCKHÉ-block' in a:self.blocks.append(a['data-ARCKHÉ-block'])
        for key in ['href','src']:
            if key in a:self.links.append(a[key])
pages={p:Page(p.read_text()) for p in site.rglob('*.html')}
locales=['']+[lang for lang in ('en','es') if (site/lang).exists()]
assert len(pages)==18*len(locales),len(pages)
for p,d in pages.items():
    assert len(d.ids)==len(set(d.ids)),p
    for link in d.links:
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        dest=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
        if dest.is_dir():dest=dest/'index.html'
        assert dest.is_relative_to(site.resolve()) and dest.exists(),(p,link)
        if u.fragment and dest.suffix=='.html':assert unquote(u.fragment) in pages[dest].ids,(p,link)
assert sum(len(d.topics) for d in pages.values())==72*len(locales)
for m in json.loads((R/'conteudo/curso.json').read_text()):
    n=m['number'];p=site/f'curso/trilha{(n-1)//4+1}/modulo-{(n-1)//4+1}-{(n-1)%4+1}.html';d=pages[p]
    assert len(d.topics)==6 and len(d.blocks)>=12,p
    text=unquote(p.read_text())
    from html import unescape
    plain=unescape(text)
    for lesson in m['lessons']:
        for field in ['example','exercise','answer']:assert lesson[field] in plain,(p,lesson['id'],field)
assert not any((site/x).exists() for x in ['doc','fontes','.env'])
print(f'Site OK: {len(pages)} páginas, {len(locales)} idiomas, links e âncoras locais válidos.')
