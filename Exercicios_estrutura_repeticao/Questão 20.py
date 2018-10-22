quant_pares = 0
quant_n = 0

while True:
    n = int(input('Digite um número: '))
    if n == 1000:
        break

    if n % 2 == 0:
        quant_pares = quant_pares + 1

    quant_n = quant_n + 1

print('Foram lidos', quant_n, 'numeros')
print('Foram lidos', quant_pares, 'números pares')
