n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 0
for i in range(n):
    ans += abs(A[i] - B[i])

print(ans)