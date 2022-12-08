#palindromo
frase = str(input('digite uma frase: ')).strip().upper()#li a frase
palavras = frase.split()#separei ela em palavras
jnt = ''.join(palavras)#juntei todas sem os espaços
inverso = ''
inverso = jnt[::-1]#inverti as palavras
'''for letra in range(len(jnt) - 1, -1, -1):#inverti as palavras
    inverso += jnt[letra]'''
print(f'o inverso de {jnt} é {inverso}')
if inverso == jnt:
    print('temos um palindromo')
else:
    print('nao temos um palindromo')
