alunos = []
nota = []
nt = 0
boletin = []
while True:
    pg = str(input('deseja cadastrar mais algum aluno: [S/N]')).strip()[0]
    if pg in 'Ss':
        alunos.append(str(input('digite o nome do aluno: ')))
        for q in range(0, 2):
            nt = float(input(f'digite a {q+1}º nota: '))
            nota.append(nt)
        alunos.append(nota[:])
        nota.clear()
        boletin.append(alunos[:])
        alunos.clear()
    elif pg in 'Nn':
        print('isso é tudo entao')
        break
print('=-'*20)
print('nº. Nome              MEDIA')
print('=-'*20)

media = 0
for c in range(len(boletin)):
    media = (boletin[c][1][0]+boletin[c][1][1]) / 2
    print(f'\033[34m{c}º ', f'{boletin[c][0]:<10}', f'{media:>11.1f}\033[m')
print('--'*20)
mostrar = 0
while True:
    pgt = int(input('a nota de qual aluno vc gostaria de ver ( 999 interrompe) ?'))

    if pgt == 999:
        break
    if pgt+1 > len(boletin) and pgt != 999:
        print('\033[31m Aluno nao encontrado\033[m')
    else:
        print(f'\033[34m as notas de {boletin[pgt][0]} foram: {boletin[pgt][1]}\033[m')