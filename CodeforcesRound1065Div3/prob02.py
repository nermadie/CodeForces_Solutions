# B. Yuu Koito and Minimum Absolute Sum
def solve(n, a):
    first = a[0]
    last = a[-1]
    if first == -1 and last == -1:
        a[0] = 0
        a[-1] = 0
    elif first == -1 and last != -1:
        a[0] = last
    elif first != -1 and last == -1:
        a[-1] = first

    for i in range(1, n - 1):
        if a[i] == -1:
            a[i] = 0

    print(abs(a[-1] - a[0]))
    return " ".join(map(str, a))


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
