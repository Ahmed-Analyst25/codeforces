# Z : Hard Compare

import math
A, B, C, D= map(int, input().split())
print("YES" if B * math.log(A) > D * math.log(C) else "NO")
