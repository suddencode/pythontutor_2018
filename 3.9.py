h, a, b = int(input()), int(input()), int(input())
x = 0
day = 0
while x < h:
	day = day + 1
	x = x + a
	if x >= h:
		print(day)
	else:
		x = x - b