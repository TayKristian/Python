n = int(input('Digite um número: '))
x = n

while True:
    if x % 11 == 0 or x % 13 == 0 or x % 17 == 0:
        print(x)
        break
    x = x + 1
