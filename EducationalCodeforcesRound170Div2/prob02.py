# B. Binomial Coefficients, Kind Of
def solve(ns, ks):
    for index in range(len(ns)):
        print(pow(2, ks[index], 1000000007))


# pow(base, exponent, mod=None)

t = int(input())
n = list(map(int, input().split()))
k = list(map(int, input().split()))
solve(n, k)
