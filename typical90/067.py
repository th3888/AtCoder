def base10to(n, b):
    if n // b:
        return base10to(n // b, b) + str(n % b)
    return str(n % b)


n, k = map(int,input().split())

num = str(n)

for i in range(k):
    base_10 = int(num, 8)
    base_9 = str(base10to(base_10, 9))
    num = ""
    for j in range(len(base_9)):
        if base_9[j] == "8":
            num += "5"
        else:
            num += base_9[j]

print(num)