P, X, Y = int(input()), int(input()), int(input())
XP, YP = (X / 100)*P, int((Y / 100)*P)
money1 = (XP + X)+(YP + Y)/100
print (int(money1), ((money1 - int(money1))*100))