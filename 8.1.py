def distance(x1, y1, x2, y2):
    a = (x1 - x2)**2
    b = (y1 - y2)**2
    c = (a + b)**0.5
    return c
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(distance(x1, y1, x2, y2))