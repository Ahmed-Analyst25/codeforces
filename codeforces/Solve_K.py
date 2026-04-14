# K : Max and Min

numbers = list(map(int, input().split()))
max_number = numbers[0]
min_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number
print(min_number, max_number, sep = " ")


# Note : Best Practise Solution

l = *map(int, input().split()),
print(min(l), max(l))