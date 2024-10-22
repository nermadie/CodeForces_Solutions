# B. Following the String
def solve(n, a):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cur_alphabet = 0
    dict_char = {}
    result = []
    for item in a:
        if item == 0:
            dict_char.setdefault(alphabet[cur_alphabet], 0)
            dict_char[alphabet[cur_alphabet]] += 1
            result.append(alphabet[cur_alphabet])
            cur_alphabet += 1
        else:
            for k, v in dict_char.items():
                if v == item:
                    dict_char[k] += 1
                    result.append(k)
                    break
    return "".join(result)


t = int(input())
for _ in range(t):
    n = int(input())
    # a = input().split()
    a = list(map(int, input().split()))
    print(solve(n, a))
