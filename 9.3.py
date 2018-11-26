my_list = list(input().split())
n, m = int(my_list[0]), int(my_list[1])
a = [['.'] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i % 2) == 0 and (j % 2) == 1:
            a[i][j] = '*'
        elif (i % 2) == 1 and (j % 2) == 0:
            a[i][j] = '*'
for row in a:
    print(' '.join([str(elem) for elem in row]))
