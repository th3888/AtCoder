N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

for i in range(N + 1):
    for j in range(N + 1):
        for k in range(N + 1):
            for l in range(N + 1):
                for m in range(N + 1):
                    if ((((A[i] * A[j] % P) * A[k] % P) * A[l] % P) * A[m]) == Q:
                        ans += 1

print(ans)