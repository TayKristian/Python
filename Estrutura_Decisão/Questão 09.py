n1 = int(input('Informe o 1° numero: '))
n2 = int(input('Informe o 2° numero: '))
n3 = int(input('Informe o 3° numero: '))

if (n1 >= n2) and (n1 >= n3):
    print (n1)
    if (n2 >= n3):
        print (n2)
        print (n3)
    else:
        print (n3)
        print (n2)
elif (n2 >= n3):
    print (n2)
    if (n1 >= n3):
        print (n1)
        print (n3)
    else:
        print (n3)
        print (n1)
else:
    print (n3)
    if (n1 >= n2):
        print (n1)
        print (n2)
    else:
        print (n2)
        print (n1)
