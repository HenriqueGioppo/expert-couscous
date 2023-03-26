#import
from bs4 import BeautifulSoup

listaCnpj = []
cnpj = ""

#lendo arquivo com BS
with open("D:\\Python\\NFeTeste.xml", 'r') as f:
    conteudo = f.read()
bsConteudo = BeautifulSoup(conteudo, 'xml')

#encontrando todos os CNPJ
for tag in bsConteudo.find_all("CNPJ"):
    #transformando em string
    tagStr = str(tag)
    #fazendo split dos caracteres 6 ao 20
    cnpj = tagStr[6:20]
    #adicionando na lista
    listaCnpj.append(cnpj)
    print(tag)

print(listaCnpj)