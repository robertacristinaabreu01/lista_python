#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno
# e tangente desse ângulo.
import math
angulo = float(input("Digite o ângulo: "))

cos = math.cos(math.radians(angulo))
sen = math.sin(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print("Para o ângulo {} será {:.2f} cos, {:.2f} seno e {:.2f} tangente".format(angulo, cos, sen, tang))


