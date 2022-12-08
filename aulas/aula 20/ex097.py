def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'{msg:^{tam}}')
    print('~'*tam)


msg = str(input('digite sua mensagem: '))

escreva(msg)

