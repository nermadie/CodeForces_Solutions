# C. Choose the Different Ones!
def solve(n, m, k, a, b):
    dict_num = {}
    for item in a:
        dict_num.setdefault(item, None)
        dict_num[item] = "a"
    for item in b:
        dict_num.setdefault(item, None)
        if dict_num[item] == "a":
            dict_num[item] = "ab"
        elif dict_num[item] == None:
            dict_num[item] = "b"
    count_a = 0
    count_b = 0
    count_ab = 0
    for i in range(1, k + 1):
        i = str(i)
        if i not in dict_num:
            return "NO"
        elif dict_num[i] == "a":
            count_a += 1
        elif dict_num[i] == "b":
            count_b += 1
        else:
            count_ab += 1
    if count_a > k // 2 or count_b > k // 2:
        return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = input().split()
    b = input().split()
    print(solve(n, m, k, a, b))
