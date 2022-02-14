from sys import stdin


def get_operation(data):
    data = data[:-1]
    if data == 'pop_front':
        if is_empty():
            print(-1)
        else:
            print(my_deque[0])
            del(my_deque[0])
    elif data == 'pop_back':
        if is_empty():
            print(-1)
        else:
            print(my_deque[-1])
            del(my_deque[-1])
    elif data == 'size':
        print(len(my_deque))
    elif data == 'empty':
        if is_empty():
            print(1)
        else:
            print(0)
    elif data == 'front':
        if is_empty():
            print(-1)
        else:
            print(my_deque[0])
    elif data == 'back':
        if is_empty():
            print(-1)
        else:
            print(my_deque[-1])
    elif data[:9] == 'push_back':
        o, n = data.split()
        n = int(n)
        my_deque.append(n)
    else:
        o, n = data.split()
        n = int(n)
        my_deque.insert(0, n)


def is_empty():
    if len(my_deque) == 0:
        return 1
    else:
        return 0


N = int(input())

my_deque = []
for n in range(N):
    get_operation(stdin.readline())
