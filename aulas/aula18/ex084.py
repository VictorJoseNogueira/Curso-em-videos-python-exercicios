temp = []
pr = []
mai = men = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('peso: ')))
    if len(pr) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    pr.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar ? [S/N]')).strip()[0]
    if resp in 'Nn':
        break

print(f' vc cadastrou {len(pr)} pessoas ao todo')
print(f' o maior peso foi de: {mai}')
for p in pr:
    if p[1] == mai:
        print(f'{p[0]}', end=', ')

print(f'\n o menor peso foi de: {men}')
for p in pr:
    if p[1] == men:
        print(f'{p[0]}', end=', ')
