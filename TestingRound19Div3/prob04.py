# Problem C2 - Message Transmission Error (hard version)
def solve(s):
    n = len(s)
    count_same = [0] * n
    for i in range(1, n):
        cur_count = count_same[i - 1]
        # Get back and check the last s[i-1] s[i] pattern by s[i-1]
        while s[cur_count] != s[i] and cur_count > 0:
            cur_count = count_same[cur_count - 1]
        if s[cur_count] == s[i]:
            cur_count += 1
        count_same[i] = cur_count
    if count_same[-1] > n // 2:
        return "YES\n" + s[: count_same[-1]]
    else:
        return "NO"


s = input()
print(solve(s))
