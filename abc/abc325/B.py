N = int(input())
W, X = [0] * N, [0] * N
for i in range(N):
    W[i], X[i] = map(int, input().split())

p_list = []

for i in range(25):
    p = 0
    for j in range(N):
        if 9 <= i + X[j] <= 17:
            p += W[j]
        elif i + X[j] >= 24:
            t = i + X[j] - 24
            if 9 <= t <= 17:
                p += W[j]
    
    p_list.append(p)

print(max(p_list))