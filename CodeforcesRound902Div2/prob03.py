def count_ways(n, m, k):
    if k == 1:
        return n if m > n else m + 1

    if k > n:
        return 0

    # Tính số cách gán giá trị cho slot n+1
    max_val = min(m, n - k + 1)
    min_val = max(0, n - m)
    ways = max_val - min_val + 1

    return ways


# Đọc số lượng test cases
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    ways = count_ways(n, m, k)
    print(ways)
