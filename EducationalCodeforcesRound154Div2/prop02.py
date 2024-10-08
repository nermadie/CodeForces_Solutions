# Two Binary Strings
def can_make_equal(a, b):
    if len(a) == 2:
        return "YES"
    for i in range(1, len(a) - 1):
        if a[i] == b[i]:
            if a[i] == "1":
                if a[i - 1] == b[i - 1] == "0":
                    return "YES"
            else:
                if a[i + 1] == b[i + 1] == "1":
                    return "YES"
    return "NO"


t = int(input())

for _ in range(t):
    a = input().strip()
    b = input().strip()
    print(can_make_equal(a, b))
