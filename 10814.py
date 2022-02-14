from sys import stdin

N = int(stdin.readline())

user_list = []
for i in range(N):
    age, user = stdin.readline().split()
    age = int(age)
    user_list.append((age, i, user))

user_list.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    print(user_list[i][0], user_list[i][2])
