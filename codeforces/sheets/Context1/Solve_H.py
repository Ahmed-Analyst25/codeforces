# H - Data Type Guessing

n, k, a = map(int, input().split())

if (n * k) % a != 0:
    print("double")
else:
    result = (n * k) // a
    if -2147483648 <= result <= 2147483647:
        print("int")
    else:
        print("long long")
