N, Q = map(int, input().split())
A = list(range(N + 1))
idx = list(range(N + 1))

for _ in range(Q):
    x = int(input())
    fi = idx[x]
    si = fi + 1 if fi != N else fi - 1
    y = A[si]
    A[fi], A[si] = A[si], A[fi]
    idx[x] = si
    idx[y] = fi

print(*A[1:])