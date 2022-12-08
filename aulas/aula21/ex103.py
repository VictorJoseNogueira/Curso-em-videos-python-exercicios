def jogatina(jog='<DESCONHECIDO>', gols=0):

    jog = str(input('Nome do jogador: ')).strip().capitalize()
    gols = str(input('gols: '))
    if jog == '':
        jog = '<DESCONHECIDO>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    print(f'o jogador {jog} fez {gols} gol(s)')



jogatina()