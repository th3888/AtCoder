H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

hor = list(map(sum, A))
ver = list(map(sum, zip(*A)))

for i in range(H):
    print(' '.join(map(lambda j: str(hor[i] + ver[j] - A[i][j]), range(W))))