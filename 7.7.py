a, b, d = [int(s) for s in input().split()], int(input()), 0
c = a.append(b)
a.sort()
a.reverse()
for i in range (len(a)):
    if a[i] == b:
        d = i
print(d + 1)