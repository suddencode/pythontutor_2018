def swap_columns(a, i, j):
	for x in a:
		x[i],x[j]=x[j],x[i]
my_list_1 = list(input().split())
n, m = int(my_list_1[0]), int(my_list_1[1])
a = [[int(j) for j in input().split()] for i in range(n)]
my_list_2 = list(input().split())
i, j = int(my_list_2[0]), int(my_list_2[1])
swap_columns(a, i, j)
for row in a:
    print(' '.join([str(elem) for elem in row]))
