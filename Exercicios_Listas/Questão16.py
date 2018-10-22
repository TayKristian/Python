list_n = []

x = 1
while x < 8:
    n = int(input('Digite o %dº numero: ' %(x + 1)))
    if n < 0:
        list_n.append(-1)
    else:
        list_n.append(n ** 0.5)
    x = x + 1
print(list_n)
