# Don't try to count
def min_operations_to_substring(n, m, x, s):
    count = 0
    tempExec = 0
    while tempExec < 2:
        if x.find(s) == -1:
            if len(x) > 2 * m:
                tempExec += 1
            count += 1
            x += x
        else:
            return count
    return -1


# Input
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = input().strip()
    s = input().strip()
    print(min_operations_to_substring(n, m, x, s))
