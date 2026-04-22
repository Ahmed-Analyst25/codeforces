# C - Next Alphabet

c = input().strip()

print('a' if c == 'z' else chr(ord(c) + 1))

# print(chr((ord(input()) - 97 + 1) % 26 + 97))
