'''num = [2, 5, 9, 1]
num.append(7)
num[2]= 6
print(num)
num.sort(reverse=True)
print(num)
print(f'essa lista tem {len(num)}')
num.insert(0, 22)
print(num)
n = 0
nume = list(input('digite um numero'))
while n != 5:
    nume.append(input('digite outro numero'))
    n += 1
for v in nume:
    print(f'o valor é {v}...')
for c,  v in enumerate(nume):
    print(f'o valor é {v}... esta na posição {c}')
print('final da lista')'''
a = list[2, 4, 5, 7]
b = a[:]
b[2] = 0
print(f'lista a : {a}')
print(f'lista b : {b}')
