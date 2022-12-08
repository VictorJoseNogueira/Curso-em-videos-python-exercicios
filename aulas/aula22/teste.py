from ex111.utilidadescev.ex110 import moeda
from ex111.utilidadescev import dado
p = dado.leiadinheiro('digite o preço: R$')
x = int(input('aumentar: '))
y = int(input('diminuir: '))
moeda.resumo(p, x, y)
