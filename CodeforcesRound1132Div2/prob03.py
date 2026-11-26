# B. Introduction to the Niche Internet
def solve(n, k, a):
    a.sort(reverse=True)
    max_count = 1
    for i in range(n - 1):
        if a[i + 1] == a[i]:
            max_count += 1
        else:
            break

    if max_count > k:
        return "NO"
    else:
        print("YES")

    result = [0] * n
    index = 0
    for i in range(k - 1, max_count - 1, -1):
        result[index] = a[i]
        index += 1

    for i in range(max_count):
        result[index] = a[0]
        index += 1

    for i in range(k, n):
        result[index] = a[i]
        index += 1

    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
