# Two Vessels
def min_moves(a, b, c):
    diff = abs(a-b)
    result = diff//(2*c)
    if result * c * 2 < diff:
        result += 1

    return result

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    print(min_moves(a, b, c))