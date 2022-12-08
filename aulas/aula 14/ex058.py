from random import randint
score = 100
palpite = 0
computador = randint(0, 10)
print('COMPUTADOR: \033[31mMUAHAHAHA\033[m nos encontramos novamente, \033[31mjogador\033[m')
print('COMPUTADOR: dessa vez eu aumentei a dificuldade agora pensarei em numeros de \033[34m 0 a 10 \033[m')
print('COMPUTADOR: nesse jogo vc começara com 100 pontos e a cada erro perdera 10 pontos, quantos pontos tera no final????')
jogador = int(input('COMPUTADOR:Entao qual o seu palpite? '))

if jogador != computador:
    print('\033[31mCOMPUTADOR: HAHAHAHAHA NAO FOI NISSO QUE EU PENSEI \033[m')
    while jogador != computador:
        jogador = int(input('qual o seu palpite? '))
        if jogador != computador:
            score = score - 10
            palpite += 1
            print('\033[31mCOMPUTADOR: HAHAHAHAHA NAO FOI NISSO QUE EU PENSEI \033[m')

print(f'COMPUTADOR: acabou eu pensei em {computador} e vc disse {jogador} ')
print('COMPUTADOR:\033[31m VC GANHOU MAIS UMA VEZ.... MAS NAO ACHE QUE ISSO ACABOU MUAHAHAHAHAHA')
print(f'vc precisou de {palpite} palpites')
print(f'e sua pontuação foi {score}')
'''acertou = false
while not acertou:
jogador = input
if jogador == computador:
acertou = true'''