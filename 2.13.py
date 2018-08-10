n, m, x, y = int(input()), int(input()), int(input()), int(input())
if n < m:
    n1 = n - x
    m1 = m - y
    if x < y and x < n and x < m and x < n1 and x < m1:
        print(x)
    if y < x and y < n and y < m and y < n1 and y < m1:
        print(y)
    if n < x and n < y and n < m and n < n1 and n < m1:
        print(n)
    if m < x and m < y and m < n and m < n1 and m < m1:
        print(m)
    if n1 < x and n1 < y and n1 < m and n1 < m and n1 < m1:
        print(n1)
    if m1 < x and m1 < y and m1 < n and m1 < n1 and m1 < n1:
        print(m1)
if m < n:
    n1 = n - y
    m1 = m - x
    if x < y and x < n and x < m and x < n1 and x < m1:
        print(x)
    if y < x and y < n and y < m and y < n1 and y < m1:
        print(y)
    if n < x and n < y and n < m and n < n1 and n < m1:
        print(n)
    if m < x and m < y and m < n and m < n1 and m < m1:
        print(m)
    if n1 < x and n1 < y and n1 < m and n1 < m and n1 < m1:
        print(n1)
    if m1 < x and m1 < y and m1 < n and m1 < n1 and m1 < n1:
        print(m1)