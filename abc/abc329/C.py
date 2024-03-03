N = int(input())
S = input()

ans = list()

for i in range(len(S) + 1):
    for j in range(i + 1, len(S) + 1):
        if S[i] == S[j]:
            ans.append(S[i:j])
        else:
            break

print(len(set(ans)))

