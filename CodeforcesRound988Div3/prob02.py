# B. Intercepted Inputs
def solve(k, a):
    appeared_list = [0] * (k + 1)
    for i in a:
        if appeared_list[i] == 0:
            if (k - 2) % i == 0:
                appeared_list[(k - 2) // i] = 1
        else:
            return str(i) + " " + str((k - 2) // i)


t = int(input())
for _ in range(t):
    k = int(input())
    a = list(map(int, input().split()))
    print(solve(k, a))
