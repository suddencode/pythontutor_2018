s = str(input())
a, b = s.find('h'), s.rfind('h')+1
old = s[a:b]
old2 = old[::-1]
new = s.replace(old, old2)
print(new)
