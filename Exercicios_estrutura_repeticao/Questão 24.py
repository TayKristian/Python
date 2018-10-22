n = int(input('Infome um numero: '))

x = 1
soma = 0
while x < n:
    if n % x == 0:
        soma = soma + x
    x = x + 1

print('A soma é', soma)

