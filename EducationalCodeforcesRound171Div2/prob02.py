# B. Black Cells
def solve(n, a):
    if n == 1:
        return 1
    if n % 2 == 0:
        max_diff = 0
        for i in range(0, n, 2):
            max_diff = max(max_diff, a[i + 1] - a[i])
        return max_diff
    else:
        odd_max_diff_left_to_right = [1] * ((n // 2) + 1)
        even_max_diff_right_to_left = [1] * ((n // 2) + 1)
        cur_max_odd = 0
        cur_max_even = 0
        for i in range(0, n - 1, 2):
            cur_max_odd = max(cur_max_odd, a[i + 1] - a[i])
            odd_max_diff_left_to_right[i // 2 + 1] = cur_max_odd
        for i in range(n - 1, 0, -2):
            cur_max_even = max(cur_max_even, a[i] - a[i - 1])
            even_max_diff_right_to_left[i // 2 - 1] = cur_max_even
        # print(
        #     "odd_max_diff_left_to_right",
        #     odd_max_diff_left_to_right,
        #     "even_max_diff_right_to_left",
        #     even_max_diff_right_to_left,
        # )
        min_diff = 1000000000000000000
        for i in range(0, n, 2):
            if (
                max(
                    odd_max_diff_left_to_right[i // 2],
                    even_max_diff_right_to_left[i // 2],
                )
                < min_diff
            ):
                min_diff = max(
                    odd_max_diff_left_to_right[i // 2],
                    even_max_diff_right_to_left[i // 2],
                )
        return min_diff


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
