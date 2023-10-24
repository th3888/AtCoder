N, K = map(int,input().split())
A = list(map(int,input().split()))

#N回移動
s = 0
for _ in range(N):
	s = A[s] - 1

path = [s]
v = s

while True:
	next_v = A[v] - 1
	if next_v == s:
		break
	path.append(next_v)
	v = next_v

t = -1

if K <= N:
	s = 0
	for _ in range(K):
		s = A[s] - 1
	t = s + 1
else:
	t = path[(K - N) % len(path)] + 1

print(t)