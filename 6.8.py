i, x, = 0, 0
while i < 1:
	n = int(input())
	if x < n:
		x = n
	if n == 0:
		break
print(x)