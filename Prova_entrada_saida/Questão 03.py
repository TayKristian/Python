#Questão 03 - Prova 02
"""
Construa um programa que recebe como entrada a quantidade de latão em Kg e
informe ao usuario a quantidade de cobre e zinco presente no mesmo, sabendo
que o latão é feito de 70% cobre e de 30% zinco.
"""

kg_lat = float(input("Digite a quantidade de Kg de lãtão: "))

cob = (kg_lat * 70) / 100
zin = (kg_lat * 30) / 100

print("A quantidade de cobre é", cob, "% e a quantidade de zinco é", zin, "%")
