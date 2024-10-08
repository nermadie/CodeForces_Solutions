# B. Square or Not
import math


def solve(n, s):
    if s == "1":
        return "Yes"
    width = math.sqrt(n)
    if width.is_integer():
        width = int(width)
        line2 = s[width : 2 * width]
        line_ref = "1" + "0" * (width - 2) + "1"
        # print("line2 ", line2, "line_ref ", line_ref)
        if line2 == line_ref:
            return "Yes"
        else:
            return "No"
    else:
        return "No"


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
