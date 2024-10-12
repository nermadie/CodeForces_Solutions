# B. Prefiquence
def solve(n, m, a, b):
    b_index = 0
    cur_count = 0
    for i in range(n):
        if b_index == m:
            return cur_count
        while a[i] != b[b_index]:
            b_index += 1
            if b_index == m:
                return cur_count
        cur_count += 1
        b_index += 1
    return cur_count


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = input()
    b = input()
    print(solve(n, m, a, b))
