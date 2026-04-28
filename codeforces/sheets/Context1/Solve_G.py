# G. Katryoshka

n, m, k = map(int, input().split())

# First use type (1 eye, 1 mouth, 1 body)
x = min(n, m, k)

n -= x
m -= x
k -= x

# Then use type (2 eyes, 1 body)
x += min(n // 2, k)

print(x)
