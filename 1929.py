from sys import stdin

M, N = map(int, stdin.readline().split())

find_primes = [0] * (N + 1)
find_primes[1] = 1
for i in range(2, N + 1):
    if find_primes[i] == 0:
        j = i + i
        while j <= N:
            find_primes[j] = 1
            j += i

for i in range(M, N+1):
    if find_primes[i] == 0:
        print(i)
