from sys import stdin
N = int(stdin.readline())

stack = []
for n in range(N):
    x = int(stdin.readline())
    while len(stack) > 0 and stack[-1] <= x:
        stack.pop()
    stack.append(x)

print(len(stack))
