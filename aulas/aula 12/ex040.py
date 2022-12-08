from datetime import date

year = date.today().year
print(f"Current Year -> {year}")

ano = int(input('em que ano vc nasceu ? '))
dt = year - ano
tempo = 18 - dt
print(f'vc tem {dt} anos')
if dt < 18:
    tempo = 18 - dt
    print('ainda tem tempo antes do alistamento ')
    print(ano+18, 'ano de alistamento militar ')
    print(f'vc tem {tempo} anos para se alistar')
elif dt == 18:
    tempo == 0
    print('vai se alistar vagabundo')
    print('preparesse para se alistar')

else:
    tempo = dt - 18
    print('ja passou do tempo do alistamento')
    print('vc deveria ter se alistado em', ano + 18, )
    print(f'vc esta {tempo} anos atrasado')

print(f'vc tem {dt} anos')
