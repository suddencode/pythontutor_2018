n, x = int(input()), 0
a = [[-1] * n for i in range(n)]
for g in range (n):
	for i in range(n):
		for j in range(n):
			if i == (j + x) or i == (j - x):
				a[i][j] = x
	x += 1
for row in a:
	print(' '.join([str(elem) for elem in row]))
