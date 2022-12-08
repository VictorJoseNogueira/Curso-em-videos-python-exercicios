from calendar import isleap
ano = int(input('qual o ano sr ? '))
#if isleap(ano):
#   print('é bicesto')
#else:
#    print('num é')
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é bicesto')
else:
    print(f' {ano} nao é bicesto')
