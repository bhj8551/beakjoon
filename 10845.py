from sys import stdin


def get_operation(data):
    data = data[:-1]
    if data == 'pop':
        if is_empty():
            print(-1)
        else:
            print(my_queue[0])
            del(my_queue[0])
    elif data == 'size':
        print(len(my_queue))
    elif data == 'empty':
        if is_empty():
            print(1)
        else:
            print(0)
    elif data == 'front':
        if is_empty():
            print(-1)
        else:
            print(my_queue[0])
    elif data == 'back':
        if is_empty():
            print(-1)
        else:
            print(my_queue[-1])
    else:
        o, n = data.split()
        n = int(n)
        my_queue.append(n)


def is_empty():
    if len(my_queue) == 0:
        return 1
    else:
        return 0


N = int(input())

my_queue = []
for n in range(N):
    get_operation(stdin.readline())
