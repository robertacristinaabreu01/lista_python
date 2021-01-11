#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

num1 = int(input("Digite a tabuada que você deseja: "))
print(" TABUADA DO {} ".format(num1))

for cont in range (10):
    print(" {0} x {1} = {2}".format(num1,cont+1,num1*(cont+1)))

print("*****************************")

##ou

print(" {} x {:2} = {}".format(num1,1, num1*1))
print(" {} x {:2} = {}".format(num1,2, num1*2))
print(" {} x {:2} = {}".format(num1,3, num1*3))
print(" {} x {:2} = {}".format(num1,4, num1*4))
print(" {} x {:2} = {}".format(num1,5, num1*5))
print(" {} x {:2} = {}".format(num1,6, num1*6))
print(" {} x {:2} = {}".format(num1,7, num1*7))
print(" {} x {:2} = {}".format(num1,8, num1*8))
print(" {} x {:2} = {}".format(num1,9, num1*9))
print(" {} x {:2} = {}".format(num1,10, num1*10))


