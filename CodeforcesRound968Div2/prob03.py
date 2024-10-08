# C. Turtle and Good Pairs
def solve(n, s):
    result = ""
    dict_char = {}
    for char in s:
        dict_char.setdefault(char, 0)
        dict_char[char] += 1
    list_char = [[k, v] for k, v in dict_char.items()]
    list_char.sort(key=lambda x: x[1])
    temp_string = "".join([x[0] for x in list_char])
    cur_count = 0
    for i in range(len(list_char)):
        cur_print = list_char[i][1] - cur_count
        cur_count = list_char[i][1]
        result += temp_string * cur_print
        temp_string = temp_string[1:]
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
