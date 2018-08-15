from math import ceil
t1 = 540
p_small = 5
p_big = 15
a = int(input())
p_small_n = a//2
p_big_n = ceil(a/2)
t2 = (p_small_n * p_small) + (p_big_n * p_big) + (a * 45) + 540 - 15
h = t2 // 60
m = t2 % 60
print(h, m)