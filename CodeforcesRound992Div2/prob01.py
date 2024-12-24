# A. Game of Division
def solve(n, k, a):
    for i in range(n):
        check = True
        for j in range(n):
            if i != j:
                if abs(a[i] - a[j]) % k == 0:
                    check = False
                    break
        if check:
            print("YES")
            print(i + 1)
            return
    print("NO")


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    solve(n, k, a)
