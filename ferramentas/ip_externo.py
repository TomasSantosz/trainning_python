import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

response = urlopen(url)

dados = json.load(response)

ip = dados['ip']
org= dados['org']
city = dados['city']
pais = dados['country']
regiao = dados['region']

print('DETALHES: ')
print('IP: {4}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrg.:{0}'.format(org,regiao,pais,city,ip))