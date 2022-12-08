import time
peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
print('\033[34mprocessando......\033[m')
time.sleep(1.5)
if altura.is_integer():
        altura = altura / 100
imc = peso / altura ** 2
if imc < 18.5:
    print('\033[31mabaixo do peso\033[m')
elif imc >= 18.5 and imc < 25:
    print('peso ideal\033[m')
elif imc >= 25 and imc < 30:
    print('sobre peso\033[m')
elif imc >= 30 and imc <40:
    print('\033[31mobesidade\033[m')
elif imc >=40:
    print('\033[31mobesidade morbida, cuidado\033[m')
print(f'{imc:.2f}')