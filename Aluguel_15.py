#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Digite a quantidade de km usados: "))
dias = int(input("Digite quantos dias de aluguel: "))
diasT = 60 * dias
kmT = 0.15 * km
total = diasT + kmT
print("Para {} dias e {}km usados, o valor total a ser pago será de: {:.2f}".format(dias, km, total))
