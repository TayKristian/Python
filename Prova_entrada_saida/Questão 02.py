#Questão 02 - Prova 2
"""
Construa um programa que leia a quantidade de quilometros rodados e a
quantidade gasta de combustível em litros por um carro e informe a média
de combustível gasto em cada quilometro rodado.
"""
km_rod = float(input("Digite quantos Km rodado: "))
q_com = float(input("Digite a quantidade de combustivel que foi gasto: "))

med_com = km_rod / q_com

print("A média de combustível usada é de",'%.2f' % med_com, "litros por quilometro")
