valor_hora = float(input('Informe o valor da hora trabalhada: '))
quant_hora = float(input('Informe a quantidade de horas trabalhadas: '))

sal_bruto = valor_hora * quant_hora

if (sal_bruto > 2500):
    IR = 20
elif (sal_bruto > 1500):
    IR = 10
elif (sal_bruto > 900):
    IR = 5
else:
    IR = 0

valor_IR = sal_bruto * (IR / 100.0)
valor_sind = sal_bruto * (10/100.0)
total_desc = valor_IR + valor_sind

valor_FGTS = sal_bruto * (11 / 100.0)

sal_liquido = sal_bruto - total_desc

print ('+ Salário Bruto: R$ %.2f' % sal_bruto)
print ('(-) IR(',IR,'%): R$', valor_IR)
print ('(-)', 'INSS (10%%): R$ %.2f' % valor_sind)
print ('FGTS','(11%%) R$ %.2f' % valor_FGTS)
print ('Total de Descontos: R$ %.2f' % total_desc)
print ('Salario Liquido: R$R$ %.2f' % sal_liquido)

