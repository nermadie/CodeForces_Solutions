# D. Three Activities
def solve(n, a, b, c):
    sorted_a = sorted(enumerate(a), key=lambda x: x[1], reverse=True)
    sorted_b = sorted(enumerate(b), key=lambda x: x[1], reverse=True)
    sorted_c = sorted(enumerate(c), key=lambda x: x[1], reverse=True)
    result = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (
                    sorted_a[i][0] != sorted_b[j][0]
                    and sorted_b[j][0] != sorted_c[k][0]
                    and sorted_a[i][0] != sorted_c[k][0]
                ):
                    result = max(
                        result,
                        a[sorted_a[i][0]] + b[sorted_b[j][0]] + c[sorted_c[k][0]],
                    )
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(solve(n, a, b, c))
