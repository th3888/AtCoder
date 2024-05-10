N, A, B = map(int, input().split())
S = list(input())

cnt_pass = 0
cnt_b = 0

for i in S:
    if i == 'a' and cnt_pass < A + B:
        cnt_pass += 1
        print('Yes')
    elif i == 'b':
        cnt_b += 1
        if cnt_b <= B and cnt_pass < A + B:
            cnt_pass += 1
            print('Yes')
        else:
            print('No')
    else:
        print('No')