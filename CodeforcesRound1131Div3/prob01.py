def solve(n, m, p, q):
    dict_char = {}
    for c in p:
        dict_char.setdefault(c, 0)
        dict_char[c] += 1
    for c in q:
        dict_char.setdefault(c, 0)
        dict_char[c] -= 1
    for k, v in dict_char.items():
        if k == "s" or k == "i" or k == "x":
            if v != 1:
                return "No"
        else:
            if v != 0:
                return "No"
    if (
        dict_char.get("s", 0) == 0
        or dict_char.get("i", 0) == 0
        or dict_char.get("x", 0) == 0
    ):
        return "No"
    return "Yes"


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    p = input()
    q = input()
    print(solve(n, m, p, q))
