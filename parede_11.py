#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro,
#pinta uma área de 2m²

largura = float(input("Digite o valor da largura de sua parede em metros: "))
altura = float(input("Digite o valor da altura de sua parede em metros: "))

area = altura * largura
tinta = area / 2

print("Você precisará de {} litros de tinta para pintar a sua parede de {}m².".format(tinta, area))
