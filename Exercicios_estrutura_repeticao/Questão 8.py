n = int(input('Digite um numero: '))
maior = n
menor = n

x = 1
while x <= 9:
    n = int(input('Digite um numero: '))
    if maior < n:
        maior = n
        
    if menor > n:
        menor = n
    x = x + 1

print('O maior número é', maior)
print('O menor número é', menor)
