# T : Sort Numbers

a, b, c = map(int, input().split())
print(*sorted([a, b, c], reverse = False), '',a, b, c, sep = '\n')

# Note : *[] ===> means to turn the list into separated values
