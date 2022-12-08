#leia o primeiro termo e a razao de um PA
p1 = int(input('digite o primeiro termo da pa: '))
r = int(input('digite a razao: '))
pn = int(input('digite o n-esimo numero: '))

pnf = p1 + (pn - 1) * r
for c in range(p1, pnf+r, r):
    print(c, end='↠')
print('acabou')
