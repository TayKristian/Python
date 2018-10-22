#Questão 2 - Python para Zumbis
"""
Determine se um ano é bissexto. Verifique no Google como fazer isso.
"""

ano = int(input('Informe o ano: '))

if ano % 4 == 0 and ano % 100 != 0:
    mensagem = 'Ano bissexto com 366'
else:
    mensagem = 'Ano normal com 365'

print (mensagem)
