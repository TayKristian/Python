frase = input('Digite uma frase: ')

cont_branco = 0
cont_a = 0
x = 0
while x < len(frase):
    if frase[x] == ' ':
        cont_branco = cont_branco + 1
    elif frase[x] == 'a' or frase[x] == 'A':
        cont_a = cont_a + 1
    x = x + 1

print('A frase tem %d espaços em branco' %cont_branco)
print('A frase tem %d letras A' %cont_a)
