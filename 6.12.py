n, max_n_1, max_n_2 = -1, 0, -1
while n != 0:
	n = int(input())
	if n > max_n_1 > max_n_2:
		max_n_2 = max_n_1
		max_n_1 = n
	if max_n_2 < n < max_n_1:
		max_n_2 = n
print(max_n_2)