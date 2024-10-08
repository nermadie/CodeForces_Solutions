# B. Card Game
def solve(a1, a2, b1, b2):
    a = [a1, a2]
    b = [b1, b2]
    result = 0
    for i in range(2):
        for j in range(2):
            if a[i] > b[j] and not a[(i + 1) % 2] < b[(j + 1) % 2]:
                result += 1
            if a[i] == b[j] and a[(i + 1) % 2] > b[(j + 1) % 2]:
                result += 1
    return result


t = int(input())
for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    print(solve(a1, a2, b1, b2))
