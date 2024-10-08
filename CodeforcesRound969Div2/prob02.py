# B. Index and Maximum Value
def solve(n, m, a, operations):
    max_val = max(a)
    for operation in operations:
        if operation[0] == "+" and int(operation[1]) <= max_val <= int(operation[2]):
            max_val += 1
        if operation[0] == "-" and int(operation[1]) <= max_val <= int(operation[2]):
            max_val -= 1
        print(max_val, end=" ")
    print()


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    operations = []
    for _ in range(m):
        operations.append(tuple(input().split()))
    solve(n, m, a, operations)
