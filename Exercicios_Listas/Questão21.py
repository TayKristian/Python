lista_temp = []

x = 0
while len(lista_temp) < 5:
    while True:
        temp = float(input('Digite a {}° temp:'.format(x + 1)))
        if temp >= 15 and temp <= 40:
            break
        print('Temperatura inválida')
    lista_temp.append(temp)
    x = x + 1
print(lista_temp)

maior_temp = lista_temp[0]
x = 1
while x < len(lista_temp):
    if lista_temp[x] > maior_temp:
        maior_temp = lista_temp[x]
    x = x + 1
print('A maior temperatura foi de %.1f°C' %maior_temp)

menor_temp = lista_temp[0]
x = 1
while x < len(lista_temp):
    if lista_temp[x] < menor_temp:
        menor_temp = lista_temp[x]
    x = x + 1
print('A menor temperatura foi de %.1f°C' %menor_temp)

soma_temp = 0
for temp in lista_temp:
    soma_temp = soma_temp + temp
media_temp = soma_temp / len(lista_temp)
print('A temperatura média é %.1f°C' %media_temp)

x = 0
lista_aba = 0
while x < len(lista_temp):
    if lista_temp[x] < media_temp:
        lista_aba = lista_aba + 1
    x = x + 1
print('Tem %.f temperaturas abaixo da média' %lista_aba)
