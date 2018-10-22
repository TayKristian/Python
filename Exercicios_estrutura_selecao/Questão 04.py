#Questão 04 - Python para Zumbis
"""
Faça um programa que leia três números e mostre o maior deles.
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n3:
    maior = n2
else:
    maior = n3

print ('O maior número é', maior)
