def solve(n, k, s):
    arr = [int(x) for x in s]
    for i in range(k):
        for j in range((n - i - 1) // k):
            left = i + j * k
            right = i + (j + 1) * k
            if arr[left] == 1:
                arr[left] = 0
                arr[right] = abs(arr[right] - 1)
    for i in range(n - 1, -1, -1):
        if arr[i] == 1:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))
