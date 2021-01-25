#Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius: "))
fahr = (celsius * 9/5)+32
print("O valor de {}° C  para Fahrenheit ficou de {}°F".format(celsius, fahr))

