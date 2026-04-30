# C - Even, Odd, Positive and Negative

n = int(input())
numbers = list(map(int, input().split()))

even = odd = positive = negative = 0

for x in numbers:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1

print(f"Even: {even}")
print(f"Odd: {odd}")
print(f"Positive: {positive}")
print(f"Negative: {negative}")
