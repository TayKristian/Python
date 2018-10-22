fim = int(input('Digite quantos números será lido: '))
n = int(input('Digite um número: '))
maior = n
quant = 1

x = 2
while x <= fim:
    n = int(input('Digite um número: '))
    if maior < n:
        maior = n
        quant = 1
    elif maior == n:
        quant = quant + 1
    x = x + 1
print('O maior número é', maior)
print('O maior número apareceu', quant,'vezes')
