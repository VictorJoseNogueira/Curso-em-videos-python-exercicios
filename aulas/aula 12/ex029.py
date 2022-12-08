from random import randint
from time import sleep
n = randint(1,5)
print('\033[35m-=-\033[m' * 20)
print('\033[0;40mvou pensar em um numero tente advinhar\033[m')
print('\033[35m-=-\033[m' * 20)
u = int(input(' ja pensei agora advinhe meu numero de 1 a 5: '))

print('\033[1;31mprocessando......\033[m')
sleep(1)
if u == n:
    print('ora ora temos um sherok rolmes')
else:
    print('haha muito burro')

print(f'\033[1;37;40mpensei no numero {n}\033[m')
