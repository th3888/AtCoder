import math

def main():
    N = int(input())
    xy = [map(int, input().split()) for _ in range(N)]
    x, y = [list(i) for i in zip(*xy)]

    ans = []

    for i in range(len(x)):
        dis_list = []
        for j in range(len(y)):
            dis_list.append(math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2))
        max_dis_list = [i for i, v in enumerate(dis_list) if v == max(dis_list)]
        ans.append(min(max_dis_list))

    for i  in range(len(ans)):
        print(ans[i] + 1)


if __name__ == "__main__":
    main()
