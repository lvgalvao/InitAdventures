# O que é o `__init__.py` e o por quê dele estar em todo lugar?

Python se apresenta com uma sintaxe clara e coesa, tornando a curva de aprendizado inicial suave e acessível. No início, tudo flui. Porém, conforme avançamos, topamos com o tal do `__init__.py` dentro de diretórios, pacotes e módulos. 

É como um rito de passagem na vida de quem programa em Python, indicando que estamos crescendo e encarando novos desafios. Neste projeto, vamos desvender esse enigma e entender como esse arquivo pode nos ajudar.

![InitAdventures](./static/image/meme.png)

## O que é um Módulo?

A medida que o nosso código cresce, precisamos organizar ele de alguma forma. Um módulo é um arquivo contendo definições e instruções Python. O nome do arquivo é o nome do módulo com o sufixo `.py` adicionado.

## O que é um Pacote?

Um pacote é um diretório que contém um arquivo `__init__.py`. Este arquivo pode estar vazio, e indica que o diretório que ele contém é um pacote Python, portanto pode ser importado da mesma maneira que um módulo pode ser importado.

- Ex: package, core, utils, pandas, numpy, etc.

## O `__init__.py` é obrigatório?

Antes do Python 3.3, o arquivo `__init__.py` era necessário para transformar qualquer diretório que você quisesse usar em um pacote Python

Acima do Python 3.3, os namespaces de pacotes foram adicionados ao Python. Isso significa que você não precisa mais de um arquivo `__init__.py` para que o Python trate os diretórios como pacotes.

## Formas de utilizar o `__init__.py`

### 1) Indicação de um Pacote: 
Em primeiro lugar, a presença de um arquivo `__init__.py`` dentro de uma pasta indica que essa pasta pode ser tratada como um pacote ou módulo em Python. Isso permite que você organize seus módulos em uma estrutura hierárquica de diretórios e acesse-os usando a notação de ponto.

### 2) Inicialização do Pacote: 
Quando você importa um pacote, o Python executa o conteúdo do arquivo `__init__.py` como código de inicialização para aquele pacote. Por exemplo, se você tiver algumas configurações ou verificações que gostaria de executar ao importar um pacote, pode colocá-las no arquivo `__init__.py.`

### 3) Definindo `__all__`: 
No arquivo `__init__.py`, você pode definir uma lista chamada `__all__` que determina quais módulos serão importados quando alguém usa `from package import *`. Por exemplo, se seu pacote tiver vários módulos, mas você quiser que apenas alguns deles sejam importados quando o usuário usar a sintaxe de importação com *, você pode especificar esses módulos na lista `__all__`.

### 4) Simplificar Importações: 
O `__init__.py` também pode ser usado para tornar certas funções, classes ou variáveis disponíveis diretamente no nível do pacote. Por exemplo, se você tiver um módulo chamado moduleA em seu pacote e quiser que uma função específica dentro de moduleA seja acessível diretamente a partir do nível do pacote, você pode importá-la no arquivo `__init__.py`.

O arquivo `__init__.py` pode ser usado para armazenar variáveis ​​que você deseja definir para o pacote, mas não deseja que sejam visíveis fora do pacote.

Podemos usar o arquivo `__init__.py` para definir quais partes do pacote serão exportadas no caso de um `from package import *` ser usado.

Caso você não queira que o `from package import *` importe todos os módulos, você pode definir uma variável `__all__` dentro do `__init__.py` que define quais módulos serão importados quando o `from package import *` for usado.

## __init__.py é obrigatório?

## O que vai dentro do __init__.py

## Exemplos de pacotes