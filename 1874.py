from sys import stdin

N = int(stdin.readline())
stack = [0]
operations = []
max = 0
for n in range(N):
    s = int(stdin.readline())
    if stack[-1] < s:
        for i in range(max + 1, s):
            stack.append(i)
            operations.append('+')
        operations.append('+')
        operations.append('-')
        max = s
    elif s == stack[-1]:
        stack.pop()
        operations.append('-')
    else:
        operations = 'NO'
        break

if operations[0] == 'N':
    print(operations)
else:
    for i in range(len(operations)):
        print(operations[i])
