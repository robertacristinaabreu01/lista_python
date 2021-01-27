# lista_python

como importar bibliotecas em python

* import math: retornará  cálculos de trigonometria --

* import ceil: retornará o menor número inteiro maior ou igual a x ou arredondar para cima. --> math.ceil()

* import floor: retornará  o arredondamento do número ou retorna o maior inteiro que é menor ou igual a x --> math.floor()

* import trunc: Retorna o valor x Real truncado com um Integral (geralmente um inteiro). --> math.trunc()

* import pow: Retorna x elevado à potência y. -->math.pow()

* import sqrt: Para achar a raiz quadrada. --> math.sqrt()

* import factorial: Retorna x fatorial como um inteiro. Levanta ValueError se x não for integral ou for negativo. --> math.factorial()

* import fabs: retona o valor absoluto de x. --> marth.fabs()

[maiores informações sobre a biblioteca math](https://docs.python.org/pt-br/3/library/math.html?highlight=math)

Para importar toda a biblioteca (import math) e  para parte da biblioteca (from math import sqrt)

exemplos: 
````
import math
num = int (input("Digite um número: "))
raiz = math.sqrt(num)
print("A raix de {} é igual a {}".format(num,raiz))

````

arredondamento com math.floor()


````
import math
num = int (input("Digite um número: "))
raiz = math.sqrt(num)
print("A raix de {} é igual a {}".format(num,math.floor(raiz)))

````
mais de uma biblioteca

````
from math import sqrt, floor
num = int(input("Digite um número: "))
raiz = sqrt(num)
print("A raiz {} é igual a {:.2f}".format(num, floor(raiz)))

````
random - números aleatórios

````
import random
num = random.random()
print(num)
````
retorna :0.3528306984583961
````
import random
num = random.randint(1,10)
print(num)
````
retorna: 8

````

import emoji
print(emoji.emojize("Olá, Mundo :earth_americas:" use_aliases=true))

````

