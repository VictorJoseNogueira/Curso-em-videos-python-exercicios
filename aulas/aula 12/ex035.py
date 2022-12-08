salario = float(input('qual seu salario ? '))
if salario > 1251:
    aumento = (salario/100)* 10 + salario
    print(f' se seu salario é  {salario} vamos aumentar para {aumento}')
else:
    aumento = (salario / 100) * 15 + salario
    print(f' se seu salario é  {salario} vamos aumentar para {aumento}')