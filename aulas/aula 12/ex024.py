cidade = str(input('digite sua cidade: '))
cdd = cidade.split()
cdc = cdd[0].lower().count('santo')
if cdc == 1:
    print('a cidade começa com santo')
else:
    print('a cidade nao começa com santo')
#jeito que o video ensina
#cid = str(input('onde tu nasceu? ').strip()
#print(cid[:5].lower() == 'santo'
