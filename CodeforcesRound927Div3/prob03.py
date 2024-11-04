# C. LR-remainders
def solve(n, m, a, s):
    cur_pos = s.count("L")
    left = cur_pos
    right = cur_pos - 1
    prod = 1
    cur_item = None
    result = []
    for i in range(n - 1, -1, -1):
        if s[i] == "L":
            left -= 1
            cur_item = a[left]
        else:
            right += 1
            cur_item = a[right]
        prod *= cur_item
        prod %= m
        result.append(prod)
    return " ".join(map(str, reversed(result)))


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = input()
    print(solve(n, m, a, s))
