# B. Plus-Minus Split
def solve(n, s):
    count_plus = 0
    count_minus = 0
    for i in s:
        if i == "+":
            count_plus += 1
        else:
            count_minus += 1
    return abs(count_plus - count_minus)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
