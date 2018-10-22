n1 = int(input('Informe o 1° numero: '))
n2 = int(input('Informe o 2° numero: '))
n3 = int(input('Informe o 3° numero: '))

if n1 == n2 and n1 == n3:
    print ('Os numeros sao iguais')
else:
    if n1 > n2 and n1 > n3:
        print ('O maior numero é', n1)
    elif n2 > n3:
        print ('O maior numero é', n2)
    else:
        print ('O maior numero é', n3)

    if n1 < n2 and n1 < n3:
        print ('O menor numero é', n1)
    elif n2 < n3:
        print ('O menor numero é', n2)
    else:
        print ('O menor numero é', n3)
