# I - Lucky Numbers

x = int(input())

a = x // 10
b = x % 10

if (b != 0 and a % b == 0) or (a != 0 and b % a == 0):
    print("YES")
else:
    print("NO")
