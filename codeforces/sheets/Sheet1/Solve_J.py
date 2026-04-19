# J : Multiples

x, y = map(int, input().split())
print("Multiples" if max(x, y) % min(x, y) == 0 else "No Multiples")
