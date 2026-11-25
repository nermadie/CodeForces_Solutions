# C. AND, OR, Sort!
def solve(n, s):
    if s[0] == "1":
        result = 0
        for i in range(1, len(s)):
            if s[i] == "0":
                result += 1
        return result
    else:
        cnt1_fromleft = [0] * (len(s) + 1)
        cnt0_fromright = [0] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            if s[i - 1] == "1":
                cnt1_fromleft[i] = cnt1_fromleft[i - 1] + 1
            else:
                cnt1_fromleft[i] = cnt1_fromleft[i - 1]
            if s[len(s) - i] == "0":
                cnt0_fromright[len(s) - i] = cnt0_fromright[len(s) - i + 1] + 1
            else:
                cnt0_fromright[len(s) - i] = cnt0_fromright[len(s) - i + 1]
        result = float("inf")
        for i in range(len(s) + 1):
            result = min(result, cnt1_fromleft[i] + cnt0_fromright[i])
        return result


t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(solve(n, s))
