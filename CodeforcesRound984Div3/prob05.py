# E. Reverse the Rivers
def solve(n, k, grid, m, queries):
    top = 0
    bottom = n - 1
    for query in queries:
        region, sign, value = query.split()
        region = int(region) - 1
        value = int(value)
        if sign == ">":
            cur_top = top
            cur_bottom = bottom
            result = -1
            while cur_top <= cur_bottom:
                mid = (cur_top + cur_bottom) // 2
                if grid[mid][region] > value:
                    result = mid
                    cur_bottom = mid - 1
                else:
                    cur_top = mid + 1
            top = result
        else:
            cur_top = top
            cur_bottom = bottom
            result = -1
            while cur_top <= cur_bottom:
                mid = (cur_top + cur_bottom) // 2
                if grid[mid][region] < value:
                    result = mid
                    cur_top = mid + 1
                else:
                    cur_bottom = mid - 1
            bottom = result
        if top == -1 or bottom == -1:
            return -1
    return top + 1


n, k, q = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(k):
        grid[i][j] |= grid[i - 1][j]
for _ in range(q):
    m = int(input())
    queries = []
    for _ in range(m):
        queries.append(input())
    print(solve(n, k, grid, m, queries))
