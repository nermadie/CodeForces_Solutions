# C1. Message Transmission Error (easy version)
def solve(s):
    n = len(s)
    if n % 2 == 0:
        for i in range((n // 2) - 1):
            if s[(n // 2) + i] == s[-1] and s[(n // 2) - i - 1] == s[0]:
                if s[: (n // 2) + i + 1] == s[(n // 2) - i - 1 :]:
                    print("YES")
                    return s[: (n // 2) + i + 1]
        return "NO"
    else:
        for i in range(len(s) // 2):
            if s[(n // 2) + i] == s[-1] and s[(n // 2) - i] == s[0]:
                if s[: (n // 2) + i + 1] == s[(n // 2) - i :]:
                    print("YES")
                    return s[: (n // 2) + i + 1]
        return "NO"


s = input()
print(solve(s))
