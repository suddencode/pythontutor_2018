a = float(input())
time_in_seconds = a*120
time_in_h = (time_in_seconds//3600)
time_in_seconds_m = time_in_seconds - (time_in_h*3600)
minutes = time_in_seconds_m/60
print(float(minutes*6))
