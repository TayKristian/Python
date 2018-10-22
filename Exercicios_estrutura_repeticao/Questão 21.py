com = int(input('Digite o começo: '))
fim = int(input('Digite o fim: '))

soma_pares = 0
prod_impares = 1

x = com
while x <= fim:
    if x % 2 == 0:
        soma_pares = soma_pares + x
    else:
        prod_impares = prod_impares * x
    x = x + 1

print('A soma dos pares é', soma_pares)
print('O produto dos impares é', prod_impares)
