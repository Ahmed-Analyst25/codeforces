
# C : Simple Calculator

x, y = input().split()
print(
    f"{x} + {y} = {int(x) + int(y)}",
    f"{x} * {y} = {int(x) * int(y)}",
    f"{x} - {y} = {int(x) - int(y)}",
    sep = '\n'
)
