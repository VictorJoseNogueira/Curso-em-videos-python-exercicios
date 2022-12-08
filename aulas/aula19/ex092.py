import datetime
from datetime import date
cadastro = {}
cadastro['nome'] = str(input('digite seu nome: ')).strip().capitalize()
ano = int(input('digite o ano do seu nascimento[yyyy]'))
cadastro['idade'] = date.today().year - ano
cadastro['carteira de trabalho'] = int(input('digite o numero da sua carteira de trabalho'))
if cadastro['carteira de trabalho'] > 0:
    cadastro['ano de contratação'] = int(input('digite o ano da sua contratação'))
    cadastro['salario'] = float(input('digite o seu salario atual: R$ '))
    cadastro['aposentadoria'] = (cadastro['ano de contratação'] - ano) + 35
print(cadastro)
for k, v in cadastro.items():
    print(f'{k}: {v}')
#pessoas cadastradas

