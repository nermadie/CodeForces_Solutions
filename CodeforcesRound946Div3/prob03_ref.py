def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    cnt = dict()
    ans = 0
    for i in range(n - 2):
        triplet = (a[i], a[i + 1], a[i + 2])
        mist = [0] * 3
        mist[0] = (0, a[i + 1], a[i + 2])
        mist[1] = (a[i], 0, a[i + 2])
        mist[2] = (a[i], a[i + 1], 0)
        for trip in mist:
            ans += cnt.get(trip, 0) - cnt.get(triplet, 0)
            cnt[trip] = cnt.get(trip, 0) + 1
        cnt[triplet] = cnt.get(triplet, 0) + 1
    print(ans)


for i in range(int(input())):
    solve()
