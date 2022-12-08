from time import sleep
p1 = int(input('digite o primeiro termo: '))
r = int(input('digite a Razão: '))
pn = 1
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end='↠ ')
        termo += r
        cont += 1
    print('pausa...')
    mais = int(input('\nquantos termos a mais gostaria de ver ?'))
print(f'P.A. finalizada com {total} termos ')