n, y, n2 = 666, -1, 0
while n != 0:
	n = int(input())
	if n > n2:
		y += 1
	n2 = n
print(y)
