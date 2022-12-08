nome = str(input('digite seu nome completo: ')).strip()
print(f'muito prazer {nome}')
pn = nome.split()
print(f'vi que seu primeiro nome é {pn[0]} e seu ultimo nome é {pn[len(pn)-1]}')
