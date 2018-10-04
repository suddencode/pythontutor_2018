a = [int(s) for s in input().split()]
if len(a) == 1:
    print(' '.join([str(i) for i in a]))
else:
    b = []
    b += a
    max_a = max(a)
    min_a = min(a)
    i_max_a = a.index(max_a)
    i_min_a = a.index(min_a)
    b.remove(max(a))
    b.remove(min(a))
    b.insert(i_min_a, max_a)
    b.insert(i_max_a, min_a)
    print(' '.join([str(i) for i in b]))
