x = 1
soma = 0
while x <= 10:
    n = int(input('Digite um número: '))
    if n > 0:
        soma = soma + n
    x = x + 1

media = soma / 10
print('A média é', media)
