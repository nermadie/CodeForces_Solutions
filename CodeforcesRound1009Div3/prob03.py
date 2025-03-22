# C. XOR and Triangle
def solve(x):
    n_bin = bin(x)[2:]
    num_1 = n_bin.count("1")
    num_0 = n_bin.count("0")
    if num_1 > 1 and num_0 > 0:
        result = int(n_bin.replace("0", "1", 1).replace("1", "0", 1), base=2)
        return result
    return -1


t = int(input())
for _ in range(t):
    x = int(input())
    print(solve(x))
