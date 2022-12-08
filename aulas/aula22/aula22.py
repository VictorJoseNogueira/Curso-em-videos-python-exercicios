from uteis import numeros


num = int(input('digite um numero: '))
fato = numeros.fac(num)
print(f' o fatorial de {num} é {fato}')
print(f' o dobro de {num} é {numeros.dobro(num)}')
print(f'o triplo de {num} é {numeros.triplo(num)}')
