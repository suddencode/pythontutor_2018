n, m, k = int(input()), int(input()), int(input())
x = (n*m)-k
if (((m%x) == 0) or ((n%x) == 0) or ((x%m) == 0) or ((x%n) == 0)) and ((n*m) > k) and ((((n*m)-k) >= n) or (((n*m)-k) >= m)):
	print('YES')
else:
	print('NO')