n2 = int(input('de qual numero vc gostaria de saber o fatorial ?'))
c = n2
f = 1
print(f'calculando {n2}!', end='')
while c > 0:

    print(f'{c} ', end='')
    print('x 'if c > 1 else ' = ', end='' )
    f *= c

    c -= 1
#fatorial
print(f)
