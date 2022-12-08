import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('nao consegui acesso ao site')
else:
    print('site esta disponivel')
    print(site.read())
