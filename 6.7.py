i, total, amount = 0, 0, 0
while i < 1:
	n = int(input())
	if n == 0:
		break
	total += n
	amount += 1
print(total / amount)
