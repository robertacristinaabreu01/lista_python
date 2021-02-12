#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteado
import random
primeiro = input("Primeiro aluno: ")
segundo = input("Segundo aluno: ")
terceiro = input("Terceiro aluno: ")
quarto = input("Quarto aluno: ")
lista = [segundo,primeiro,terceiro,quarto]
random.shuffle(lista)
print("A ordem de apresentação será: ",lista)