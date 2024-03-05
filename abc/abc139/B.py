def main():
    A, B = map(int, input().split())

    ans = (B - 1 + A - 2) / (A - 1)

    print(int(ans))


if __name__ == "__main__":
    main()
