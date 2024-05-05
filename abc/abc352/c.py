N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

A_sum = 0
B_minus_A_max = 0

for a, b in AB:
    A_sum += a
    B_minus_A_max = max(B_minus_A_max, b - a)

print(A_sum + B_minus_A_max)