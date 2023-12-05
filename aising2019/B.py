N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

c, d, e = 0, 0, 0

for i in range(N):
    if P[i] <= A:
        c += 1
    elif A + 1 <= P[i] <= B:
        d += 1
    else:
        e += 1

print(min(c, d, e))