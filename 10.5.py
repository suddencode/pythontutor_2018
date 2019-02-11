NM = input()
N, M = int(NM[0]), int(NM[2])
nSet, mSet = set(), set()
for i in range(N):
		nSet.add(int(input()))
for j in range(M):
	mSet.add(int(input()))
print(len(nSet.intersection(mSet)))
matshList1 = list(nSet.intersection(mSet))
matshList1.sort()
for q in matshList1:
	print(q, end=' ')
print(end='\n')
print(len(nSet.difference(mSet)))
matshList2 = list(nSet.difference(mSet))
matshList2.sort()
for w in matshList2:
	print(w, end=' ')
print(end='\n')
print(len(mSet.difference(nSet)))
matshList3 = list(mSet.difference(nSet))
matshList3.sort()
for e in matshList3:
	print(e, end=' ')
print(end='\n')
