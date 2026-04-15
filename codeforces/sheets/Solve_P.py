# P : First digit !

x = int(input())

while x >= 10:
    x //= 10

if x % 2 == 0:
    print("EVEN")
else:
    print("ODD")
