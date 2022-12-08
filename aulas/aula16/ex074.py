from random import randint
n = (randint(0, 999), randint(0, 999), randint(0, 999),randint(0, 999),randint(0, 999))
print(n)
print(max(n), min(n))
'''from random import sample
a = tuple(sample(range(1000), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')#isso é mais efetivo'''