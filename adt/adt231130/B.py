s = input()

print(s.translate(s.maketrans({'0' : '1', '1' : '0'})))