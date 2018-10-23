#Questão 04 - Prova 02
"""
Construa um programa que receba como entrada o peso e a altura de uma pessoa
e calcule o IMC

IMC = peso / altura²
"""
peso = float(input("Digite o peso: "))
alt = float(input("Digite sua altura: "))

imc = peso / (alt ** 2)

print("O valor do imc é",'%.2f' % imc)
