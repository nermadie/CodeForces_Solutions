# A. Question Marks
def solve(n, s):
    count = {"A": 0, "B": 0, "C": 0, "D": 0}
    for c in s:
        if c == "A":
            count["A"] += 1
        if c == "B":
            count["B"] += 1
        if c == "C":
            count["C"] += 1
        if c == "D":
            count["D"] += 1
    result = 0
    for k, v in count.items():
        result += min(n, v)
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
