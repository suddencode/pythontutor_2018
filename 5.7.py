s = str(input())
a, b = s.find('h'), s.rfind('h')+1
old = s[a:b]
new = s.replace(old, '')
print(new)
