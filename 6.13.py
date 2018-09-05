n, max_n = -1, 0
x = 1
while n != 0:
	n = int(input())
	if n > max_n:
		max_n = n
		x = 1
	elif n == max_n:
		x += 1
print(x)