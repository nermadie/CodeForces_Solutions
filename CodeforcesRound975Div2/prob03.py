# C. Cards Partition
def solve(n, k, a):
    sum_a = sum(a)
    max_a = max(a)
    for i in range(n, 0, -1):
        temp = (sum_a + k) // i
        if temp * i >= sum_a and temp >= max_a:
            return i


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
