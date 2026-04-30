# D - Fixed Password

tries = []

while True:
    entered_value = int(input())
    if entered_value != 1999:
        tries.append("Wrong")
    else:
        tries.append("Correct")
        break

for t in tries:
    print(t)
