a, c = [int(s) for s in input().split()], 1
for i in range (len(a)-1):
	if a[i] != a[i+1]:
		c += 1
print(c)
