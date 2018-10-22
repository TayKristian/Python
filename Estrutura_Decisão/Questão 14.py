not1 = float(input('Informe o valor da primeira nota: '))
not2 = float(input('Informe o valor da segunda nota: '))

med = (not1 + not2) / 2

if (med < 4):
    print ('Conceito E')
    aprovado = False
elif (med < 6):
    print ('Conceito D')
    aprovado = False
elif (med < 7.5):
    print ('Conceito C')
    aprovado = True
elif (med < 9):
    print ('Conceito B')
    aprovado = True
else:
    print ('Conceito A')
    aprovado = True

if aprovado:
    print ('Aprovado')
else:
    print ('Reprovado')
