# A. Make it White
def solve(n, s):
    first_index = s.index("B")
    last_index = s.rindex("B")
    return last_index - first_index + 1


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
