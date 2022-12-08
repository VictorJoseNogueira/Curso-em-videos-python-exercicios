total = {}
gols = []
saldo = 0
total['jogador'] = str(input('digite o nome do jogador: ')).strip().capitalize()
partidas = int(input('quantas partidas ele jogou? '))
for c in range(0, partidas):
    g = (int(input(f'quantos gols ele fez na {c+1}º partida: ')))
    gols.append(g)
    saldo += g
total['gol'] = gols.copy()

total['saldo'] = saldo
print('=-'* 30)
print(total)
print('=-'* 30)
for k, v in total.items():
    print(f'{k}: {v}')
print('=-'* 30)
print(f'o jogador {total["jogador"]} jogou {partidas} partidas ')
for l, o in enumerate(gols):
    print(f'======>na partida {l+1}ª ele fez {o} gols')
print(f'foi um total de {total["saldo"]}')
