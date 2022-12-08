brasileirao = ('palmeiras', 'internacional', 'fluminense', 'corinthians', 'flamengo', 'atletico-pr', 'atletico-mg', 'fortaleza', 'sao paulo', 'america-mg', 'botafogo', 'santos', 'goias', 'bragantino', 'coritiba', 'cuiaba', 'ceara-sc', 'atletico-go', 'avai', 'juventude')
print(len(brasileirao))
h = -1

for c in range(0, len(brasileirao[:5])):
    print(f' o {brasileirao[c]} esta na {c+1}º posição')
print('=-' * 50)
for u in range(20, 16, -1):
    print(f'{brasileirao[h]} esta na {u}º posição')
    h -= 1
print('=-' * 50)
print(sorted(brasileirao))
print('=-'*50)
print(f' chapeconce esta na posição :{brasileirao.count("chapecoence")}' if brasileirao.count("chapecoence") > 0 else ' chapecoence esta abaixo da 20º posição' )
print('=-'*50)
