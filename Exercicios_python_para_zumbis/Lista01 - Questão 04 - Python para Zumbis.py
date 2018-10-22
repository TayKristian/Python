#Questão 4 - Python para Zumbis
"""
Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do
salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
"""

sal = float(input('Digite o valor do seu salário: '))
por = float(input('Digite a porcentagem do aumento: '))

aum = sal * (por / 100)
sal_atual = sal + aum

print("O valor do aumento: ", aum)
print("O seu salário novo é: ", sal_atual)
