num = int(input('Informe um numero inteiro: '))

centenas = num / 100
dezenas = (num - (centenas * 100)) / 10
unidades = (num - (centenas * 100) - (dezenas * 10))


