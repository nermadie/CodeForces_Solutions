# D. Product of Binary Decimals
def check_binary(n):
    n = str(n)
    for i in n:
        if i not in "01":
            return False
    return True


def solve(n):
    while not check_binary(n):
        check_divisible = False
        for i in range(2, 65):
            cur_bin = int(bin(i)[2:])
            if n % cur_bin == 0:
                n //= cur_bin
                check_divisible = True
                break
        if not check_divisible:
            return "NO"

    if check_binary(n):
        return "YES"
    else:
        return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
