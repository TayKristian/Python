pre1 = float(input('Informe o 1° preco: '))
pre2 = float(input('Informe o 2º preco: '))
pre3 = float(input('Informe o 3° preco: '))

if (pre1 == pre2) and (pre1 == pre3):
    print ('Pode comprar qualquer um, ja que os precos sao iguais.')
elif (pre1 < pre2) and (pre1 < pre3):
    print ('Compre o primeiro produto')
elif (pre2 < pre3):
    print ('Compre o segundo produto')
else:
    print ('Compre o segundo produto')
