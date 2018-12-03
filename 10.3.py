a, b = sorted(set(input().split()).intersection(set(input().split()))), []
for i in a:
    b.append(int(i))
b = sorted(b)
for g in b:
    print(g, end=' ')
