import bisect

n = int(input())

A = list(map(int, input().split()))

q = int(input())

B = []
for i in range(q):
    B.append(int(input()))

A.sort()

for i in range(q):
    tmp1 = int(1e9)
    tmp2 = int(1e9)
    num = bisect.bisect_left(A, B[i])
    if num >= 1:
        tmp1 = abs(A[num-1] - B[i])
    if num <= n-1:
        tmp2 = abs(A[num] - B[i])
    ans = min(tmp1, tmp2)
    print(ans)