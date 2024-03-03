N = int(input())
user = set()

for i in range(1, N + 1):
    S = input()
    if S in user:
        continue
    user.add(S)
    print(i)