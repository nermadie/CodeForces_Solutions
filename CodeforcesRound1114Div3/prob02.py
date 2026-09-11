def solve(n, s):
    is_minus = False
    for i in range(n - 2):
        if s[i] != s[i + 1] and s[i] == s[i + 2]:
            is_minus = True
            break

    is_3_diff = False
    for i in range(1, n - 1):
        if s[i - 1] != s[i] and s[i] != s[i + 1]:
            is_3_diff = True
            break

    result = 1
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            result += 1

    if is_minus:
        return result - 2
    if is_3_diff:
        return result - 1
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
