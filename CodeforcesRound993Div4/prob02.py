# B. Normal Problem
def solve(a):
    result = []
    for i in range(len(a) - 1, -1, -1):
        if a[i] == "q":
            result.append("p")
        elif a[i] == "p":
            result.append("q")
        else:
            result.append("w")
    return "".join(result)


t = int(input())
for _ in range(t):
    a = input()
    print(solve(a))
