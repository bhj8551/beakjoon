from sys import stdin

N, K = map(int, stdin.readline().split())

up = 1
down = 1

for i in range(N, N-K, -1):
    up *= i

for i in range(1, K+1):
    down *= i

print(int(up/down))
