# A. Primary Task
def solve(a):
    if len(a) < 3:
        return "No"
    if a[0:2] != "10":
        return "No"
    if a[2] == "1":
        return "Yes" if len(a) > 3 else "No"
    if a[2] == "0":
        return "No"
    else:
        return "Yes"


t = int(input())
for _ in range(t):
    a = input()
    print(solve(a))
