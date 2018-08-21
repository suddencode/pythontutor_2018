a = float(input())
time_in_seconds = a*120
h = time_in_seconds//3600
m = (time_in_seconds - (h*3600))//60
s = (time_in_seconds - (h*3600)) - m*60
print(int(h), int(m), int(s))
