import sys

input = sys.stdin.readline


############ ---- Input Functions ---- ############
def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


def main():
    n = inp()
    p = [-1] + [i - 1 for i in inlt()]
    t = insr()
    dps = [0] * n
    dpp = [0] * n
    for i in range(n)[::-1]:
        if t[i] == "P":
            dps[i] = float("inf")
        if t[i] == "S":
            dpp[i] = float("inf")
        if p[i] != -1:
            dps[p[i]] += min(dps[i], dpp[i] + 1)
            dpp[p[i]] += min(dpp[i], dps[i] + 1)

    return min(dps[0], dpp[0])


if __name__ == "__main__":
    n = inp()
    for i in range(n):
        print(main())
