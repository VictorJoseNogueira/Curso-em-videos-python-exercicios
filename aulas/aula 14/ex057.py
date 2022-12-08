sexo = str(input('qual seu sexo ? M/F ')).strip().upper()[0]
while sexo not in 'MFmf':
    print('\033[31mopção nao aceita tente novamente\033[m')
    sexo = str(input('qual seu sexo ? M/F ')).strip().upper()[0]

print(f'\033[34msexo {sexo} registrado com sucesso \033[m')
