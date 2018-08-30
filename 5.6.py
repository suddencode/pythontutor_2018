s = str(input())
count_f = s.count('f')
if count_f == 0:
	print(-2)
if count_f == 1:
	print(-1)
if count_f >= 2:
	ind1 = s.find('f')
	s2 = s[ind1+1:]
	print(ind1+s2.find('f')+1)
