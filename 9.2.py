n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if (i == j) or (j == n // 2) or (i == n // 2) or (j + (i+1) == n) :
            a[i][j] = '*'
for row in a:
    print(' '.join([str(elem) for elem in row]))
