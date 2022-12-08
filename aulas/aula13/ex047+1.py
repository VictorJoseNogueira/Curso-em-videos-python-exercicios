n = int(input('digite um numero: '))
for cxx in range(2, n+1, 2):
    cx = cxx % 2
    print(end='.')
    if cx == 0:
        print(cxx, end='')
#jeito mais rapido
#   for n in range(2, 51, 2)
#print('acabou')
