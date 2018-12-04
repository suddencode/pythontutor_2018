mySet = set()
myList = list(input().split())
for j, elem in enumerate(myList):
    myList[j] = int(elem)
for i in range(len(myList)):
	if myList[i] in mySet:
		print('YES')
	else:
		print('NO')
		mySet.add(myList[i])
