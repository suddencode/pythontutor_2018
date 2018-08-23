a, b = int(input()), int(input())
if a % 2 != 0:
    for i in range (a, b - 1, -2):
        print(i-1, end=' ')
else:
    for i in range (a, b - 1, -2):
        print(i-1, end=' ')