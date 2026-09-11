def solve(a, b, c):
    arr = [a, b, c]
    arr.sort()
    return min(arr[1] - arr[0], arr[2] - arr[1])


t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))
