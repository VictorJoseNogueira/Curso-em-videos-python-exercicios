n = total = cont = 0
n = int(input('digite um numero [digite 999 para parar]: '))
while n != 999:
    total += n
    cont += 1
    n = int(input('digite um numero [digite 999 para parar]: '))
print(f'vc digitou {cont} e a soma desses numeros é {total}')
