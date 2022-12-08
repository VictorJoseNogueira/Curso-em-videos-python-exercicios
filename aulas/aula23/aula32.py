'''try:
    a = int(input('numero : '))
    b = int(input('numero: '))
    r = a/b
except(ValueError, TypeError):
    print('tivemos um problema com os dados enviados')
except ZeroDivisionError:
    print('é impossivel dividir um numero por zero ')
except KeyboardInterrupt:
    print('zé ruela nao digitou nada')

except Exception as erro:
    print(f' o problema encontrado foi {erro.__class__}')
else:
    print(f'o resultado foi {r:.2f}')
finally:
    print('volte sempre')'''

listaz = []