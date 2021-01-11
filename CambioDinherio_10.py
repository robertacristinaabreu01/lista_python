#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos doláres ela pode comprar.
#cambio => USS1.00 = R$3.27

carteira = float(input("Quantos reais você tem na carteira? "))
dollar = carteira / 3.27
print("Para {} que você tem na carteira, você poderá comprar {:.2f} dollares.".format(carteira, dollar))