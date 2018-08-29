stroka = str(input())
stroka_len = len(stroka)
polovina_1 = stroka_len//2
polovina_2 = stroka_len - polovina_1
print(stroka[polovina_2:], stroka[:polovina_2], sep = '')