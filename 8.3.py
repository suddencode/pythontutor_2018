def capitalize(word):
	x = ''
	for i in range(len(word)):
		f1 = word[i]
		f2 = f1[0].upper()
		f3 = (f2 + f1[1:])
		x += f3 + ' '
	return x
word = input().split()
print(capitalize(word))
