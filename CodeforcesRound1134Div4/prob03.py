def solve(n, h):
    list_result = [0] * n
    h.sort()
    left = 0
    right = n - 1
    current = -1
    result = 0
    already_right = False
    for i in h:
        if i != current:
            current = i
            already_right = False
            list_result[left] = i
            left += 1
            result += 1
        else:
            list_result[right] = i
            right -= 1
            if not already_right:
                result += 1
            already_right = True
    print(result)
    return " ".join(map(str, list_result))


t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    print(solve(n, h))
