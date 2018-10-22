#Questão 06 - Python para Zumbis
"""
Faça um programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao
INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto -
Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme
a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
"""

gh = float(input('Quanto ganha por hora: '))
nh = int(input('Digite quantas horas foram trabalhadas no mês:'))

sal_br = gh * nh
ir = sal_br * 0.11
inss = sal_br * 0.08
sind = sal_br * 0.05
sal_liq = sal_br - ir - inss - sind

print('+ Salário Bruto: R$ %.2f' % sal_br)
print('- IR: R$ %.2f' % ir)
print ('- INSS: R$ %.2f' % inss)
print ('- Sindicato: R$ %.2f' % sind)
print ('= Salário Líquido: R$ %.2f' % sal_liq)
