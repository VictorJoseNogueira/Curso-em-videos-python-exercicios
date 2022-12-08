from time import sleep
cont = 0
while True:
    print('--' * 30)
    n = int(input('qual numero gostaria de ver a tabuada ?\n [caso queira encerrar o programa digite qualquer numero negativo]'))
    cont = 0
    if n < 0:
        break
    while cont <= 10:#podia ter usado o For in range(1,11)
        produto = n * cont
        print(f'\033[34m{n} x {cont} = {produto}\033[m')
        cont += 1
print('processando....')
sleep(1)
print('\033[31mprograma encerrado volte sempre\033[m')
