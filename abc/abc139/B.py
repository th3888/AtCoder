def main():
    A, B = map(int, input().split())

    ans = 0

    for i in range(1, B):
        if A * i - (i - 1) >= B:
            ans = i
            break

    print(ans)


if __name__ == "__main__":
    main()
