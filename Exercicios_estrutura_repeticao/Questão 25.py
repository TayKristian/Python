x = 1
soma = 0

while x <= 1000:
    if x % 3 == 0 or x % 5 == 0:
        soma = soma + x
    x = x + 1
print('A soma é', soma)
