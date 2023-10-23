from collections import defaultdict

w = input()
cnt = defaultdict(int)

for i in w:
    cnt[i] += 1

ans = True

for j, k in cnt.items():
    if k % 2 == 1:
        ans = False

print('Yes' if ans else 'No')