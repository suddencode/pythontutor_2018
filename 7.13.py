a = [int(s) for s in input().split()]
c = 0
for i in range (len(a)):
	for j in range (i, len(a)-1):
		if a[i] == a[j+1]:
			c += 1
print(c)
