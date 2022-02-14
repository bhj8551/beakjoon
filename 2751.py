from sys import stdin

N = int(stdin.readline())
number = []

for n in range(N):
    number.append(int(stdin.readline()))

number.sort()

for i in range(N):
    print(number[i])
