from sys import stdin

N = int(stdin.readline())
stack = [0]
operations = []
for n in range(N):
    s = int(stdin.readline())

    if stack[-1] < s:
        for i in range(stack[-1] + 1, s):
            stack.append(i)
            operations.append('+')
        operations.append('-')
    elif s == stack[-1]:
        stack.pop()
        operations.append('-')
    else:
        operations = 'NO'
        break
    print('stack', stack)
    print('operations', operations)
print(operations)
