ano = int(input('Informe o ano: '))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    mens = 'Ano bissexto com 366 dias'
else:
    mens = 'Ano normal com 365 dias'

print (mens)
