import re
import json
from urllib.request import urlopen

url = "https://ipinfo.io/json"

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print("Detalhes do IP externo \n")
print("IP: {4}\nRegiao: {1}\nPaís: {2}\nCidade: {3}\nOrg.: {0}".format(org,region,pais,cid,ip))