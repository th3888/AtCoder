n, x, y, z= map(int, input().split())

up = list(range(x, y + 1))
down = list(range(x, y - 1, -1))

if z in up or z in down:
    print('Yes')
else:
    print('No')