from collections import defaultdict

N = int(input())
ac = [map(int, input().split()) for _ in range(N)]
a, c = [list(i) for i in zip(*ac)]

taste = defaultdict(int)

