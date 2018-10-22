soma = 0
q = 0

while True:
    nota = float(input('Digite a nota: '))
    if nota < 10 or nota > 20:
         break
    soma = soma + nota
    q = q + 1

media = soma / q

print('A média é', media)
