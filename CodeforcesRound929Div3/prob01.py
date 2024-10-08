# A. Turtle Puzzle: Rearrange and Negate
def max_sum_after_operations(n, arr):
    result = 0
    for item in arr:
        result += item if item >=0 else -item
    return result

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_sum_after_operations(n, arr))


