from sys import stdin

N = int(stdin.readline())

point = []
for i in range(N):
    x, y = map(int, stdin.readline().split())
    point.append((x, y))

point.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(point[i][0], point[i][1])
