def solve(n, k, s):
    count1 = 0
    count0 = 0
    for i in range(n):
        if s[i] == "0":
            count0 += 1
        else:
            count1 += 1
    if count0 > count1:
        count0 = min(n, count0 + k)
        count1 = n - count0
    else:
        count1 = min(n, count1 + k)
        count0 = n - count1

    result = 1 + (count1 * (count1 + 1)) // 2 + (count0 * (count0 + 1)) // 2
    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))
