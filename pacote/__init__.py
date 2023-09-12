from pacote.sub_pacote.modulo import minha_primeira_funcao

print("Meu primeiro pacote")

# esse código só pode funcionar com Python 3 ou superior

import sys

if sys.version_info.major == 3:
    print("Versão do Python ok")
else:
    print("Versão do Python não é compatível com o pacote")

# verifica se a biblioteca requests está instalada

try:
    import requests
    print("Biblioteca requests instalada")
except:
    print("Biblioteca requests não instalada")