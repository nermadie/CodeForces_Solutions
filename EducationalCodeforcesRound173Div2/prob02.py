# B. Digits
def solve(n, d):
    result = [1]
    if d == 5:
        result.append(5)
    times3 = 0
    if n >= 3:
        times3 += 1
    if n >= 6:
        times3 += 1
    if d == 3 or d == 6:
        times3 += 1
    if d == 9:
        times3 += 2
    if times3 == 1:
        result.append(3)
    elif times3 >= 2:
        result.append(3)
        result.append(9)

    # Divide the number -> group of 3 digits (the fisrt group may have less than 3 digits)
    # N = g1 - g2 + g3 - g4 + g5 ...
    # if N is divisible by 7, then the number is divisible by 7 because 1001 divisible by 7
    if n >= 3 or d == 7:
        result.append(7)
    result.sort()
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    print(solve(n, d))
