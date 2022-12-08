import random
num = random.randint(0,10000)

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'o numero tem {num} {m} milhares, {c} centenas {d} dezenas e {u} unidades')
