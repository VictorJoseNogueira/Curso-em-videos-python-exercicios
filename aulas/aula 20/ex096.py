def area():
    l = float(input("digite a largura do terrreno: "))
    c = float(input('digite o comprimento do terreno: '))
    print(f'a area desse terreno com {l} m de largura e {c} m de comprimento é {l * c}m²')
def erro():
    print('-' * 40)
    print('\033[31mERRO!\033[m por favor responda com \033[34mS\033[m ou \033[31mN\033[m')
    print('-' * 40)


while True:
    area()
    resp = str(input('Deseja saber a area de outro terreno? [S/N]')).strip().upper()[0]
    if resp in "Nn":
        print('ENCERRANDO PROGRAMA.....')
        break
    elif resp in "sS":
        print('certo...')
    else:
        erro()
'''def area(larg, comp):
    a = larg * comp 
    print(f' a area do terreno é de {comp}x{larg}={a}m²
    l = input
    c = input
    area(l, c)'''
