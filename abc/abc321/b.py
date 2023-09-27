N,X = map(int,input().split())
A = list(map(int,input().split()))
A.append(-1)

for last in range(0,101):
    B = A.copy()
    B[N-1] = last
    sum = 0
    ma = 0
    mi = 100
    for p in B:
        sum += p
        ma = max(ma,p)
        mi = min(mi,p)
    score = sum - ma - mi

    if score >= X:
        print(last)
        exit()
    
print("-1")
