#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

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
	
	
# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open('textfile.txt', 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

me = "Meu email"
pswd = "minha senha"
you = "para quem enviar"
s
# you == the recipient's email address
msg['Subject'] = 'Assunto do email' 
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
server = smtplib.SMTP('smtp.gmail.com:587') #Servidor de email
server.starttls() # inciar Serviço
server.login(me, pswd) # Login
server.sendmail(me, you, msg.as_string()) # Enviar, quem, para quem, mensagem
server.close() # Fechar Conexão


