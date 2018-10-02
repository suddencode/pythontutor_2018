a, b = input().split(), ''
for i in range (len(a)):
	if int(a[i]) % 2 == 0:
		b += a[i] + ' '
print(b[:-1])
