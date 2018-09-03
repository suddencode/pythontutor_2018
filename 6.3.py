n, x, i = int(input()), 1, 0
while n >= x:
	if x*2 > n:
		break
	i += 1
	x = x*2
print(i, x)