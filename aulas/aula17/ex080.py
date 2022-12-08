l = []

for c in range(0, 5):
    n = int(input('digite um valor: '))
    if c == 0 or n > l[-1]:
        l.append(n)
    else:
        pos = 0
        while pos < len(l):
            if n <= l[pos]:
                l.insert(pos, n)
                break
            pos += 1
print(l)

