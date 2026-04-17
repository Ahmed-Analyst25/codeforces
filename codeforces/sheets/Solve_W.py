# W : Mathematical Expression

expression, result = input().split("=")
output = eval(expression)
print("Yes" if output == int(result) else output)
