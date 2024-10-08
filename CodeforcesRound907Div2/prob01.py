# Sorting with Twos
def can_sort_array(n, arr):
    left = 0
    right = 1
    pow_result = 1
    while True:
        for i in range(left, right - 1):
            if arr[i] > arr[i + 1]:
                return "NO"
        if right == n:
            return "YES"
        left = right
        if pow_result > n:
            right = n
        else:
            right = pow_result
        pow_result *= 2


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_sort_array(n, arr))
