palavras = ('lista', 'palavras', 'jabuticaba', 'amor', 'linda', 'vida')

for t in palavras:
    print(f'\n na palavra {t.upper()} temos ', end='')
    for letra in t:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\n', palavras)
