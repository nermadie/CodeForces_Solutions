# A. Strong Password
def solve(s):
    alphabet = []
    index = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            index = i
            break
    result = s[:index] + chr(((ord(s[index]) + 1 - 97) % 26) + 97) + s[index:]
    return result


t = int(input())
for _ in range(t):
    s = input()
    print(solve(s))
