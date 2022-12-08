#jokenpo
from random import choice
from time import sleep
pc = choice(['tesoura', 'papel', 'pedra'])
player = str(input('pedra, papel ou tesoura ? ')).strip().lower()
print('\033[32m-==-' * 20)
print('jo...')
sleep(0.5)
print('ken....')
sleep(0.5)
print('po!!!\033[m')
sleep(0.5)
print('-=-'*20, ' \033[36m')
print(f'computador jogou {pc} e player jogou {player}')
print('-=-'*20, '\033[m')

if player == 'papel' and pc == 'pedra':
    print('\033[34mplayer win....\033[31mthis time....\033[m')

elif player == 'papel' and pc == 'tesoura':
    print('\033[31mperdeu otarro\033[m')

elif player == 'tesoura' and pc == 'papel':
    print('\033[34mplayer win....\033[31mthis time....\033[m')

elif player == 'tesoura' and pc == 'pedra':
    print('\033[31mperdeu otarro\033[m')

elif player == 'pedra' and pc == 'tesoura':
    print('\033[34mplayer win....\033[31mthis time....\033[m')

elif player == 'pedra' and pc == 'papel':
    print('\033[31mperdeu otarro\033[m')
elif player == pc:
    print('empate')
else:
    print('\033[31m erro tente novamente\033[m')
