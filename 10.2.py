myArray = []
for i in range(2):
    myArray.append([int(j) for j in input().split()])
a, b = set(myArray[0]), set(myArray[1])
print(len(a.intersection(b)))
