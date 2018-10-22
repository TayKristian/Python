la = float(input('Informe o valor do primeiro lado: '))
lb = float(input('Informe o valor do segundo lado: '))
lc = float(input('Informe o valor do terceiro lado: '))

if (la < lb + lc) and (lb < lc + la) and (lc < lb + la):
    print('É um triângulo')

    if la == lb and lb == lc and la == lc:
        tipo = 'Triângulo eqüilátero'
    elif (la == lb and lb != lc) or (lb == lc and lc != la) or (la == lc and lc != lb):
        tipo = 'Triângulo isósceles'
    else:
        tipo = 'Triângulo escaleno'

    print (tipo)
else:
    print('Não é triângulo')

