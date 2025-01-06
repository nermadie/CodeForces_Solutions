# C. Increasing Sequence with Fixed OR
def solve(n):
    n_bin = bin(n)[2:]
    num1 = n_bin.count("1")
    if num1 == 1:
        print(1)
        return n
    result = []
    index = 0
    for i in range(num1):
        while n_bin[index] != "1":
            index += 1
        result.append(int(n_bin[:index] + "0" + n_bin[index + 1 :], 2))
        index += 1
    print(num1 + 1)
    result.append(n)
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
