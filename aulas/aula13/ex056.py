somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
mulhermenor20 = 0
for p in range(1, 5):
    print(f'{p}º pessoa')
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo M/F:' )).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhermenor20 += 1
mediaidade = somaidade / 4
print(f'a media idade do grupo é de {mediaidade} anos')
print(f' o homem mais velho tem {maioridadehomem} anos e se chama {nomemaisvelho}')
print(f'temos {mulhermenor20} mulheres menores de 20 anos ')
