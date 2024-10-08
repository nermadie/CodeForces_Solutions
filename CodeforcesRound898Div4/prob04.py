# 1D Eraser
def min_operations_to_remove_black_cells(n, k, s):
    operations = 0
    i = 0

    while i < n:
        if s[i] == "B":
            operations += 1
            i = i + k if i + k < n else n
        else:
            i += 1

    return operations


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    print(min_operations_to_remove_black_cells(n, k, s))
