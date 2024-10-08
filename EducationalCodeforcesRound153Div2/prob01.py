# Not a Substring
def generate_regular_sequence(s):
    if s == "()":
        return "NO"
    check = False
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            check = True
            break
    print("YES")
    if check:
        return "()" * len(s)
    else:
        return "(" * len(s) + ")" * len(s)


t = int(input())
for _ in range(t):
    s = input().strip()
    print(generate_regular_sequence(s))
