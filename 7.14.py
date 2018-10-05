a = [int(s) for s in input().split()]
c = ''
for f in range(len(a)):
	if a.count(a[f]) == 1:
		c += str(a[f]) + ' '
print(c)
