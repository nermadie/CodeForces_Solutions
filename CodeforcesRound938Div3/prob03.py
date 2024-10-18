# C. Inhabitant of the Deep Sea
def solve(n, k, a):
    left = 0
    right = n - 1
    result = 0
    minus = 0
    cur_left_check = True
    while left < right and k > 0:
        if a[left] < a[right]:
            if cur_left_check:
                minus = a[left] * 2 - 1
            else:
                minus = a[left] * 2
            if k >= minus:
                result += 1
                a[right] -= minus // 2
                left += 1
                cur_left_check = False
                k -= minus
            else:
                return result
        elif a[left] > a[right]:
            if not cur_left_check:
                minus = a[right] * 2 - 1
            else:
                minus = a[right] * 2
            if k >= minus:
                result += 1
                a[left] -= minus // 2
                right -= 1
                cur_left_check = True
                k -= minus
            else:
                return result
        else:
            if cur_left_check:
                minus = a[left] * 2 - 1
                if k >= minus:
                    result += 1
                    a[right] -= minus // 2
                    left += 1
                    cur_left_check = False
                    k -= minus
                else:
                    return result
            else:
                minus = a[right] * 2 - 1
                if k >= minus:
                    result += 1
                    a[left] -= minus // 2
                    right -= 1
                    cur_left_check = True
                    k -= minus
                else:
                    return result
    if left == right and k >= a[left]:
        result += 1
    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
