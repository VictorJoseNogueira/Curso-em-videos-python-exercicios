s = tuple(int(input('Digite valores '))for c in range(1, 5))
print(s)
print(f' 9 apareceu {s.count(9)} vezes ')
print(f' o numero 3 apareceu pela primeira vez na {s.index(3)+1}º posição' if 3 in s else 'nao temos numero 3')
print('os numeros pares sao ', end='')
for n in s:
    if n % 2 == 0:
        print(n, end=' ')
