import os
os.system('cls')

sonidos = {
    3: 'Plic',
    5: 'Plac',
    7: 'Ploc'
}


def gotas(n, sonido=''):
    for divisor in [3, 5, 7]:
        if n % divisor == 0:
            sonido += sonidos.get(divisor)

    if sonido == '':
        return n
    return sonido


resultado = gotas((n := int(input('Ingresa un número:\n--> '))))
print(f"\n{resultado}\n")
