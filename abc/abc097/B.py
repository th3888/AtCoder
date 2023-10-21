X = int(input())

exp = []

for i in range(X + 1):
    for j in range(2, 10000):
        if i ** j <= X:
            exp.append(i ** j)
        else:
            break

print(max(exp))