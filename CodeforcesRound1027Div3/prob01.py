# A. Square Year
def solve(s):
    num = int(s)
    sqrt_num = num**0.5
    if sqrt_num.is_integer():
        print("0 ", int(sqrt_num))
    else:
        print(-1)


t = int(input())
for _ in range(t):
    s = input()
    solve(s)