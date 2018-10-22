#Questão 10 - Python para Zumbis
"""
Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dia e quantos
anos ele já fumou. Considere que um fumante perde 10 minutos de vida
a cada cigarro, calcule quantos dias de vida um fumante perderá.
Exiba o total de dias.
"""

cig = int(input('Digite o número de cigarros fumados por dia: '))
temp = int(input('Quantos anos você fuma?: '))

num_cig = cig * temp * 365
di = (num_cig * 10) / 24
an = di / 395

print("Você já perdeu",'%.2f' % di, "dias ou", '%.2f' % an, "anos")
