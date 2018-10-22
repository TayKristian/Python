# Questão 3 - Python para Zumbis
"""
Escreva um programa que leia a quantidade de dias, horas, minutos
e segundos do usuário. Calcule o total em segundos.

dia --> 24 * 60 * 60 = 86400 s
hora --> 60 * 60 = 3600 s
minuto --> 60 s
"""

di = int(input('Digite a quantidade de dias: '))
ho = int(input('Digite a quantidade de horas: '))
mi = int(input('Digite a quantidade de minutos: '))
se = int(input('Digite a quantidade de segundos: '))
to_se = di * 86400 + ho * 3600 + mi * 60 + se

print(to_se, 'segundos')
