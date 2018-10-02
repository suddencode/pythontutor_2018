a, c = input().split(), 0
for i in range(1,len(a)-1):
	if int(a[i-1]) < int(a[i]) > int(a[i+1]):
		c += 1
print(c)