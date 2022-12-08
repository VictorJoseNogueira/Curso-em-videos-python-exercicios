'''c = 1
while c < 200:
    print(c)
    c += 1

print(c)'''
'''name = ''
while name != 'zé':
    name = str(input('qual seu vulgo ?'))
print(name)'''
'''tab = int(input('digite um valor: '))
uada = 0
while uada != tab or uada > 10:
    uada += 1
    tabuada = tab * uada

print(f'{tab} x {uada} ={tabuada}')'''
'''r = 's'
while r == 's':
    n = int(input('digite um numero '))
    r = str(input('quer continuar ? S/N ')).lower()
print('fim')'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'vc digitou {par} pares e {impar} impares')
