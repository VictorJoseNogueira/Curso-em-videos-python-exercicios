def leiaint():
    while True:
        n = input('digite um numero: ')
        if n.isnumeric():
            return n   #return funciona como brake
        else:
            print('\033[31m ERRO! por favor digite um numero inteiro, valido!\033[m')



nume = leiaint()
print(f'o numero digitado foi {nume}')