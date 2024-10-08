# Reverse Madness
import bisect


def reverse_substring(s, a, b):
    return s[:a] + s[a : b + 1][::-1] + s[b + 1 :]


def modify_string(n, k, s, l, r, q, x):
    for i in range(q):
        x_i = x[i]
        l.append(n + 1)
        lower_bound = bisect.bisect_left(l, x_i)
        upper_bound = bisect.bisect_right(l, x_i)
        if lower_bound == upper_bound:
            lower_bound -= 1
        a = min(x_i, l[upper_bound] - 1 + l[lower_bound] - x_i)
        b = max(x_i, l[upper_bound] - 1 + l[lower_bound] - x_i)
        s = reverse_substring(s, a - 1, b - 1)
    return s


# Input
t = int(input())
results = []

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    q = int(input())
    x = list(map(int, input().split()))
    print(modify_string(n, k, s, l, r, q, x))
