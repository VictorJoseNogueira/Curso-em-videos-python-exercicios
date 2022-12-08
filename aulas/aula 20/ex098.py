from time import sleep
def l():
    print('-'*30)

def contador(inicio, fim, passo):
    n = inicio
    if passo > 0:
        for c in range(inicio, fim+1, passo):
            print(n, end=' ')
            n += passo
            sleep(0.5)
        print('\nFIM')
    elif passo < 0:
        for c in range(inicio, fim-1, passo):
            print(n, end=' ')
            n += passo
            sleep(0.5)
        print('\nFIM')
    elif passo == 0:
        if inicio < fim:
            passo = 1
            for c in  range(inicio, fim+1, passo):
                print(n, end=' ')
                n += 1
                sleep(0.5)
            print('\nFIM')

        elif inicio > fim:
            passo = -1
            for c in range(inicio, fim-1, passo):
                print(n, end=' ')
                n += -1
                sleep(0.5)
            print('\nFIM')
print('\ncontagem de 1 a 10 de  1 em 1: ')
contador(1, 10, 1)
l()
print('\ncontagem de 10 a 0 de -2 em -2')
contador(10, 0, -2)
l()
print('agora sua vez')
l()
i = int(input('inicio: '))
f = int(input('final: '))
p = int(input('de quanto em quanto: '))
contador(i, f, p)
