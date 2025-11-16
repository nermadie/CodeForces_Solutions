# B. Subsequence Update
def solve(n, l, r, a):
    l = l - 1
    r = r - 1
    larr = a[:l]
    marr = a[l : r + 1]
    rarr = a[r + 1 :]
    larr.sort()
    marr.sort(reverse=True)
    rarr.sort()

    min_decrease = 0
    lsum = 0
    msum = 0
    rsum = 0
    lcheck = True
    rcheck = True
    i = 0
    while i < len(marr) and (lcheck or rcheck):
        msum += marr[i]
        if lcheck:
            if i < len(larr) and larr[i] < marr[i]:
                lsum += larr[i]
                min_decrease = min(min_decrease, lsum - msum)
            else:
                lcheck = False
        if rcheck:
            if i < len(rarr) and rarr[i] < marr[i]:
                rsum += rarr[i]
                min_decrease = min(min_decrease, rsum - msum)
            else:
                rcheck = False

        i += 1
    return sum(marr) + min_decrease


t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, l, r, a))
