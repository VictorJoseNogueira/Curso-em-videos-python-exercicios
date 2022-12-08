nt1 = float(input('qual a nota da sua primeira prova ? '))
nt2 = float(input('qual a nota da sua segunda prova ? '))
media = (nt1 + nt2) / 2
if media < 5.0:
    print(f'\033[31mreprovado \033[m{media}')
elif 6.9 > media >= 5.0:
    print(f'vc esta de recuperaçao {media}')
else:
    print(f'parabens vc foi aprovado {media}')
