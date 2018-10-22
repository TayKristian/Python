#Questão 09 - Python para Zumbis
"""
Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de
dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
"""

km_per = float(input('Digite a quantidade de KM percorridos: '))
quant_d = int(input('Digite a quantidade de dias que o carro foi alugado: '))

valor_pagar = ((km_per * 0.15) + quant_d * 60)

print('O valor a pagar pelo aluguel do carro será R$', valor_pagar)
