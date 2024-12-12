# B. Replace Character
def solve(n, s):
    char_dict = {}
    for i in s:
        char_dict.setdefault(i, 0)
        char_dict[i] += 1
    char_list = list(char_dict.items())
    char_list.sort(key=lambda x: x[1], reverse=True)
    alt_index = s.index(char_list[-1][0])
    return s[:alt_index] + char_list[0][0] + s[alt_index + 1 :]


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
