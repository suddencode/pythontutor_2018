a = int(input())
buf1 = 0
buf2 = 0
while a != 0:
	b = int(input())
	if a == b:
		buf1 += 1
		if buf1>buf2:
			buf2=buf1
	else:
		buf1=0
		a=b
print(buf2+1)
