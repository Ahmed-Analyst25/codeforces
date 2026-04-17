# V : Comparison

expression = input().strip()

expression = expression.replace("=", "==")

print("Right" if eval(expression) else "Wrong")
