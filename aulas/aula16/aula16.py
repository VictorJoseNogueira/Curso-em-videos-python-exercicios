'''from time import sleep
from random import choice

lanche = ('suco', 'burger', 'pudim', 'pizza', 'batata frita')
abc = ('a', 'h', 'b', 'c', 'j', 'k', 'm', 'z')

#print(lanche[2:])
#print(lanche[:2])
#print(lanche[1:3])
#print(lanche[1:2])
#tuplas sao imutaveis
#lanche[1] = 'sanduiche'
for comida in range(0, len(lanche)):
    #print(f'eu vou comer {lanche[comida]} na posicao {comida}')
# para momentos em que funciona apenas um
for pos, cont in enumerate(lanche):
    print(f'vou comer {cont} na posição {pos}')
print(sorted(lanche))
print(sorted(abc))
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = (a+b)
d = (b+a)
print(c, d)
print(len(c))
print(c.count(5))
print(d.index(8))
print(d.index(5, 1))
pessoa = ('gustavo', 39, 'm', 99.88)
#del pessoa# tupla é imutavel, mas deletavel
print(pessoa)
