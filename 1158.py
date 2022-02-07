from sys import stdin

N, K = map(int, stdin.readline().split())

input_list = [x for x in range(1, N + 1)]
output_list = []
index = K-1
while True:
    if len(output_list) == N:
        break

    if len(input_list) <= index:
        index = index % len(input_list)

    else:
        output_list.append(str(input_list.pop(index)))
        index = index + K-1

print('<' + ', '.join(output_list) + '>')
