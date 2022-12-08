frase = str(input('digite uma frase: ')).strip()
fs = frase.lower().count('a')
ab = frase.lower().find('a')
az = frase.lower().rfind('a')

print(f'a letra "a" aparece {fs} vezes nessa frase ')
print(f'a primeira vez que ela aparece é no caracter {ab + 1}')
print(f'a ultima letra "a" aparece na posição {az + 1}')
