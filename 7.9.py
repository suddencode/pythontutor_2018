a = [int(s) for s in input().split()]
b = []
if len(a) % 2 == 0:
    for i in range (0, len(a), 2):
        b += a[i+1], a[i]
else:
    for i in range (0, len(a)-1, 2):
        b += a[i+1], a[i]
    b.append(a[-1])
print(' '.join([str(i) for i in b]))
