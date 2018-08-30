s = str(input())
count_f = s.count('f')
if count_f == 0:
	pass
if count_f == 1:
	print(s.find('f'))
if count_f >= 2:
	print(s.find('f'), s.rfind('f'))