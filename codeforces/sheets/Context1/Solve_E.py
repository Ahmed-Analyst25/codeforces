# E - Interval Sweep

x, y = map(int, input().split())

if abs(x - y) <= 1 and (x + y) > 0:
    print("YES")
else:
    print("NO")
