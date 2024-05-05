S = input()
T = input()

ans = []
s = 0

for t in range(len(T)):
    if S[s] == T[t]:
        ans.append(t + 1)
        s += 1

print(*ans)