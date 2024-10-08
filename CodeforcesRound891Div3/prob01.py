# Array Coloring
def can_color_array_with_same_parity(n, arr):
    total_sum = sum(arr)
    return "YES" if total_sum % 2 == 0 else "NO"


t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))
    print(can_color_array_with_same_parity(n, arr))
