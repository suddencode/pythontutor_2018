a = input().split()
for i in range(len(a)-1):
	if (int(a[i]) > 0 and int(a[i+1]) > 0) or (int(a[i]) < 0 and int(a[i+1]) < 0):
		print(int(a[i]), int(a[i+1]))
		break
