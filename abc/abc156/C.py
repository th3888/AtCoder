def main():
    N = int(input())
    X = list(map(int, input().split()))

    ans = float('inf')
    X.sort()

    for i in range(1, 101):
        total = 0
        for j in range(N):
            total += (X[j] - i) ** 2
        ans = min(ans, total)

    print(ans)


if __name__ == "__main__":
    main()
