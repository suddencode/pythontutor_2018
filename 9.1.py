my_list = list(input().split())
n, m, t0 = int(my_list[0]), int(my_list[1]), -99999999999
a = [[int(m) for m in input().split()] for i in range(n)]
for i in range(n):
    for j in range(m):
        if t0 < a[i][j]:
            t0 = a[i][j]
            t1, t2 = i, j
        
print(t1, t2)
