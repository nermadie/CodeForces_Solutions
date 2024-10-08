# How Much Does Daytona Cost?
def most_common_subsegment(n, k, arr):
    try:
        arr.index(k)
        return "YES"
    except ValueError:
        return "NO"


# Input
t = int(input())
results = []

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(most_common_subsegment(n, k, arr))
