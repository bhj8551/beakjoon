from sys import stdin


def get_operation(data):
    data = data[:-1]
    if data == 'pop':
        if is_empty():
            print(-1)
        else:
            print(my_stack[-1])
            del(my_stack[-1])
    elif data == 'size':
        print(len(my_stack))
    elif data == 'empty':
        if is_empty():
            print(1)
        else:
            print(0)
    elif data == 'top':
        if is_empty():
            print(-1)
        else:
            print(my_stack[-1])
    else:
        o, n = data.split()
        n = int(n)
        my_stack.append(n)


def is_empty():
    if len(my_stack) == 0:
        return 1
    else:
        return 0


N = int(input())

my_stack = []
for n in range(N):
    get_operation(stdin.readline())
