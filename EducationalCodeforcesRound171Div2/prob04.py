# D. Sums of Segments
def convert_b_to_s(x, n):
    if x <= n:
        return 1, x
    if n < x <= n + n - 1:
        return 2, x - n + 1
    # (n + n - y) * (y+1)/2 <=x
    # (2*n - y) * (y+1) <= 2*x
    # 2*n*y - y^2 + 2*n - y <= 2*x
    # -y^2 + y*(2*n-1) + 2*n - 2*x <= 0
    # find y by quadratic equation
    delta = (2 * n - 1) ** 2 - 4 * (-1) * (2 * n - 2 * x)
    y1 = (2 * n - 1 + delta**0.5) / 2
    y2 = (2 * n - 1 - delta**0.5) / 2
    l = int(y2) + 2
    if y2.is_integer():
        l -= 1
    return l, x - (((n + n - l + 2) * (l - 1)) // 2) + l - 1


def solve(n, a, q, queries):
    mem = [0] * (n + 1)
    mem_of_mem = [0] * (n + 1)
    mem_of_b = [0] * (n + 1)
    for i in range(n):
        mem[i + 1] = mem[i] + a[i]
        mem_of_mem[i + 1] = mem_of_mem[i] + mem[i + 1]
    for i in range(n):
        mem_of_b[i + 1] = (
            mem_of_mem[n] - mem_of_mem[i] - (mem[i]) * (n - i)
        ) + mem_of_b[i]

    for query in queries:
        l, r = query
        sum_from_l_to_nearest = 0
        sum_from_r_to_nearest = 0
        sum_middle = 0
        l = convert_b_to_s(l, n)
        r = convert_b_to_s(r, n)
        if l[0] == r[0]:
            sum_from_l_to_nearest = (
                mem_of_mem[r[1]]
                - mem_of_mem[l[1] - 1]
                - (r[1] - l[1] + 1) * mem[l[0] - 1]
            )
        elif l[0] < r[0]:
            sum_from_l_to_nearest = (
                mem_of_mem[n] - mem_of_mem[l[1] - 1] - (n - l[1] + 1) * mem[l[0] - 1]
            )
            sum_from_r_to_nearest = (
                mem_of_mem[r[1]]
                - mem_of_mem[r[0] - 1]
                - (r[1] - r[0] + 1) * mem[r[0] - 1]
            )
            sum_middle = mem_of_b[r[0] - 1] - mem_of_b[l[0]]
        print(sum_from_l_to_nearest + sum_from_r_to_nearest + sum_middle)


n = int(input())
a = list(map(int, input().split()))
q = int(input())
queries = []
for _ in range(q):
    queries.append(list(map(int, input().split())))
solve(n, a, q, queries)
