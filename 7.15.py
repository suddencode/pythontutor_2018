a = input()
b = a.split()
N = int(b[0])
K = int(b[1])
kl = []
for i in range (K):
	kn = input()
	kns = kn.split()
	e1 = int(kns[0])
	e2 = int(kns[1])
	kl.append(e1)
	kl.append(e2)
keg = []
for y in range(N):
	keg.append('I')
h = 0
for g in range(K):
	for w in range(N):
		if keg[w] != '.':
			if w in range(kl[h]-1,kl[h+1]):
				keg[w] = '.'
	h += 2
print(''.join(keg))
