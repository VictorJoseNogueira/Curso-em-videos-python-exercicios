from  time import sleep
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except Exception as erro:
            print('\033[31m ERRO! por favor digite um numero inteiro, valido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mok...encerrando programa\033[m')
            sleep(2)
            return 3
        else:
            sleep(2)
            return n


def leiafloat(msg):
    while True:
        try:
            f = float(input(msg))
        except Exception as erro:
            print('\033[31m ERRO! por favor digite um numero inteiro, valido!\033[m')
            continue
        else:
            return f'{f}'.replace('.', ',')



