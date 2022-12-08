from random import randint
from time import sleep
print('-' * 30)
print('      MEGA SENA PALPITES        ')
print('-' * 30)
qntd = int(input('quantos jogos deseja que eu crie ?'))
jogo = []
jogos = []
u = 0
for q in range(0, qntd):
    while len(jogo) < 6:
        u = randint(1, 60)
        if u not in jogo:
            jogo.append(u)

    jogos.append(jogo[:])
    jogo.clear()
print('=-'*30)
print('<<<<<<<', f'SORTEANDO {qntd} jogos', '>>>>>>>')
sleep(1)
for q in range(0, len(jogos)):
    print(f'jogo {q+1}º{sorted(jogos[q])}\n')
    sleep(0.5)
print('-' * 30)
print(f'{"BOA SORTE":^30}')
print('-' * 30)
