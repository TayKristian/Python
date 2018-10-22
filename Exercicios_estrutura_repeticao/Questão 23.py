n = int(input('Infome um numero: '))

x = 1
soma = 0
while x <= n:
    if n % x == 0:
        print(x, 'é divisor de', n)
    x = x + 1
