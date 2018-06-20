#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get
from bs4 import BeautifulSoup

url = 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar/padrao-tiss-historico-das-versoes-dos-componentes-do-padrao-tiss'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

data = html_soup.find_all('table', class_ = 'table table-bordered')
ano = data[0]
ultima_versao = ano.tbody.tr.td
print ultima_versao

if str(ultima_versao) == '<td>dez/17</td>':
	print "TISS não atualizou"
else:
	print "TISS foi atualizado"


