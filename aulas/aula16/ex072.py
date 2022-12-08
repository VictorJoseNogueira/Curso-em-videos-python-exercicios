numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('digite um numero entre (0 e 20): '))
while n > 20 or n < 0:
    n = int(input('vc é burro ? é de 0 a 20. tente novamente: '))
print(f'vc digitou o numero {numero[n]}')
