#Questão 06 - Python para Zumbis
"""
Calcule o tempo de uma viagem de carro. Pergunte a distância
a percorrer e a velocidade média esperada para a viagem.
"""
dist = float(input('Digite a distância a percorrer: '))
vel = float(input('Digite a velocidade média: '))

temp = dist/vel

print('O tempo de viagem é', temp, 'h')
