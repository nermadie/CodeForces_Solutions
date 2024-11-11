# A. Rudolf and the Ticket
def solve(n, m , k ,b ,c):
    result = 0
    for i in range(n):
        for j in range(m):
            if b[i] + c[j] <=k:
                result += 1
    return result
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(solve(n, m, k, b, c))