# C. Clock Conversion
def solve(hh, mm):
    check_AM = True
    if hh >= 12:
        check_AM = False
    if hh == 0:
        hh = 12
    if hh > 12:
        hh -= 12
    if check_AM:
        return f"{hh:02d}:{mm:02d} AM"
    else:
        return f"{hh:02d}:{mm:02d} PM"


t = int(input())
for _ in range(t):
    hh, mm = map(int, input().split(":"))
    print(solve(hh, mm))
