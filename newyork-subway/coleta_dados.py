# coding: utf-8

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

def recuperar_html(url):
    try:
        return str(urlopen(url).read())
    except Exception as e:
        print('Erro ao carregar url', e)

def recuperar_tag_a(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all('a')

def filtrar_links(tags, filtro):
	values = []
	for t in tags:
		if t.get('href') and filtro in t.get('href'):
			values.append(t)
	
	return values

def recuperar_arquivos(url, tag):
	try:
		link = ''
		
		if not url.endswith('/'):
			link = url[:(url.rfind('/') + 1)] + tag.get('href')
		else:
			link = url + tag.get('href')
		
		filename = link[(link.rfind('/') + 1):]
		print('Recuperar arquivos {} para {}'.format(link, filename))
		req = urlretrieve(link, filename)
		
		return filename
		
	except Exception as e:
		print('Erro ao recuperar arquivos', e)
	
url = 'http://web.mta.info/developers/turnstile.html'
filtro = 'turnstile_1706'

tags = filtrar_links(recuperar_tag_a(recuperar_html(url)), filtro)
for t in tags:
	recuperar_arquivos(url, t)
	
print('fim')