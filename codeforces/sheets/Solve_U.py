# U : Float or int

# number = input()
# print(f"int {number}" if number.isdigit() else f"float {number}")

n = input().strip()

if '.' in n:
    a, b = n.split('.')

    if int(b) == 0:
        print("int", a)
    else:
        print("float", a, "." + b)
else:
    print("int", n)
