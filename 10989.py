from sys import stdin
N = int(stdin.readline())
num_list = [0]*10001

for n in range(N):
    num_list[int(stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
