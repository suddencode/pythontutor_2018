x = int(input())
n = 0
s = 0
s_sq = 0
while x != 0:
	n += 1
	s += x
	s_sq += x ** 2
	x = int(input())
print(((s_sq - s ** 2 / n) / (n - 1)) ** 0.5)