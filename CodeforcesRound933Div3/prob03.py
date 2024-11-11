# C. Rudolf and the Ugly String
def solve(n, s):
    ref_string = set(["m", "ma", "map", "p", "pi", "pie", "mapie", "mapi"])
    correct_ref_string = set(["map", "pie", "mapie", "mapi"])
    cur_string = ""
    result = 0
    for i in range(n):
        if cur_string + s[i] in ref_string:
            cur_string += s[i]
        else:
            if cur_string in correct_ref_string:
                result += 1
                cur_string = s[i]
            else:
                cur_string = s[i]
    if cur_string in correct_ref_string:
        result += 1
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
