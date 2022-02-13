from sys import stdin

T = int(stdin.readline())

for t in range(T):
    ps = input()
    stack = []
    result = 'NO'
    for s in ps:
        if s == '(':
            stack.append(s)
        elif len(stack) != 0 and s == ')':
            stack.pop()
        else:
            break
    else:
        if len(stack) == 0:
            result = 'YES'

    print(result)
