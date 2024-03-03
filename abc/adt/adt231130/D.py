n, m = map(int, input().split())

g = [[False] * n for _ in range(n)]

for _ in range(m):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  g[u][v] = True
  g[v][u] = True

ans = 0

for i in range(n):
  for j in range(i + 1, n):
    for k in range(j + 1, n):
      if g[i][j] and g[j][k] and g[k][i]:
        ans += 1

print(ans)
