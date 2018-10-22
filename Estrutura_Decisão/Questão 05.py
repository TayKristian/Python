nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

med = (nota1 + nota2) / 2.0

print ('A media do aluno é:', med)

if (med == 10):
    print ('Aprovado com Distincao')
elif (med >= 7):
    print ('Aprovado')
else:
    print ('Reprovado')
