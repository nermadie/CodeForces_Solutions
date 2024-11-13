# C. Concatenation of Arrays
def solve(n, a):
    sum_a = [(index, item[1] + item[0]) for index, item in enumerate(a)]
    sum_a.sort(lambda x: x[1])
    for index, _ in sum_a:
        print(a[index][0], a[index][1], end=" ")
    print()


t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    solve(n, a)
