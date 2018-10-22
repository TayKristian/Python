tc = input('Informe (A) para Alcool ou (G) para Gasolina: ').upper()
ql = float(input('Informe a quantidade de litros: '))

if (tc == 'A'):
    valor = 1.9
    if (ql <= 20):
        desc = 3
    else:
        desc = 5
else:
    valor = 2.5
    if (ql <= 20):
        desc = 4
    else:
        desc = 6

total = (valor * ql) * ((100 - desc) / 100.0)

print ('Total a pagar é %.2f' % total)
