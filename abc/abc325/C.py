from collections import deque

h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]

def bfs(S, i, j):
    dq = deque([(i, j)])
    S[i][j] = "."
    while dq:
        x, y = dq.popleft()
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                if not(0 <= nx < h and 0 <= ny < w): continue
                if S[nx][ny] == ".": continue
                S[nx][ny] = "."
                dq.append((nx, ny))
    return S

cnt = 0
for i in range(h):
    for j in range(w):
        if S[i][j] == ".": continue
        S = bfs(S, i, j)
        cnt += 1
print(cnt)