def solve(n, k, s):
    result = 0
    for i in range(n // k):
        all_nhoj = True
        for j in range(k):
            idx = i * k + j
            if s[idx] == "0":
                all_nhoj = False
                break
        if all_nhoj:
            result += 1
    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))
