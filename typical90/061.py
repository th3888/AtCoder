import collections

q = int(input())

T = []
X = []
for i in range(q):
    t, x = map(int,input().split())
    T.append(t)
    X.append(x)

cards = collections.deque()
for i in range(q):
    if T[i] == 1:
        cards.appendleft(X[i])
    elif T[i] == 2:
        cards.append(X[i])
    else:
        print(cards[X[i]-1])