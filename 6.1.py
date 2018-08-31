n, x, i = int(input()), 0, 1
while x < n:
	x = i*i
	i+=1
	if x > n:
		break
	print(x, end = ' ')
