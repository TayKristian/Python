list_n = []

x = 0
while x < 10:
    n = int(input('Digite o %dº numero: ' %(x + 1)))
    list_n.append(n ** 3)
    x = x + 1
print(list_n)
