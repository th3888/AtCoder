from collections import defaultdict

N = int(input())
ac = [list(map(int, input().split())) for _ in range(N)]

inf = float('INF')
taste = defaultdict(lambda: inf)

for a, c in ac:
    taste[c] = min(taste[c], a)

ans = 0

for min_a in taste.values():
    ans = max(min_a, ans)

print(ans)