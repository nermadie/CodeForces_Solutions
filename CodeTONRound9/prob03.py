# C1. Shohag Loves XOR (Easy Version)
# x % xor == 0 or i % xor == 0 only when i < 2 * x because a divisor of x(or y) is at most x(or y) // 2 but if i >= 2 * x then the left most bit is 1 -> > i // 2
def solve(x, m):
    upper_bound = min(m, 2 * x - 1)
    result = 0
    for i in range(1, upper_bound + 1):
        xor = x ^ i
        if xor != 0 and (x % xor == 0 or i % xor == 0):
            result += 1
    return result


t = int(input())
for _ in range(t):
    x, m = map(int, input().split())
    print(solve(x, m))
