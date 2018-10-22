morango = float(input('Morangos em Kg: '))
maca = float(input('Maças em Kg: '))

if tmo <= 5:
    v_mo = t_mo * 2.5
else:
    v_mo = t_mo * 2.2

if t_ma <= 5:
    v_ma = t_ma * 1.8
else:
    v_ma = v_ma * 1.5

v_br = v_mo + v_ma



