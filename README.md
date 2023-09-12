## `__init__.py`: A Cerimônia de Iniciação Python

Vídeo: https://www.youtube.com/watch?v=H7rINLV6e0I
_____

Quando mergulhamos no mundo Python, somos acolhidos por sua sintaxe limpa e fluidez. Tudo parece tranquilo. Mas, cedo ou tarde, esbarramos no intrigante `__init__.py`, aparecendo em quase todos os cantos.

Encare-o como um marco na jornada Python. Ele sinaliza que você está se aprofundando, enfrentando novidades. Aqui, desvendaremos os mistérios por trás deste arquivo emblemático.

![InitAdventures](./static/image/meme.png)

### O que são Módulos?

Conforme nosso código se expande, surge a necessidade de organização. Um módulo é, basicamente, um arquivo com definições e comandos Python, sendo identificado pelo nome do arquivo acrescido de `.py`.

### E Pacotes?

Pacotes são diretórios que albergam o famoso `__init__.py`. Mesmo vazio, este arquivo dá o recado: "Este é um pacote Python!". Assim, ele pode ser importado tal qual um módulo.

* Alguns exemplos: package, core, utils, pandas, numpy...

### Preciso do `__init__.py`?

Até o Python 3.3, sim! Ele era essencial para que diretórios fossem reconhecidos como pacotes. A partir desta versão, porém, com a introdução dos namespaces, o `__init__.py` deixou de ser uma obrigação.

### Explorando o `__init__.py`

#### 1) Sinalizando Pacotes:

Ter um `__init__.py` numa pasta é como um selo: esta é uma estrutura de pacote/módulo em Python! Assim, você pode criar uma arquitetura de diretórios e navegar por ela usando pontos.

#### 2) Validações do Pacote:

Ao importar um pacote, o Python roda o `__init__.py`. Se você tem configurações específicas ou verificações a fazer durante essa importação, é aqui que elas devem morar.

```python
# Verifica a versão do python

import sys

if sys.version_info.major == 3:
    print("Versão do Python ok")
else:
    print("Versão do Python não é compatível com o pacote")

# Verifica se a biblioteca requests está instalada

try:
    import requests
    print("Biblioteca requests instalada")
except:
    print("Biblioteca requests não instalada")
```

#### 3) Tornando Importações Diretas:

O `__init__.py` pode ser o atalho para funções, classes ou variáveis dentro de pacotes, facilitando sua chamada direta sem navegar por múltiplos módulos.

```python
from pacote.sub_pacote.modulo import minha_primeira_funcao
```
