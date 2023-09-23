N = int(input())
n = [int(x) for x in list(str(N))]

ans = True

for i in range(len(str(N)) - 1):
    if n[i] > n[i + 1]:
        continue
    else:
        ans = False

if ans:
    print('Yes')
else:
    print('No')