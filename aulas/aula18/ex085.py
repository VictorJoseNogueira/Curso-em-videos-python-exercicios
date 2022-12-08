from random import randint
todos = [[], []]
for c in range(0, 7):
    n = randint(0, 999)
    if n % 2 == 0:
        todos[0].append(n)
    else:
        todos[1].append(n)
todos[0].sort()
todos[1].sort()
print(f'os numeros pares sao : {todos[0]}')
print(f'os numeros impares sao: {todos[1]}')
