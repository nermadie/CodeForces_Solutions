# A. Sakurako's Exam
def solve(a, b):
    if b % 2 == 0:
        if a % 2 == 0:
            return "YES"
        else:
            return "NO"
    else:
        if a % 2 == 0 and a >= 2:
            return "YES"
        else:
            return "NO"


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(solve(a, b))
