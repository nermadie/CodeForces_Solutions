# B. Symmetric Encoding
def solve(n, s):
    set_s = set(s)
    list_unique_s = sorted(list(set_s))
    n_list_unique_s = len(list_unique_s)
    dict_convert = {}
    for i in range(n_list_unique_s):
        dict_convert[list_unique_s[i]] = list_unique_s[n_list_unique_s - i - 1]
    return "".join([dict_convert[c] for c in s])


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
