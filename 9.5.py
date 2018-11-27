n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
	for j in range(n):
		if j + (i+1) == n:
			a[i][j] = 1
		elif j + (i+1) > n:
			a[i][j] = 2
for row in a:
	print(' '.join([str(elem) for elem in row]))
