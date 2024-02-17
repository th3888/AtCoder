N = int(input())

ans = ""

for i in range(2 * N + 1):
    if i % 2 == 1:
        ans = ans + "0"
    else:
        ans = ans + "1"

print(ans)