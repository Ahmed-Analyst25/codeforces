
# S : Interval

number = float(input())

if 0 <= number <= 25:
    print("Interval [0,25]")
elif 25 < number <= 50:
    print("Interval (25,50]")
elif 50 < number <= 75:
    print("Interval (50,75]")
elif 75 < number <= 100:
    print("Interval (75,100]")
else:
    print("Out of Intervals")