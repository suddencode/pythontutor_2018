li = []
for i in range (8):
    inp = input()
    list_2 = inp.split()
    e1 = int(list_2[0])
    e2 = int(list_2[1])
    li.append(e1)
    li.append(e2)
end = 0
n = 1
b1, b2, b3, b4, b5, b6, b7, b8 = li[0:2], li[2:4], li[4:6], li[6:8], li[8:10], li[10:12], li[12:14], li[14:16]
b = [b1, b2, b3, b4, b5, b6, b7, b8]
for r in range (1,8):
    for j in range (0, 16, 2):
        n = 1
        for g in range(8):
            a1 = [li[j]+n, li[j+1]] #идем вправо
            a2 = [li[j]-n, li[j+1]] #идем влево
            a3 = [li[j], li[j+1]+n] #идем вверх
            a4 = [li[j], li[j+1]-n] #идем вниз
            a5 = [li[j]+n, li[j+1]+n] #идем вправо и вверх
            a6 = [li[j]-n, li[j+1]-n] #идем влево и вниз
            a7 = [li[j]+n, li[j+1]-n] #идем вправо и вниз
            a8 = [li[j]-n, li[j+1]+n]
            if b[r] in (a1,a2,a3,a4,a5,a6,a7,a8):
                print('YES')
                end += 1
                break
            n += 1
        if end != 0:
            break
    if end != 0:
        break
if end == 0:
    print('NO')