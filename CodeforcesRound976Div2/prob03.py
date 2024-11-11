# C. Bitwise Balancing
def solve(b, c, d):
    binb = bin(b)[2:]
    binc = bin(c)[2:]
    bind = bin(d)[2:]
    max_len = max(len(binb), len(binc), len(bind))
    binb = binb.zfill(max_len)
    binc = binc.zfill(max_len)
    bind = bind.zfill(max_len)
    # print(binb, binc, bind)
    result = ["0"] * max_len
    for i in range(max_len):
        if binb[i] == "1" and binc[i] == "1" and bind[i] == "0":
            result[i] = "1"
        elif binb[i] == "1" and binc[i] == "0" and bind[i] == "1":
            result[i] = "1"
        elif binb[i] == "0" and binc[i] == "1" and bind[i] == "0":
            result[i] = "1"
        elif binb[i] == "0" and binc[i] == "0" and bind[i] == "1":
            result[i] = "1"
        elif binb[i] == "0" and binc[i] == "1" and bind[i] == "1":
            return -1
        elif binb[i] == "1" and binc[i] == "0" and bind[i] == "0":
            return -1
    return int("".join(result), 2)


t = int(input())
for _ in range(t):
    b, c, d = map(int, input().split())
    print(solve(b, c, d))
