#Questão 03 - Python para Zumbis
"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento
diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo
excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique
se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá 
pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
"""
peso = float(input('Informe o peso de peixes: '))

peso_estabelecido = 50
excesso = 0
multa = 0

if peso > peso_estabelecido:
    excesso = peso - peso_estabelecido
    multa = 4 * excesso

print ('Excesso:', excesso)
print ('Multa de R$ %.2f' % multa)
