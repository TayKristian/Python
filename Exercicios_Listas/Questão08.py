list_n = []

x = 1
while len(list_n) < 100:
    if x % 2 != 0:
        list_n.append(x)
    x = x + 1
print(list_n)
print('Tamanho da lista é %d' %len(list_n))
