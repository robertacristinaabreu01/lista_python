#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com  5% de desconto.

preco= float(input("Digite o preço do produto: "))
desconto = preco *0.25
final = preco - desconto
print("O produto custa R${} mas com desconto ele passará a custar R${},o produto teve R${}"
      " de desconto".format(preco, final, desconto))