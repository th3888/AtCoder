N = int(input())
A = list(map(int, input().split()))

A_ex = [a for a in A if a != max(A)]

print(max(A_ex))