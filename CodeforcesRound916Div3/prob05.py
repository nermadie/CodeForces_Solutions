# E1. Game with Marbles (Easy Version)
def solve(n, a, b):
    moves = []
    for i in range(n):
        moves.append((i, a[i] - 1 + b[i] - 1))
    moves.sort(key=lambda x: x[1], reverse=True)
    alice = 0
    bob = 0
    for i in range(n):
        if i % 2 == 0:
            alice += a[moves[i][0]] - 1
        else:
            bob += b[moves[i][0]] - 1
    return alice - bob


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, a, b))
