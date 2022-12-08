import random
spds = [30,40,50,60,70,80,90,100]
lmt = random.choice(spds)
spd = int(input('sabe a quantos km/h vc estava ? '))
print(f'vc estava a {spd} numa vida de {lmt}')
if spd > lmt:
    multa = (spd - lmt) * 7
    print(f'parabens vc ganhou uma multa de R$ {multa} reais')
else:
    print('muito bem, prociga entao: ')