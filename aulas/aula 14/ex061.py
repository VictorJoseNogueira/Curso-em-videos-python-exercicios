#pa
p1 = int(input('digite o primeiro termo: '))
r = int(input('digite a Razão: '))
pn = 1
termo = p1
while pn <= 10:
    print(termo, end='↠')
    termo += r
    pn += 1
print('fim')
