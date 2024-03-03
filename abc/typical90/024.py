N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

cnt = 0
for i in range(N):
    cnt += abs(A[i]-B[i])

ans = 'No'
if cnt <= K:
    if (K-cnt)%2 == 0:
        ans = 'Yes'
print(ans)