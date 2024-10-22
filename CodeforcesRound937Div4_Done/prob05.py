# E. Nearly Shortest Repeating Substring
def check_pattern(n, s, i):
    cur_diff_first = 0
    cur_diff_last = 0
    cur_diff_total = 0
    for j in range(i):
        first_char = s[j]
        last_char = s[n - i + j]
        cur_diff_first = 0
        cur_diff_last = 0
        for k in range(n // i):
            if s[j + k * i] != first_char:
                cur_diff_first += 1
                if cur_diff_first > 1 and cur_diff_last > 1:
                    return False
            if s[j + k * i] != last_char:
                cur_diff_last += 1
                if cur_diff_first > 1 and cur_diff_last > 1:
                    return False
        cur_diff_total += min(cur_diff_first, cur_diff_last)
        if cur_diff_total > 1:
            return False
    return True


def solve(n, s):
    large_divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            large_divisors.append(n // i)
            if check_pattern(n, s, i):
                return i
    for i in range(len(large_divisors) - 1, -1, -1):
        if check_pattern(n, s, large_divisors[i]):
            return large_divisors[i]
    return n


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
