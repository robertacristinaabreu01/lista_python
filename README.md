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

exemplos: 
````
import math
num = int (input("Digite um número: "))
raiz = math.sqrt(num)
print("A raix de {} é igual a {}".format(num,raiz))

```

* para importar toda a biblioteca (import math)
* para parte da biblioteca (from math import sqrt)
