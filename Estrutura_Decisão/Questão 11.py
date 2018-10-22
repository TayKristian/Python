sal = float(input('Informe o valor do salario do colaborador: '))

if (sal <= 280):
    perce = 20
elif (sal <= 700):
    perce = 15
elif (sal <= 1500):
    perce = 10
else:
    perce = 5

aum = sal * (perce / 100.0)
novo_sal = sal + aum

print ('Salario antes do reajuste:', sal)
print ('Percentual de aumento:', perce, '%')
print ('Valor do aumento:', aum)
print ('Novo Salario:', novo_sal)
