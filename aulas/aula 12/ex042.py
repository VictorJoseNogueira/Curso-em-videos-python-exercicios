from datetime import date
ano = date.today().year
print(ano)

nascimento = int(input('digite seu ano de nascimento: '))
idade = ano - nascimento

print(nascimento)
print('vc tem', ano-nascimento, 'anos')
print('sua categoria na natação é ', end='')
if idade <= 9:
    print('\033[32mmirim\033[m')
elif idade <= 14:
    print('\033[33minfantil\033[m')
elif idade <= 19:
    print('\033[34mjunior\033[m')
elif idade == 20:
    print('\033[35msenior\033[m')
else:
    print('\033[31mmaster\033[m')
