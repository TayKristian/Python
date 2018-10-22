#Questão 07 - Python para Zumbis
"""
Converta uma temperatura digitada em Celsius para Fahrenheit.
F = 9*C/5 + 32
"""

cel = float(input('Digite a temperatura em Celsius: '))

fah = (9 * cel / 5) + 32

print('A temperatura em fahrenheit é', fah, '°F')
