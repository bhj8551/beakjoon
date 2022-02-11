from sys import stdin

N = int(stdin.readline())

find_primes = [0] * 1000
primes = []

find_primes[0] = 1
find_primes[1] = 1
for i in range(1000):
    if find_primes[i] == 0:
        primes.append(i)
        j = i
        while True:
            j += i
            if j > 999:
                break
            find_primes[j] = 1

input_list = [x for x in map(int, stdin.readline().split())]

result = 0
for x in input_list:
    if x in primes:
        result += 1
print(result)
