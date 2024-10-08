# D. Right Left Wrong
def solve(n, a, s):
    l_list = []
    r_list = []
    sum_list = [0] * (n + 1)
    for i in range(len(s)):
        if s[i] == "L":
            l_list.append(i)
        else:
            r_list.append(i)
        if i > 0:
            sum_list[i + 1] = sum_list[i] + a[i]
        else:
            sum_list[i + 1] = a[i]
    lower_len = min(len(l_list), len(r_list))
    r_list.reverse()
    result = 0
    for i in range(lower_len):
        if l_list[i] > r_list[i]:
            break
        result += sum_list[r_list[i] + 1] - sum_list[l_list[i]]
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    print(solve(n, a, s))
