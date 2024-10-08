# B. Maximum Multiple Sum
def solve(n):
    result = 0
    max_val = 0
    for i in range(2, n + 1):
        if n // i >= max_val:
            result = i
            max_val = n // i
        else:
            break
    return result


# (1+k) * k/2 * x
# k <= n // x
# <= (1 + n//x) * n/2x * x
# (1 + n//2) * n/2


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
