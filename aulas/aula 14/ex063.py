#fibonacci
#fn=fn-1+fn-2
print('~~'* 30)
print('divina proporção')
print('~~'* 30)
termo = int(input('sobre a divina proporção qual termo quer ler ?'))

ultimo = 1
primeiro = 0
fibo = 0
print(primeiro, end='↠')
while fibo <= termo:

    func = primeiro + ultimo

    print(func, end='↠')
    ultimo = primeiro
    primeiro = func
    fibo += 1

print(f'\no {termo}º termo de fibonacci é {func}')
print('~~' * 30)
