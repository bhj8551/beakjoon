from sys import stdin
from collections import deque

N = int(stdin.readline())
deck = deque([x for x in range(1, N + 1)])

while len(deck) != 1:
    deck.popleft()
    deck.append(deck.popleft())

print(deck[0])
