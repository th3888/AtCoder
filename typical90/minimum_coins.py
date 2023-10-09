N = int(input())
A, B, C = map(int, input().split())

ans = 10000

for x in range(10000):
    for y in range(10000):
        temp = A * x - B * y
        if temp % C != 0 or temp > N:
            continue
        z = (N - temp) // C
        if ans > x + y + z:
            ans = x + y + z

print(ans)