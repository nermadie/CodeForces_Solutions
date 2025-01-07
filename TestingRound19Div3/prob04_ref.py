# Problem C2 - Message Transmission Error (hard version)
def prefix(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            print("k: ", k, "i: ", i)
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    print(p)
    return p


s = input()
ans = prefix(s)[-1]
if ans <= len(s) // 2:
    print("NO")
else:
    print("YES")
    print(s[:ans])
