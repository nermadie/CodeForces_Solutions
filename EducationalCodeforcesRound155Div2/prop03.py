# Make it Alternating
import math

MOD = 998244353


def min_operations(s):
    count = 1
    ans1 = 0
    ans2 = 1
    cur_bit = s[0]
    for i in range(1, len(s)):
        if s[i] == cur_bit:
            count += 1
        else:
            ans1 += count - 1
            ans2 *= count
            cur_bit = s[i]
            count = 1
    ans1 += count - 1
    ans2 *= count * math.factorial(ans1)

    return ans1, ans2


t = int(input())
for _ in range(t):
    s = input().strip()
    min_ops, sequences = min_operations(s)
    print(min_ops, sequences % MOD)
