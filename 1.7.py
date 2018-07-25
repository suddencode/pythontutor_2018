a, b ,c = int(input()), int(input()), int(input())
p1a = a % 2
p2a = a//2 + p1a
p1b = b % 2
p2b = b//2 + p1b
p1c = c % 2
p2c = c//2 + p1c
print(p2a + p2b + p2c)