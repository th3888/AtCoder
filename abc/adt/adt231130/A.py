N = int(input())

if N < 42:
    ans = 'AGC' + format(N, '03')
    print(ans)
else:
    ans = 'AGC' + format(N + 1, '03')
    print(ans)