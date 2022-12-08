#3 pegue retas e veja se podem formar um triangulo ?
t1 = int(input('digite um lado para o triangulo: '))
t2 = int(input('digite um outro lado para o triangulo: '))
t3 = int(input('digite mais um lado para o triangulo: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('sim é possivel formar um triangulo', end='')
    if t1 == t2 == t3:
        print('  equilatero')
    elif t1 != t2 != t3 != t1:
        print('  escaleno')
    else:
        print('  isoceles')
else:
    print('impossivel formar um triangulo...')
