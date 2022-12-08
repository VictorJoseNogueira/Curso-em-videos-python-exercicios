nome = str(input('digite seu nome completo: ')).strip()
ng = nome.lower().count('silva')
print(f'seu nome tem silva?', {'silva' in nome.lower()})

if ng >= 1:
    print('sim vc tem silva zé')
else:
    print('nao vc nao tem silva zé')
