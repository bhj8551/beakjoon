from sys import stdin

a, b = map(int, stdin.readline().split())

small = min(a, b)
cd_1 = []
cd_2 = []
for i in range(1, small + 1):
    if a % i == 0:
        cd_1.append(i)
    if b % i == 0:
        cd_2.append(i)

gcd = max(list(set(cd_1) & set(cd_2)))
lcm = int(a*b/gcd)
print(gcd)
print(lcm)
