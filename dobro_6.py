#Crie um algoritmo que leia um número e mostre o seu dobro,
#triplo e raiz quadrada

a = int(input("Digite um número: "))
print("Analisando o número {} , o seu dobro será: {} , o seu triplo será: {} e sua raiz quadrada será: {:.2f}".format(a, (a*a), (a*a*a), pow(a,(1/2))))
#ou criando variaveis
#d= n*2
#t = n *3
#raiz = n ** (1/2)
#print("Analisando o número {} , o seu dobro será: {} , o seu triplo será: {} e sua raiz quadrada será: {:.2f}".format(a,d,t,raiz)