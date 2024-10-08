# Three Threadlets
def can_make_equal_length_threadlets(a, b, c):
    # 3 threadlets
    if a == b == c:
        return "YES"

    threadlets = sorted([a, b, c])

    # 4 threadlets
    if threadlets[0] == threadlets[1] and threadlets[2] == threadlets[1] * 2:
        return "YES"

    # 5 threadlets
    if threadlets[1] == threadlets[0] and threadlets[2] == threadlets[1] * 3:
        return "YES"
    if threadlets[2] == threadlets[1] and threadlets[1] == threadlets[0] * 2:
        return "YES"

    # 6 threadlets
    if threadlets[2] == threadlets[0] * 4 and threadlets[0] == threadlets[1]:
        return "YES"
    if threadlets[2] == threadlets[0] * 3 and threadlets[1] == threadlets[0] * 2:
        return "YES"

    return "NO"


# Input
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    result = can_make_equal_length_threadlets(a, b, c)
    print(result)
