dist = float(input('quantos kms vc viajara ? '))
if dist >= 200:
   prç = dist * 0.45
else:
    prç = dist * 0.50
print(f' a passagem custa {prç}')
