def onoTochnoNeOtrizat (a, r, h, v):
    if a > 0 and r > 0 and h > 0 and v > 0:
        return 1
    else:
        return 0
def chtoZapolnitsa  (k, z, b):
    if b >= v:
        return 'Можно полностью заполнить и куб, и цилиндр'
    if k >= v:
        return 'Можно полностью заполнить куб'
    if z >= v:
        return 'Можно полностью заполнить цилиндр'

    else:
        return 'Нельзя полностью заполнить одновременно обе ёмкости'

try:
    a=float(input('Введите длину стороны куба:'))
    r=float(input('Введите радиус цилиндра:'))
    h=float(input('Введите высоту цилиндра:'))
    v=float(input('Введите объем жидкости:'))
    while onoTochnoNeOtrizat(a, r, h, v) != 1:
        print('Введите неотрицательне числа')
        a = float(input('Введите длину стороны куба:'))
        r = float(input('Введите радиус цилиндра:'))
        h = float(input('Введите высоту цилиндра:'))
        v = float(input('Введите объем жидкости:'))
    k = a**3
    z = r**2 * h * 3.14
    b = a**3 + r**2 * h * 3.14
    print(chtoZapolnitsa(k, z, b))

except ValueError: 
    print('Это не число. Введите число.') 
