#Questão 05 - Python para Zumbis
"""
Solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.
"""

pr = float(input('Digite o preço da mercadoria: '))
per = float(input('Digite o valor do desconto:  '))

desc = pr  * (per / 100)
pr_pagar = pr - desc

print("O valor do desconto é R$", desc)
print("O total a pagar é de R$", pr_pagar)
