N = int(input())
S = input()

ans = 0

for i in range(1, N):
    X = S[:i]
    Y = S[i:]

    co = len(set(X) & set(Y))

    if ans < co:
        ans = co

print(ans)