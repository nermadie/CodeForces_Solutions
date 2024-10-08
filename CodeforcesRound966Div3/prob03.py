# C. Numeric String Template


def solve(n, a, s):
    for string in s:
        if len(string) != n:
            print("NO")
            continue
        str_dict = {}
        num_dict = {}
        check = True
        for i in range(n):
            if string[i] not in str_dict:
                str_dict[string[i]] = a[i]
            if str_dict[string[i]] != a[i]:
                print("NO")
                check = False
                break
            if a[i] not in num_dict:
                num_dict[a[i]] = string[i]
            if num_dict[a[i]] != string[i]:
                print("NO")
                check = False
                break
        if check:
            print("YES")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    s = []
    for _ in range(m):
        s.append(input())
    solve(n, a, s)
