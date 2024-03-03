import sys
import math
sys.setrecursionlimit(10 ** 6)

a, b, c = map(int, input().split())

gcd_inp = math.gcd(c, math.gcd(a, b))
ans = a // gcd_inp - 1 + b // gcd_inp - 1 + c // gcd_inp - 1
print(ans)