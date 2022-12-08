maior = menor = 0
n = []
for c in range(0, 5):
    n.append(input(f'digite um valor para a {c+1}º posição : '))
    if c == 0:
        maior = menor = n[c]
    else:
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor = n[c]

print(n)
print(f'o maior é {maior} e ele esta nas posiçoes', end='')
for i, v in enumerate(n):
    if v == maior:
        print(f' {i+1}...', end='')
print(f'\n o menor é {menor} e ele esta nas posiçoes', end='')
for i, v in enumerate(n):
    if v == menor:
        print(f' {i+1}...', end='')
