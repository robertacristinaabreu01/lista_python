# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o salário de um funcionário: "))
novo = salario + (salario *15/100)
print("O salario {:.2f} com aumento de 15% será de {:.2f} então o aumento foi de {:.2f}  ".format(salario,novo, (salario*15/100)))