list_alt = []

x = 0
soma = 0
while x < 10:
    alt = float(input('Digite a altura do %d° atleta: ' %(x + 1)))
    list_alt.append(alt)
    soma = soma + alt
    x = x + 1

print("Alturas", list_alt)
media = soma / len(list_alt)

x = 0
while x < len(list_alt):
    if list_alt[x] > media:
        print('A altura é %.2f m' %(list_alt[x]))
    x = x + 1
