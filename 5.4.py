stroka = str(input())
ind = stroka.find(' ')
print(stroka[ind+1:], stroka[:ind], sep=' ')
