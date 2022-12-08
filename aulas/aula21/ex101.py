def voto(nascimento):
    from datetime import date
    year = date.today().year
    idade = year - nascimento
    if 15 >= idade:
        return  f'com {idade} anos, seu voto é proibido'
    elif 15 < idade <= 18 or idade > 65:
        return f'com {idade} anos, seu voto é opcional'
    else:
        return f'com {idade} anos, seu voto é obrigatorio'


nascimento = int(input('digite o ano de nacimento: '))
print(voto(nascimento))
