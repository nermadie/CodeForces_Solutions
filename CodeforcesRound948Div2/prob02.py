# B. Binary Colouring
def solve(n):
    cur_bin = reversed(bin(n)[2:])
    result = [int(bit) for bit in cur_bin]
    result.append(0)
    for i in range(len(result) - 1):
        if result[i] != 0 and result[i + 1] != 0:
            result[i] = -1
            for j in range(i + 1, len(result)):
                if result[j] == 1:
                    result[j] = 0
                else:
                    result[j] += 1
                    break
    if result[-1] == 0:
        result.pop()
    print(len(result))
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
