n = int(input('escolha um numero inteiro qualquer: '))
base = int(input('''por favor escolha entre
1 [binaria]
2 [octal]
3 [hexadecimal]
'''))
if base == 1:
    print(f'{n} convertido para binario é igual a...{bin(n)[2:]}')
elif base == 2:
    print(f'{n} convertido para octal é igual a...{oct(n)[2:]}')
elif base == 3:
    print(f'{n} convertido para hexadecimal é igual a...{hex(n)[2:]}')

else:
    print('opção invalida tente novamente')