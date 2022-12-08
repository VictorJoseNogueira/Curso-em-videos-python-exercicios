#sistema de aproveitamento de jogadores
jogadores = {}
banco = []
gols = []
saldogol = 0
while True:
    gols.clear()
    jogadores.clear()
    jogador = str(input('Digite o nome do jogador: '))
    partidas = int(input('quantas partidas ele jogou ? '))
    for c in range(0, partidas):
        gol = int(input(f'quantos gols ele fez na {c+1}º partida: '))
        gols.append(gol)
        saldogol += gol
    jogadores['jogador'] = jogador
    jogadores['gols'] = gols.copy()
    jogadores['saldo gol'] = saldogol
    saldogol = 0
    banco.append(jogadores.copy())
    while True:
        pergunta = str(input('deseja continuar ? [S/N]')).strip().upper()[0]
        if pergunta in "SN":
            break
        print('ERRO! por favor digite apenas "S" ou "N"')
    if pergunta in 'Nn':
        break
print('-'*100)
print('cod ', end='')
for i in jogadores.keys():
    print(f'{i:<15}', end='')
print()
print('-'*100)
for k, v in enumerate(banco):
    print(f'{k:>3}º ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 100)
while True:
    busca = int(input('mostrar dados de qual jogador? (999 para)'))
    if busca == 999:
        break
    if busca >= len(banco):
        print('\033[31mERRO! JOGADOR NAO ENCONTRADO\033[m')
    else:
        print(f'LEVANTAMENTO DO JOGADOR: `{banco[busca]["jogador"]}: ')
        for i, g in enumerate(banco[busca]['gols']):
            print(f'    no  {i+1}º jogo fez {g} gols')
    print('-' * 100)
