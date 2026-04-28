# B - Memo & Momo

a, b, x = map(int, input().split())

if a % x == 0 and b % x == 0:
    print("Both")
elif a % x == 0 and b % x != 0:
    print("Memo")
elif a % x != 0 and b % x == 0:
    print("Momo")
else:
    print("No One")
