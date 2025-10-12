# C. Preparing for the Exam
def solve(n, m, k, a, q):
    if len(q) == n:
        return "1" * m
    if len(q) != n - 1:
        return "0" * m
    sum_known_question = 0
    for item in q:
        sum_known_question += item
    unknown_question = (1 + n) * n // 2 - sum_known_question
    result = []
    for item in a:
        if item != unknown_question:
            result.append("0")
        else:
            result.append("1")
    return "".join(result)


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(solve(n, m, k, a, q))
