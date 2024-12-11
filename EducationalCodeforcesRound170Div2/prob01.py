# A. Two Screens
def solve(s1, s2):
    max_same_len = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            max_same_len += 1
        else:
            break
    return (
        len(s1) + len(s2) - max_same_len + 1 if max_same_len > 0 else len(s1) + len(s2)
    )


t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    print(solve(s1, s2))
