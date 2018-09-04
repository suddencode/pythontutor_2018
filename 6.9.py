n = 666
index = -1
x = 0
len = 0
while n != 0:
	n = int(input())
	if x < n:
		x = n
		index = len
	len += 1
print(index)
