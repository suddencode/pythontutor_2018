def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
res = 0
a, n = float(input()), int(input())
print(power(a, n))
