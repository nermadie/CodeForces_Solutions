def solve(n, a):
    cnt_odd = 0
    cnt_even_divided_4 = 0
    cnt_event_not_divided_4 = 0
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 4 == 0:
                cnt_even_divided_4 += 1
            else:
                cnt_event_not_divided_4 += 1
        else:
            cnt_odd += 1
    return max(cnt_odd, cnt_even_divided_4, cnt_event_not_divided_4)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
