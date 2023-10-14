N = int(input())
A = list(map(int, input().split()))

ans = False

if len(set(A)) == 1:
    ans = True

if ans:
    print('Yes')
else:
    print('No')