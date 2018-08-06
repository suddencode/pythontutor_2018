x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
step = '0'
if (x2 == x1 + 2) or (x2 == x1 - 2):
	if (y1 == y2 + 1) or (y1 == y2 - 1):
		print('YES')
	else:
		print('NO')
elif (y2 == y1 + 2) or (y2 == y1 - 2):
	if (x1 == x2 + 1) or (x1 == x2 - 1):
		print('YES')
	else:
		print('NO')
else:
	print('NO')