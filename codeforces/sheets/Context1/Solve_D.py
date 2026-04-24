# D - Ali Baba and Puzzles

import sys

def solve():
    # Read input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Map inputs to integers a, b, c, and d
    a, b, c, d = map(int, input_data)

    # Check the 6 possible combinations of distinct operators
    # Python follows standard mathematical precedence (PEMDAS/BODMAS)
    if (a + b - c == d or
            a + b * c == d or
            a - b + c == d or
            a - b * c == d or
            a * b + c == d or
            a * b - c == d):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
