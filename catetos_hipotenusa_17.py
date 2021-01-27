#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo. Calcule e mostre o comprimento da hipotenusa.
#h2 = ca2 + co2
#hipotenusa = co **2 +ca **2 )**(1/2)
#hipotenusa = co **2 +ca **2 )**(1/2)

import math
oposto = float(input("Digite o comprimento do cateto oposto: "))
adja = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = math.hypot(oposto,adja)
print("A hipotenusa será: {:.2f}".format(hipotenusa))

