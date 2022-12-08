boletin = {}
boletin['aluno'] = str(input('digite seu nome: '))
boletin['media'] = float(input('digite sua media: '))
if boletin['media'] >= 7:
    boletin['situação'] = 'aprovado'
elif 5 <= boletin['media'] < 7:
    boletin['situação'] = 'recuperação'
else:
    boletin['situação'] = 'reprovado'
print('=-'* 30)
for k , v in boletin.items():
    print(f'{k}: {v}')

print(f" o aluno {boletin['aluno']} teve como media final {boletin['media']}\n e por isso sua situação atual é de {boletin['situação']}")